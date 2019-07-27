from django.core.management.base import BaseCommand, CommandError
from healtcheck.models import Endereco, Verificacao

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):

        enderecos = Endereco.objects.filter(ativo=True)

        for endereco in enderecos:
            endereco.verificar()