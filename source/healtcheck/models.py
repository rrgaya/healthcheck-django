import logging

import requests
from django.core.mail import mail_admins
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string

log = logging.getLogger(__name__)

class Endereco(models.Model):
    url = models.URLField()
    ativo = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Endereço"
        verbose_name_plural = "Endereços"

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

    class Meta:
        verbose_name = "Verificação"
        verbose_name_plural = "Verificações"

    def __str__(self):
        return self.endereco



@receiver(post_save, sender=Verificacao)
def verificacao_post_save(sender, instance, *args, **kwargs):

    if instance.status >= 400:
        subject = "[HealthCheck] Erro ao acessar o site/serviço"
        context = {
            'url': instance.endereco.url,
            'status_code': instance.status
        }
        message = render_to_string('email/erro_verificacao.txt', context)
        mail_admins(subject, message)

