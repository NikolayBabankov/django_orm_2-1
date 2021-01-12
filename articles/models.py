from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')
    category = models.ManyToManyField('Category', related_name = 'to_article', blank = True, through = 'ArticleCategory')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=30, verbose_name = 'Название')

    class Meta:
        ordering = ['title']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    
    def __str__(self):
        return f'{self.title}'

class ArticleCategory(models.Model):
    article = models.ForeignKey(Article, related_name='category_to_article', on_delete = models.CASCADE)
    category = models.ForeignKey(Category, related_name='category_for_article', on_delete = models.CASCADE)
    is_main = models.BooleanField(verbose_name='Основной')
    
    class Meta:
        verbose_name = 'Категория статьи'
        verbose_name_plural = 'Категории статьи'


    def __str__(self):
        return f'Статья - {self.article}, категория: {self.category}, основной: {self.is_main}'