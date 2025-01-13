from django.contrib.auth.models import AbstractUser
from django.db import models
from materials.models import Treatise, Lesson


class User(AbstractUser):
    email = models.EmailField(unique=True, help_text='Введите вашу почту')
    avatar = models.ImageField(upload_to='users/photo', blank=True, null=True)
    phone_number = models.CharField(max_length=11, verbose_name='Номер телефона', help_text='Введите номер телефона')
    city = models.CharField(max_length=20, verbose_name='Город', help_text='Введите город')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

    def __str__(self):
        return self.email


class Payments(models.Model):
    STATUS_CHOICES = [
        ('наличные', 'Наличные'),
        ('перевод на счет', 'Перевод на счет'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pay_date = models.DateField(blank=True, null=True, help_text='Введите дату в формате "гггг-мм-дд"')
    paid_course = models.ForeignKey(Treatise, on_delete=models.CASCADE)
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=20, choices=STATUS_CHOICES, default='перевод на счет')

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платеж'
        ordering = ['user', 'pay_date', 'payment_method',]

    def __str__(self):
        return f'{self.user} - {self.payment_method}'
