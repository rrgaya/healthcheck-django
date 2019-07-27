from django.db import models



class Endereco(models.Model):
    url = models.BooleanField()
    ativo = models.BooleanField(default=True)


class Verificacao(models.Model):

    OK_200 = 200
    NOT_FOUND_404 = 404

    CHOICES_STATUS = (
        (OK_200, "OK"),
        (NOT_FOUND_404, "NOT FOUND"),
    )

    endereco = models.ForeignKey(Endereco, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.BooleanField(choices=CHOICES_STATUS)