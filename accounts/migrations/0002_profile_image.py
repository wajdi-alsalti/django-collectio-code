# Generated by Django 3.2.6 on 2021-08-15 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='', upload_to='user_profile'),
            preserve_default=False,
        ),
    ]
