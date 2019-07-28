from django.test import TestCase
from healtcheck.models import Endereco, Verificacao
import requests_mock

class TestEndereco(TestCase):

    @requests_mock.Mocker()
    def test_verifica_ok(self, r_mock):
        url = "https://www.google1.com"
        r_mock.get(url, status_code=200)
        endereco = Endereco.objects.create(url=url)
        endereco.verificar()
        v = Verificacao.objects.last()

        self.assertEqual(1, Verificacao.objects.all().count())
        self.assertEqual(endereco, v.endereco)
        self.assertEqual(200, v.status)

    @requests_mock.Mocker()
    def test_verifica_404(self, r_mock):
        url = "https://www.google1.com"
        r_mock.get(url, status_code=404)
        endereco = Endereco.objects.create(url=url)
        endereco.verificar()
        v = Verificacao.objects.last()

        self.assertEqual(1, Verificacao.objects.all().count())
        self.assertEqual(endereco, v.endereco)
        self.assertEqual(404, v.status)