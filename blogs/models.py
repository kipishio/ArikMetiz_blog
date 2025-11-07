from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class Topic(models.Model):
#     """Тема, которую изучает пользователь"""
#     title = models.CharField(max_length=200)
#     text = models.TextField()
#     date_added = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         """Возвращает строковое представление модели"""
#         if len(self.title) > 100:
#             print(len(self.title))
#             return f"{self.title[:100]}..."
#         else:
#             return self.title


class BlogPost(models.Model):
    """Тема, которую изучает пользователь"""
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Возвращает строковое представление модели"""
        if len(self.title) > 100:
            print(len(self.title))
            return f"{self.title[:100]}..."
        else:
            return self.title
