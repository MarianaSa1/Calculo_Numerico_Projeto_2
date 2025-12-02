# ===============================================================
# PROGRAMA: Regras de Integração Numérica
# Métodos: Regra dos Trapézios e Regra de Simpson 1/3
# Objetivo: Calcular a integral aproximada de uma função definida
# pelo usuário, dentro de um intervalo [a, b], dividindo esse
# intervalo em n subintervalos.
# ===============================================================


# ---------------------------------------------------------------
# Função f(x) que será integrada
# Aqui você define a função matemática. No exemplo, usamos
# a mesma função presente no código C fornecido:
#
# Para trocar a função, basta alterar a expressão do return.
# ---------------------------------------------------------------
def f(x):
    return (0.02552 * x**4) + (-0.29958 * x**3) + (0.42111 * x**2) + (-0.47631 * x) + 3.01602


# ---------------------------------------------------------------
# Regra dos Trapézios
#
# Fórmula geral:
# ∫ f(x) dx ≈ (h/2) * Σ [ f(x_i) + f(x_{i+1}) ]
#
# Onde:
# - h é o tamanho de cada subintervalo: h = (b - a) / n
# - Soma feita sobre cada par (x0, x1), (x1, x2), ...
#
# A ideia é aproximar a área sob a curva usando trapézios.
# Cada trapézio tem altura h e bases f(x0) e f(x1).
# ---------------------------------------------------------------
def trapezios(a, b, n):
    h = (b - a) / n  # calcula o tamanho de cada subintervalo

    soma = 0  # acumulador das somas das bases dos trapézios

    # Percorre todos os subintervalos
    for i in range(1, n + 1):
        x0 = a + (i - 1) * h  # início do trapézio
        x1 = x0 + h           # fim do trapézio

        # Soma das bases do trapézio
        soma = soma + (f(x0) + f(x1))

    # Fórmula final da regra dos trapézios
    resultado = (h / 2) * soma
    return resultado


# ---------------------------------------------------------------
# Regra de Simpson 1/3
#
# A Regra de Simpson é mais precisa que a dos trapézios.
# Ela usa parábolas para aproximar a função.
#
# Fórmula:
# ∫ f(x) dx ≈ (h/3) * [ f(x0) + f(xn) + 
#                       4*(f(x1)+f(x3)+...) +
#                       2*(f(x2)+f(x4)+...) ]
#
# OBSERVAÇÃO IMPORTANTE:
# Para usar Simpson 1/3, o número de subintervalos n deve ser PAR.
#
# Caso não seja, o programa ajusta automaticamente somando +1.
# ---------------------------------------------------------------
def simpson(a, b, n):
    # Verifica se n é par
    if n % 2 != 0:
        print("AVISO: Para Simpson, n deve ser par. Somando 1 ao valor.")
        n = n + 1  # ajusta n para o próximo número par

    h = (b - a) / n  # largura dos subintervalos

    # Simpson começa somando os extremos da integral
    soma = f(a) + f(b)

    # Agora somamos os termos internos, alternando pesos 4 e 2
    for i in range(1, n):
        x = a + i * h

        if i % 2 == 0:
            # Índices pares recebem peso 2,
            soma = soma + 2 * f(x)
        else:
            # Índices ímpares recebem peso 4
            soma = soma + 4 * f(x)

    # Fórmula final de Simpson
    resultado = (h / 3) * soma
    return resultado


# ---------------------------------------------------------------
# PROGRAMA PRINCIPAL
# Versão simples, estilo iniciante, sem estruturas avançadas.
# Aqui o usuário digita os limites e o número de subintervalos
# e o programa mostra o resultado usando os dois métodos.
# ---------------------------------------------------------------

print("=======================================================")
print("   CÁLCULO DE INTEGRAIS - TRAPÉZIOS E SIMPSON")
print("=======================================================\n")

# Solicita ao usuário os valores necessários
a = float(input("Limite inferior a = "))
b = float(input("Limite superior b = "))
n = int(input("Número de sub-intervalos n = "))

# Calcula a integral pelos dois métodos
valor_trap = trapezios(a, b, n)
valor_simp = simpson(a, b, n)

# Mostra os resultados na tela
print("\n================ RESULTADOS ================")
print(f"Regra dos Trapézios : {valor_trap}")
print(f"Regra de Simpson    : {valor_simp}")
print("============================================")
