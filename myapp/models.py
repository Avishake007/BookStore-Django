from django.db import models

# Create your models here.
class BookSchema(models.Model):
    book_img = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=122)
    author = models.CharField(max_length=122)
    price = models.IntegerField()
    description = models.TextField(max_length = 30) 
    inCart = models.BooleanField(default = False)
    date = models.DateField()
    userId = models.IntegerField()

    def __str__(self):
        return self.name
    

