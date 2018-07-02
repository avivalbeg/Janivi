from django.db import models
class Notebook(models.Model):
    subject = models.CharField(max_length=250)
    graph_description = models.CharField(max_length=1000)
    graph_image = models.CharField(max_length=500)
    def __str__(self):
        return(self.graph_name)

# Create your models here.
