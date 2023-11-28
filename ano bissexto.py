Ano = int(input("Insira um ano:"))

bissexto = [i for i in range(2020, 1, -4) ]and [i for i in range(2020, 1000000, 4)] #utilizei o loop "for" para calcular todos os anos bissextos à partir do ano de 2020 que foi o ultimo em relação a presente data)

if Ano == bissexto:
    print("O ano de: ", Ano,"é um ano bissexto")
else:
    print("O ano de: ", Ano,"não é um ano bissexto")

