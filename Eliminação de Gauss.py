000000000000000000000000000000# ===================================================================
# PROGRAMA: Método de Eliminação de Gauss Simples
# Descrição:
#   Resolve sistemas lineares do tipo A·x = b usando eliminação de Gauss
#   sem pivotamento. O método transforma a matriz aumentada [A|b] em
#   uma matriz triangular superior, permitindo calcular a solução através
#   da substituição retroativa.
# ===================================================================


def obter_numero(mensagem):
    # ---------------------------------------------------------------
    # Solicita um número ao usuário com tratamento de erro.
    # A entrada só é aceita quando for possível converter para float.
    # Se o usuário digita algo inválido, o programa informa o erro
    # e solicita novamente.
    # ---------------------------------------------------------------
    while True:
        try:
            valor = float(input(mensagem))   # tenta converter a entrada
            return valor                     # retorna somente se for válido
        except ValueError:
            print("❌ Erro: Digite um número válido!")  # mensagem amigável


def exibir_guia_entrada(numero_equacoes):
    # ---------------------------------------------------------------
    # Exibe uma representação visual da matriz aumentada [A|b].
    # Isto ajuda o usuário a entender onde cada coeficiente será inserido.
    # Apenas informativo — não realiza cálculos.
    # ---------------------------------------------------------------
    print("\n" + "=" * 70)
    print("GUIA VISUAL - Posições da Matriz Aumentada [A|b]:")
    print("=" * 70)
    print("\nA matriz será lida conforme o formato abaixo:")
    print("(Coeficientes) | (Termo Independente)\n")

    linha_cabecalho = "Equação |"
    for j in range(1, numero_equacoes + 1):
        linha_cabecalho += f" X{j} |"
    linha_cabecalho += " b |"
    print(linha_cabecalho)
    print("-" * len(linha_cabecalho))

    for i in range(1, numero_equacoes + 1):
        linha = f"   {i}    |"
        for j in range(1, numero_equacoes + 1):
            linha += f"a{i}{j}|"
        linha += f"b{i}|"
        print(linha)

    print("\nExemplo: Para inserir a equação '2x₁ + 3x₂ = 8'")
    print("         Insira: X1=2  X2=3  b=8")
    print("=" * 70)


def exibir_matriz(matriz, numero_equacoes, titulo):
    # ---------------------------------------------------------------
    # Exibe a matriz aumentada de forma organizada, com sinais e
    # duas casas decimais para facilitar a visualização.
    # ---------------------------------------------------------------
    print(f"\n\n\n{titulo}")
    print("=" * (numero_equacoes * 10 + 5))

    for i in range(1, numero_equacoes + 1):
        for j in range(1, numero_equacoes + 2):
            print(f"{matriz[i][j]:+8.2f}", end=" ")
        print()


def triangularizar_matriz(matriz, numero_equacoes):
    # ---------------------------------------------------------------
    # Executa a eliminação de Gauss sem pivotamento.
    # ---------------------------------------------------------------
    for k in range(1, numero_equacoes):
        for i in range(k + 1, numero_equacoes + 1):
            multiplicador = (-1.0) * matriz[i][k] / matriz[k][k]
            for j in range(1, numero_equacoes + 2):
                matriz[i][j] = matriz[i][j] + multiplicador * matriz[k][j]


def substituicao_retroativa(matriz, vetor_x, numero_equacoes):
    # ---------------------------------------------------------------
    # Resolve o sistema pela substituição retroativa.
    # ---------------------------------------------------------------
    for i in range(numero_equacoes, 0, -1):
        vetor_x[i] = matriz[i][numero_equacoes + 1]
        for j in range(numero_equacoes, i, -1):
            vetor_x[i] -= vetor_x[j] * matriz[i][j]
        vetor_x[i] = vetor_x[i] / matriz[i][i]


