from django import template_name
from base.constants import CEP, CITY

register = template.Library()

@register.simple_tag
def set_constant_city(city):
    '''
    This function sets the city constant
    '''
    city = CITY
    return city

@register.simple_tag
def set_constant_cep(cep):
    '''
    This function sets the CEP constant
    '''
    cep = CEP
    return cep

