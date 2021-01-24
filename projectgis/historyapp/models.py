from django.contrib.gis.db import models

# Create your models here.

class WojnaTrzydziestoletnia(models.Model):
    ogc_fid = models.AutoField(primary_key=True, blank=True)
    nazwa = models.CharField(blank=True, null=True, max_length=80)
    BITWA = 'bitwa'
    WYDARZENIE = 'wydarzenie'
    TYP_CHOICES = [
        (BITWA, 'bitwa'),
        (WYDARZENIE, 'wydarzenie'),
    ]
    typ = models.CharField(max_length=80, choices=TYP_CHOICES, default=BITWA)
    data = models.DateField(blank=True, null=True)
    opis = models.CharField(blank=True, null=True, max_length=254)
    str_kon_1 = models.CharField(blank=True, null=True, max_length=80)
    str_kon_2 = models.CharField(blank=True, null=True, max_length=80)
    dowod_1 = models.CharField(blank=True, null=True, max_length=80)
    dowod_2 = models.CharField(blank=True, null=True, max_length=80)
    zwyciestwo = models.CharField(blank=True, null=True, max_length=80)
    geometry = models.PointField(srid=3857, blank=True, null=True)
    okres = models.CharField(blank=True, null=True, max_length=80)
    
    def __str__(self):
        return self.nazwa

    class Meta:
        db_table = 'wojna_trzydziestoletnia'
        ordering = ['data']

class PowstanieStyczniowe(models.Model):
    ogc_fid = models.AutoField(primary_key=True, blank=True)
    nazwa = models.CharField(blank=True, null=True, max_length=80)
    BITWA = 'bitwa'
    WYDARZENIE = 'wydarzenie'
    TYP_CHOICES = [
        (BITWA, 'bitwa'),
        (WYDARZENIE, 'wydarzenie'),
    ]
    typ = models.CharField(max_length=80, choices=TYP_CHOICES, default=BITWA)
    data = models.DateField(blank=True, null=True)
    opis = models.CharField(blank=True, null=True, max_length=254)
    str_kon_1 = models.CharField(blank=True, null=True, max_length=80)
    str_kon_2 = models.CharField(blank=True, null=True, max_length=80)
    dowod_1 = models.CharField(blank=True, null=True, max_length=80)
    dowod_2 = models.CharField(blank=True, null=True, max_length=80)
    zwyciestwo = models.CharField(blank=True, null=True, max_length=80)
    geometry = models.PointField(srid=3857, blank=True, null=True)
    okres = models.CharField(blank=True, null=True, max_length=80)
    
    def __str__(self):
        return self.nazwa

    class Meta:
        db_table = 'powstanie_styczniowe'
        ordering = ['data']

class PowstanieListopadowe(models.Model):
    ogc_fid = models.AutoField(primary_key=True, blank=True)
    nazwa = models.CharField(blank=True, null=True, max_length=80)
    BITWA = 'bitwa'
    WYDARZENIE = 'wydarzenie'
    TYP_CHOICES = [
        (BITWA, 'bitwa'),
        (WYDARZENIE, 'wydarzenie'),
    ]
    typ = models.CharField(max_length=80, choices=TYP_CHOICES, default=BITWA)
    data = models.DateField(blank=True, null=True)
    opis = models.CharField(blank=True, null=True, max_length=254)
    str_kon_1 = models.CharField(blank=True, null=True, max_length=80)
    str_kon_2 = models.CharField(blank=True, null=True, max_length=80)
    dowod_1 = models.CharField(blank=True, null=True, max_length=80)
    dowod_2 = models.CharField(blank=True, null=True, max_length=80)
    zwyciestwo = models.CharField(blank=True, null=True, max_length=80)
    geometry = models.PointField(srid=3857, blank=True, null=True)
    okres = models.CharField(blank=True, null=True, max_length=80)

    def __str__(self):
        return self.nazwa

    class Meta:
        db_table = 'powstanie_listopadowe'
        ordering = ['data']

class RewolucjaAmerykanska(models.Model):
    ogc_fid = models.AutoField(primary_key=True, blank=True)
    nazwa = models.CharField(blank=True, null=True, max_length=80)
    BITWA = 'bitwa'
    WYDARZENIE = 'wydarzenie'
    TYP_CHOICES = [
        (BITWA, 'bitwa'),
        (WYDARZENIE, 'wydarzenie'),
    ]
    typ = models.CharField(max_length=80, choices=TYP_CHOICES, default=BITWA)
    data = models.DateField(blank=True, null=True)
    opis = models.CharField(blank=True, null=True, max_length=254)
    str_kon_1 = models.CharField(blank=True, null=True, max_length=80)
    str_kon_2 = models.CharField(blank=True, null=True, max_length=80)
    dowod_1 = models.CharField(blank=True, null=True, max_length=80)
    dowod_2 = models.CharField(blank=True, null=True, max_length=80)
    zwyciestwo = models.CharField(blank=True, null=True, max_length=80)
    geometry = models.PointField(srid=3857, blank=True, null=True)
    okres = models.CharField(blank=True, null=True, max_length=80)

    def __str__(self):
        return self.nazwa

    class Meta:
        db_table = 'rewolucja_amerykanska'
        ordering = ['data']