def main():
    # ---------------------------------------------------------------
    # Função principal do programa. Aqui acontece todo o processo:
    # 1) O usuário informa o número de equações do sistema.
    # 2) O programa mostra um guia visual explicando a matriz aumentada.
    # 3) São lidos todos os coeficientes A e os termos independentes b.
    # 4) A matriz original é exibida.
    # 5) A eliminação de Gauss é aplicada para triangular a matriz.
    # 6) A matriz triangular é exibida.
    # 7) A substituição retroativa é executada para obter as incógnitas.
    # 8) O programa mostra os valores finais de cada X[i].
    # Essa função coordena todo o fluxo chamando funções auxiliares.
    # ---------------------------------------------------------------

    matriz = [[0.0 for _ in range(10)] for _ in range(10)]   # matriz aumentada
    vetor_x = [0.0] * 10                                      # vetor solução

    print("=" * 50)
    print("RESOLUÇÃO DE SISTEMAS LINEARES - ELIMINAÇÃO DE GAUSS")
    print("=" * 50)

    # ---------------------------------------------------------------
    # 1) Leitura da quantidade de equações.
    # O programa aceita valores somente entre 1 e 9.
    # A função obter_numero() garante que a entrada seja numérica.
    # ---------------------------------------------------------------
    while True:
        numero_equacoes = obter_numero("\nDigite o número de equações (1-9): ")
        if 1 <= numero_equacoes <= 9:
            numero_equacoes = int(numero_equacoes)
            break
        else:
            print("❌ Erro: O número de equações deve estar entre 1 e 9!")

    # ---------------------------------------------------------------
    # 2) Mostra o guia visual para ajudar o usuário a entender
    # como funciona a matriz aumentada [A|b] e onde os valores serão inseridos.
    # ---------------------------------------------------------------
    exibir_guia_entrada(numero_equacoes)

    print("\n" + "=" * 50)
    print("ENTRADA DE DADOS DA MATRIZ")
    print("=" * 50)

    # ---------------------------------------------------------------
    # 3) Leitura dos coeficientes da matriz A e dos termos independentes b.
    # A matriz aumentada tem a forma:
    # [ a11 a12 ... a1n | b1 ]
    # [ a21 a22 ... a2n | b2 ]
    # Cada coeficiente é digitado individualmente pelo usuário.
    # ---------------------------------------------------------------
    for i in range(1, numero_equacoes + 1):
        print(f"\n--- Equação {i} ---")
        for j in range(1, numero_equacoes + 1):
            matriz[i][j] = obter_numero(f"  a[{i},{j}] (coeficiente de X{j}): ")
        matriz[i][numero_equacoes + 1] = obter_numero(
            f"  b[{i}]    (termo independente): "
        )

    exibir_matriz(matriz, numero_equacoes, "MATRIZ ORIGINAL (AUMENTADA):")

    # ---------------------------------------------------------------
    # 4) Aplicação da eliminação de Gauss.
    # Essa etapa transforma a matriz aumentada em uma matriz triangular
    # superior, zerando os elementos abaixo da diagonal principal usando
    # combinações lineares das linhas. Não é utilizado pivotamento.
    # ---------------------------------------------------------------
    print("\n" + "=" * 50)
    print("EXECUTANDO ELIMINAÇÃO DE GAUSS...")
    print("=" * 50)

    triangularizar_matriz(matriz, numero_equacoes)
    exibir_matriz(matriz, numero_equacoes, "MATRIZ MODIFICADA (TRIANGULAR):")

    input("\nPressione ENTER para continuar com a substituição retroativa...")

    # ---------------------------------------------------------------
    # 5) Execução da substituição retroativa.
    # A solução começa pela última linha (que contém apenas uma incógnita)
    # e segue voltando até chegar na primeira equação. Cada valor de X[i]
    # é calculado usando os valores já encontrados anteriormente.
    # ---------------------------------------------------------------
    print("\n" + "=" * 50)
    print("EXECUTANDO SUBSTITUIÇÃO RETROATIVA...")
    print("=" * 50)

    substituicao_retroativa(matriz, vetor_x, numero_equacoes)

    # ---------------------------------------------------------------
    # 6) Exibição final da solução do sistema.
    # Os valores são exibidos com duas casas decimais e sinal.
    # ---------------------------------------------------------------
    print("\n" + "=" * 50)
    print("SOLUÇÃO DO SISTEMA LINEAR:")
    print("=" * 50)

    for i in range(1, numero_equacoes + 1):
        print(f"X[{i}] = {vetor_x[i]:+8.2f}")

    print("\n" + "=" * 50)
    print("FIM DO PROGRAMA")
    print("=" * 50)



main()
