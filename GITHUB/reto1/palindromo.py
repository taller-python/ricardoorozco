
"""funcion de validacion de palabras palindromas"""

def palindromo(input_word):

    longitud = len(input_word)
    cont_i = 0
    cont_j = longitud - 1
    word = input_word.upper()

    while cont_i <= (longitud/2):
        if word[cont_i] != word[cont_j]:
            return False
        cont_i += 1
        cont_j -= 1

    return True
