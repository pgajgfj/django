from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()
    image = models.ImageField(upload_to='movies/', null=True, blank=True)  # Додаємо поле для фото

    def __str__(self):
        return self.title
