# Generated by Django 3.2 on 2022-10-30 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SampleKeyword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(blank=True, max_length=255)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
