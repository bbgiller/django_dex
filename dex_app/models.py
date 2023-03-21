from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    firebase_id = models.CharField(max_length=100)
    dexcom_id = models.CharField(max_length=100)
    dexcom_username = models.CharField(max_length=100)
    dexcom_password = models.CharField(max_length=100)
    # Add more fields as needed

class Insulin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dose = models.FloatField()
    time = models.DateTimeField()
    type = models.CharField(max_length=5, choices=[('short', 'Short-acting'), ('long', 'Long-acting')])

  