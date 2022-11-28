# Generated by Django 4.1.3 on 2022-11-28 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseuser', '0003_taskuser_django_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='baseusers',
            name='password',
        ),
        migrations.AddField(
            model_name='baseusers',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='baseusers',
            name='password1',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='baseusers',
            name='password2',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='baseusers',
            name='email',
            field=models.EmailField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='baseusers',
            name='username',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='taskuser',
        ),
    ]
