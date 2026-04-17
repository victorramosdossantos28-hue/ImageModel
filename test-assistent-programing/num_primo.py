"""
Módulo de verificação de números primos.

Este módulo fornece funções otimizadas para verificar se um número é primo
e executar testes em lotes de números.
"""

import math
from typing import List

# Constantes
VALOR_MINIMO_PRIMO = 2
NUMERO_PAR_PRIMO = 2
LIMITE_INFERIOR = 1
FATOR_INCREMENTO = 2
LARGURA_SEPARADOR = 50

# Mensagens
TITULO_TESTE = "TESTE DE NÚMEROS PRIMOS"
MSG_TESTE_INDIVIDUAL = "Testando números individuais:"
MSG_PRIMOS_ATE_50 = "Números primos até 50:"
MSG_PRIMOS_ATE_100 = "Números primos de 1 a 100:"
MSG_TOTAL_PRIMOS = "Total de primos:"
FORMATO_PRIMO = "PRIMO"
FORMATO_NAO_PRIMO = "NÃO PRIMO"


def eh_primo(numero: int) -> bool:
    """
    Verifica se um número inteiro é primo.

    Um número primo é um número natural maior que 1 que possui apenas
    dois divisores positivos: 1 e ele próprio.

    Args:
        numero: Um número inteiro a ser verificado.

    Returns:
        bool: True se o número é primo, False caso contrário.

    Raises:
        TypeError: Se o argumento não for um inteiro.

    Exemplos:
        >>> eh_primo(2)
        True
        >>> eh_primo(4)
        False
        >>> eh_primo(17)
        True
    """
    if not isinstance(numero, int):
        raise TypeError(f"Esperado int, recebido {type(numero).__name__}")

    # Números menores ou iguais a 1 não são primos
    if numero <= LIMITE_INFERIOR:
        return False

    # 2 é o único número primo par
    if numero == NUMERO_PAR_PRIMO:
        return True

    # Números pares maiores que 2 não são primos
    if numero % 2 == 0:
        return False

    # Verifica divisibilidade pelos números ímpares até √n
    limite_verificacao = int(math.sqrt(numero)) + 1
    for divisor in range(3, limite_verificacao, FATOR_INCREMENTO):
        if numero % divisor == 0:
            return False

    return True


def encontrar_primos_ate(limite: int) -> List[int]:
    """
    Encontra todos os números primos até um determinado limite.

    Args:
        limite: O limite superior (inclusive) para buscar números primos.

    Returns:
        Uma lista contendo todos os números primos encontrados.

    Exemplos:
        >>> encontrar_primos_ate(10)
        [2, 3, 5, 7]
    """
    return [numero for numero in range(VALOR_MINIMO_PRIMO, limite + 1) if eh_primo(numero)]


def exibir_resultado_individual(numero: int) -> None:
    """
    Exibe o resultado da verificação de um número individual.

    Args:
        numero: O número a ser verificado e exibido.
    """
    resultado = FORMATO_PRIMO if eh_primo(numero) else FORMATO_NAO_PRIMO
    print(f"Número {numero:3d}: {resultado}")


def exibir_separador(caractere: str = "=") -> None:
    """
    Exibe uma linha separadora.

    Args:
        caractere: O caractere a ser usado na linha (padrão: "=").
    """
    print(caractere * LARGURA_SEPARADOR)


def solicitar_entrada_usuario() -> None:
    """
    Solicita um número ao usuário e verifica se é primo.

    Funcionalidade interativa que:
    - Solicita entrada do usuário
    - Valida se é um número inteiro válido
    - Verifica primalidade
    - Exibe resultado de forma clara
    """
    exibir_separador()
    print("VERIFICADOR DE NÚMEROS PRIMOS - MODO INTERATIVO")
    exibir_separador()

    while True:
        try:
            print("\nDigite um número inteiro para verificar se é primo")
            print("(Digite 'sair' ou 'exit' para encerrar):\n")

            entrada = input(">>> ").strip()

            # Verifica comando de saída
            if entrada.lower() in ["sair", "exit", "quit"]:
                print("\nAté logo! 👋")
                exibir_separador()
                break

            # Converte entrada para inteiro
            numero = int(entrada)

            # Verifica e exibe resultado
            resultado = FORMATO_PRIMO if eh_primo(numero) else FORMATO_NAO_PRIMO
            print(f"\nO número {numero} é: {resultado}")

            # Informações adicionais
            if numero <= 1:
                print("Nota: Números ≤ 1 não são primos por definição.")
            elif numero == 2:
                print("Nota: 2 é o único número primo par.")
            elif numero % 2 == 0:
                print(f"Nota: {numero} é divisível por 2.")

        except ValueError:
            print("\n❌ ERRO: Digite um número inteiro válido!")
        except TypeError as e:
            print(f"\n❌ ERRO DE TIPO: {e}")
        except KeyboardInterrupt:
            print("\n\nPrograma interrompido pelo usuário.")
            exibir_separador()
            break
        except Exception as e:
            print(f"\n❌ ERRO INESPERADO: {e}")


def executar_testes() -> None:
    """
    Executa uma bateria de testes para a função eh_primo.

    Inclui:
    - Testes com números específicos
    - Listagem de primos até 50
    - Listagem de primos até 100 com contagem
    """
    numeros_teste = [1, 2, 3, 4, 5, 10, 11, 13, 17, 19, 20, 23, 25, 29, 30, 97]

    exibir_separador()
    print(TITULO_TESTE)
    exibir_separador()

    # Testes com números específicos
    print(f"\n{MSG_TESTE_INDIVIDUAL}")
    exibir_separador("-")
    for numero in numeros_teste:
        exibir_resultado_individual(numero)

    # Primos até 50
    print("\n" + "=" * LARGURA_SEPARADOR)
    print(MSG_PRIMOS_ATE_50)
    exibir_separador("-")
    primos_50 = encontrar_primos_ate(50)
    print(primos_50)

    # Primos até 100
    print("\n" + "=" * LARGURA_SEPARADOR)
    print(MSG_PRIMOS_ATE_100)
    exibir_separador("-")
    primos_100 = encontrar_primos_ate(100)
    print(f"{MSG_TOTAL_PRIMOS} {len(primos_100)}")
    print(primos_100)
    exibir_separador()


if __name__ == "__main__":
    solicitar_entrada_usuario()
