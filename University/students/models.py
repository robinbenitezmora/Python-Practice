from django.db import models
from datetime import datetime

from base import constants

from base.validators import (
    validate_digits,
    validate_no_digits,
    validate_data_birth,
    validate_student_inep,
    validate_cpf,
    validate_ddd,
    validate_phone,
    validate_cep,
    validate_nis,
    validate_birth_certified,
)

from base.models import City, Country

class Student(models.Model):

    CHOICES_STUDENT_JUSTIFICATION_DOCUMENTS = (
        ('1', '0 student does not have the requested documents'),
        ('2', 'The school has not received the requested documents')
    )

    CHOICES_STUDENT_COLOR = (
        ('0', 'Not declared')
        ('1', 'White'),
        ('2', 'Black'),
        ('3', 'Brown'),
        ('4', 'Yellow'),
        ('5', 'Indigenous'),       
    )

    CHOICES_STUDENT_SEX = (
        ('1', 'Male'),
        ('2', 'Female')
    )

    CHOICES_STUDENT_NATIONALITY = (
        ('1', 'Colombian'),
        ('2', 'Naturalized'),
        ('3', 'Foreign')
    )

    CHOICES_STUDENT_STATE = (
        ('AM', 'Amazonas'),
        ('AR', 'Arauca'),
        ('AT', 'Atlántico'),
        ('BO', 'Bolívar'),
        ('CA', 'Caldas'),
        ('CAQ', 'Caquetá'),
        ('CAS', 'Casanare'),
        ('C', 'Cauca'),
        ('CH', 'Chocó'),
        ('CO', 'Córdoba'),
        ('CU', 'Cundinamarca'),
        ('GU', 'Guainía'),
        ('G', 'Guaviare'),
        ('H', 'Huila'),
        ('GUA', 'La Guajira'),
        ('MAG', 'Magdalena'),
        ('META', 'Meta'),
        ('NAR', 'Nariño'),
        ('N', 'Norte de Santander'),
        ('PUT', 'Putumayo'),
        ('QU', 'Quindío'),
        ('RIS', 'Risaralda'),
        ('SAP', 'San Andrés y Providencia'),
        ('SAN', 'Santander'),
        ('SUC', 'Sucre'),
        ('TOL', 'Tolima'),
        ('V', 'Valle del Cauca'),
        ('VAU', 'Vaupés'),
        ('VICH', 'Vichada'),
    )

    CHOICES_STUDENT_ZONE = (
        ('1', 'Urban'),
        ('2', 'Rural')
    )

    CHOICES_STUDENT_DIFFERENTIATED_ZONE = (
        ('1', 'Settlement area'),
        ('2', 'Indigenous land'),
        ('3', 'Not in a differentiate location'),
    )

    CHOICES_AFFILIATION = (
        ('0', 'Not declared/Ignored'),
        ('1', 'Affiliation 1 and/or Affiliation 2')
    )

    CHOICES_SCHOOL_OUTING = (
        ('1', 'Accompanied'),
		('2', 'Alone'),
		('3', 'School transport (accompanied)')
	)

    CHOICES_TEACHING_OTHER_PLACE = (
		('1', 'No'),
		('2', 'Hospital'),
		('3', 'Home'),
		('4', 'Outdoor facilities')
	)

    CHOICES_POWER_RESPONSIBLE_TRANSPORT = (
		('1', 'State'),
		('2', 'Municipal')
	)

    CHOICES_YES_NO = (
        ('1', 'Yes'),
        ('2', 'No')
    )

    # Use for personal code in school
    student_id = models.AutoField(
        primary_key=True,
    )

    # ---- Student Documents ---- #
    studen_inep = models.CharField(
        max_length=12,
        validators=[validate_student_inep, validate_digits],
        blank=True,
        null=True,
        unique=True,
        verbose_name='INEP',
    )

    student_cpf = models.CharField(
        max_length=14,
        validators=[validate_cpf],
        blank=True,
        null=True,
        unique=True,
        verbose_name='CPF',
    )

    student_rg = models.CharField(
        max_length=20,
        validators=[validate_no_digits],
        blank=True,
        null=True,
        verbose_name='RG',
    )


    student_nis = models.CharField(
        max_length=11,
        validators=[validate_nis, validate_digits],
        blank=True,
        null=True,
        unique=True,
        verbose_name='NIS',
    )

    student_birth_certified = models.CharField(
        max_length=20,
        validators=[validate_birth_certified],
        blank=True,
        null=True,
        unique=True,
        verbose_name='Birth Certified',
    )

    student_justification_documents = models.CharField(
        max_length=1,
        choices=CHOICES_STUDENT_JUSTIFICATION_DOCUMENTS,
        blank=True,
        verbose_name='Justification Documents',
    )

    student_name = models.CharField(
        max_length=100,
        validators=[validate_no_digits],
        verbose_name='Name',
    )

    student_birth_data = models.CharField(
        max_length=10,
        validators=[validate_data_birth],
        verbose_name='Birth Data',
    )

    student_sex = models.CharField(
        max_length=1,
        choices=CHOICES_STUDENT_SEX,
    )

    student_color = models.CharField(
        max_length=1,
        choices=CHOICES_STUDENT_COLOR,
        default='0'
    )

    student_nationality = models.CharField(
        max_length=1,
        choices=CHOICES_STUDENT_NATIONAL,
        verbose_name='Nationality',
        default='1'
    )

    student_country = models.ForeignKey(
        Country,
        on_delete=models.DO_NOTHING,
        verbose_name='Birth Country',
        related_name='studentparentsbirth',
        default=constants.COUNTRY,
    )

    student_state = models.CharField(
        max_length=4,
        choices=CHOICES_STUDENT_STATE,
        blank=True,
        verbose_name='State',
        default='CO',
    )


    student_city = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Birth City',
    )

    student_residence_location = models.CharField(
        max_length=100,
        choices=CHOICES_STUDENT_ZONE,
        verbose_name='Residence Location',
    )

    student_residence_number = models.CharField(
        max_length=10,
        verbose_name='Residence Number',
    )

    student_residence_complement = models.CharField(
        max_length=100,
        verbose_name='Residence Complement',
        blank=True,
    )

    student_residence_location = models.CharField(
        max_length=1,
        choices=CHOICES_STUDENT_DIFFERENTIATED_ZONE,
        verbose_name='Residence Location',
        default='7',
    )

    student_residence_neighborhood = models.CharField(
        max_length=100,
        verbose_name='Residence Neighborhood',
        blank=True,
    )

    student_residence_cep = models.CharField(
        max_length=9,
        validators=[validate_cep],
        verbose_name='CEP',
    )

    student_residence_state = models.CharField(
        max_length=4,
        choices=CHOICES_STUDENT_STATE,
        verbose_name='State',
        default=constants.STATE,
    )

    student_residence_city = models.ForeignKey(
        City,
        on_delete=models.DO_NOTHING,
        verbose_name='City',
        related_name='studentresidencecity',
        default=constants.CITY,
    )

    # ---- Student Contact ---- #
    student_ddd = models.CharField(
        max_length=2,
        validators=[validate_ddd, validate_digits],
        verbose_name='Student - DDD Telephone',
        blank=True,
    )

    student_phone = models.CharField(
        max_length=9,
        validators=[validate_phone, validate_digits],
        verbose_name='Student - Telephone',
        blank=True,
    )

    student_email = models.EmailField(
        verbose_name='Student - Email',
        blank=True,
        max_length=250,
        null=True,
        unique=True,
    )

    # ---- Student Family ---- #
    student_responsible = models.CharField(
        max_length=1,
        choices=CHOICES_AFFILIATION,
        verbose_name='Affiliation',
    )

    student_responsible1_name = models.CharField(
        max_length=100,
        validators=[validate_no_digits],
        verbose_name='Responsible 1 Name',
    )

    student_responsible1_cpf = models.CharField(
        max_length=14,
        validators=[validate_cpf],
        verbose_name='Responsible 1 CPF',
        blank=True,
    )

    student_responsible1_rg = models.CharField(
        max_length=20,
        validators=[validate_no_digits],
        verbose_name='Responsible1 RG',
        blank=True,
    )

    student_responsible1_ddd1 = models.CharField(
        max_length=2,
        validators=[validate_ddd, validate_digits],
        verbose_name='Responsible 1 - DDD Telephone 1',
        blank=True,
    )

    student_responsible1_phone1 = models.CharField(
        max_length=9,
        validators=[validate_phone, validate_digits],
        verbose_name='Responsible - Telephone 1',
        blank=True,
    )

    student_responsible1_ddd2 = models.CharField(
        max_length=2,
        validators=[validate_ddd, validate_digits],
        verbose_name='Responsible 1 - DDD Telephone 2',
        blank=True,
    )

    student_responsible1_phone2 = models.CharField(
        max_length=9,
        validators=[validate_phone, validate_digits],
        verbose_name='Responsible 1 - Telephone 2',
        blank=True,
    )

    student_responsible1_email = models.EmailField(
        verbose_name='Responsible 1 - Email',
        blank=True,
        max_length=250,
        null=True,
        unique=True,
    )

    student_responsible1_respon_educative = models.CharField(
        max_length=1,
        choices=CHOICES_YES_NO,
        verbose_name='Responsible 1 - Responsible for the student education',
    )

    student_responsible1_respon_financial = models.CharField(
        max_length=1,
        choices=CHOICES_YES_NO,
        verbose_name='Responsible 1 - Financially responsible for the student',
    )

    student_responsible1_respon_legal = models.CharField(
        max_length=1,
        choices=CHOICES_YES_NO,
        verbose_name='Responsible 1 - Legal responsible for the student',
    )

    student_responsible1_doc_guard = models.CharField(
        max_length=1,
        choices=CHOICES_YES_NO,
        verbose_name='Responsible 1 - Legal guardian',
    )

    student_responsible1_kinship = models.CharField(
        max_length=100,
        verbose_name='Responsible 1 - Kinship',
        blank=True,
    )

    student_responsible2_name = models.CharField(
        max_length=100,
        validators=[validate_no_digits],
        verbose_name='Responsible 2 Name',
        blank=True,
    )

    student_responsible2_cpf = models.CharField(
        max_length=14,
        validators=[validate_cpf],
        verbose_name='Responsible 2 CPF',
        blank=True,
    )

    student_responsible2_rg = models.CharField(
        max_length=20,
        validators=[validate_no_digits],
        verbose_name='Responsible 2 RG',
        blank=True,
    )

    student_responsible2_ddd1 = models.CharField(
        max_length=2,
        validators=[validate_ddd, validate_digits],
        verbose_name='Responsible 2 - DDD Telephone 1',
        blank=True,
    )

    student_responsible2_phone1 = models.CharField(
        max_length=9,
        validators=[validate_phone, validate_digits],
        verbose_name='Responsible 2 - Telephone 1',
        blank=True,
    )

    student_responsible2_ddd2 = models.CharField(
        max_length=2,
        validators=[validate_ddd, validate_digits],
        verbose_name='Responsible 2 - DDD Telephone 2',
        blank=True,
    )

    student_responsible2_phone2 = models.CharField(
        max_length=9,
        validators=[validate_phone, validate_digits],
        verbose_name='Responsible 2 - Telephone 2',
        blank=True,
    )

    student_responsible2_email = models.EmailField(
        verbose_name='Responsible 2 - Email',
        blank=True,
        max_length=250,
        null=True,
        unique=True,
    )

    student_responsible2_respon_educative = models.CharField(
        max_length=1,
        choices=CHOICES_YES_NO,
        verbose_name='Responsible 2 - Responsible for the student education',
        blank=True,
    )

    student_responsible2_respon_financial = models.CharField(
        max_length=1,
        choices=CHOICES_YES_NO,
        verbose_name='Responsible 2 - Financially responsible for the student',
        blank=True,
    )

    student_responsible2_respon_legal = models.CharField(
        max_length=1,
        choices=CHOICES_YES_NO,
        verbose_name='Responsible 2 - Legal responsible for the student',
        blank=True,
    )

    student_responsible2_doc_guard = models.CharField(
        max_length=1,
        choices=CHOICES_YES_NO,
        verbose_name='Responsible 2 - Legal guardian',
        blank=True,
    )

    student_responsible2_kinship = models.CharField(
        max_length=100,
        verbose_name='Responsible 2 - Kinship',
        blank=True,
    )

    # ---- Student Disabilities ---- #
    student_deficiency = models.CharField(
        max_length=1,
        choices=CHOICES_YES_NO,
        verbose_name='Physical Deficiency',
    )

    student_blindness = models.CharField(
        max_length=1,
        choices=CHOICES_YES_NO,
        verbose_name='Blindness',
    )

    student_low_vision = models.CharField(
        max_length=1,
        choices=CHOICES_YES_NO,
        verbose_name='Low Vision',
        blank=True,
    )

    student_deafness = models.CharField(
        max_length=1,
        choices=CHOICES_YES_NO,
        verbose_name='Deafness',
    )

    student_hearing_loss = models.CharField(
        max_length=1,
        choices=CHOICES_YES_NO,
        verbose_name='Hearing Loss',
        blank=True,
    )

    student_deafblindness = models.CharField(
        max_length=1,
        choices=CHOICES_YES_NO,
        verbose_name='Deafblindness',
        blank=True,
    )

    student_physical_disability = models.CharField(
        max_length=1,
        choices=CHOICES_YES_NO,
        verbose_name='Physical Disability',
    )

    student_intellectual_disability = models.CharField(
        max_length=1,
        choices=CHOICES_YES_NO,
        verbose_name='Intellectual Disability',
    )

    student_multiple_disabilities = models.CharField(
        max_length=1,
        choices=CHOICES_YES_NO,
        verbose_name='Multiple Disabilities',
    )

    student_autism = models.CharField(
        max_length=1,
        choices=CHOICES_YES_NO,
        verbose_name='Autism',
    )

    student_high_abilities = models.CharField(
        max_length=1,
        choices=CHOICES_YES_NO,
        verbose_name='High Abilities',
        blank=True,
    )

    # ---- Students with different needs ---- #

    student_need_special = models.CharField(
        max_length=1,
        choices=CHOICES_YES_NO,
        verbose_name='None Special Needs',
    )

    studnet_reader_assistance = models.CharField(
        max_length=1,
        choices=CHOICES_YES_NO,
        verbose_name='Reader Assistance',
    )

    student_aid_transcription = models.CharField(
        max_length=1,
        choices=CHOICES_YES_NO,
        verbose_name='Aid Transcription',
        blank=True,
    )

    student_need_interpreter = models.CharField(
        max_length=1,
        choices=CHOICES_YES_NO,
        verbose_name='Interpreter',
    )

    student_need_braille = models.CharField(
        max_length=1,
        choices=CHOICES_YES_NO,
        verbose_name='Braille',
    )

    student_need_libras = models.CharField(
        max_length=1,
        choices=CHOICES_YES_NO,
        verbose_name='Translator Libras',
    )

    student_need_lip_reading = models.CharField(
        max_length=1,
        choices=CHOICES_YES_NO,
        verbose_name='Lip Reading',
    )

    student_extended_proof18 = models.CharField(
        max_length=1,
        choices=CHOICES_YES_NO,
        verbose_name='Extended Proof (18)',
    )

    student_super_extended_proof24 = models.CharField(
        max_length=1,
        choices=CHOICES_YES_NO,
        verbose_name='Super Extended Proof (24)',
        blank=True,
    )

    student_cd_audio = models.CharField(
        max_length=1,
        choices=CHOICES_YES_NO,
        verbose_name='CD Audio',
    )

    student_portuguese_proof = models.CharField(
        max_length=1,
        choices=CHOICES_YES_NO,
        verbose_name='Portuguese Proof',
    )

    student_video_proof = models.CharField(
        max_length=1,
        choices=CHOICES_YES_NO,
        verbose_name='Video Proof',
    )

    student_school_outing = models.CharField(
        max_length=1,
        choices=CHOICES_SCHOOL_OUTING,
        verbose_name='School Outing',
        blank=True,
        default='1',
    )

    student_teaching_other_place = models.CharField(
        max_length=1,
        choices=CHOICES_TEACHING_OTHER_PLACE,
        verbose_name='Teaching in another place',
        blank=True,
    )

    # ---- Transport ---- #
    student_public_transport = models.CharField(
        max_length=1,
        choices=CHOICES_YES_NO,
        verbose_name='Public Transport',
    )

    student_power_transport = models.CharField(
        max_length=1,
        choices=CHOICES_POWER_RESPONSIBLE_TRANSPORT,
        verbose_name='Power Responsible Transport',
        blank=True,
    )

    # ----  Road transport ---- #

    student_private_road = models.CharField(
        max_length=1,
        choices=CHOICES_YES_NO,
        verbose_name='Private Road',
        blank=True,
    )

    student_bike_road = models.CharField(
        max_length=1,
        choices=CHOICES_YES_NO,
        verbose_name='Bike Road',
        blank=True,
    )

    student_animal_road = models.CharField(
        max_length=1,
        choices=CHOICES_YES_NO,
        verbose_name='Animal Road',
        blank=True,
    )

    student_minibuses_road = models.CharField(
        max_length=1,
        choices=CHOICES_YES_NO,
        verbose_name='Minibuses',
        blank=True,
    )

    student_bus_road = models.CharField(
        max_length=1,
        choices=CHOICES_YES_NO,
        verbose_name='Bus',
        blank=True,
    )

    student_van_road = models.CharField(
        max_length=1,
        choices=CHOICES_YES_NO,
        verbose_name='Van',
        blank=True,
    )

    student_other_road = models.CharField(
        max_length=1,
        choices=CHOICES_YES_NO,
        verbose_name='Other',
        blank=True,
    )

    # ----  Water Transport  ---- #

    student_private_water = models.CharField(
        max_length=1,
        choices=CHOICES_YES_NO,
        verbose_name='Private Water',
        blank=True,
    )

    student_5_water = models.CharField(
        max_length=1,
        choices=CHOICES_YES_NO,
        verbose_name='5 Seats',
        blank=True,
    )

    student_15_water = models.CharField(
        max_length=1,
        choices=CHOICES_YES_NO,
        verbose_name='15 Seats',
        blank=True,
    )

    student_35_water = models.CharField(
        max_length=1,
        choices=CHOICES_YES_NO,
        verbose_name='35 Seats',
        blank=True,
    )

    student_more_than_35_water = models.CharField(
        max_length=1,
        choices=CHOICES_YES_NO,
        verbose_name='More than 35 Seats',
        blank=True,
    )

    # ---- Urgency ---- #

    student_urgency1_name = models.CharField(
        max_length=100,
        validators=[validate_no_digits],
        verbose_name='Urgency 1 Name',
        blank=True,
    )

    student_urgency1_ddd = models.CharField(
        max_length=2,
        validators=[validate_ddd, validate_digits],
        verbose_name='Urgency 1 - DDD',
        blank=True,
    )

    student_urgency1_phone = models.CharField(
        max_length=9,
        validators=[validate_phone, validate_digits],
        verbose_name='Urgency 1 - Telephone',
        blank=True,
    )

    student_urgency1_kinship = models.CharField(
        max_length=100,
        verbose_name='Urgency 1 - Kinship',
        blank=True,
    )

    student_urgency2_name = models.CharField(
        max_length=100,
        validators=[validate_no_digits],
        verbose_name='Urgency 2 Name',
        blank=True,
    )

    student_urgency2_ddd = models.CharField(
        max_length=2,
        validators=[validate_ddd, validate_digits],
        verbose_name='Urgency 2 - DDD',
        blank=True,
    )

    student_urgency2_phone = models.CharField(
        max_length=9,
        validators=[validate_phone, validate_digits],
        verbose_name='Urgency 2 - Telephone',
        blank=True,
    )

    student_urgency2_kinship = models.CharField(
        max_length=100,
        verbose_name='Urgency 2 - Kinship',
        blank=True,
    )

    student_urgency_procedures = models.TextField(
        verbose_name='Urgency Procedures',
        blank=True,
    )

    # ---- Student Special Care  ---- #

    student_alergy = models.CharField(
        max_length=1,
        choices=CHOICES_YES_NO,
        verbose_name='Alergy',
    )

    student_alergy_description = models.TextField(
        max_length = 1000,
        verbose_name='Alergy Description',
        blank=True,
    )

    student_fitness_edfisica = models.CharField(
        max_length=1,
        choices=CHOICES_YES_NO,
        verbose_name='Fitness Education',
    )

    student_fitness_edfisica_justification = models.CharField(
        max_length=1000,
        verbose_name='Fitness Education Justification',
        blank=True,
    )

    student_medication = models.TextField(
        max_length = 1000,
        verbose_name='Instruction for Medication',
        blank=True,
    )

    student_differentiated_care = models.TextField(
        max_length = 1000,
        verbose_name='Differentiated Care',
        blank=True,
    )

    # ---- Health Plan ---- #

    student_health_plan = models.CharField(
        max_length=1,
        choices=CHOICES_YES_NO,
        verbose_name='Health Plan',
    )

    student_health_plan_name = models.CharField(
        max_length=100,
        verbose_name='Health Plan Name',
        blank=True,
    )

    student_health_plan_ddd = models.CharField(
        max_length=2,
        validators=[validate_ddd, validate_digits],
        verbose_name='Health Plan - DDD',
        blank=True,
    )

    student_health_plan_phone = models.CharField(
        max_length=9,
        validators=[validate_phone, validate_digits],
        verbose_name='Health Plan - Telephone',
        blank=True,
    )

    student_health_plan_email = models.EmailField(
        verbose_name='Health Plan - Email',
        blank=True,
        max_length=250,
        null=True,
        unique=True,
    )

    # ---- Agreements ---- #

    student_agreement = models.CharField(
        max_length=1,
        choices=CHOICES_YES_NO,
        verbose_name='Agreement',
        blank=True,
    )

    student_agreement_name = models.CharField(
        max_length=100,
        verbose_name='Agreement Name',
        blank=True,
    )

    student_agreement_ddd = models.CharField(
        max_length=2,
        validators=[validate_ddd, validate_digits],
        verbose_name='Agreement - DDD',
        blank=True,
    )

    student_agreement_phone = models.CharField(
        max_length=9,
        validators=[validate_phone, validate_digits],
        verbose_name='Agreement - Telephone',
        blank=True,
    )

    student_agreement_email = models.EmailField(
        verbose_name='Agreement - Email',
        blank=True,
        max_length=250,
        null=True,
        unique=True,
    )

    # ---- Social Program ---- #

    student_social_program = models.CharField(
        max_length=1,
        choices=CHOICES_YES_NO,
        verbose_name='Social Program',
        blank=True,
    )

    student_social_program_name = models.CharField(
        max_length=100,
        verbose_name='Social Program Name',
        blank=True,
    )

    student_social_program_ddd = models.CharField(
        max_length=2,
        validators=[validate_ddd, validate_digits],
        verbose_name='Social Program - DDD',
        blank=True,
    )

    student_social_program_phone = models.CharField(
        max_length=9,
        validators=[validate_phone, validate_digits],
        verbose_name='Social Program - Telephone',
        blank=True,
    )

    student_social_program_email = models.EmailField(
        verbose_name='Social Program - Email',
        blank=True,
        max_length=250,
        null=True,
        unique=True,
    )

    # ---- Bag ---- #

    student_bag = models.CharField(
        max_length=1,
        choices=CHOICES_YES_NO,
        verbose_name='Bag',
        blank=True,
    )

    student_bag_type = models.CharField(
        max_length=100,
        verbose_name='Bag Type',
        blank=True,
    )

    student_bag_reason = models.CharField(
        max_length=1000,
        verbose_name='Bag Reason',
        blank=True,
    )

    # ---- Observations ---- #

    student_observations = models.TextField(
        max_length=1000,
        verbose_name='Observations',
        blank=True,
    )

    # --- Date created or modified --- #

    created = models.DateTimeField('Date of Created', auto_now_add=True)
    modified = models.DateTimeField('Date of Modified', auto_now=True)

    def student_code_id(self):
        '''
        Return the student code id
        '''

        d1 = datetime.now().year
        dn = int(self.student_birth_data[-4:])

        return str(d1 - dn)

    class Meta:
            verbose_name = 'Student'
            verbose_name_plural = 'Students'
            ordering = ['student_name']

    def __str__(self):
        return self.student_name
