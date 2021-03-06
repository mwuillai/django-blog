# Generated by Django 2.0.7 on 2018-07-29 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180729_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='article',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='comments',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='newsletter',
            field=models.BooleanField(default=False),
        ),
    ]
