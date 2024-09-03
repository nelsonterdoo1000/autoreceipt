from django.db import models

# Create your models here.

class ClientDetail(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    
    email = models.EmailField(max_length=240)
    serialnumber = models.CharField(max_length=20)
    address = models.CharField(max_length=256)
    pcmodel = models.CharField(max_length=256)
    processor = models.CharField(max_length=20)
    ram = models.CharField(max_length=10)
    rom = models.CharField(max_length=20)
    amount = models.CharField(max_length=30)
    date = models.DateField(auto_now=False,auto_now_add=True)
    
    def __str__(self):
        return f"{self.fname} {self.lname}"