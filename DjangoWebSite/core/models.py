from django.db import models


class Files(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название файла')
    file = models.FileField(upload_to='upload/%Y/%m/%d/', verbose_name='Файл')

    class Meta:
        verbose_name = 'файл'
        verbose_name_plural = 'файлы'

        ordering = ('title',)


class Messages(models.Model):
    title = models.CharField(max_length=255, verbose_name='Тема письма')
    message = models.TextField(verbose_name='Текст письма')
    file = models.FileField(upload_to='send/%Y/%m/%d/', verbose_name='Файл')

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'

        ordering = ('title', 'message')
