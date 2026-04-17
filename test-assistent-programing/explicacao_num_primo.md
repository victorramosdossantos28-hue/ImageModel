# Explicação Técnica do Código: Verificador de Números Primos

## **Visão Geral das Melhorias (Clean Code)**

O código foi refatorado aplicando as seguintes técnicas de clean code:

✅ **Type Hints (PEP 484)** - Melhor legibilidade e detecção de erros
✅ **Constantes Bem Nomeadas** - Evita "números mágicos"
✅ **Docstrings Detalhadas** - Documentação clara e precisa
✅ **Funções Auxiliares** - Separação de responsabilidades
✅ **Validação de Tipo** - Tratamento de exceções
✅ **Nomes Descritivos** - Variáveis e funções com significado semântico

---

## **Análise Linha a Linha**

### **1. Módulo Docstring (Linhas 1-5)**
```python
"""
Módulo de verificação de números primos.

Este módulo fornece funções otimizadas para verificar se um número é primo
e executar testes em lotes de números.
"""
```
**Lógica:** Documenta o propósito do módulo inteiro. Segue as convenções PEP 257.

---

### **2. Importações (Linhas 7-8)**
```python
import math
from typing import List
```
- `math`: Fornece `math.sqrt()` para calcular raiz quadrada
- `typing.List`: Type hint para indicar que uma função retorna uma lista

---

### **3. Constantes (Linhas 10-17)**
```python
VALOR_MINIMO_PRIMO = 2
NUMERO_PAR_PRIMO = 2
LIMITE_INFERIOR = 1
FATOR_INCREMENTO = 2
LARGURA_SEPARADOR = 50
```
**Benefício:** Elimina "números mágicos" no código. Facilita manutenção.

### **4. Constantes de Mensagens (Linhas 19-24)**
```python
TITULO_TESTE = "TESTE DE NÚMEROS PRIMOS"
MSG_TESTE_INDIVIDUAL = "Testando números individuais:"
# ... etc
```
**Benefício:** Centraliza textos da aplicação. Facilita internacionalização.

---

### **5. Função Principal com Type Hints (Linhas 27-66)**
```python
def eh_primo(numero: int) -> bool:
    """
    Verifica se um número inteiro é primo.
    ...
    """
```
**Type Hints Explicados:**
- `numero: int` - Parâmetro deve ser inteiro
- `-> bool` - Função retorna booleano

**Docstring Detalhada (Linhas 32-50):** Inclui:
- Descrição da lógica
- Args e Returns com tipos
- Raises (exceções possíveis)
- Exemplos de uso (doctests)

---

### **6. Validação de Tipo (Linhas 51-52)**
```python
if not isinstance(numero, int):
    raise TypeError(f"Esperado int, recebido {type(numero).__name__}")
```
**Melhoria:** Valida entrada antes de processar. Facilita debug.

---

### **7. Verificações de Primalidade (Linhas 54-71)**
```python
if numero <= LIMITE_INFERIOR:
    return False

if numero == NUMERO_PAR_PRIMO:
    return True

if numero % 2 == 0:
    return False

limite_verificacao = int(math.sqrt(numero)) + 1
for divisor in range(3, limite_verificacao, FATOR_INCREMENTO):
    if numero % divisor == 0:
        return False

return True
```
**Melhorias:**
- Usa constantes em vez de valores hardcoded
- Nome `divisor` é mais descritivo que `i`
- `limite_verificacao` explica o cálculo

---

### **8. Função Auxiliar: encontrar_primos_ate (Linhas 74-87)**
```python
def encontrar_primos_ate(limite: int) -> List[int]:
    """Encontra todos os números primos até um determinado limite."""
    return [numero for numero in range(VALOR_MINIMO_PRIMO, limite + 1) if eh_primo(numero)]
```
**Benefício:**
- Separação de responsabilidades
- Reutilizável em diferentes contextos
- Type hint clara do retorno

---

### **9. Função Auxiliar: exibir_resultado_individual (Linhas 90-98)**
```python
def exibir_resultado_individual(numero: int) -> None:
    """Exibe o resultado da verificação de um número individual."""
    resultado = FORMATO_PRIMO if eh_primo(numero) else FORMATO_NAO_PRIMO
    print(f"Número {numero:3d}: {resultado}")
```
**Benefício:**
- Isolam lógica de exibição
- Facilita testes unitários
- Reduzem complexidade

---

