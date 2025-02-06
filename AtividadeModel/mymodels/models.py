from django.db import models


class User(models.Model):
    # id é um atributo já padrão
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=128)
    birth_date = models.DateField()

    def __str__(self):
        return f'{self.email}'


class Profile(models.Model):
    name = models.CharField(max_length=200)
    # Deleta o perfil se o usuário for deletado (CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} - {self.name}'


class Post(models.Model):
    text = models.TextField()
    # Adiciona a data atual ao ser criado (auto_now_add=True)
    date = models.DateField(auto_now_add=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.text} - {self.date} - {self.profile}'


class Comment(models.Model):
    text = models.TextField()
    date = models.DateField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.text} - {self.date} - {self.post} - {self.profile}'


class Reaction(models.Model):
    type_choices = (
        ('S', 'Smile'),
        ('C', 'Cry'),
        ('T', 'Thumbs Up')
    )

    reaction_type = models.CharField(choices=type_choices, max_length=1)
    weight = models.FloatField()
    date = models.DateField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.reaction_type} - {self.weight} - {self.date} - {self.post} - {self.profile}'
