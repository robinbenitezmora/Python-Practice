'''
Module with Validators for validators attributes fields in models
'''

# TODO - change if not use masks with JQuery - alphanumeric

from django.core.exceptions import ValidationError
from datetime import date

# ---- General Validators ---- #
def validate_digits(value):
    '''
    Validate if value is only digits
    '''
    if not value.isdigit():
        raise ValidationError('This field must contain only digits')

    else:
        return value

def validate_alpha(value):
    '''
    Validate if value is only alpha
    '''
    if any(n.isdigit() for n in value):
        raise ValidationError('This field must contain only alpha characters')

    else:
        return value

def validate_data_nasc(value):
    '''
    Validate if value is a valid date
    '''
    if value > date.today():
        raise ValidationError('The date of birth is wrong')

    else:
        return value

# ---- Documents Validators ---- #
def validate_cpf(value):
    '''
    Validate if value is a valid CPF
    '''
    if len(value) != 14:
        raise ValidationError('CPF must have 14 characters')

    else:
        cpf = value.replace('.', '').replace('-', '')
        if len(cpf) != 11:
            raise ValidationError('CPF must have 11 digits')

        else:
            if cpf == '00000000000' or cpf == '11111111111' or cpf == '22222222222' or cpf == '33333333333' or cpf == '44444444444' or cpf == '55555555555' or cpf == '66666666666' or cpf == '77777777777' or cpf == '88888888888' or cpf == '99999999999':
                raise ValidationError('CPF is invalid')

            else:
                sum = 0
                for i in range(9):
                    sum += int(cpf[i]) * (10 - i)

                rest = 11 - (sum % 11)
                if rest == 10 or rest == 11:
                    rest = 0

                if rest != int(cpf[9]):
                    raise ValidationError('CPF is invalid')

                else:
                    sum = 0
                    for i in range(10):
                        sum += int(cpf[i]) * (11 - i)

                    rest = 11 - (sum % 11)
                    if rest == 10 or resto == 11:
                        rest = 0

                    if rest != int(cpf[10]):
                        raise ValidationError('CPF is invalid')

                    else:
                        return value

def validate_born_certified(value):
    '''
    Validate if value is a valid Born Certified
    '''
    if len(value) != 15:
        raise ValidationError('Born Certified must have 15 characters')

    else:
        if value[0] != 'R':
            raise ValidationError('Born Certified must start with R')

        else:
            if not value[1:].isdigit():
                raise ValidationError('Born Certified must have only digits')

            else:
                return value

# ---- Contact Validators ---- #
def validate_cep(value):
    '''
    Validate if value is a valid CEP
    '''
    if len(value) != 9:
        raise ValidationError('CEP must have 8 characters')

    else:
        cep = value.replace('-', '')
        if len(cep) != 8:
            raise ValidationError('CEP must have 8 digits')

        else:
            return value

def validate_ddd(value):
    '''
    Validate if value is a valid DDD
    '''
    if len(value) != 4:
        raise ValidationError('DDD must have 4 characters')

    else:
        if value[0] != '(':
            raise ValidationError('DDD must start with (')

        else:
            if value[3] != ')':
                raise ValidationError('DDD must end with )')

            else:
                if not value[1:3].isdigit():
                    raise ValidationError('DDD must have only digits')

                else:
                    return value

def validate_phone(value):
    '''
    Validate if value is a valid Phone
    '''
    if len(value) != 14:
        raise ValidationError('Phone must have 13 characters')

    else:
        phone = value.replace('-', '').replace('(', '').replace(')', '')
        if len(phone) != 11:
            raise ValidationError('Phone must have 11 digits')

        else:
            return value

# ---- Student Validators ---- #
def validate_student_inep(value):
    '''
    Validate if value is a valid INEP
    '''
    if len(value) != 12:
        raise ValidationError('INEP must have 12 characters')

    else:
        if not value.isdigit():
            raise ValidationError('INEP must have only digits')

        else:
            return value

# ---- School Validators ---- #
def validate_lective_year(value):
    '''
    Validate if value is a valid Lective Year
    '''
    if len(value) != 4:
        raise ValidationError('Lective Year must have 4 characters')

    else:
        if not value.isdigit():
            raise ValidationError('Lective Year must have only digits')

        else:
            return value
