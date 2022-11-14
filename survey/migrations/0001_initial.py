# Generated by Django 4.1.3 on 2022-11-14 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
        ('baseuser', '0003_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='SurveyQuestion',
            fields=[
                ('question_id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('txt', 'Text'), ('scl', 'Scale')], max_length=3)),
                ('question', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SurveyAnswer',
            fields=[
                ('answer_id', models.AutoField(primary_key=True, serialize=False)),
                ('scale_answer', models.CharField(choices=[('5', 'Very Good'), ('4', 'Good'), ('3', 'Neutral'), ('2', 'Poor'), ('1', 'Very Poor'), ('0', 'Not Applicable')], max_length=1, null=True)),
                ('comment', models.TextField(null=True)),
                ('question_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='survey.surveyquestion')),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('survey_id', models.AutoField(primary_key=True, serialize=False)),
                ('defunct_company', models.CharField(max_length=100)),
                ('answers', models.ManyToManyField(to='survey.surveyanswer')),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.company')),
                ('questions', models.ManyToManyField(to='survey.surveyquestion')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='baseuser.baseusers')),
            ],
        ),
    ]
