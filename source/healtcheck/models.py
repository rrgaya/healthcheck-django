from django.db import models
import requests
import logging

log = logging.getLogger(__name__)

class Endereco(models.Model):
    url = models.URLField()
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.url

    def verificar(self):
        log.debug("Verificando URL={URL}".format(URL=self.url))
        r = requests.get(self.url)
        Verificacao.objects.create(
            endereco=self,
            status=r.status_code
        )



class Verificacao(models.Model):

    OK_200 = 200
    NOT_FOUND_404 = 404

    CHOICES_STATUS = (
        (OK_200, "OK"),
        (NOT_FOUND_404, "NOT FOUND"),
    )

    endereco = models.ForeignKey(Endereco, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.IntegerField(choices=CHOICES_STATUS)

    def __str__(self):
        return self.endereco