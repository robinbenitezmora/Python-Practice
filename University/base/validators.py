'''
    Module with Validators for validators attributes fields in models
'''

from django.core.exceptions import ValidationError
from datetime import date


# --- General Validators --- #
def validate_digits(value):
	if not value.isdigit():
		raise ValidationError('It only accepts numbers.')

	else:
		return value


def validate_no_digits(value):
	if any(n.isdigit() for n in value):
		raise ValidationError('This field does not accept numbers')

	else:
		return value


def validate_data(value):

	if len(value) != 10:
		raise ValidationError('The date is wrong')

	else:
		return value


def validate_year(value):

	if len(value) != 4:
		raise ValidationError('You need 4 digits')

	else:
		return value


# --- Documents Validators --- #
def validate_cpf(value):

	if len(value) != 14:
		raise ValidationError('The CPF requires 11 numbers')

	else:
		return value


def validate_nis(value):

	if len(value) != 11:
		raise ValidationError('The NIS requires 11 numbers')

	else:
		return value


def validate_birth_certificate(value):

	if len(value) != 40:
		raise ValidationError('The certificate needs 32 numbers')

	else:
		return value


# --- Contact Validators --- #
def validate_cep(value):

	if len(value) != 9:
		raise ValidationError('The CEP code needs 8 numbers')

	else:
		return value


def validate_ddd(value):
	if len(value) != 2:
		raise ValidationError('The DDD needs to have 2 numbers')

	else:
		return value


def validate_phone(value):

	if len(value) != 9:
		raise ValidationError('The phone needs to have 9 numbers')

	else:
		return value


# --- Aluno Validators --- #
def validate_student_inep(value):

	if len(value) != 12:
		raise ValidationError('Inep needs 12 numbers')

	else:
		return value


# --- Professor Validators --- #
def validate_teacher_inep(value):

	if len(value) != 12:
		raise ValidationError('Inep needs 12 numbers')

	else:
		return value


# --- School Validators --- #
def validate_lective_year(value):

	if len(value) != 4:
		raise ValidationError('The school year needs 4 numbers')

	else:
		return value
