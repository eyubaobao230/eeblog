# Generated by Django 2.1.4 on 2019-01-10 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edblog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SuperUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=5, unique=True)),
                ('password', models.CharField(max_length=5)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('recreate_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'superuser',
            },
        ),
    ]
