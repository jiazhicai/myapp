# Generated by Django 3.1.2 on 2020-10-18 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appdata', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinallPageDatas',
            fields=[
                ('user_uuid', models.CharField(max_length=50)),
                ('user_url', models.CharField(blank=True, max_length=1000, null=True)),
                ('user_name', models.CharField(blank=True, max_length=1000, null=True)),
                ('json', models.TextField(blank=True, null=True)),
                ('prob', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'finall_page_datas',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='AllBaseInfo',
        ),
    ]
