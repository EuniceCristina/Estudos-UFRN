from django.db import models


class User(models.Model):
    user_nickname = models.CharField(primary_key=True,max_length=100, default='')
    user_name = models.CharField(max_length=100,default='')
    user_email = models.EmailField(max_length=100,default='')
    user_age = models.IntegerField(default=0)
    
    def __str__(self):
        return f'Nickename : {self.user_nickname} | E-mail : {self.user_email}'

class UserTaks(models.Model):
    user_nickname = models.CharField(primary_key=True,max_length=100, default='')
    user_task = models.CharField(max_length=250,default='')

    
