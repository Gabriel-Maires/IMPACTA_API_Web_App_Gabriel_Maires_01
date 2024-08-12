def calcular_imc(peso, altura):
  imc = peso / (altura ** 2)
  return imc

def classificar_imc(imc):
  if imc < 18.5:
    return "Abaixo do peso"
  elif 18.5 <= imc < 25:
    return "Peso normal"
  elif 25 <= imc < 30:
    return "Sobrepeso"
  else:
    return "Obesidade"

peso = float(input("Digite seu peso em quilogramas: "))
altura = float(input("Digite sua altura (Exemplo: 1.80): "))

imc = calcular_imc(peso, altura)

classificacao = classificar_imc(imc)

print(f"Seu IMC é {imc:.2f} e você está classificado como {classificacao}.")
