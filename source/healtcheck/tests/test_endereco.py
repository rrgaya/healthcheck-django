from django.test import TestCase
from healtcheck.models import Endereco, Verificacao


class TestEndereco(TestCase):

    def test_verifica_ok(self):
        endereco = Endereco.objects.create(url="https://www.google.com")
        endereco.verificar()
        v = Verificacao.objects.last()

        self.assertEqual(1, Verificacao.objects.all().count())
        self.assertEqual(endereco, v.endereco)
        self.assertEqual(200, v.status)

    def test_verifica_404(self):
        endereco = Endereco.objects.create(url="http://gestao-clientes-rrgaya.herokuapp.com/test")
        endereco.verificar()
        v = Verificacao.objects.last()

        self.assertEqual(1, Verificacao.objects.all().count())
        self.assertEqual(endereco, v.endereco)
        self.assertEqual(404, v.status)