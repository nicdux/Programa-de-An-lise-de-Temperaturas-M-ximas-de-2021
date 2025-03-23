# Programa de Análise de Temperaturas Máximas de 2021
# Fase 1 - Projeto de Lógica de Programação

# Lista com os nomes dos meses por extenso
nomes_meses = [
    "janeiro", "fevereiro", "março", "abril", "maio", "junho",
    "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
]

# Lista para armazenar as temperaturas máximas de cada mês
temperaturas_maximas = [0] * 12

# Função para validar o número do mês
def validar_mes(mes):
    return mes.isdigit() and 1 <= int(mes) <= 12

# Função para validar a temperatura
def validar_temperatura(temp):
    try:
        temp_float = float(temp.replace(",", "."))
        return -60 <= temp_float <= 50
    except ValueError:
        return False

# Coleta de dados do usuário com validação
for i in range(12):
    # Validação do mês
    while True:
        mes_input = input(f"Digite o número do mês ({i+1}/12) [1 a 12]: ")
        if validar_mes(mes_input):
            mes_num = int(mes_input)
            break
        else:
            print("Valor inválido para o mês! Digite um número entre 1 e 12.")
    
    # Validação da temperatura máxima
    while True:
        temp_input = input(f"Digite a temperatura máxima de {nomes_meses[mes_num - 1]} (de -60°C a 50°C): ")
        if validar_temperatura(temp_input):
            temperatura = float(temp_input.replace(",", "."))
            temperaturas_maximas[mes_num - 1] = temperatura
            break
        else:
            print("Valor inválido! A temperatura deve estar entre -60°C e 50°C.")

# Cálculo da temperatura média máxima anual
media_anual = sum(temperaturas_maximas) / 12

# Contagem de meses escaldantes (temperatura > 33°C)
meses_escaldantes = sum(1 for temp in temperaturas_maximas if temp > 33)

# Mês mais escaldante (maior temperatura)
maior_temperatura = max(temperaturas_maximas)
indice_maior = temperaturas_maximas.index(maior_temperatura)
mes_mais_escaldante = nomes_meses[indice_maior]

# Mês menos quente (menor temperatura)
menor_temperatura = min(temperaturas_maximas)
indice_menor = temperaturas_maximas.index(menor_temperatura)
mes_menos_quente = nomes_meses[indice_menor]

# Resultados finais
print("\n===== RESULTADOS FINAIS =====")
print(f"Temperatura média máxima anual: {media_anual:.2f}°C")
print(f"Quantidade de meses escaldantes (> 33°C): {meses_escaldantes}")
print(f"Mês mais escaldante do ano: {mes_mais_escaldante} ({maior_temperatura:.1f}°C)")
print(f"Mês menos quente do ano: {mes_menos_quente} ({menor_temperatura:.1f}°C)")
