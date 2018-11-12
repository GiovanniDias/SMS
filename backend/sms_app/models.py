from django.db import models


class Course(models.Model):
    code = models.CharField(verbose_name='Código', max_length=10)
    name = models.CharField(verbose_name='Nome', max_length=50)
    register_date = models.DateField(
        verbose_name='Data de registro', auto_now_add=True)
    hourly_load = models.IntegerField(verbose_name='Carga Horária')

    class Meta:
        ordering = ['name']
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'


class Student(models.Model):
    code = models.CharField(verbose_name='Código', max_length=10)
    name = models.CharField(verbose_name='Nome', max_length=100)
    cpf = models.CharField(verbose_name='CPF', max_length=11)
    email = models.EmailField(verbose_name='E-mail', null=True)
    phone = models.CharField(
        verbose_name='Telefone', max_length=15, blank=True)
    cep = models.CharField(verbose_name='CEP', max_length=8)
    address = models.TextField(
        verbose_name='Endereço Principal', max_length=100)
    number = models.IntegerField(verbose_name='Número')
    complement = models.TextField(
        verbose_name='Complemento', max_length=100, blank=True)
    course = models.ForeignKey(
        Course, verbose_name='Curso', on_delete=models.CASCADE, related_name='course')

    class Meta:
        ordering = ['name']
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
