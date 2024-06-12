from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discipline_name', models.CharField(choices=[('en', 'English'), ('es', 'Spanish'), ('ma', 'mathematics'), ('ci', 'Science'), ('hi', 'History'), ('ar', 'art'), ('ge', 'geography'), ('fi', 'Filosophy'), ('pe', 'Physical Education'), ('re', 'Religion')], max_length=30, verbose_name='Discipline')), 
                ('discipline_teacher', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, related_name='disciplineteacher', to='teachers.teacher', verbose_name='Teacher')),
            ],
            options={
                'verbose_name': 'Discipline',
                'verbose_name_plural': 'Disciplines',
                'ordering': ['discipline_name', 'discipline_teacher']
            },
        ),
        migrations.AddConstraint(
            model_name='discipline',
            constraint=models.UniqueConstraint(fields=['discipline_name', 'discipline_teacher'], name='unique_discipline_teacher'),
        ),
    ]
