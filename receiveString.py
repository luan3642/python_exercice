def recebeVogal(vogal):
    vogais = 'aeiouAEIOU'
    if vogal in vogais:
        return "*"
    return vogal

print(recebeVogal("b"))