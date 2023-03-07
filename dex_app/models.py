from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    firebase_id = models.CharField(max_length=100)
    dexcom_id = models.CharField(max_length=100)
    dexcom_username = models.CharField(max_length=100)
    dexcom_password = models.CharField(max_length=100)
    # Add more fields as needed

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
