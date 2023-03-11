from django.db import models


class Countries_to_apply(models.Model):
    Country_Name = models.CharField(max_length=250)


class Cities_to_apply(models.Model):
    # to protect data if last table was deleted
    # on_delete=models.PROTECT
    from_country = models.ForeignKey(
        'Countries_to_apply', on_delete=models.CASCADE)
    City_Name = models.CharField(max_length=250)


class University_to_apply(models.Model):
    from_city = models.ForeignKey('Cities_to_apply', on_delete=models.CASCADE)
    Uni_Name = models.CharField(max_length=250)
    Uni_Acronym = models.CharField(max_length=250)
    Uni_Logo = models.FileField()
    Uni_Type = models.CharField(max_length=200)
    Uni_Overview = models.TextField()
    Uni_EstablishedYear = models.PositiveSmallIntegerField()
    Uni_All_Students = models.PositiveIntegerField()
    Uni_International_Students = models.PositiveIntegerField()
    Uni_Website = models.URLField()
    Uni_ApplyRate = models.FloatField()
