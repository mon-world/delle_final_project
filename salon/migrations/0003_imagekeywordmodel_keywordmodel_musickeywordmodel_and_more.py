# Generated by Django 4.0.4 on 2022-11-03 05:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0002_samplekeyword'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageKeywordModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='KeywordModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(blank=True, max_length=255)),
                ('admin_mode', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='MusicKeywordModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salon.keywordmodel')),
            ],
        ),
        migrations.DeleteModel(
            name='SampleKeyword',
        ),
        migrations.RemoveField(
            model_name='imageuploadmodel',
            name='description',
        ),
        migrations.RemoveField(
            model_name='imageuploadmodel',
            name='document',
        ),
        migrations.RemoveField(
            model_name='musicuploadmodel',
            name='file',
        ),
        migrations.RemoveField(
            model_name='musicuploadmodel',
            name='title',
        ),
        migrations.AddField(
            model_name='imageuploadmodel',
            name='filename',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='imageuploadmodel',
            name='input_text',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='imageuploadmodel',
            name='keyword',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='imageuploadmodel',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='imageuploadmodel',
            name='thumbnail',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='musicuploadmodel',
            name='filename',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='musicuploadmodel',
            name='input_text',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='musicuploadmodel',
            name='keyword',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='musicuploadmodel',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='musicuploadmodel',
            name='thumbnail',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='musickeywordmodel',
            name='music_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salon.musicuploadmodel'),
        ),
        migrations.AddField(
            model_name='imagekeywordmodel',
            name='image_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salon.imageuploadmodel'),
        ),
        migrations.AddField(
            model_name='imagekeywordmodel',
            name='keyword_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salon.keywordmodel'),
        ),
    ]
