import math

# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.

numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))

resultado_soma = numero1 + numero2

print(f"A soma é: {resultado_soma}")

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

numero = int(input("Digite um número: "))

resultado_resto = numero % 5

print(f"O resto da divisão desse número por 5 é: {resultado_resto}")


# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

resultado_multiplicacao = numero1 * numero2

print(f"O resultado da multiplicação desses números é: {resultado_multiplicacao}")

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

resultado_divisao = numero1 // numero2

print(f"O resultado da divisão inteira é: {resultado_divisao}")

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

numero = int(input("Digite um número: "))

resultado_quadrado = numero ** 2

print(f"O quadrado do número é: {resultado_quadrado}")

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.

numero1 = float(input("Digite o primeiro número decimal: "))
numero2 = float(input("Digite o segundo número decimal: "))

resultado_soma = numero1 + numero2

print(f"O resultado da soma é: {resultado_soma}")

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

numero1 = float(input("Digite o primeiro número decimal: "))
numero2 = float(input("Digite o segundo número decimal: "))

resultado_media = (numero1 + numero2) / 2

print(f"A média é: {resultado_media}")

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

base = float(input("Digite a base: "))
expoente = float(input("Digite o expoênte: "))

resultado_potencia = base ** expoente

print(f"O resultado da potência é: {resultado_potencia}")

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.

celcius = float(input("Digite a temperatura em celcius: "))
fahrenheit = (celcius * (9 / 5)) + 32

print(f"{celcius}°C é igual a {fahrenheit}°F")

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

raio = float(input("Digite o raio do circulo: "))

area_circulo = math.pi * (raio ** 2)

print(f"A área do circulo é: {area_circulo:.2f} m²")

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

texto = input("Digite um texto qualquer: ")

texto_maiuscula = texto.upper()

print(f"Texto em maiúsculas: {texto_maiuscula}")

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

nome_completo = input("Digite seu nome completo: ")

nome_minusculas = nome_completo.lower()

print(f"Nome em minúsculas: {nome_minusculas}")

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

frase = input("Digite uma frase: ")

frase_sem_espacos = frase.strip()

print(f"Frase sem espaços vázios no início e no final: {frase_sem_espacos}")

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

data = input("Digite uma data no formato (dd/mm/aaaa): ")

dia, mes, ano = data.split("/")

print(f"Dia: {dia}")
print(f"Mêa: {mes}")
print(f"Ano: {ano}")

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

parte1 = input("Digite um texto: ")
parte2 = input("Digite outro texto: ")

texto_concatenado = parte1 + parte2

print(f"Texto concatenado: {texto_concatenado}")

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.

valor1 = True
Valor2 = False

resultado_and = valor1 and Valor2

print(f"Resultado do AND lógico: {resultado_and}")

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.

resultado_or = valor1 or Valor2

print(f"Resultado do OR lógico: {resultado_or}")

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.

resultado_not = not valor1

print(f"Resultado do NOT lógico: {resultado_not}")

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

resultado_igualdade = (numero1 == numero2)

print(f"Resultado da igualdade: {resultado_igualdade}")

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

resultado_diferenca = (numero1 != numero2)

print(f"Resultado da diferença: {resultado_diferenca}")

# #### try-except e if

# 21: Conversor de Temperatura

try:
    elcius = float(input("Digite a temperatura em celcius: "))
    fahrenheit = (celcius * (9 / 5)) + 32

    print(f"{celcius}°C é igual a {fahrenheit}°F")
except ValueError:
    print("Por favor, digite um valor válido para a temperatura.")

# 22: Verificador de Palíndromo

entrada = input("Digite uma palavra ou frase: ")

if isinstance(entrada, str):
    formatado = entrada.replace(" ", "").lower()
    if formatado == formatado[::-1]: # A sintaxe geral de fatiamento (slice): string[inicio:fim:passo]
        print("É um palíndromo.")
    else:
        print("Não é um palíndromo.")
else:
    print("Entrada inválida. Por favor, digite uma palavra ou frase.")


# 23: Calculadora Simples

try:
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    operador = input("Digite o operador (+, -, *, /): ")

    if operador == "+":
        resultado = numero1 + numero2
    elif operador == "-":
        resultado = numero1 - numero2
    elif operador == "*":
        resultado = numero1 * numero2
    elif operador == "/":
        resultado = numero1 / numero2
    else:
        print("Operador inválido.")
    print(f"{numero1} {operador} {numero2} = {resultado}")
except ZeroDivisionError:
    print("Erro de divisão por zero.")
except ValueError:
    print("Erro: Entrada inválida. Certifique-se de inserir números.") 

# 24: Classificador de Números

try:
    numero = int(input("Digite um número: "))

    if numero > 0:
        print("Positivo.")
    elif numero < 0:
        print("Negativo.")
    else:
        print("Zero.")

    if (numero % 2) == 0:
        print("Par")
    else:
        print("Impar")

except ValueError:
    print("Entrada inválida. Por favor, digite um número.")


# 25: Conversão de Tipo com Validação

try:
    numeros = input("Digite uma lista de números separados por virgula: ")
    lista_numeros_string = numeros.split(",")
    lista_numeros_inteiros = []

    for numero in lista_numeros_string:
        if isinstance(numero, int):
            lista_numeros_inteiros.append(int(numero.strip()))
    
    print(f"Lista de inteiros: {lista_numeros_inteiros}")
except ValueError:
    print("Erro: certifique-se de que todos os elementos são números inteiros válidos.")