# Generated by Django 4.1.6 on 2023-02-11 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0010_remove_adds_date_of_publication'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adds',
            name='status',
        ),
        migrations.AddField(
            model_name='adds',
            name='date_of_publication',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата публикации'),
        ),
    ]
