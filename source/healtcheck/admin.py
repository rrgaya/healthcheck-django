from django.contrib import admin
from .models import Endereco, Verificacao


@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('url', 'ativo')


@admin.register(Verificacao)
class VerificacaoAdmin(admin.ModelAdmin):
    list_display = ('endereco', 'status')


# admin.site.register(Endereco, EnderecoAdmin)
# admin.site.register(Verificacao, VerificacaoAdmin)