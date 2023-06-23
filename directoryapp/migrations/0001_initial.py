# Generated by Django 4.1.3 on 2023-05-11 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LoginTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'LoginTable',
            },
        ),
        migrations.CreateModel(
            name='TeacherModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=100)),
                ('LastName', models.CharField(max_length=100)),
                ('Profilepicture', models.CharField(max_length=100)),
                ('EmailAddress', models.CharField(max_length=100, unique=True)),
                ('PhoneNumber', models.CharField(max_length=100)),
                ('RoomNumber', models.CharField(max_length=100)),
                ('Subjectstaught', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'Teachers',
            },
        ),
    ]