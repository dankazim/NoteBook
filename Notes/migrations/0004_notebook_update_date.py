# Generated by Django 3.1.7 on 2021-03-19 01:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Notes', '0003_auto_20210317_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='notebook',
            name='update_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
