# Generated by Django 3.1.6 on 2021-02-16 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App2', '0002_auto_20210215_1048'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=10)),
                ('Image', models.ImageField(upload_to='userpics')),
            ],
        ),
    ]
