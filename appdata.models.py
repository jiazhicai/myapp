# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class FinallPageDatas(models.Model):
    user_uuid = models.CharField(max_length=50)
    user_url = models.CharField(max_length=1000, blank=True, null=True)
    user_name = models.CharField(max_length=1000, blank=True, null=True)
    json = models.TextField(blank=True, null=True)
    prob = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'finall_page_datas'
