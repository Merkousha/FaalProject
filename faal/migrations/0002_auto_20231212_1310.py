# Generated by Django 3.2.20 on 2023-12-12 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faal',
            name='full_title',
        ),
        migrations.RemoveField(
            model_name='faal',
            name='html_text',
        ),
        migrations.AddField(
            model_name='faal',
            name='faal_text',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='faal',
            name='full_text',
            field=models.TextField(default=''),
        ),
    ]
