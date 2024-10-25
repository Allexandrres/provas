velocidade = float(input("Qual é a velocidade do carro em km/h? "))

if velocidade > 80:
    excesso = velocidade - 80
    multa = excesso * 20
    print(f"Você foi multado! A velocidade permitida é de 80 km/h.")
    print(f"Você ultrapassou {excesso:.1f} km/h acima do permitido.")
    print(f"O valor da multa é de R${multa:.2f}.")
else:
    print("Velocidade dentro do limite permitido. Dirija com segurança!")
