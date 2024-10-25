quantidade = 0
soma = 0

while True:
    numero = int(input("Digite um número inteiro (ou 0 para encerrar): "))
    
    if numero == 0:
        break  # Encerra o loop se o usuário digitar 0
    
    quantidade += 1  # Incrementa a contagem de números
    soma += numero   # Soma o valor do número à soma total

if quantidade > 0:
    media = soma / quantidade
else:
    media = 0

print(f"\nQuantidade de números digitados: {quantidade}")
print(f"Soma dos números: {soma}")
print(f"Média aritmética: {media:.2f}")
