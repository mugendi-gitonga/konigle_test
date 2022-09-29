from email.policy import default
from django.db import models

# Create your models here.


class CustomerEmail(models.Model):

    email = models.EmailField(blank=True, null=True, unique=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return '%s,%s' % self.email, self.creation_date