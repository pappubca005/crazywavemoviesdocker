from django.db import models
from django.contrib.auth.models import User

class register_model(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    usrname = models.CharField(max_length=30, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    email_confirm = models.BooleanField(default=False, null=True, blank=True)
    email_code = models.IntegerField(null=True, blank=True)
    message_code = models.IntegerField(null=True, blank=True)
    #pass
    premium_pass = models.BooleanField(default=False, null=True, blank=True)
    vip_pass = models.BooleanField(default=False, null=True, blank=True)
    classic_pass = models.BooleanField(default=True, null=True, blank=True)


