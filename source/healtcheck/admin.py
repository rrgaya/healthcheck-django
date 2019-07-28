from django.contrib import admin
from .models import Endereco, Verificacao


@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ['url', 'ativo', 'get_last_status']

    def get_last_status(self, obj):
        # TODO: Refactoring para adicionar created_at no modelo de Verificacao
        # verificacoes = obj.verificacao_set.all().order_by("-created_at")
        verificacoes = obj.verificacao_set.all()
        if verificacoes.count() == 0:
            return "N/A"
        else:
            return verificacoes[0].get_status_display()
    get_last_status.short_description = "Last Status"


@admin.register(Verificacao)
class VerificacaoAdmin(admin.ModelAdmin):
    list_display = ['endereco', 'status']

