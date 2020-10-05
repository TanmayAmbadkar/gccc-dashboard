# Generated by Django 3.1.1 on 2020-10-05 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(max_length=20)),
                ('long_name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('email', models.EmailField(max_length=100)),
                ('csv', models.FileField(upload_to='csv')),
            ],
        ),
    ]