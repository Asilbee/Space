from django.db import models



class IconGallery(models.Model):
    img = models.ImageField(upload_to='images/')





class RuServices(models.Model):
    name = models.CharField(max_length=250)
    info = models.TextField()
    img = models.ImageField(upload_to='images/')
    left = models.BooleanField(default=True)


    def __str__(self):
        return self.name
class UzServices(models.Model):
    name = models.CharField(max_length=250)
    info = models.TextField()
    img = models.ImageField(upload_to='images/')
    left = models.BooleanField(default=True)


    def __str__(self):
        return self.name


class TeamIcon(models.Model):
    img = models.ImageField(upload_to='images/')



class Email(models.Model):
    email = models.EmailField()
    message = models.TextField()