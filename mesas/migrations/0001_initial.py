# Generated by Django 3.2.7 on 2021-10-08 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Mesas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numerom', models.IntegerField()),
                ('cantidad', models.IntegerField()),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mesas.estado')),
            ],
        ),
    ]
