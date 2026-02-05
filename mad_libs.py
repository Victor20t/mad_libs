import random

def play_mad_libs(): 
    history = random.choice(stories)
    verbo = input("Digite um verbo: ")
    substantivo = input("Digite um substantivo: ")
    adjetivo = input("Digite um adjetivo: ")

    history_final = history.format(adjetivo=adjetivo, substantivo=substantivo, verbo=verbo)

    print(history_final)

stories = [
    '''
    Era uma vez um(a) {substantivo} muito {adjetivo} que vivia em um(a) {lugar}.
    Todos os dias, ele(a) gostava de {verbo} enquanto pensava em {substantivo_abstrato}.
    Um dia, encontrou um(a) {animal} {adjetivo} e tudo mudou para sempre.''',

    '''
    Hoje acordei {adjetivo} porque tinha prova de {materia}.
    Antes de sair de casa, comi {comida} e bebi {bebida}.
    No caminho, vi um(a) {substantivo} {adjetivo} {verbo_gerundio} na rua.
    Definitivamente, foi um dia {adjetivo}.''',

    '''
    Meu animal favorito é um(a) {animal} {adjetivo}.
    Ele adora {verbo} pela casa e dormir em {lugar}.
    Quando fica bravo, faz um som tipo {onomatopeia}!''',
    

    ]

play = 1 

while play == 1: 
    play_mad_libs()
    play = int(input("Deseja Jogar novamente? SIM _> 1 ou NÃO -> 0: "))