from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status 

from catalogo.services.usuario_service import listar_usuarios as listar_usuarios_service
from catalogo.services.usuario_service import cadastrar_usuarios as cadastrar_usuario_service
from catalogo.services.usuario_service import editar_usuario as editar_usuario_service

@api_view(['GET'])
def listar_usuarios():
    usuarios = listar_usuarios_service()
    return Response(usuarios, status=status.HTTP_200_OK)

@api_view(['POST'])
def cadastrar_usuarios(request):
    novo_usuario = cadastrar_usuario_service(request.data)

    if 'erros' in novo_usuario:
        return Response(novo_usuario['erros'], status=novo_usuario['status'])

    return Response(novo_usuario['data'], status=novo_usuario['status'])

@api_view(['PUT'])
def editar_usuario(request):
    usuario_editado = editar_usuario_service(request.data)

    if 'erros' in usuario_editado:
        return Response(usuario_editado['erros'], status=usuario_editado['status'])
    
    return Response(usuario_editado['data'], status=usuario_editado['status'])

