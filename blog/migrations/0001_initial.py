# Generated by Django 4.0.4 on 2022-11-26 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=40)),
                ('password', models.CharField(max_length=40)),
            ],
        ),
    ]
