from django.db import models

from base import constants

from base.validators import (
    validate_digits,
    validate_no_digits,
    validate_data,
    validate_teacher_inep,
    validate_cpf,
    validate_ddd,
    validate_phone,
    validate_cep,
    validate_year,
)

from base.models import KnowledgeArea, CourseFS, City, country

class Teacher(models.Model):

    CHOICES_TEACHER_SITUATION = (
        ('0', 'Competitive'),
		('1', 'CLT'),
		('2', 'Temporary'),
		('3', 'Substitute'),
		('4', 'Trainee'),
		('5', 'Outsourced'),
		('6', 'Curriculum'),
		('7', 'Certificate'),
		('8', 'Dismissed')
    )

    CHOICES_TEACHER_JUSTIFICATION_DOCUMENTS = (
        ('1', 'The student does not have the requested documents'),
        ('2', 'The school has not received the requested documents')
    )

    CHOICES_TEACHER_COLOR = (
        ('0', 'Undeclared'),
        ('1', 'White'),
        ('2', 'Black'),
        ('3', 'Brown'),
        ('4', 'Yellow'),
        ('5', 'Indigenous'),
    )

    CHOICES_TEACHER_SEX = (
        ('1', 'Male'),
        ('2', 'Female'),
    )

    CHOICES_TEACHER_NATIONALITY = (
        ('1', 'Colombian'),
        ('2', 'Naturalized Colombian'),
        ('3', 'Foreign'),
    )

    CHOICES_TEACHER_STATE = (
        ('AM', 'Amazonas'), ('ANT', 'Antioquia'), ('AR', 'Arauca'), 
        ('ATL', 'Atlantico'), ('BOL', 'Bolivar'), ('BOY', 'Boyaca'), 
        ('CAL', 'Caldas'), ('CAQ', 'Caqueta'), ('CAS', 'Casanare'), 
        ('CAU', 'Cauca'), ('CES', 'Cesar'), ('CHO', 'Choco'), 
        ('CUND', 'Cundinamarca'), ('COR', 'Cordoba'), 
        ('DC', 'Distrito Capital de Bogota'), ('GUA', 'Guainia'), 
        ('GUA', 'GUAVIARE'), ('HUI', 'Huila'), ('LAG', 'La Guajira'), 
        ('MAG', 'Magdalena'), ('MET', 'Meta'), ('NAR', 'Narino'), 
        ('NSA', 'Norte de Santander'), ('PUT', 'Putumayo'), 
        ('QUI', 'Quindio'), ('RIS', 'Risaralda'), 
        ('SAP', 'San Andres, Providencia y Santa Catalina'), 
        ('SAN', 'Santander'), ('SUC', 'Sucre'), ('TOL', 'Tolima'), 
        ('VAC', 'Valle del Cauca'), ('VAU', 'Vaupes'), ('VID', 'VICHADA')
    )

    CHOICES_TEACHER_ZONE = (
        ('1', 'Urban'),
        ('2', 'Rural'),
    )

    CHOICES_TEACHER_DIFFERENTIATED_ZONE = (
        ('1', 'Settlement area'),
		('2', 'Indigenous land'),
		('3', 'Quilombola area'),
		('7', 'Not in a differentiated location')
    )

    CHOICES_AFFILIATION = (
        ('0', 'Not declared/Ignored'),
		('1', 'Affiliation 1 and/or Affiliation 2')
    )

    CHOICES_YES_NO = (
        ('0', 'No'),
        ('1', 'Yes'),
    )

    CHOICES_TEACHING_OTHER_PLACE = (
        ('1', 'No'),
		('2', 'Hospital'),
		('3', 'Home'),
		('4', 'Outdoor facilities')
    )

    CHOICES_EDUCATION_LEVEL = (
		('1', 'Did not complete elementary school'),
		('2', 'Elementary school'),
		('7', 'High school'),
		('6', 'Higher education')
	)

    CHOICES_MEDIUM_EDUCATION_TYPE = (
        ('1', 'General education'),
        ('2', 'Normal education'),
        ('3', 'Technical course'),
        ('4', 'Indigenous teaching, normal mode')
    )

    teacher_id = models.AutoField(
        primary_key=True,
    )

    teacher_situation = models.CharField(
        max_length=1,
        choices=CHOICES_TEACHER_SITUATION,
        verbose_name='Situatin of Teacher',
    )

    teacher_inep = models.CharField(
        max_length=12,
        validators=[validate_teacher_inep],
        verbose_name='Teacher INEP',
        blak=True,
        null=True,
        unique=True,
        validators=[validate_teacher_inep, validate_digits]
    )

    teacher_cpf = models.CharField(
        max_length=11,
        validators=[validate_cpf],
        verbose_name='Teacher CPF',
        blank=True,
        null=True,
        unique=True,
    )

    teacher_rg = models.CharField(
        max_length=20,
        verbose_name='Teacher RG',
        blank=True,
        null=True,
        unique=True,
    )

    teacher_name = models.CharField(
        max_length=100,
        verbose_name='Teacher Name',
        validators=[validate_no_digits],
    )

    teacher_birth_date = models.CharField(
        max_length=10,
        verbose_name='Teacher Birth Date',
        validators=[validate_data],
    )

    teacher_sex = models.CharField(
        max_length=1,
        choices=CHOICES_TEACHER_SEX,
        verbose_name='Sex'
    )

    teacher_color = models.CharField(
        max_length=1,
        choices=CHOICES_TEACHER_COLOR,
        verbose_name='Color / Race',
        default='0',
    )

    teacher_nationality = models.CharField(
        max_length=1,
        choices=CHOICES_TEACHER_NATIONAL,
        verbose_name='Nationality',
        default='1',
    )

    teacher_birth_country = models.ForeignKey(
        Country,
        on_delete=models.DO_NOTHING,
        verbose_name='Birth Country',
        related_name='teacherbirthcountry',
        default=constants.COUNTRY,
    )

    teacher_birth_state = models.CharField(
        max_length=4,
        choices=CHOICES_TEACHER_STATE,
        verbose_name='Birth State',
        blank=True,
    )

    teacher_birth_city = models.CharField(
        max_length=100,
        verbose_name='Birth City',
        blank=True,
    )

    teacher_residence_street = models.CharField(
        max_length=100,
        verbose_name='Residence Street',
        blank=True,
    )

    teacher_residence_number = models.CharField(
        max_length=10,
        verbose_name='Residence Number',
        blank=True,
    )

    teacher_residence_complement = models.CharField(
        max_length=100,
        verbose_name='Residence Complement',
        blank=True,
    )

    teacher_residence_zone = models.CharField(
        max_length=1,
        choices=CHOICES_TEACHER_ZONE,
        verbose_name='Residence Zone',
        blank=True,
    )

    teacher_residence_location = models.CharField(
        max_length=1,
        choices=CHOICES_TEACHER_DIFFERENTIATED_ZONE,
        verbose_name='Residence Location',
        blank=True,
    )

    teacher_residence_neighborhood = models.CharField(
        max_length=100,
        verbose_name='Residence Neighborhood',
        blank=True,
    )

    teacher_residence_cep = models.CharField(
        max_length=8,
        verbose_name='Residence CEP',
        validators=[validate_cep],
        blank=True,
    )

    teacher_residence_state = models.CharField(
        max_length=4,
        choices=CHOICES_TEACHER_STATE,
        verbose_name='Residence State',
        blank=True,
    )

    teacher_residence_city = models.CharField(
        max_length=100,
        verbose_name='Residence City',
        blank=True,
    )

    teacher_residence_country = models.ForeignKey(
        Country,
        on_delete=models.DO_NOTHING,
        verbose_name='Residence Country',
        related_name='teacherresidencecountry',
        default=constants.COUNTRY,
    )

    teacher_ddd = models.CharField(
        max_length=2,
        validators=[validate_ddd],
        verbose_name='Teacher DDD',
        blank=True,
    )

    teacher_phone = models.CharField(
        max_length=9,
        validators=[validate_phone],
        verbose_name='Teacher Phone',
        blank=True,
    )
    
    teacher_email = models.EmailField(
        max_length=100,
        verbose_name='Teacher Email',
        blank=True,
    )

    teacher_affiliation = models.CharField(
        max_length=1,
        choices=CHOICES_AFFILIATION,
        verbose_name='Affiliation',
        default='0',
    )

    teacher_affiliation_1_name = models.CharField(
        max_length=100,
        verbose_name='Affiliation 1 Name',
        blank=True,
        validators=[validate_no_digits],
    )

    teacher_affiliation_2_name = models.CharField(
        max_length=100,
        verbose_name='Affiliation 2 Name',
        blank=True,
        validators=[validate_no_digits],
    )

    other_place_teacher = models.CharField(
        max_length=1,
        choices=CHOICES_TEACHING_OTHER_PLACE,
        verbose_name='Teaching in another place',
        default='1',
    )

    teacher_education_level = models.CharField(
        max_length=1,
        choices=CHOICES_EDUCATION_LEVEL,
        verbose_name='Education Level',
        default='1',
    )

    teacher_medium_education_type = models.CharField(
        max_length=1,
        choices=CHOICES_MEDIUM_EDUCATION_TYPE,
        verbose_name='Medium Education Type',
        default='1',
    )

    teacher_course_1 = models.ForeignKey(
        CourseFS,
        on_delete=models.DO_NOTHING,
        verbose_name='Course 1',
        related_name='teacher_course_1',
        blank=True,
        null=True,
    )

    professor_course_conclusion1 = models.CharField(
        max_length=4,
        validators=[validate_year, validate_digits],
        verbose_name='Course Conclusion 1',
        blank=True,
    )

    teacher_course_public_1 = models.CharField(
        max_length=1,
        verbose_name='Course Public 1',
        blank=True,
    )

    teacher_course_private_1 = models.CharField(
        max_length=1,
        verbose_name='Course Private 1',
        blank=True,
    )

    teacher_course_institution_1 = models.CharField(
        max_length=100,
        verbose_name='Course Institution 1',
        blank=True,
    )

    teacher_course_2 = models.ForeignKey(
        CourseFS,
        on_delete=models.DO_NOTHING,
        verbose_name='Course 2',
        related_name='teacher_course_2',
        blank=True,
        null=True,
    )

    professor_course_conclusion2 = models.CharField(
        max_length=4,
        validators=[validate_year, validate_digits],
        verbose_name='Course Conclusion 2',
        blank=True,
    )

    teacher_course_public_2 = models.CharField(
        max_length=1,
        verbose_name='Course Public 2',
        blank=True,
    )

    teacher_course_private_2 = models.CharField(
        max_length=1,
        verbose_name='Course Private 2',
        blank=True,
    )

    teacher_course_institution_2 = models.CharField(
        max_length=100,
        verbose_name='Course Institution 2',
        blank=True,
    )

    teacher_course_3 = models.ForeignKey(
        CourseFS,
        on_delete=models.DO_NOTHING,
        verbose_name='Course 3',
        related_name='teacher_course_3',
        blank=True,
        null=True,
    )

    professor_course_conclusion3 = models.CharField(
        max_length=4,
        validators=[validate_year, validate_digits],
        verbose_name='Course Conclusion 3',
        blank=True,
    )

    teacher_course_public_3 = models.CharField(
        max_length=1,
        verbose_name='Course Public 3',
        blank=True,
    )

    teacher_course_private_3 = models.CharField(
        max_length=1,
        verbose_name='Course Private 3',
        blank=True,
    )

    teacher_course_institution_3 = models.CharField(
        max_length=100,
        verbose_name='Course Institution 3',
        blank=True,
    )

    teacher_knowdledge_area_1 = models.ForeignKey(
        KnowledgeArea,
        on_delete=models.DO_NOTHING,
        verbose_name='Knowledge Area 1',
        related_name='teacher_knowledge_area_1',
        blank=True,
        null=True,
    )

    teacher_knowdledge_area_2 = models.ForeignKey(
        KnowledgeArea,
        on_delete=models.DO_NOTHING,
        verbose_name='Knowledge Area 2',
        related_name='teacher_knowledge_area_2',
        blank=True,
        null=True,
    )

    teacher_knowdledge_area_3 = models.ForeignKey(
        KnowledgeArea,
        on_delete=models.DO_NOTHING,
        verbose_name='Knowledge Area 3',
        related_name='teacher_knowledge_area_3',
        blank=True,
        null=True,
    )

    teacher_pos_graduation_completed = models.CharField(
        max_length=1,
        choices=CHOICES_YES_NO,
        verbose_name='Post-Graduation Completed',
    )

    teacher_specialization = models.CharField(
        max_length=1,
        verbose_name='Specialization',
        blank=True,
    )

    teacher_master_degree = models.CharField(
        max_length=1,
        verbose_name='Master Degree',
        blank=True,
    )

    teacher_doctorate = models.CharField(
        max_length=1,
        verbose_name='Doctorate',
        blank=True,
    )

    teacher_others_courses = models.CharField(
        max_length=1,
        verbose_name='Others Courses',
        choices=CHOICES_YES_NO
    )

    teacher_course_creche = models.CharField(
        max_length=1,
        verbose_name='Course Creche',
        blank=True,
    )

    teacher_course_kindergarten = models.CharField(
        max_length=1,
        verbose_name='Course Kindergarten',
        blank=True,
    )

    teacher_course_fundamental_1 = models.CharField(
        max_length=1,
        verbose_name='Course Fundamental 1',
        blank=True,
    )

    teacher_course_fundamental_2 = models.CharField(
        max_length=1,
        verbose_name='Course Fundamental 2',
        blank=True,
    )

    teacher_high_school_course = models.CharField(
        max_length=1,
        verbose_name='High School Course',
        blank=True,
    )

    teacher_course_young_adults = models.CharField(
        max_length=1,
        verbose_name='Course Young Adults',
        blank=True,
    )

    teacher_course_indigenous_education = models.CharField(
        max_length=1,
        verbose_name='Course Indigenous Education',
        blank=True,
    )

    teacher_course_field_education = models.CharField(
        max_length=1,
        verbose_name='Course Field Education',
        blank=True,
    )

    teacher_course_environmental_education = modeld.CharField(
        max_length=1,
        verbose_name='Course Environmental Education',
        blank=True,
    )

    teacher_course_human_rights = models.CharField(
        max_length=1,
        verbose_name='Course Human Rights',
        blank=True,
    )

    teacher_course_sexual_diversity = models.CharField(
        max_length=1,
        verbose_name='Course Sexual Diversity',
        blank=True,
    )

    teacher_course_child_rights = models.CharField(
        max_length=1,
        verbose_name='Course Child Rights',
        blank=True,
    )

    teacher_course_ethnic_relations = models.CharField(
        max_length=1,
        verbose_name='Course for ethnic relationship',
        blank=True,
    )

    teacher_course_school_management = models.CharField(
        max_length=1,
        verbose_name='Course School Management',
        blank=True,
    )

    teacher_course_others = models.CharField(
        max_length=1,
        verbose_name='Course Others',
        blank=True,
    )

    teacher_justification_documents = models.CharField(
        max_length=1,
        choices=CHOICES_TEACHER_JUSTIFICATION_DOCUMENTS,
        verbose_name='Justification Documents',
        blank=True,
    )

    teacher_physical_dificiency = models.CharField(
        max_length=1,
        choices=CHOICES_YES_NO,
        verbose_name='Physical Dificiency',
    )

    teacher_low_vision = models.CharField(
        max_length=1,
        choices=CHOICES_YES_NO,
        verbose_name='Low Vision',
    )

    teacher_blindness = models.CharField(
        max_length=1,
        choices=CHOICES_YES_NO,
        verbose_name='Blindness',
    )

    teacher_deafness = models.CharField(
        max_length=1,
        choices=CHOICES_YES_NO,
        verbose_name='Deafness',
    )

    teacher_hearing_loss = models.CharField(
        max_length=1,
        choices=CHOICES_YES_NO,
        verbose_name='Hearing Loss',
    )

    teacher_deafblindness = models.CharField(
        max_length=1,
        choices=CHOICES_YES_NO,
        verbose_name='Deafblindness',
    )

    teacher_physical_disability = models.CharField(
        max_length=1,
        choices=CHOICES_YES_NO,
        verbose_name='Physical Disability',
    )

    teacher_intelectual_disability = models.CharField(
        max_length=1,
        choices=CHOICES_YES_NO,
        verbose_name='Intelectual Disability',
    )

    teacher_multiple_disabilities = models.CharField(
        max_length=1,
        choices=CHOICES_YES_NO,
        verbose_name='Multiple Disabilities',
    )
    
    teacher_autism = models.CharField(
        max_length=1,
        choices=CHOICES_YES_NO,
        verbose_name='Autism',
    )

    teacher_asperger_syndrome = models.CharField(
        max_length=1,
        choices=CHOICES_YES_NO,
        verbose_name='Asperger Syndrome',
    )

    teacher_urgency_name = models.CharField(
        max_length=100,
        verbose_name='Urgency Name',
        blank=True,
    )

    teacher_urgency_ddd = models.CharField(
        max_length=2,
        validators=[validate_ddd, validate_digits],
        verbose_name='Urgency DDD',
        blank=True,
    )

    teacher_urgency_phone = models.CharField(
        max_length=9,
        validators=[validate_phone, validate_digits],
        verbose_name='Urgency Phone',
        blank=True,
    )

    teacher_urgency_kinship = models.CharField(
        max_length=100,
        verbose_name='Urgency Kinship',
        blank=True,
    )

    teacher_urgency_procedures = models.CharField(
        max_length=1,
        verbose_name='Urgency Procedures',
        blank=True,
    )

    teacher_alergy = models.CharField(
        max_length=1,
        verbose_name='Alergy',
        blank=True,
    )

    teacher_alergy_type = models.TextField(
        verbose_name='Alergy Type',
        max_length=1000,
        blank=True,
    )

    teacher_differenciat_care = models.TextField(
        verbose_name='Differentiated Care',
        max_length=1000,
        blank=True,
    )

    teacher_health_plan = models.CharField(
        max_length=100,
        verbose_name='Health Plan',
        blank=True,
    )

    teacher_health_plan_name = models.CharField(
        max_length=100,
        verbose_name='Health Plan Name',
        blank=True,
    )

    teacher_health_plan_ddd = models.CharField(
        max_length=2,
        validators=[validate_ddd, validate_digits],
        verbose_name='Health Plan DDD',
        blank=True,
    )

    teacher_health_plan_phone = models.CharField(
        max_length=9,
        validators=[validate_phone, validate_digits],
        verbose_name='Health Plan Phone',
        blank=True,
    )

    teacher_health_plan_email = models.EmailField(
        max_length=100,
        verbose_name='Health Plan Email',
        blank=True,
    )

    teacher_agreement = models.CharField(
        max_length=1,
        verbose_name='Agreement',
        blank=True,
    )

    teacher_agreement_name = models.CharField(
        max_length=100,
        verbose_name='Agreement Name',
        blank=True,
    )

    teacher_agreement_ddd = models.CharField(
        max_length=2,
        validators=[validate_ddd, validate_digits],
        verbose_name='Agreement DDD',
        blank=True,
    )

    teacher_agreement_phone = models.CharField(
        max_length=9,
        validators=[validate_phone, validate_digits],
        verbose_name='Agreement Phone',
        blank=True,
    )

    teacher_social_program = models.CharField(
        max_length=1,
        verbose_name='Social Program',
        blank=True,
    )

    teacher_social_program_name = models.CharField(
        max_length=100,
        verbose_name='Social Program Name',
        blank=True,
    )

    teacher_social_program_ddd = models.CharField(
        max_length=2,
        validators=[validate_ddd, validate_digits],
        verbose_name='Social Program DDD',
        blank=True,
    )

    teacher_social_program_phone = models.CharField(
        max_length=9,
        validators=[validate_phone, validate_digits],
        verbose_name='Social Program Phone',
        blank=True,
    )

    teacher_social_program_email = models.EmailField(
        max_length=100,
        verbose_name='Social Program Email',
        blank=True,
    )


    teacher_internship = models.CharField(
        max_length=1,
        verbose_name='Internship',
        blank=True,
    )

    teacher_institution_intership = models.CharField(
        max_length=100,
        verbose_name='Institution Internship',
        blank=True,
    )

    teacher_comments_intership = models.TextField(
        verbose_name='Comments Internship',
        max_length=1000,
        blank=True,
    )

    teacher_comments = models.TextField(
        verbose_name='Comments',
        max_length=1000,
        blank=True,
    )

    created = models.DateTimeField('Creation Date', auto_now_add=True)
    modified = models.DateTimeField('Modification Date', auto_now=True)

    def teacher_code_id(self):
        '''
            Return custom unique identification
        '''

        return 'pr-' + str(self.teacher_id)

        class Meta:
            verbose_name = 'Teacher'
            verbose_name_plural = 'Teachers'
            ordering = ['teacher_name']

        def __str__(self):
            return self.teacher_name
