history = "Era uma vez um(a) {substantivo} {adjetivo} que adorava {verbo} todos os dias."
print(history)
verbo = input("Digite um verbo: ")
substantivo = input("Digite um substantivo: ")
adjetivo = input("Digite um adjetivo: ")

history_final = history.format(adjetivo=adjetivo, substantivo=substantivo, verbo=verbo)

print(history_final)