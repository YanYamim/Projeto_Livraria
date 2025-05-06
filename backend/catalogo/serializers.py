from rest_framework import serializers
from .models import Usuario, Livro, Usuario_Livro

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'

class UsuarioLivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario_Livro
        fields = '__all__'