
from django.db import models
class CellData(models.Model):
    site = models.CharField(max_length=15)
    company = models.CharField(max_length=15)
    title = models.CharField(max_length=100)
    price = models.CharField(max_length=20)
    rating_review = models.CharField(max_length=20)
    url = models.CharField(max_length=500)
    status=models.CharField(max_length=50)
    redirect_url=models.CharField(max_length=1000)
    
    def __str__(self):
        return self.name
