# Generated by Django 4.2.10 on 2024-02-28 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_rename_blogs_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='Subtitle',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='blog',
            name='Title',
            field=models.TextField(),
        ),
    ]
