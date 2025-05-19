from ..model.models import Usuario
from ..serializer.serializers import UsuarioSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404

def listar_usuarios():
    usuarios = Usuario.objects.all()
    return UsuarioSerializer(usuarios, many=True)

def cadastrar_usuarios(dados):
    serializer = UsuarioSerializer(data=dados)
    if serializer.is_valid():
        serializer.save()
        return {
            'data': serializer.data,
            'status': status.HTTP_201_CREATED
        }
    
    return {
        'erros': serializer.errors,
        'status': status.HTTP_400_BAD_REQUEST
    }

def editar_usuario(dados):
    id_usuario = dados.get('id_usuario')

    if not id_usuario:
        return {
            'errors': {'id_usuario': 'ID de usuário não disponível'},
            'status': status.HTTP_404_NOT_FOUND
        }
    
    usuario = get_object_or_404(Usuario, id_usuario=id_usuario)

    serializer = UsuarioSerializer(instance=usuario, data=dados, partial=True)

    if serializer.is_valid():
        serializer.save()
        return {
            'data': serializer.data,
            'status': status.HTTP_200_OK
        }
    
    return {
        'errors': serializer.errors,
        'status':status.HTTP_400_BAD_REQUEST
    }