from datetime import datetime

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Profile(models.Model):
    author = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name=_('Author'))
    bio = models.TextField(default='', blank=True)
    gender = models.CharField(
        max_length=65, blank=True, verbose_name=_('Gender'))
    cover = models.ImageField(
        upload_to=r'authors/covers/%Y/%m/%d',
        blank=True,
        default='',
        verbose_name=_('Cover')
    )
    date_of_birth = models.DateField(
        default=datetime.now().strftime('%Y-%m-%d'),
        verbose_name=_('Date of birth')
    )

    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')
