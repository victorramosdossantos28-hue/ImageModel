# Explicação linha por linha.

Este documento descreve cada linha do código presente em `Teste001.py`, inclusive os erros existentes no código original.

1. `#                                      CÓDIGO COM ERROS`  
   - Comentário indicando que o código contém erros.

2. `# ENTRADA DE DADOS`  
   - Comentário que separa a seção onde o programa irá solicitar dados ao usuário.

3. `cliente = input("Qual é seu nome? ")`  
   - Lê uma string do usuário com a pergunta sobre o nome. O valor digitado é armazenado na variável `cliente`.

4. `qtd1 = int(input("Quantidade do item 1: "))`  
   - Lê um valor do usuário e converte para inteiro (`int`). Este valor representa a quantidade do item 1.

5. `item1 = float(input(Preço do item 1? ))`  
   - Tenta ler o preço do item 1 como número decimal.  
   - **Erro:** A string de prompt não está entre aspas, portanto o Python não entende e gera um erro de sintaxe.

6. `qtd2 = int(input("Quantidade do item 2: "))`  
   - Lê a quantidade do item 2 e converte para inteiro.

7. `item2 = float(input("Preço do item 2? "))`  
   - Lê o preço do item 2 e converte para float.

8. `qtd3 = int(input("Quantidade do item 3: "))`  
   - Lê a quantidade do item 3 e converte para inteiro.

9. `item3 = float(input("Preço do item 3? "))`  
   - Lê o preço do item 3 e converte para float.

10. `# CÁLCULOS DOS ITENS`  
    - Comentário que marca o início da seção de cálculo dos valores.

11. `total_item1 = qtd1 * item1`  
    - Calcula o valor total do item 1 multiplicando quantidade por preço.

12. `total_item2 = qtd2 * item2`  
    - Calcula o valor total do item 2.

13. `total_item3 = qtd3 * item3`  
    - Calcula o valor total do item 3.

14. `subtotal = total_item1 + total_item2 + total_item3`  
    - Soma os totais dos três itens para obter o subtotal.

15. `imposto = subtotal * 0.10`  
    - Calcula o imposto como 10% do `subtotal`.

16. `# DESCONTO`  
    - Comentário que marca a seção de desconto.

17. `desconto_cupom = (input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))`  
    - Lê do usuário um valor para o desconto.  
    - **Nota:** O resultado é uma string e não um número. O código abaixo tenta usar essa string em operações matemáticas, o que causa erro se não for convertida.

18. `desconto = subtotal * (desconto_cupom / 100)`  
    - Calcula o valor do desconto baseado no subtotal e no percentual informado.  
    - **Erro potencial:** `desconto_cupom` é string, então a divisão por 100 não funciona sem conversão para `float` ou `int`.

19. `# TOTAL FINAL`  
    - Comentário que indica o cálculo do total final.

20. `total = subtotal + imposto - desconto`  
    - Calcula o valor total a pagar somando subtotal e imposto, e subtraindo o desconto.

21. `# EXIBIÇÃO`  
    - Comentário que separa a parte de exibição dos resultados.

22. `linha = "=" * 31`  
    - Cria uma string com 31 sinais de igual `=` para formatar a saída.

23. `separador = "-" * 31`  
    - Cria uma string com 31 hífens `-` para separar seções na saída.

24. `print(linha)`  
    - Imprime a linha de iguals no console.

25. `print(f" Cliente: {cliente}")`  
    - Exibe o nome do cliente em formato formatado.

26. `print(linha)`  
    - Imprime novamente a linha de iguals.

27. `print(f" Item 1:        R$ {total_item1:.2f}")`  
    - Mostra o valor total do item 1 com duas casas decimais.

28. `print(" Item 2:        R$ {total_item2:.2f}")`  
    - Tenta exibir o valor total do item 2, mas não usa `f-string` corretamente.  
    - **Erro:** O texto não é formatado; será exibido literalmente como `{total_item2:.2f}`.

29. `print(f" Item 3:        R$ {total_item3:.2f}")`  
    - Mostra o valor total do item 3 com duas casas decimais.

30. `print(separador)`  
    - Imprime a linha de hífens para separar a listagem do total.

31. `print(f" Subtotal:      R$ {subtotal:.2f}")`  
    - Exibe o subtotal com duas casas decimais.

32. `print(f" Imposto (10%): R$ {imposto:.2f}")`  
    - Exibe o imposto calculado.

33. `if desconto_cupom > 0: `  
    - Verifica se o valor do cupom de desconto é maior que zero.  
    - **Erro:** `desconto_cupom` ainda é string, então essa comparação pode falhar ou lançar erro.

34. `print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")`  
    - Exibe o desconto aplicado.  
    - **Erro de indentação:** A linha de impressão não está indentada sob o `if`, gerando erro de sintaxe.

35. `print(linha)`  
    - Imprime a linha de iguals antes do total final.

36. `print(f" TOTAL:         R$ {round(total, 2):.2f}")`  
    - Exibe o total final com duas casas decimais. O `round(total, 2)` garante arredondamento adequado.

37. `print(linha)`  
    - Imprime a última linha de iguals para concluir a saída.

---

Observações gerais:
- O código precisa corrigir a string do prompt em `item1`.
- O valor de `desconto_cupom` deve ser convertido para número (`int` ou `float`) antes de usar em operações.
- A formatação do `print` de `Item 2` deve usar `f-string`.
- A linha `print(f" Desconto ...")` deve ser indentada corretamente dentro do bloco `if`.
- Se quiser, posso também corrigir o script e criar uma versão funcional em Python.


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
