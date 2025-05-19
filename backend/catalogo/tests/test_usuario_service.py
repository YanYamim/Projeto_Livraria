import pytest
from catalogo.model.models import Usuario
from catalogo.services.usuario_service import listar_usuarios, cadastrar_usuarios, editar_usuario
from rest_framework import status

@pytest.mark.django_db
def test_listar_usuarios_sucesso():
    dados = {
        "nome_usuario": "Larry",
        "email_usuario": "larry@email.com",
        "senha_usuario": "1234"
    }
    cadastrar_usuarios(dados)
    resultado = listar_usuarios().data

    assert isinstance(resultado, list)
    assert len(resultado) == 1
    assert resultado[0]['nome_usuario'] == "Larry"
    assert resultado[0]['email_usuario'] == "larry@email.com"
    assert resultado[0]['senha_usuario'] == "1234"

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
    
@pytest.mark.django_db
def test_editar_usuarios_sucesso():
    dados = {
        "nome_usuario": "Larry",
        "email_usuario": "larry@email.com",
        "senha_usuario": "1234"
    }

    resultado_cadastro = cadastrar_usuarios(dados)
    usuario_id = resultado_cadastro['data']['id_usuario']

    dadosEdicao = {
        "id_usuario": usuario_id,
        "nome_usuario": "Larry Barry",
        "email_usuario": "larryBarry@email.com",
        "senha_usuario": "1234"
    }

    resultado = editar_usuario(dadosEdicao)
    assert resultado['status'] == status.HTTP_200_OK
    assert resultado['data']['nome_usuario'] == "Larry Barry"
    assert resultado['data']['email_usuario'] == "larryBarry@email.com"
    assert resultado['data']['senha_usuario'] == "1234"
