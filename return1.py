def greet(lang):
    if lang == 'en':
        return 'Hello'
    elif lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return "language not supported"
print(greet('en')) #'en' means english
    