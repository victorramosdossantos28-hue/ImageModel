# Test Assistant Programming

Este projeto é uma coleção de exemplos práticos de programação em Python, focados em boas práticas de desenvolvimento, refatoração de código e correção de bugs. Cada exemplo demonstra conceitos importantes como clean code, type hints, validação de entrada e otimização de algoritmos.

## 📁 Estrutura do Projeto

```
test-assistent-programing/
├── num_primo.py                    # Verificador otimizado de números primos
├── pedido_corrigido.py             # Calculadora de pedidos com correções
├── refatoracao.py                  # Estatísticas básicas refatoradas
├── explicacao_num_primo.md         # Análise detalhada do código de primos
├── explicacao_pedido_corrigido.md  # Correções aplicadas no código de pedidos
├── explicacao_refatoracao.md       # Comparação antes/depois da refatoração
└── README.md                       # Este arquivo
```

## 🚀 Funcionalidades

### 1. Verificador de Números Primos (`num_primo.py`)
- ✅ Verificação otimizada de primalidade
- ✅ Interface interativa para testes manuais
- ✅ Bateria completa de testes automatizados
- ✅ Listagem de primos até limites específicos
- ✅ Tratamento robusto de erros e validações

**Características técnicas:**
- Algoritmo O(√n) para verificação
- Type hints completos (PEP 484)
- Constantes bem nomeadas (sem números mágicos)
- Docstrings detalhadas no padrão Google
- Validação de tipos de entrada

### 2. Calculadora de Pedidos (`pedido_corrigido.py`)
- ✅ Cálculo de subtotal, imposto e desconto
- ✅ Interface amigável para entrada de dados
- ✅ Recibo formatado e profissional
- ✅ Suporte a cupons de desconto

**Correções aplicadas:**
- Sintaxe corrigida (aspas faltantes, conversões de tipo)
- Lógica de cálculo corrigida
- Formatação consistente de saída
- Comentários explicativos inline

### 3. Estatísticas Básicas (`refatoracao.py`)
- ✅ Cálculo de total, média, máximo e mínimo
- ✅ Código refatorado com boas práticas
- ✅ Type hints e docstrings
- ✅ Separação clara de responsabilidades

**Melhorias na refatoração:**
- Nomes descritivos de variáveis e funções
- Uso de funções built-in (sum, max, min)
- Estrutura modular com função main
- Documentação completa

## 🛠️ Requisitos

- Python 3.6 ou superior
- Nenhum pacote externo necessário (usa apenas bibliotecas padrão)

## 📖 Como Usar

### Verificador de Primos
```bash
python num_primo.py
```
Execute testes interativos ou visualize os resultados dos testes automatizados.

### Calculadora de Pedidos
```bash
python pedido_corrigido.py
```
Siga as instruções na tela para inserir dados do cliente e itens.

### Estatísticas
```bash
python refatoracao.py
```
Executa automaticamente com uma lista de exemplo e exibe as estatísticas.

## 📚 Exemplos de Uso

### Verificação de Primo
```python
from num_primo import eh_primo, encontrar_primos_ate

print(eh_primo(17))  # True
print(encontrar_primos_ate(50))  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
```

### Cálculo de Pedido
```
Cliente: João Silva
===============================
 Item 1:        R$ 50.00
 Item 2:        R$ 30.00
 Item 3:        R$ 20.00
-------------------------------
 Subtotal:      R$ 100.00
 Imposto (10%): R$ 10.00
 Desconto (5%): -R$ 5.00
===============================
 TOTAL:         R$ 105.00
===============================
```

### Estatísticas
```
Total:   354
Média:   35.40
Máximo: 89
Mínimo: 2
```

## 🎯 Conceitos Demonstrados

- **Clean Code**: Nomes descritivos, constantes, funções auxiliares
- **Type Hints**: Anotações de tipo para melhor legibilidade
- **Docstrings**: Documentação no padrão Google
- **Tratamento de Erros**: Validação de entrada e exceções
- **Refatoração**: Transformação de código "ruim" em código limpo
- **Otimização**: Algoritmos eficientes (ex: verificação de primos)
- **Separação de Responsabilidades**: Funções com propósitos claros
- **Interface Interativa**: Entrada/saída amigável ao usuário

## 📝 Arquivos de Explicação

Cada exemplo inclui um arquivo `.md` detalhado explicando:
- Análise linha por linha do código
- Decisões de design tomadas
- Melhorias aplicadas
- Comparação antes/depois (quando aplicável)

## 🤝 Contribuição

Este projeto serve como material educativo. Para contribuir:
1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

## 📄 Licença

Este projeto é distribuído sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👨‍💻 Autor

Projeto desenvolvido como material de estudo para boas práticas de programação em Python.