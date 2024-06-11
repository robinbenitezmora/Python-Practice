from django.db import models


class City(models.Model):
	"""
	Populate table with 'base_city.csv' in:
	BASE_ROOT
		notes_and_extras
			Tabelas necessárias
	"""
	city_code = models.CharField(
		'Code of City',
		max_length=7,
		primary_key=True,
		unique=True
	)
	city_uf = models.CharField(
		'UF',
		max_length=2
	)
	city_name = models.CharField(
		'City',
		max_length=50
	)

	class Meta:
		verbose_name = 'City'
		verbose_name_plural = 'Cities'

	def __str__(self):
		return self.city_name


class country(models.Model):
	"""
	Populate table with 'base_country.csv' in:
	BASE_ROOT
		notes_and_extras
			Tabelas necessárias
	"""
	country_code = models.CharField(
		'Code of Country',
		max_length=3,
		primary_key=True,
		unique=True
	)
	country_name = models.CharField(
		'Country',
		max_length=50,
	)

	class Meta:
		verbose_name = 'Country'
		verbose_name_plural = 'Countries'

	def __str__(self):
		return self.country_name


class CourseFS(models.Model):
	"""
	Curso de Formação Superior
	Populate table with 'base_cfs.csv' in:
	BASE_ROOT
		notes_and_extras
			Tabelas necessárias
	"""
	cfs_code = models.CharField(
		'Higher Education Course Code',
		max_length=6,
		primary_key=True,
		unique=True
	)
	cfs_name_grau = models.CharField(
		'name of the higher education course',
		max_length=100,
		unique=True
	)

	class Meta:
		verbose_name = 'Higher Education'
		verbose_name_plural = 'Higher Education Courses'

	def __str__(self):
		return self.cfs_name_grade


class KnowledgeArea(models.Model):
	"""
	Knowledge Area
	Populate table with 'base_area_conhecimento.csv' in:
	BASE_ROOT
		notes_and_extras
			Tabelas necessárias
	"""
	area_code = models.CharField(
		'Curriculum component code',
		max_length=2,
		primary_key=True,
		unique=True
	)
	curricular_component = models.CharField(
		'Curricular Component',
		max_length=50,
		unique=True
	)
	knowledge_area = models.CharField(
		'Knowledge Area',
		max_length=50
	)

	class Meta:
		verbose_name = 'Curricular Component'
		verbose_name_plural = 'Curricular Components'
		ordering = ['curricular_component']

	def __str__(self):
		return self.curricular_component


class ComplimentActivity(models.Model):
	"""
	Compliment Activity
	Populate table with 'atividade_complementar.csv' in:
	BASE_ROOT
		notes_and_extras
			Tabelas necessárias
	"""
	code_area = models.CharField(
		'Code of Area',
		max_length=2
	)
	name_area = models.CharField(
		'Name of Area',
		max_length=50
	)
	code_subarea = models.CharField(
		'Code of Subarea',
		max_length=3
	)
	name_subarea = models.CharField(
		'Name of Area',
		max_length=50
	)
	code_activity = models.CharField(
		'Code of Activity',
		primary_key=True,
		max_length=5,
		unique=True
	)
	name_activity = models.CharField(
		'Name of Activity',
		max_length=100
	)

	class Meta:
		verbose_name = 'Complementary Acivity'
		verbose_name_plural = 'Complementary Activities'
		ordering = ['code_area', 'code_subarea', 'name_activity']

	def __str__(self):
		return self.name_activity
        