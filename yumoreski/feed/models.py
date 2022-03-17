from django.db import models


# Create your models here.
class Jokes(models.Model):

    class Meta:
        verbose_name = 'joke'
        verbose_name_plural = 'jokes'

    text = models.TextField('текст юморэски')

    def __str__(self):
        return str(self.text)[:50].strip()+('...' if len(str(self.text)) > 50 else '')