### **10. Função de Separador (Linhas 101-107)**
```python
def exibir_separador(caractere: str = "=") -> None:
    """Exibe uma linha separadora."""
    print(caractere * LARGURA_SEPARADOR)
```
**Melhoria:** DRY (Don't Repeat Yourself) - evita repetição de `print("=" * 50)`

---

### **11. Função de Entrada Interativa (Linhas 110-159)**
```python
def solicitar_entrada_usuario() -> None:
    """Solicita um número ao usuário e verifica se é primo."""
```

**Fluxo da Função:**
1. **Loop infinito** - Permite múltiplas verificações
2. **Solicitação de entrada** - `input()` (função nativa do Python)
3. **Validação de comando** - Verifica se usuário quer sair ("sair", "exit", "quit")
4. **Conversão para inteiro** - `int(entrada)` com tratamento de erro
5. **Verificação de primalidade** - Chama `eh_primo(numero)`
6. **Exibição de resultado** - Mostra se é PRIMO ou NÃO PRIMO
7. **Informações adicionais** - Dicas sobre o número testado

**Tratamento de Exceções:**
- `ValueError` - Entrada não é número inteiro válido
- `TypeError` - Erro de tipo na validação
- `KeyboardInterrupt` - Usuário pressiona Ctrl+C
- `Exception` - Erros inesperados

---

### **12. Função de Testes Automáticos (Linhas 162-203)**
```python
def executar_testes() -> None:
    """Executa uma bateria de testes para a função eh_primo."""
```
**Melhoria:** Mantida como função separada para fins educacionais e testes automatizados.

---

### **13. Ponto de Entrada Principal (Linhas 206-207)**
```python
if __name__ == "__main__":
    solicitar_entrada_usuario()
```
Agora chama a função interativa em vez dos testes automáticos.

---

## **Modo de Uso Interativo**

Para usar o programa agora, basta executar:

```bash
python num_primo.py
```

O programa irá abrir uma interface interativa pedindo números:

```
==================================================
VERIFICADOR DE NÚMEROS PRIMOS - MODO INTERATIVO
==================================================

Digite um número inteiro para verificar se é primo
(Digite 'sair' ou 'exit' para encerrar):

>>> 17

O número 17 é: PRIMO

Digite um número inteiro para verificar se é primo
(Digite 'sair' ou 'exit' para encerrar):

>>> 24

O número 24 é: NÃO PRIMO
Nota: 24 é divisível por 2.

Digite um número inteiro para verificar se é primo
(Digite 'sair' ou 'exit' para encerrar):

>>> sair

Até logo! 👋
==================================================
```

---

## **Funcionalidades da Versão Interativa**

| Recurso | Descrição |
|---------|-----------|
| **Loop contínuo** | Permite testar múltiplos números sem reiniciar |
| **Validação de entrada** | Trata valores inválidos com mensagens de erro claras |
| **Encerramento gracioso** | Aceita "sair", "exit" ou Ctrl+C |
| **Informações adicionais** | Fornece contexto sobre o número testado |
| **Tratamento de exceções** | Captura erros e continua funcionando |

---

## **Exemplos de Entrada**

| Entrada | Saída | Nota |
|---------|-------|------|
| `2` | PRIMO | Único primo par |
| `17` | PRIMO | Número primo válido |
| `100` | NÃO PRIMO | 100 é divisível por 2 |
| `abc` | ❌ ERRO | Entrada inválida, solicita novamente |
| `sair` | Encerra | Sai do programa graciosamente |
| Ctrl+C | Encerra | Interrupção do usuário |

---

## **Imports Utilizados**

```python
import math              # Para math.sqrt() na verificação de primalidade
from typing import List # Para type hints (PEP 484)
```

**Nota:** Não foi necessário adicionar imports extras. A função `input()` é nativa do Python.

---

| Aspecto | Antes | Depois |
|---------|-------|--------|
| **Constantes** | Números hardcoded | Constantes nomeadas |
| **Type Hints** | Nenhum | Completo (PEP 484) |
| **Validação** | Nenhuma | Validação de tipo |
| **Separação** | Tudo em main | Funções bem definidas |
| **Docstrings** | Básicas | Detalhadas com exemplos |
| **Nomes Variáveis** | `i`, `num` | `divisor`, `numero` |
| **Duplicação** | Sim (print repetido) | DRY (função separadora) |

---

## **Benefícios do Clean Code Aplicado**

🎯 **Legibilidade:** Código mais fácil de entender à primeira leitura

🔍 **Manutenibilidade:** Mudanças centralizadas, menos erros

🧪 **Testabilidade:** Funções pequenas e bem definidas

📚 **Documentação:** Docstrings e type hints como documentação viva

🛡️ **Robustez:** Validação de entrada e tratamento de erros

⚙️ **Reutilização:** Funções podem ser importadas e usadas em outros projetos

---

## **Complexidade e Eficiência**

| Métrica | Valor |
|---------|-------|
| **Complexidade de Tempo** | O(√n) |
| **Complexidade de Espaço** | O(1) para `eh_primo()`, O(m) para `encontrar_primos_ate()` |
| **Melhor Caso** | O(1) - número ≤ 1 ou par |
| **Pior Caso** | O(√n) - número primo grande |

---

## **Exemplos de Execução**

### Programático (Em outro arquivo ou script):
```python
from num_primo import eh_primo, encontrar_primos_ate

# Verificação individual
print(eh_primo(2))        # True
print(eh_primo(17))       # True
print(eh_primo(100))      # False

# Encontrar primos até um limite
print(encontrar_primos_ate(20))  # [2, 3, 5, 7, 11, 13, 17, 19]
```

### Interativo (Executando o script):
```bash
$ python num_primo.py
==================================================
VERIFICADOR DE NÚMEROS PRIMOS - MODO INTERATIVO
==================================================

Digite um número inteiro para verificar se é primo
(Digite 'sair' ou 'exit' para encerrar):

>>> 7
O número 7 é: PRIMO

>>> 15
O número 15 é: NÃO PRIMO

>>> sair
Até logo! 👋
==================================================
```

---

## **Boas Práticas Aplicadas**

1. **PEP 8** - Formatação e estilo Python
2. **PEP 257** - Docstring conventions
3. **PEP 484** - Type hints
4. **SOLID** - Single Responsibility Principle
5. **DRY** - Don't Repeat Yourself
6. **KISS** - Keep It Simple, Stupid

---

## **Conclusão**

O código refatorado agora oferece duas interfaces de uso:

1. **Modo Interativo** - O usuário digita números e o programa verifica se são primos
2. **Modo Programático** - Funções podem ser importadas e usadas em outros projetos

O código mantém a eficiência algorítmica (O(√n)) enquanto oferece uma experiência de usuário intuitiva e tratamento robusto de erros. Resultado: uma ferramenta educacional completa, profissional e fácil de usar! 🚀
