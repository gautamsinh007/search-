from django.db import models

# Create your models here.



class blog(models.Model):
    tital =  models.CharField(max_length=20)
    con =  models.TextField(max_length=100)
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)


    def __str__(self):
        return self.tital







