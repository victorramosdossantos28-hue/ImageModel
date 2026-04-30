# ENTRADA DE DADOS
cliente = input("Qual é seu nome? ")  # nome do cliente para personalizar o recibo

# Cada item usa int para quantidade e float para preço porque quantidades são inteiras
# enquanto valores monetários podem conter centavos.
qtd1 = int(input("Quantidade do item 1: "))
item1 = float(input("Preço do item 1? "))

qtd2 = int(input("Quantidade do item 2: "))
item2 = float(input("Preço do item 2? "))

qtd3 = int(input("Quantidade do item 3: "))
item3 = float(input("Preço do item 3? "))

# CÁLCULOS DOS ITENS
# Multiplica quantidade pelo preço unitário para obter o total de cada item.
total_item1 = qtd1 * item1
total_item2 = qtd2 * item2
total_item3 = qtd3 * item3

# O subtotal é a soma dos valores parciais dos três itens.
subtotal = total_item1 + total_item2 + total_item3

# Imposto fixo de 10% aplicado sobre o subtotal.
imposto = subtotal * 0.10

# DESCONTO
# O cupom é informado como percentual, então convertemos para fração antes de aplicar.
desconto_cupom = float(input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
desconto = subtotal * (desconto_cupom / 100)

# TOTAL FINAL
# Primeiro soma-se o imposto e depois subtrai-se o desconto para refletir o valor final do pedido.
total = subtotal + imposto - desconto

# EXIBIÇÃO
# As linhas fixas tornam a saída mais legível e estruturam o recibo.
linha = "=" * 31
separador = "-" * 31

print(linha)
print(f" Cliente: {cliente}")
print(linha)
print(f" Item 1:        R$ {total_item1:.2f}")
print(f" Item 2:        R$ {total_item2:.2f}")
print(f" Item 3:        R$ {total_item3:.2f}")
print(separador)
print(f" Subtotal:      R$ {subtotal:.2f}")
print(f" Imposto (10%): R$ {imposto:.2f}")

# Só exibimos a linha de desconto se houver um cupom válido.
if desconto_cupom > 0:
    print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")

print(linha)
print(f" TOTAL:         R$ {total:.2f}")
print(linha)
