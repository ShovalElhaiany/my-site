# Generated by Django 4.1.7 on 2023-04-02 17:09

import django.core.validators
from django.db import migrations, models
import polls.models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(verbose_name='Date published'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(max_length=200, validators=[polls.models.validateCleanLang, django.core.validators.MinLengthValidator(5)]),
        ),
    ]
