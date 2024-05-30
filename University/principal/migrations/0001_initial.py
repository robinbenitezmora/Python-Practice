import base.validators
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LectiveYear',
            fields=[
                ('lective_year_id', models.AutoField(primary_key=True, serialize=False)),
                ('lective_year_name', models.CharField(max_length=4, unique=True, validators=[base.validators.validate_digits, base.validators.validate_lective_year], varbose_name='Lective Year')),
            ],
            options={
                'verbose_name': 'Lective Year',
                'verbose_name_plural': 'Lective Years',
                'ordering': ['lective_year_name'],
            },
        ),
        migrations.CreateModel(
            name='BasicStage',
            fields=[
                ('basic_stage_id', models.AutoField(primary_key=True, serialize=False)),
                ('basic_stage_name', models.CharField(choices=[('IN', 'Childhood'), ('F1', 'Fundamental I'), ('F2', 'Fundamental II'), ('HS', 'High School')], max_length=2, verbose_name='Education Stage')), ('stage_basic_year', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='principal.lectiveyear', verbose_name='Lective Year')),
            ],
            options={
                'verbose_name': 'Basic Stage Education',
                'verbose_name_plural': 'Basic Stages Education',
                'ordering': ['stage_basic_year', 'stage_basic_name'],
            },
        ),
        migrations.CreateModel(
            name='SchoolYear',
            fields=[
                ('school_year_id', models.AutoField(primary_key=True, serialize=False,)),
                ('school_year_name', models.CharField(choices=[('CR', 'Creche'), ('G1', 'Kindergarten I'), ('G2', 'Kindergarten II'), ('G3', 'Kindergarten III'), ('G4', 'Garden I'), ('G5', 'Garden I'), ('1A', '1st Year'), ('2A', '2nd Year'), ('3A', '3rd Year'), ('4A', '4th Year'), ('5A', '5th Year'), ('6A', '6th Year'), ('7A', '7th Year'), ('8A', '8th Year'), ('9A', '4th Year')], max_length=2, verbose_name='School year')),
                ('school_year_stage', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='principal.basicstage', verbose_name='Basic Stage')),
            ],
            options={
                'verbose_name': 'School Year',
                'verbose_name_plural': 'School Years',
                'ordering': ['school_year_stage', 'school_year_name'],
            },
        ),
        migrations.AddConstraint(
            model_name='basicstage',
            constraint=models.UniqueConstraint(fields=['basic_stage_name', 'stage_basic_year'], name='unique_basic_stage'),
        ),
        migrations.AddConstraint(
            model_name='schoolyear',
            constraint=models.UniqueConstraint(fields=['school_year_name', 'school_year_stage'], name='unique_school_year'),
        ),
    ]
