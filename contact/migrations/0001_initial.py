# Generated by Django 3.2 on 2021-05-17 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, upload_to='')),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(blank=True, max_length=100)),
                ('nickName', models.CharField(blank=True, max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('groups', models.CharField(blank=True, choices=[('Family', 'Family'), ('Friends', 'Friends'), ('Co-Workers', 'Co-Workers'), ('other', 'other')], max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['firstName'],
            },
        ),
    ]