# Generated by Django 2.0.8 on 2018-10-29 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20181027_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, default='profile_image/defalt.png', upload_to='profile_image'),
        ),
    ]
