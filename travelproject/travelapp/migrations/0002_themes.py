# Generated by Django 4.2.3 on 2023-07-19 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Themes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.CharField(max_length=250)),
                ('pic', models.ImageField(upload_to='pics')),
                ('msg', models.TextField()),
            ],
        ),
    ]
