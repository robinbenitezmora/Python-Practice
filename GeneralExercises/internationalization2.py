
def local_greet(locale):
    locale = locale.split('_')[1][:2]
    if locale == 'US':
        return 'Hello'
    elif locale == 'GB':
        return 'Hi'
    elif locale == 'AU':
        return 'Howdy'
    elif locale == 'KR':
        return '안녕하세요'
    elif locale == 'CN':
        return '你好'
    elif locale == 'FR':
        return 'Bonjour'
    elif locale == 'DE':
        return 'Hallo'
    elif locale == 'ES':
        return 'Hola'
    elif locale == 'IT':
        return 'Ciao'
    elif locale == 'JP':
        return 'こんにちは'
    else:
        return f'I\'m not sure how to greet you in your locale: {locale}'

print(local_greet('en_US.UTF-8'))       # Hey!
print(local_greet('en_GB.UTF-8'))       # Hello!
print(local_greet('en_AU.UTF-8'))       # Howdy!
print(local_greet('ko_KR.UTF-16'))      # I'm not sure how to greet you in your locale: KR   
print(local_greet('zh_CN.UTF-8'))       # 你好!
print(local_greet('fr_FR.UTF-8'))       # Bonjour!
print(local_greet('de_DE.UTF-8'))       # Hallo!
print(local_greet('es_ES.UTF-8'))       # Hola!
print(local_greet('it_IT.UTF-8'))       # Ciao!
print(local_greet('ja_JP.UTF-8'))       # こんにちは!     