# Generated by Django 2.2.1 on 2019-05-30 18:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190530_1550'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('slug', models.SlugField(max_length=20, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='posts',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 30, 18, 46, 54, 346534)),
        ),
        migrations.AddField(
            model_name='posts',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='posts', to='blog.Tags'),
        ),
    ]
