import pytest
from ..model import Usuario
from ..services.livros_service import listar_livros, cadastrar_livros, editar_livros

@pytest.mark.django_db
def test_listar_livros_sucesso():
    pass