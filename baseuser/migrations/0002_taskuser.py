# Generated by Django 4.1.3 on 2022-11-22 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseuser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='taskuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200, null=True)),
                ('password1', models.CharField(max_length=200, null=True)),
                ('password2', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
