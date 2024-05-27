from django.db import migrations, models

class Migration(migrations.Migration):
    
        initial = True
    
        dependencies = [
        ]
    
        operations = [
            migrations.CreateModel(
                name='City',
            fields=[
                ('city_code', models.CharField(max_length=7, primary_key=True, serialize=False, unique=True, verbose_name='Code of city')),
                ('city_uf', models.CharField(max_length=2, verbose_name='UF')),
                ('city_name', models.CharField(max_length=50, verbose_name='City')),
            ],
            options={
                'verbose_name': 'City',
                'verbose_name_plural': 'Cities',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('code_country', models.CharField(max_length=3, primary_key=True, serialize=False, unique=True, verbose_name='Code of Country')),
                ('country_name', models.CharField(max_length=50, verbose_name='Country')),
            ],
            options={
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
            },
        ),
    ]
    