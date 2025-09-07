def greet(lang):
    greetings = {
        'en':'Hello', 'es': 'Hola',
        'fr': 'Bonjour',
        'ne': 'Namaste'
    }
    return greetings.get(lang,"Language not supported")
print(greet('en'))
print(greet('es'))
print(greet('fr'))
print(greet('ne'))
print(greet('jp')) #not supported language
