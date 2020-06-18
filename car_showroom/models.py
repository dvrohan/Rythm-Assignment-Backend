from django.db import models

# Create your models here.
class Car(models.Model  ):
    name = models.TextField(max_length=50)
    company_name = models.TextField(max_length=50)
    model_name = models.TextField(max_length=20)
    mileage = models.FloatField()
    horse_power = models.FloatField()

    def __str__(self):
        return self.name