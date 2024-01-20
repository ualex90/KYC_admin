from django.contrib.auth.models import AbstractUser
from django.db import models


NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    """ Модель пользователя """
    email = models.CharField(max_length=255, unique=True, verbose_name='Email')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    first_name = models.CharField(max_length=30, verbose_name='Имя')
    surname = models.CharField(max_length=30, **NULLABLE, verbose_name='Отчество')
    is_active = models.BooleanField(default=True, verbose_name='Признак активности')
    comments = models.TextField(**NULLABLE, verbose_name='Информация о пользователе')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = "user"


class StatusFile(models.TextChoices):
    UNDER_REVIEW = 'under_review'
    ACCEPTED = 'accepted'
    REJECTED = 'rejected'


class File(models.Model):
    """ Модель файла """
    name = models.CharField(max_length=50, verbose_name='Имя файла')
    size = models.IntegerField(verbose_name='Размер файла')
    content_type = models.CharField(max_length=30, verbose_name='Тип файла')
    filename = models.CharField(max_length=30, unique=True, verbose_name='Имя файла на диске')
    is_public = models.BooleanField(default=False, verbose_name='Признак публичности')
    status = models.CharField(
        max_length=12,
        choices=StatusFile,
        default=StatusFile.UNDER_REVIEW,
        verbose_name='Статус файла'
    )
    owner: models.ForeignKey(
        'models.User',
        related_name='files',
        on_delete=models.SET_NULL,
        **NULLABLE,
        verbose_name='Владелец'
    )
    upload_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время загрузки файла')
    change_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения статуса')

    class Meta:
        db_table = "file"
