# Explicação: Refatoração do Código de Estatísticas

## Código Original (Não Refatorado)

```python
def c(l):
    t=0
    for i in range(len(l)):
        t=t+l[i]
    m=t/len(l)
    mx=l[0]
    mn=l[0]
    for i in range(len(l)):
        if l[i]>mx:
            mx=l[i]
        if l[i]<mn:
            mn=l[i]
    return t,m,mx,mn

x=[23,7,45,2,67,12,89,34,56,11]
a,b,c2,d=c(x)
print("total:",a)
print("media:",b)
print("maior:",c2)
print("menor:",d)
```

## Código Refatorado

```python
def calculate_statistics(numbers: list[int]) -> tuple[int, float, int, int]:
    """
    Calcula estatísticas básicas de uma lista de números.
    
    Args:
        numbers: Lista de números inteiros para análise.
    
    Returns:
        Tupla contendo (total, média, máximo, mínimo).
    """
    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    
    return total, average, maximum, minimum


def main() -> None:
    """Executa o programa principal."""
    numbers = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]
    
    total, average, maximum, minimum = calculate_statistics(numbers)
    
    print(f"Total:   {total}")
    print(f"Média:   {average:.2f}")
    print(f"Máximo:  {maximum}")
    print(f"Mínimo:  {minimum}")


if __name__ == "__main__":
    main()
```

---

## Análise Detalhada: Problemas do Código Original

### 1. **Nomenclatura Inadequada**

| Original | Refatorado | Problema |
|----------|-----------|----------|
| `c(l)` | `calculate_statistics(numbers)` | Nomes de função e parâmetro muito curtos e sem significado |
| `t` | `total` | Variável confusa - não dá significado |
| `m` | `average` | Uma letra não descreve o que é média |
| `mx` | `maximum` | Abreviação dificulta leitura |
| `mn` | `minimum` | Abreviação não segue convenção clara |
| `x` | `numbers` | Variável global sem contexto |
| `a, b, c2, d` | `total, average, maximum, minimum` | Nomes genéricos e confusos |

### 2. **Ausência de Documentação**

**Original**: Nenhuma documentação
- Não há docstring explicando o que a função faz
- Parâmetros e retorno não documentados
- Dificulta compreensão para outros desenvolvedores

**Refatorado**: Docstring completa
```python
"""
Calcula estatísticas básicas de uma lista de números.

Args:
    numbers: Lista de números inteiros para análise.

Returns:
    Tupla contendo (total, média, máximo, mínimo).
"""
```

### 3. **Type Hints Ausentes**

**Original**: 
```python
def c(l):  # Qual é o tipo? O que retorna?
```

**Refatorado**:
```python
def calculate_statistics(numbers: list[int]) -> tuple[int, float, int, int]:
```
- Melhor compreensão do código
- Detecção de erros em IDEs
- Facilita manutenção e debugging

### 4. **Uso de Loops Desnecessários**

**Original**: 
```python
# Cálculo de soma com loop
t=0
for i in range(len(l)):
    t=t+l[i]

# Cálculo de máximo com loop
mx=l[0]
for i in range(len(l)):
    if l[i]>mx:
        mx=l[i]

# Cálculo de mínimo com loop
mn=l[0]
for i in range(len(l)):
    if l[i]<mn:
        mn=l[i]
```

**Refatorado**:
```python
total = sum(numbers)        # Função built-in mais legível
maximum = max(numbers)      # Função built-in mais eficiente
minimum = min(numbers)      # Função built-in mais concisa
```

**Benefícios**:
- Código mais legível
- Funções built-in são otimizadas em C
- Menos linhas, menos bugs
- Segue princípio DRY (Don't Repeat Yourself)

### 5. **Formatação Inadequada**

**Original**:
```python
print("total:",a)
print("media:",b)
print("maior:",c2)
print("menor:",d)
```

**Refatorado**:
```python
print(f"Total:   {total}")
print(f"Média:   {average:.2f}")
print(f"Máximo:  {maximum}")
print(f"Mínimo:  {minimum}")
```

**Melhorias**:
- F-strings são mais modernas e legíveis
- Formatação de número decimal com `.2f`
- Alinhamento visual com espaços
- Capitalização adequada nos labels

### 6. **Estrutura do Programa**

**Original**: Código espalhado no escopo global
```python
x=[23,7,45,2,67,12,89,34,56,11]
a,b,c2,d=c(x)
print(...)
```

**Refatorado**: Estrutura profissional com `main()`
```python
def main() -> None:
    """Executa o programa principal."""
    numbers = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]
    total, average, maximum, minimum = calculate_statistics(numbers)
    print(...)

if __name__ == "__main__":
    main()
```

**Benefícios**:
- Protetor `if __name__ == "__main__"` permite importar o módulo sem executar
- Código mais modular e testável
- Segue boas práticas de desenvolvimento
- Facilita reutilização do código

---

## Resumo das Melhorias

| Aspecto | Antes | Depois |
|--------|-------|--------|
| **Nomes** | Confusos e abreviados | Descritivos e claros |
| **Documentação** | Nenhuma | Docstring completa |
| **Type Hints** | Ausentes | Presentes em toda a função |
| **Loops** | Manuais e repetitivos | Funções built-in |
| **Formatação** | String concatenation | F-strings |
| **Estrutura** | Global | Função `main()` organizada |
| **Readability** | Baixa | Alta |
| **Manutenibilidade** | Difícil | Fácil |

---

## Lições Aprendidas

1. ✅ Use nomes descritivos para variáveis e funções
2. ✅ Sempre adicione type hints em Python 3.5+
3. ✅ Documente suas funções com docstrings
4. ✅ Prefira funções built-in quando disponíveis
5. ✅ Use f-strings para formatação de strings
6. ✅ Estruture código com função `main()` e protetor `if __name__ == "__main__"`
7. ✅ Siga PEP 8 para compatibilidade com comunidade Python
