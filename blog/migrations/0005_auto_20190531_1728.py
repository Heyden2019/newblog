# Generated by Django 2.2.1 on 2019-05-31 17:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190531_1727'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='posts',
            options={'ordering': ['create_date']},
        ),
        migrations.AlterField(
            model_name='posts',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 31, 17, 28, 22, 723733)),
        ),
    ]
