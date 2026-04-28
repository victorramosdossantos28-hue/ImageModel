#                                      CÓDIGO COM ERROS                           
# ENTRADA DE DADOS
cliente = input("Qual é seu nome? ")

qtd1 = int(input("Quantidade do item 1: "))
item1 = float(input(Preço do item 1? ))

qtd2 = int(input("Quantidade do item 2: "))
item2 = float(input("Preço do item 2? "))

qtd3 = int(input("Quantidade do item 3: "))
item3 = float(input("Preço do item 3? "))

# CÁLCULOS DOS ITENS
total_item1 = qtd1 * item1
total_item2 = qtd2 * item2
total_item3 = qtd3 * item3

subtotal = total_item1 + total_item2 + total_item3
imposto = subtotal * 0.10

# DESCONTO
desconto_cupom = (input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
desconto = subtotal * (desconto_cupom / 100)

# TOTAL FINAL
total = subtotal + imposto - desconto

# EXIBIÇÃO
linha = "=" * 31
separador = "-" * 31

print(linha)
print(f" Cliente: {cliente}")
print(linha)
print(f" Item 1:        R$ {total_item1:.2f}")
print(" Item 2:        R$ {total_item2:.2f}")
print(f" Item 3:        R$ {total_item3:.2f}")
print(separador)
print(f" Subtotal:      R$ {subtotal:.2f}")
print(f" Imposto (10%): R$ {imposto:.2f}")

if desconto_cupom > 0: 
print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")

print(linha)
print(f" TOTAL:         R$ {round(total, 2):.2f}")
print(linha)
```

## Identificação dos erros

1. `item1 = float(input(Preço do item 1? ))`
   - Falta de aspas no texto exibido ao usuário.
   - Isso causa um erro de sintaxe.

2. `item2 = float(input("Preço do item 2? "))` estava correto no valor, mas o `print` de `Item 2` não usava `f-string`.
   - A linha `print(" Item 2:        R$ {total_item2:.2f}")` imprime o literal em vez do valor.

3. `desconto_cupom` era lido como string.
   - O cálculo `desconto = subtotal * (desconto_cupom / 100)` falha porque não é possível dividir uma string por número.

4. A condição `if desconto_cupom > 0:` estava indentada incorretamente no bloco original.
   - Isso gera `IndentationError` em Python.

## Explicação da causa

- Strings em `input(...)` devem estar entre aspas. Sem aspas, o Python tenta interpretar o texto como expressão, o que é inválido neste contexto.
- Um `f-string` (`f"..."`) é necessário sempre que se quer interpolar variáveis dentro de uma string. Sem ele, o Python não substitui `{total_item2:.2f}` pelo valor real.
- `input()` retorna texto. Para fazer operações matemáticas, é preciso converter o resultado para `int` ou `float`.
- Em Python, o corpo do `if` deve ser indentado corretamente. Sem indentação, o código quebra.

## Proposta de correção

1. Adicionar aspas nas strings de prompts:
   - `float(input("Preço do item 1? "))`
2. Converter `desconto_cupom` para número:
   - `desconto_cupom = float(input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))`
3. Usar `f-string` para imprimir valores formatados:
   - `print(f" Item 2:        R$ {total_item2:.2f}")`
4. Ajustar a indentação do bloco `if`:
   - ```
     if desconto_cupom > 0:
         print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")
     ```

## Resultado

O código agora lê corretamente os valores, calcula subtotal, imposto e desconto, e exibe o relatório final com formatação adequada.
