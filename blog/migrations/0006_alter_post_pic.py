# Generated by Django 4.0.6 on 2022-08-29 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_post_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pic',
            field=models.FileField(upload_to='tests.py/'),
        ),
    ]