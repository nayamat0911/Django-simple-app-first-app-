from django.db import models

# Create your models here.


class Myskill(models.Model):
    image = models.ImageField(upload_to='skillimage/')
    title = models.CharField(max_length=50, blank=False)
    desc = models.TextField(max_length=500, blank=True)
    date = models.DateTimeField()

    def summary(self):
        return self.desc[0:150]

    def __str__(self):
        return self.title
class Contactinfo(models.Model):
    cname = models.CharField(max_length=50)
    cemail = models.EmailField(max_length=50)
    cquery = models.TextField(max_length=500)
    
    def __str__(self):
        return self.cname