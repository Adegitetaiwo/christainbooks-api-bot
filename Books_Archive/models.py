from django.db import models

# cloudinary
from cloudinary.models import CloudinaryField

class Author(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.name}'


# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=250)
    file = CloudinaryField(folder='christain_books_bot/books/', use_filename=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    volume = models.CharField(max_length=250, blank=True)

    verified = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title} by {self.author}'
    

    class Meta:
        verbose_name_plural = 'Books Archive'
