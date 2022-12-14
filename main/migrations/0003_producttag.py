# Generated by Django 4.1 on 2022-08-30 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_productimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('slug', models.SlugField(max_length=48)),
                ('description', models.TextField(blank=True)),
                ('active', models.BooleanField(default=True)),
                ('products', models.ManyToManyField(blank=True, to='main.product')),
            ],
        ),
    ]
