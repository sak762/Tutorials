from django.db import models

# Create your models here.
class Crop_Details(models.Model):
    farmer_id = models.BigAutoField(primary_key=True)
    farmer_name = models.CharField(max_length=100)
    contact_no = models.PositiveIntegerField()
    n = models.PositiveIntegerField()
    p = models.PositiveIntegerField()
    k = models.PositiveIntegerField()
    temperature = models.CharField(max_length=20)
    humidity = models.CharField(max_length=20)
    ph = models.CharField(max_length=20)
    rainfall = models.CharField(max_length=20)
    prediction = models.CharField(max_length=50)
    date = models.DateField()

    def __str__(self):
        return self.farmer_name