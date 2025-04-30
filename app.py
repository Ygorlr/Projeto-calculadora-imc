peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))
resultado = peso / (altura**2)
situacao = ''

if resultado < 19.1:
    situacao = "Abaixo do Peso"
elif resultado >= 19.1 and resultado <= 25.8:
    situacao = "Peso Normal"
elif resultado >= 25.9 and resultado <= 27.3:
    situacao = "Pouco Acima do Peso"
elif resultado >= 27.4 and resultado <= 32.3:
    situacao = "Acima do Peso"
elif resultado >= 32.4:
    situacao = "Obesidade"

print(resultado)
print(situacao)
