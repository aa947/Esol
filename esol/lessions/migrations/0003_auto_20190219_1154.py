# Generated by Django 2.1.5 on 2019-02-19 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessions', '0002_auto_20190210_1915'),
    ]

    operations = [
        migrations.CreateModel(
            name='Work_groups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='lession',
            name='number_of_students',
        ),
    ]
