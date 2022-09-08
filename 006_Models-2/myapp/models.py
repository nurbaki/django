from django.db import models





# modelde degisiklik yapildiginda veya yeni bir  model olusturuldugunda make migrations yapiyoruz

class Student(models.Model):
    # https://docs.djangoproject.com/en/4.1/ref/models/fields/#field-types
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    number = models.IntegerField()

    def __str__(self):
        return f"{self.number} - {self.first_name} {self.last_name}"

    class Meta:
        # https://docs.djangoproject.com/en/4.1/ref/models/options/#model-meta-options
        ordering = ['number'] # for DESC -> '-number'
        verbose_name_plural = 'Öğrenciler'