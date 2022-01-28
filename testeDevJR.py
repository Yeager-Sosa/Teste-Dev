#teste dev em python com back pois em C# o codigo ficou muito extenso
def anagramaAgrupado(palavras):

    grupoAnagrama = {}

    for palavra in palavras:
        palavraOrdenada = "".join(sorted(palavra))

        if palavraOrdenada in grupoAnagrama:
            grupoAnagrama[palavraOrdenada].append(palavra)
        else:
            grupoAnagrama[palavraOrdenada] = [palavra]

    return list(grupoAnagrama.values())

palavras = ['nata', 'sorvete', 'anta',
            'paralelepipedo', 'tana', 'dopelelerapaip']

print(anagramaAgrupado(palavras))
