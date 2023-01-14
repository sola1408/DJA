from django.db import models 

# Create your models here.
class Geography(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')

    
    
    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name = ("Geography")
        verbose_name_plural = ("Geographys")


class Demand(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')


    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name = ("Demand")
        verbose_name_plural = ("Demands")


class Skills(models.Model):
    name = models.CharField(max_length=50)
    key_skills = models.IntegerField()
    year = models.CharField(max_length=10)

    
    def __str__(self) -> str:
        return self.name

    
    class Meta:
        verbose_name = ("Skills")