from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status 

from catalogo.services.livros_service import listar_livros as listar_livros_service
from catalogo.services.livros_service import cadastrar_livros as cadastrar_livros_service
from catalogo.services.livros_service import editar_livros as editar_livros_service

@api_view(['GET'])
def listar_livros():
    livros = listar_livros_service()
    return Response(livros, status=status.HTTP_200_OK)

@api_view(['POST'])
def cadastrar_livros(request):
    novo_livro = cadastrar_livros_service(request.data)

    if 'erros' in novo_livro:
        return Response(novo_livro['erros'], status=novo_livro['status'])

    return Response(novo_livro['data'], status=novo_livro['status'])

@api_view(['PUT'])
def editar_usuario(request):
    livro_editado = editar_livros_service(request.data)

    if 'erros' in livro_editado:
        return Response(livro_editado['erros'], status=livro_editado['status'])
    
    return Response(livro_editado['data'], status=livro_editado['status'])

