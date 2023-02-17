from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=128, verbose_name="Заголовок")
    text=models.TextField(blank=False, verbose_name="Текст")
    published=models.BooleanField(default=False, verbose_name="Опубликовано")
    publish_date=models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    change_date=models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    likes = models.ManyToManyField(User, related_name="liked_posts", verbose_name="Лайки")

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ["-publish_date", "-change_date"]