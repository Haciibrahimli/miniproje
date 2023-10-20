from django.db import models

# Create your models here.
class Electronics(models.Model):
    name = models.CharField(max_length=255,verbose_name='mehsulin adi')
    herz = models.CharField(max_length=255,verbose_name='herz')
    color = models.CharField(max_length=255,verbose_name='mehsulun rengi')
    price = models.CharField(max_length=255,verbose_name='pehsulun qiymeti')
    marka =models.CharField(max_length=255,verbose_name='mehsulun markasi')

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ("marka",)
        verbose_name = "mehsulin adi"
        verbose_name_plural = "mehsulin adlari"