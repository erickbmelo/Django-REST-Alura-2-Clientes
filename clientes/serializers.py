from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    """Exibindo todos os clientes"""
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        errors = {}
        
        if not cpf_valido(data['cpf']):
            errors['cpf'] = "Número de CPF inválido."
        if not nome_valido(data['nome']):
            errors['nome'] = "Não inclua números neste campo."
        if not rg_valido(data['rg']):
            errors['rg'] = "O RG deve ter 9 dígitos."
        if not celular_valido(data['celular']):
            errors['celular'] = "O número de celular deve seguir este padrão: 11 91234-1234, respeitando os espaços e traço."

        if errors:
            raise serializers.ValidationError(errors)
        return data