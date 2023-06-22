# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class BloodBank(models.Model):
    blood_bank_id = models.IntegerField(primary_key=True)
    location = models.ForeignKey('Location', models.DO_NOTHING)
    blood_bank_name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'blood_bank'


class BloodGroup(models.Model):
    blood_type = models.CharField(unique=True, max_length=45)
    blood_group_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'blood_group'


class DonarDetails(models.Model):
    donar_id = models.IntegerField(primary_key=True)
    donar_name = models.CharField(max_length=45)
    blood_group = models.ForeignKey(BloodGroup, models.DO_NOTHING, db_column='blood_group')
    donar_age = models.CharField(max_length=45)
    gender = models.CharField(max_length=45)
    aadhar_no = models.CharField(max_length=45)
    transfusion_date = models.DateField(blank=True, null=True)
    blood_bank = models.ForeignKey(BloodBank, models.DO_NOTHING, db_column='blood_bank')
    units = models.IntegerField()
    eligibility = models.CharField(max_length=45)
    donar_location = models.ForeignKey('Location', models.DO_NOTHING, db_column='donar_location')

    class Meta:
        managed = False
        db_table = 'donar_details'


class Location(models.Model):
    location_id = models.IntegerField(primary_key=True)
    city = models.CharField(max_length=45)
    area = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'location'


class PatientDetails(models.Model):
    patient_id = models.IntegerField(primary_key=True)
    patient_name = models.CharField(max_length=45)
    blood_group_type = models.ForeignKey(BloodGroup, models.DO_NOTHING, db_column='blood_group_type')
    location = models.ForeignKey(Location, models.DO_NOTHING, db_column='location')
    units = models.IntegerField()
    hospital = models.CharField(max_length=45)
    contact = models.BigIntegerField(blank=True, null=True)
    gender = models.CharField(max_length=45, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=45)
    units_required = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patient_details'


class TotalUnits(models.Model):
    units_id = models.AutoField(primary_key=True)
    blood_type = models.ForeignKey(BloodGroup, models.DO_NOTHING, db_column='blood_type')
    total_units = models.IntegerField()
    blood_bank = models.ForeignKey(BloodBank, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'total_units'


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    role = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'user'
