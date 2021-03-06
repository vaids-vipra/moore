# Generated by Django 2.0.5 on 2018-06-28 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('involvement', '0018_auto_20180625_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='contact_email',
            field=models.EmailField(blank=True, help_text='The email address for the current position holder', max_length=254, verbose_name='Contact email address'),
        ),
    ]
