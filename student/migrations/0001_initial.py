# Generated by Django 2.1.4 on 2019-05-28 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('nam', models.CharField(max_length=20, null=True)),
                ('age', models.IntegerField(default=20, null=True)),
                ('roll_number', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]
