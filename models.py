from django.db import models

# Create your models here.

class ToDo(models.Model):
    person = models.EmailField()
    phone_number = models.TextField()
    date_of_meeting = models.DateTimeField(auto_now_add=True)
    ic_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)
    
