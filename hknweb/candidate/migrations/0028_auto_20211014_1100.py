# Generated by Django 2.2.8 on 2021-10-14 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0027_auto_20211010_0141'),
    ]

    operations = [
        migrations.AddField(
            model_name='requirementbitbyteactivity',
            name='bitByteDateEnd',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='requirementbitbyteactivity',
            name='bitByteDateStart',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
