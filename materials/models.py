from django.db import models


class Treatise(models.Model):
    name = models.CharField(max_length=100, verbose_name='Курс', help_text='Введите название курса')
    preview = models.ImageField(upload_to='treatise/photo', blank=True, null=True)
    description = models.TextField('Введите описание курса')
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='owner_treatise',blank=True, null=True)


    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ['name', ]

    def __str__(self):
        return self.name

class Lesson(models.Model):
    name = models.CharField(max_length=100, verbose_name='Урок', help_text='Введите название урок')
    preview = models.ImageField(upload_to='lesson/photo', blank=True, null=True)
    link_to_video = models.CharField(max_length=200, verbose_name='Ссылка', help_text='Введите ссылку на урок', blank=True, null=True)
    treatise = models.ForeignKey(Treatise,on_delete=models.CASCADE, related_name='lessons')
    description = models.TextField('Введите описание урока',blank=True, null=True)
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='owner_lesson', blank=True, null=True)

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        ordering = ['treatise', 'name']


    def __str__(self):
        return f'{self.name} - {self.treatise}'
