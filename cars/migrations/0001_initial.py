# Generated by Django 2.2.9 on 2020-08-19 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=80)),
                ('homepage', models.URLField(blank=True, max_length=240, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('model_name', models.CharField(max_length=80)),
                ('color', models.CharField(max_length=80)),
                ('url', models.URLField(max_length=250, null=True)),
                ('brand', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='cars.Brand')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
