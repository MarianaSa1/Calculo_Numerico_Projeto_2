# -*- coding: utf-8 -*-
# Importamos a biblioteca math apenas para usar a função log10(),
# que calcula o logaritmo na base 10.
import math

# ================================================================
# LISTA DE DADOS ORIGINAIS
# Cada linha contém:
#   (ano de lançamento, número de transistores do chip)
#
# Esses dados foram extraídos da tabela fornecida no enunciado.
# ================================================================
dados = [
    (1971, 2250),
    (1972, 3500),
    (1974, 6000),
    (1978, 29000),
    (1982, 134000),
    (1986, 275000),
    (1989, 1200000),
    (1993, 3100000),
    (1997, 7500000),
    (1999, 9500000),
    (2000, 42000000)
]

print("===== LEI DE MOORE - PREVISÃO DE TRANSISTORES =====\n")
print("Dados originais (Ano, Transistores, Log10):")
print("-" * 50)

# =====================================================================
# Aqui percorremos os dados e, para cada chip, calculamos o log10(N).
# A transformação logarítmica é essencial, pois a Lei de Moore cresce
# de forma aproximadamente exponencial; ao aplicar log10, transformamos
# esse crescimento em algo mais parecido com uma linha reta.
# =====================================================================

anos = [a for a, _ in dados]                          # lista com os anos
log_transistores = [math.log10(n) for _, n in dados]  # log10 dos transistores

for i in range(len(dados)):
    ano, trans = dados[i]
    print(f"Ano: {ano} | Transistores: {trans:>12} | Log10: {log_transistores[i]:.4f}")

# =====================================================================
# CÁLCULO DOS COEFICIENTES DA REGRESSÃO LINEAR (MÍNIMOS QUADRADOS)
#
# Queremos ajustar uma reta da forma:
#       log10(N) = a + b * ano
#
# onde:
#   a = intercepto da reta
#   b = inclinação (quanto log10(N) cresce a cada ano)
# =====================================================================

n = len(anos)

soma_x  = sum(anos)
soma_y  = sum(log_transistores)
soma_x2 = sum(x*x for x in anos)
soma_xy = sum(anos[i] * log_transistores[i] for i in range(n))

denominador = (n * soma_x2) - (soma_x * soma_x)

coeficiente_b = ((n * soma_xy) - (soma_x * soma_y)) / denominador
coeficiente_a = (soma_y - coeficiente_b * soma_x) / n

print("\n" + "=" * 50)
print("COEFICIENTES CALCULADOS:")
print("=" * 50)
print(f"Coeficiente a (intercepto da reta): {coeficiente_a:.6f}")
print(f"Coeficiente b (inclinação da reta): {coeficiente_b:.6f}")

# =====================================================================
# FUNÇÕES DE PREVISÃO
# =====================================================================

def calcular_log_transistores(ano):
    return coeficiente_a + coeficiente_b * ano

def calcular_transistores(ano):
    log_valor = calcular_log_transistores(ano)
    return 10 ** log_valor

# =====================================================================
# PREVISÕES PARA OS ANOS 2010 E 2020
# =====================================================================

print("\n" + "=" * 50)
print("PREVISÕES:")
print("=" * 50)

ano_2010 = 2010
ano_2020 = 2020

log_2010 = calcular_log_transistores(ano_2010)
trans_2010 = calcular_transistores(ano_2010)

log_2020 = calcular_log_transistores(ano_2020)
trans_2020 = calcular_transistores(ano_2020)

print(f"\nAno 2010:")
print(f"  Log10(transistores) = {log_2010:.4f}")
print(f"  Transistores = {trans_2010:.0f}")

print(f"\nAno 2020:")
print(f"  Log10(transistores) = {log_2020:.4f}")
print(f"  Transistores = {trans_2020:.0f}")

# =====================================================================
# CÁLCULO DO R² (Coeficiente de Determinação)
#
# O R² mede o quanto a reta ajustada consegue explicar o comportamento
# dos dados originais após aplicarmos log10. 
#
# Interpretação:
#   • R² próximo de 1 → o modelo explica muito bem os dados.
#   • R² próximo de 0 → o modelo não consegue representar os dados.
#
# Como a Lei de Moore é quase exponencial, esperamos que o R²
# (no espaço log10) seja bastante alto.
# =====================================================================

media_y = soma_y / n

ss_total = sum((y - media_y)**2 for y in log_transistores)
ss_resid = sum((log_transistores[i] - calcular_log_transistores(anos[i]))**2 for i in range(n))

r2 = 1 - ss_resid / ss_total

print("\n" + "=" * 50)
print("QUALIDADE DO AJUSTE (R²):")
print("=" * 50)
print(f"R² = {r2:.6f}")
print("\nInterpretação:")
print("  Quanto mais próximo de 1, melhor a reta ajustada representa os dados.")
print("  Como estamos trabalhando com log10(N), um R² alto indica que a evolução")
print("  do número de transistores segue muito de perto um crescimento exponencial.")
