# Generated by Django 3.0.3 on 2020-05-11 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(default='No Description Available', max_length=100)),
                ('slug', models.SlugField()),
                ('body', models.TextField()),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('type', models.CharField(choices=[('ANALYSIS', 'Analysis'), ('NEWS', 'News'), ('TRANSFERS', 'Transfers')], max_length=10)),
                ('thumb', models.ImageField(blank=True, upload_to='thumbnail_pics')),
            ],
        ),
    ]
