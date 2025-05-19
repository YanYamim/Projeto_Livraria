import pytest
from catalogo.model.models import Livro
from catalogo.services.livros_service import listar_livros, cadastrar_livros, editar_livros
from rest_framework import status

@pytest.mark.django_db
def test_listar_livros_sucesso():
    dados = {
        "nome_livro": "1984",
        "sinopse_livro": "Várias fita"
    }

    cadastrar_livros(dados)
    resultado = listar_livros()
    
    assert isinstance(resultado, list)
    assert len(resultado) == 1
    assert resultado[0]['nome_livro'] == "1984"
    assert resultado[0]['sinopse_livro'] == "Várias fita"

@pytest.mark.django_db
def test_cadastrar_livros_sucesso():
    dados = {
        "nome_livro": "1984",
        "sinopse_livro": "Várias fita"
    }
    resultado = cadastrar_livros(dados)
    assert resultado['status'] == status.HTTP_201_CREATED
    assert resultado['data']['nome_livro'] == "1984"
    assert resultado['data']['sinopse_livro'] == "Várias fita"
    assert Livro.objects.count() == 1

@pytest.mark.django_db
def test_editar_livros_sucesso():
    dados = {
        "nome_livro": "1984",
        "sinopse_livro": "Várias fita"
    }

    resultado_cadastro = cadastrar_livros(dados)
    livro_id = resultado_cadastro['data']['id_livro']

    dadosEdicao = {
        "id_livro": livro_id,
        "nome_livro": "1984",
        "sinopse_livro": "Ele curte várias fita, várias balada"
    }

    resultado = editar_livros(dadosEdicao)
    assert resultado['status'] == status.HTTP_200_OK
    assert resultado['data']['nome_livro'] == "1984"
    assert resultado['data']['sinopse_livro'] == "Ele curte várias fita, várias balada"