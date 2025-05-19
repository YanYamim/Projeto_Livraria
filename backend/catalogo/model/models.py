from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome_usuario = models.CharField(max_length=30, default='')
    email_usuario = models.CharField(max_length=30, default='')
    senha_usuario = models.CharField(max_length=20, null=False)

    def __str__(self):
        return f'Nome: {self.nome_usuario} | Email: {self.email_usuario}'
    
class Livro(models.Model):
    id_livro = models.AutoField(primary_key=True)
    nome_livro = models.CharField(max_length=50, null=False)
    sinopse_livro = models.CharField(max_length=300, default='')

    def __str__(self):
        return f'Nome: {self.nome_livro} | Sinopse: {self.sinopse_livro}'
    
class Usuario_Livro(models.Model):
    id_usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, related_name='usuario_livros')
    id_livro = models.ForeignKey('Livro', on_delete=models.CASCADE, related_name='livro_usuarios')
