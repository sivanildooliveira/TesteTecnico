
def validar_expressao(string):

    #variaveis de teste.
    pa = co = ch = 0

    for c in string:

        #teste para os caracter '()'.
        if c in '()':
            if c == '(':
                pa += 1
            else:
                pa -= 1
            if pa < 0: #caso seja encontrada uma falha nos 'pares'.
                break

        #teste para os caracter '[]'.
        if c in '[]':
            if c == '[':
                co += 1
            else:
                co -= 1
            if co < 0:
                break

        #teste para os caracter '{}'.
        if c in '{}':
            if c == '{':
                ch += 1
            else:
                ch -= 1
            if ch < 0:
                break

    return True if [pa, co, ch] == [0,0,0] else False
