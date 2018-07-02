from django.db import models
class Site(models.Model):
    site = models.CharField(max_length=250)
    site_location = models.CharField(max_length=1000)
    site_description = models.CharField(max_length=500)
    site_date_added = models.DateField()
    def __str__(self):
        return(self.site)

# Create your models here.
