from base import constants

def templates_global_context(request):
    '''
    This function sets the global context for the templates
    '''
    global_context = {
        'constant_ddd': constants.DDD,
        'constant_cep': constants.CEP,
        'constant_city': constants.CITY,
        'constant_country': constants.COUNTRY,
        'constant_state': constants.STATE,
        'constant_current_year': constants.CURRENT_YEAR,
    }

    return global_context