# Generated by Django 4.1 on 2022-11-18 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=18)),
                ('apellido', models.CharField(max_length=18)),
                ('fecha_nacimiento', models.DateField()),
            ],
        ),
    ]