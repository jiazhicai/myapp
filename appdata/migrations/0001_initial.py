# Generated by Django 3.1.2 on 2020-10-17 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllBaseInfo',
            fields=[
                ('user_uuid', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('user_id', models.CharField(blank=True, max_length=1000, null=True)),
                ('user_url', models.CharField(blank=True, max_length=1000, null=True)),
                ('user_name', models.CharField(blank=True, max_length=1000, null=True)),
                ('cmt_uuid', models.CharField(max_length=50)),
                ('cmt_id', models.CharField(blank=True, max_length=300, null=True)),
                ('cmt_time', models.DateTimeField(blank=True, null=True)),
                ('cmt_text', models.CharField(blank=True, max_length=8000, null=True)),
                ('blog_uuid', models.CharField(max_length=50)),
                ('blog_id', models.CharField(blank=True, max_length=1000, null=True)),
                ('blog_url', models.CharField(blank=True, max_length=1000, null=True)),
                ('blog_time', models.DateTimeField(blank=True, null=True)),
                ('blog_text', models.CharField(blank=True, max_length=8000, null=True)),
                ('blog_writer_uuid', models.CharField(max_length=50)),
                ('blog_writer_url', models.CharField(blank=True, max_length=1000, null=True)),
                ('blog_writer', models.CharField(blank=True, max_length=1000, null=True)),
                ('blog_writer_group', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'all_base_info',
                'managed': False,
            },
        ),
    ]
