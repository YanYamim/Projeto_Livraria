import pytest
from catalogo.model.models import Usuario
from catalogo.services.usuario_service import listar_usuarios, cadastrar_usuarios, editar_usuario
from rest_framework import status

@pytest.mark.django_db
def test_cadastrar_usuarios_sucesso():
    dados = {
        "nome_usuario": "Larry",
        "email_usuario": "larry@email.com",
        "senha_usuario": "1234"
    }
    resultado = cadastrar_usuarios(dados)
    assert resultado['status'] == status.HTTP_201_CREATED
    assert resultado['data']['nome_usuario'] == "Larry"
    assert resultado['data']['email_usuario'] == "larry@email.com"
    assert resultado['data']['senha_usuario'] == "1234"
    assert Usuario.objects.count() == 1
    
