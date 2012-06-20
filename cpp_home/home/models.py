# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models
from compositekey import db

class Usr(models.Model):
    id = models.CharField(max_length=192, primary_key=True)
    date_created = models.DateTimeField(null=True, blank=True)
    last_updated = models.DateTimeField(null=True, blank=True)
    first_name = models.CharField(max_length=765, blank=True)
    last_name = models.CharField(max_length=765, blank=True)
    email = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'usr'

class IncidentType(models.Model):
    id = models.CharField(max_length=48, primary_key=True)
    name = models.CharField(max_length=765)
    class_field = models.CharField(max_length=765, db_column='class', blank=True) # Field renamed because it was a Python reserved word.
    class Meta:
        db_table = u'incident_type'

class Incident(models.Model):
    id = models.IntegerField(primary_key=True)
    date_created = models.DateTimeField(null=True, blank=True)
    last_updated = models.DateTimeField(null=True, blank=True)
    ts = models.DateTimeField(null=True, blank=True)
    ts_end = models.DateTimeField(null=True, blank=True)
    type = models.ForeignKey(IncidentType, null=True, db_column='type', blank=True)
    source = models.CharField(max_length=48, blank=True)
    source_id = models.CharField(max_length=192, blank=True)
    usr = models.CharField(max_length=192, blank=True)
    name = models.CharField(max_length=765, blank=True)
    descr = models.TextField(blank=True)
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    class Meta:
        db_table = u'incident'

class Country(models.Model):
    id = models.CharField(max_length=6, primary_key=True)
    name = models.CharField(max_length=765, blank=True)
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    bb_nw_lat = models.FloatField(null=True, blank=True)
    bb_nw_lon = models.FloatField(null=True, blank=True)
    bb_se_lat = models.FloatField(null=True, blank=True)
    bb_se_lon = models.FloatField(null=True, blank=True)
    incidents = models.ManyToManyField('Incident',through='CountryIncident')
    def __unicode__(self):
        return self.id
    class Meta:
        db_table = u'country'

class CountryContent(models.Model):
    country = models.ForeignKey(Country, db_column='country')
    id = models.CharField(max_length=48, primary_key=True)
    date_created = models.DateTimeField(null=True, blank=True)
    last_updated = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    usr = models.ForeignKey(Usr, db_column='usr')
    class Meta:
        db_table = u'country_content'

class CountryIncident(models.Model):
    id = db.MultiFieldPK("incident","country")
    incident = models.ForeignKey(Incident, db_column='incident')
    country = models.ForeignKey(Country, db_column='country')
    class Meta:
        db_table = u'country_incident'

class Page(models.Model):
    id = models.CharField(max_length=192, primary_key=True)
    date_created = models.DateTimeField(null=True, blank=True)
    last_updated = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'page'

class Region(models.Model):
    id = models.CharField(max_length=48, primary_key=True)
    type = models.CharField(max_length=48, blank=True)
    name = models.CharField(max_length=765, blank=True)
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    class Meta:
        db_table = u'region'


class RegionContent(models.Model):
    region = models.ForeignKey(Region, db_column='region')
    id = models.CharField(max_length=48, primary_key=True)
    date_created = models.DateTimeField(null=True, blank=True)
    last_updated = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    usr = models.ForeignKey(Usr, db_column='usr')
    class Meta:
        db_table = u'region_content'

class RegionCountry(models.Model):
    id = db.MultiFieldPK("region","country")
    region = models.ForeignKey(Region, db_column='region')
    country = models.ForeignKey(Country, db_column='country')
    class Meta:
        db_table = u'region_country'

class RegionIncident(models.Model):
    incident = models.ForeignKey(Incident, db_column='incident')
    region = models.ForeignKey(Region, db_column='region')
    class Meta:
        db_table = u'region_incident'

class Source(models.Model):
    id = models.CharField(max_length=48, primary_key=True)
    name = models.CharField(max_length=765)
    class Meta:
        db_table = u'source'

