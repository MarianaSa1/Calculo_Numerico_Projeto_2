# ===================================================================
# ======================   MÉTODO DE GAUSS–SEIDEL   =================
# ===================================================================
# PROGRAMA: Método de Gauss-Seidel
#
# Descrição:
#   Resolve sistemas de equações lineares do tipo A·x = b utilizando
#   o método iterativo de Gauss-Seidel.
# ===================================================================

def obter_numero(mensagem):
    """
    Solicita um número ao usuário com validação.
    Garante que sempre será digitado um valor numérico real.
    """
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Entrada inválida! Digite um número.")

print("\n" + "="*70)
print("                MÉTODO ITERATIVO DE GAUSS–SEIDEL")
print("="*70 + "\n")
# ================================================================
# 1. Entrada do tamanho do sistema
# ================================================================
while True:
    try:
        n = int(input("Digite o número de equações (Ordem do sistema): "))
        if 1 <= n <= 30:
            break
        else:
            print("Digite um valor entre 1 e 30.")
    except ValueError:
        print("Digite um número inteiro válido!")


# ================================================================
# 2. Exibir GUIA VISUAL (modelo da matriz)
# ================================================================
print("\n" + "="*70)
print("GUIA VISUAL - Posições da Matriz [A | b]")
print("="*70)

print("""
A matriz será preenchida conforme o formato abaixo:
(Coeficientes)  |  (Termo Independente)

Equação | X1 | X2 | X3 | ... | Xn | b |
----------------------------------------

   1    | a11| a12| a13| ... | a1n| b1|
   2    | a21| a22| a23| ... | a2n| b2|
   3    | a31| a32| a33| ... | a3n| b3|
  ...   | ... ... ... ... ... ... ...
   n    | an1| an2| an3| ... | ann| bn|

Exemplo:
Para a equação "2x1 + 3x2 = 8", digite:
a[1,1] = 2
a[1,2] = 3
b[1]   = 8
""")
print("="*70)


# ================================================================
# 3. Entrada da matriz A e do vetor b
# ================================================================
A = [[0.0 for _ in range(n)] for _ in range(n)]
b = [0.0 for _ in range(n)]

print("\nAgora insira os coeficientes do sistema:")

for i in range(n):
    print(f"\n--- Equação {i+1} ---")

    for j in range(n):
        A[i][j] = obter_numero(f"a[{i+1},{j+1}] (coef. de X{j+1}): ")

    b[i] = obter_numero(f"b[{i+1}] (termo independente): ")


# ================================================================
# 4. Parâmetros do método
# ================================================================
tol = obter_numero("\nDigite a tolerância desejada (ex: 0.001): ")
max_iter = int(obter_numero("Digite o número máximo de iterações: "))


# ================================================================
# 5. Método de Gauss-Seidel
# ================================================================
x = [0.0] * n  # chute inicial

print("\n\n================ INICIANDO GAUSS-SEIDEL ================\n")

for k in range(1, max_iter + 1):
    x_ant = x.copy()

    for i in range(n):
        soma = 0
        for j in range(n):
            if j != i:
                soma += A[i][j] * x[j]

        x[i] = (b[i] - soma) / A[i][i]

    erro = max(abs(x[i] - x_ant[i]) for i in range(n))

    print(f"It {k:3d} | x = {x} | Erro = {erro:e}")

    if erro < tol:
        print("\nConvergência atingida!")
        break
else:
    print("\nATENÇÃO: Número máximo de iterações atingido sem convergência.")


# ================================================================
# 6. Exibição da solução final
# ================================================================
print("\n=================== SOLUÇÃO FINAL ===================\n")

for i in range(n):
    print(f"x{i+1} = {x[i]}")

print("\n======================================================\n")
