# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AllBaseInfo(models.Model):
    user_uuid = models.CharField(max_length=50, primary_key=True)
    user_id = models.CharField(max_length=1000, blank=True, null=True)
    user_url = models.CharField(max_length=1000, blank=True, null=True)
    user_name = models.CharField(max_length=1000, blank=True, null=True)
    cmt_uuid = models.CharField(max_length=50)
    cmt_id = models.CharField(max_length=300, blank=True, null=True)
    cmt_time = models.DateTimeField(blank=True, null=True)
    cmt_text = models.CharField(max_length=8000, blank=True, null=True)
    blog_uuid = models.CharField(max_length=50)
    blog_id = models.CharField(max_length=1000, blank=True, null=True)
    blog_url = models.CharField(max_length=1000, blank=True, null=True)
    blog_time = models.DateTimeField(blank=True, null=True)
    blog_text = models.CharField(max_length=8000, blank=True, null=True)
    blog_writer_uuid = models.CharField(max_length=50)
    blog_writer_url = models.CharField(max_length=1000, blank=True, null=True)
    blog_writer = models.CharField(max_length=1000, blank=True, null=True)
    blog_writer_group = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'all_base_info'
