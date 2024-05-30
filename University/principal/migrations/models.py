from django.db import models
from base.validators import validate_digits, validate_lective_year

class LectiveYear(models.Model):
    lective_year_id = models.AutoField(primary_key=True)
    lective_year_name = models.CharField('Lective Year', max_length=4, unique=True, validators=[validate_digits, validate_lective_year]
    )

    class Meta:
        verbose_name = 'Lective Year'
        verbose_name_plural = 'Lective Years'
        ordering = ['lective_year_name']

    def __str__(self):
        return self.lective_year_name

class BasicStage(models.Model):

    STAGE_BASIC_CHOICES = [
        ('IN', 'Childhood'),
        ('F1', 'Fundamental I'),
        ('F2', 'Fundamental II'),
        ('HS', 'High School'),
    ]

    basic_stage_id = models.AutoField(primary_key=True)
    basic_stage_name = models.CharField('Education Stage', max_length=2, choices=STAGE_BASIC_CHOICES)
    stage_basic_year = models.ForeignKey('LectiveYear', on_delete=models.DO_NOTHING, verbose_name='Lective Year')

    class Meta:
        verbose_name = 'Basic Stage Education'
        verbose_name_plural = 'Basic Stages Education'
        constraints = [
            models.UniqueConstraint(fields=['basic_stage_name', 'stage_basic_year'], name='unique_basic_stage'),
        ]
        ordering = ['stage_basic_year', 'stage_basic_name']

    def __str__(self):
        return '{} - {}'.format(
            self.get_stage_basic_name_display(),
            self.stage_basic_year
        )

class SchoolYear(models.Model):

    SCHOOL_YEAR_CHOICES = [
        ('CR', 'Creche'),
        ('G1', 'Kindergarten I'),
        ('G2', 'Kindergarten II'),
        ('G3', 'Kindergarten III'),
        ('G4', 'Garden I'),
        ('G5', 'Garden I'),
        ('1A', '1st Year'),
        ('2A', '2nd Year'),
        ('3A', '3rd Year'),
        ('4A', '4th Year'),
        ('5A', '5th Year'),
        ('6A', '6th Year'),
        ('7A', '7th Year'),
        ('8A', '8th Year'),
        ('9A', '4th Year'),
    ]

    school_year_id = models.AutoField(primary_key=True)
    school_year_name = models.CharField('School year', max_length=2, choices=SCHOOL_YEAR_CHOICES)
    school_year_stage = models.ForeignKey('BasicStage', on_delete=models.DO_NOTHING, verbose_name='Basic Stage')

    class Meta:
        verbose_name = 'School Year'
        verbose_name_plural = 'School Years'
        constraints = [
            models.UniqueConstraint(fields=['school_year_name', 'school_year_stage'], name='unique_school_year'),
        ]
        ordering = ['school_year_stage', 'school_year_name']

    def __str__(self):
        return '{} - {}'.format(
            self.get_school_year_name_display(),
            self.school_year_stage
        )

