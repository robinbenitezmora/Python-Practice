from django.db import models
from teachers.models import Teacher

class Discipline(models.Model):
    DISCIPLINE_CHOICES = (
        ('en', 'English'),
        ('es', 'Spanish'),
        ('ma', 'mathematics'),
        ('ci', 'Science'),
        ('hi', 'History'),
        ('ar', 'art'),
        ('ge', 'geography'),
        ('fi', 'Filosophy'),
        ('pe', 'Physical Education'),
        ('re', 'Religion')
    )

    discipline_id = models.AutoField(primary_key=True),
    discipline_name = models.CharField(max_length=30, choices=DISCIPLINE_CHOICES, verbose_name='Discipline')
    discipline_teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, related_name='disciplineteacher', verbose_name='Teacher', null=True)

    class Meta:
        verbose_name = 'Discipline'
        verbose_name_plural = 'Disciplines'
        constraints = [
            models.UniqueConstraint(fields=['discipline_name', 'discipline_teacher'], name='unique_discipline_teacher')
        ]
        ordering = ['discipline_name', 'discipline_teacher']

    def __str__(self):
        return '{} - {}'.format(
            self.discipline_name_display(),
            self.discipline_teacher
        )