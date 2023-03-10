# Generated by Django 4.1.6 on 2023-02-11 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0013_alter_comments_adds'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adds',
            name='status',
            field=models.CharField(choices=[('On_moderated', 'На модерации'), ('Published', 'Опубликовано'), ('On_deleted', 'На удалении'), ('Rejected', 'Отклоненые')], default='On_moderated', max_length=50, verbose_name='Статус'),
        ),
    ]
