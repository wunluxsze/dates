from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Создатель'
        verbose_name_plural = 'Создатели'


class Publisher(models.Model):
    name = models.CharField(max_length=255)
    authors = models.ManyToManyField(Author)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'



class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'



class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

