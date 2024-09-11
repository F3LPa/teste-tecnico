def inverte_string(string):
    frase_inversa = ''

    tamanho_frase = len(string)
    for letra in string:
        tamanho_frase -= 1
        frase_inversa += string[tamanho_frase]
    return frase_inversa


palavra = inverte_string('programador')

print(palavra)