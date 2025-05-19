from ..model.models import Livro
from ..serializer.serializers import LivroSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404

def listar_livros():
    livros = Livro.objects.all()
    return LivroSerializer(livros, many=True).data

def cadastrar_livros(dados):
    serializer = LivroSerializer(data=dados)
    if serializer.is_valid():
        serializer.save()
        return {
            'data': serializer.data,
            'status': status.HTTP_201_CREATED
        }
    
    return {
        'errors': serializer.errors,
        'status': status.HTTP_400_BAD_REQUEST
    }

def editar_livros(dados):
    id_livro = dados.get('id_livro')

    if not id_livro:
        return {
            'errors': {'id_livro': 'ID do livro não disponível'},
            'status': status.HTTP_404_NOT_FOUND
        }
    
    livro = get_object_or_404(Livro, id_livro=id_livro)

    serializer = LivroSerializer(instance=livro, data=dados, partial=True)

    if serializer.is_valid():
        serializer.save()
        return {
            'data': serializer.data,
            'status': status.HTTP_200_OK
        }
    
    return {
        'errors': serializer.errors,
        'status': status.HTTP_400_BAD_REQUEST
    }