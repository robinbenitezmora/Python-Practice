from django.db import migrations, models

class Migration(migrations.Migration):
    
        initial = True
    
        dependencies = [
        ]
    
        operations = [
            migrations.CreateModel(
                name='AreaKnowledge',
                fields=[
                    ('area_code', models.CharField(max_length=2, primary_key=True, serialize=False,unique=True, verbose_name='Curricular component code')),
                    ('curricular_component', models.CharField(max_length=50, unique=True, verbose_name='Curricular Componet')),
                    ('knowledge_area', models.CharField(max_length=50, verbose_name='Knowledge Area')),
                ],
                options={
                    'verbose_name': 'Curricular Component',
                    'verbose_name_plural': 'Curricular Components',
                    'ordering': ['curricular_component']
                },
            ),
            migrations.CreateModel(
                name='ComplementActivity',
                fields=[
                    ('area_code', models.CharField(max_length=2, verbose_name='Area Code')),
                    ('area_name', models.CharField(max_length=50, verbose_name='Area Name')),
                    ('subarea_code', models.CharField(max_length=4, verbose_name='Subarea Code')),
                    ('subarea_name', models.CharField(max_length=50, verbose_name='Subarea Name')),
                    ('activity_code', models.CharField(max_length=5, primary_key=True, serialize= False, , unique=True, verbose_name='Activity Code')),
                    ('activity_name', models.CharField(max_length=100, verbose_name='Activity name')),
                ],
                options={
                    'verbose_name': 'Complementary activity',
                    'verbose_name_plural': 'Complementary activities',
                    'ordering': ['area_code', 'subarea-code', 'activity_name']
                },
            ),
            migrations.CreateModel(
                name='CourseFS',
                fields=[
                    ('cfs_code', models.CharField(max_length=6, primary_key=True, serialize=False, unique=True, verbose_name='Higher Education Course Code')),
                    ('cfs_name_grade', models.CharField(max_length=100, unique=True, verbose_name='Name of higher education course')),
                ],
                options={
                    'verbose_name': 'Higher Education Course',
                    'verbose_name_plural': 'Higher Education Courses',
                    'ordering': ['cfs_name_grade']
                },
            ),
            migrations.CreateModel(
                name='City',
                fields=[
                    ('city_code', models.CharField(max_length=7, primary_key=True, serialize=False, unique=True, verbose_name='City Code')),
                    ('city_name', models.CharField(max_length=50, verbose_name='City Name')),
                    ('city_uf', models.CharField(max_length=2, verbose_name='UF')),
                ],
                options={
                    'verbose_name': 'City',
                    'verbose_name_plural': 'Cities',
                    'ordering': ['city_name']
                },
            ),
            migrations.CreateModel(
                name='Country',
                fields=[
                    ('country_code', models.CharField(max_length=3, primary_key=True, serialize=False, unique=True, verbose_name='Country Code')),
                    ('country_name', models.CharField(max_length=50, verbose_name='Country Name')),
                ],
                options={
                    'verbose_name': 'Country',
                    'verbose_name_plural': 'Countries',
                    'ordering': ['country_name']
                },
            ),
        ]
        