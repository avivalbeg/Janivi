from django.db import models
class Notebook(models.Model):
    subject = models.CharField(max_length=250)
    notebook_location = models.CharField(max_length=1000)
    notebook_description = models.CharField(max_length=500)
    notebook_date_added = models.DateField()
    def __str__(self):
        return(self.subject)

# Create your models here.
