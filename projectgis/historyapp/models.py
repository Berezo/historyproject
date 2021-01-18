from django.contrib.gis.db import models

# Create your models here.

class WojnaTrzydziestoletnia(models.Model):
    ogc_fid = models.AutoField(primary_key=True, blank=True)
    nazwa = models.CharField(blank=True, null=True, max_length=80)
    typ = models.CharField(blank=True, null=True, max_length=80)
    data = models.DateField(blank=True, null=True)
    opis = models.CharField(blank=True, null=True, max_length=254)
    str_kon_1 = models.CharField(blank=True, null=True, max_length=80)
    str_kon_2 = models.CharField(blank=True, null=True, max_length=80)
    dowod_1 = models.CharField(blank=True, null=True, max_length=80)
    dowod_2 = models.CharField(blank=True, null=True, max_length=80)
    zwyciestwo = models.CharField(blank=True, null=True, max_length=80)
    geometry = models.PointField(srid=3857, blank=True, null=True)
    
    def __str__(self):
        return self.nazwa

    class Meta:
        managed = False
        db_table = 'wojna_trzydziestoletnia'
        ordering = ['data']