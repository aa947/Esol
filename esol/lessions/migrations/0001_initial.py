# Generated by Django 2.1.5 on 2019-02-10 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='lession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_students', models.ImageField(upload_to='')),
                ('number_of_students_per_group', models.IntegerField()),
                ('topic', models.CharField(max_length=250)),
                ('content', models.TextField()),
            ],
        ),
    ]
