from django.db import models

from django.contrib.auth import get_user_model




# class MessageManager(models.Manager):
#     filter_key = 'receiver'
#
#     def get_filterd_query(self,filter_key,filter_value):
#         return self.get_queryset().filter(filter_key=filter_value)








class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100,default=None)

    def __str__(self):
        return self.first_name



class Message(models.Model):
    Sender =  models.ForeignKey(User, default=None, on_delete=models.CASCADE,related_name='+')
    Message = models.CharField(max_length=100)
    Receiver = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    date = models.DateTimeField(default=None)







