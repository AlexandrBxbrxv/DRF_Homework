from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    title = models.CharField(max_length=200, verbose_name='название')
    preview = models.ImageField(upload_to='materials/courses', **NULLABLE, verbose_name='превью')
    description = models.TextField(**NULLABLE, verbose_name='описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


