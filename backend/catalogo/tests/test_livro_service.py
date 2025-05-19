import pytest
from catalogo.model.models import Livro
from catalogo.services.livros_service import listar_livros, cadastrar_livros, editar_livros
from rest_framework import status

@pytest.mark.django_db
def test_listar_livros_sucesso():
    dados = {
        "nome_livro": "1984",
        "sinopse": "Várias fita"
    }

    cadastrar_livros(dados)
    resultado = listar_livros()
    
    assert isinstance(resultado, list)
    assert len(resultado) == 1
    assert resultado[0]['nome_livro'] == "1984"

@pytest.mark.django_db
def test_cadastrar_livros_sucesso():
    dados = {
        "nome_livro": "1984",
        "sinopse": "Várias fita"
    }
    resultado = cadastrar_livros(dados)
    assert resultado['status'] == status.HTTP_201_CREATED
    assert resultado['data']['nome_livro'] == "1984"
    assert Livro.objects.count() == 1

