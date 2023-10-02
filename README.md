# Projeto de Gerenciamento de Produtos

Este projeto consiste em desenvolver um sistema de gerenciamento de produtos, onde você pode pesquisar produtos por ID ou tipo, adicionar novos produtos ao menu e calcular o subtotal do consumo de uma mesa. O projeto está estruturado em módulos e pacotes, seguindo as melhores práticas de organização de código.

## Tecnologias Utilizadas

- Python 3.9
- Git
- GitHub

[![Python](https://img.shields.io/badge/Python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)

## Estrutura do Projeto

O projeto está organizado da seguinte maneira:

- `management`: Pacote que contém o módulo `product_handler`.
- `tests`: Pasta com testes unitários para as funções do projeto.
- `main.py`: Arquivo principal para testar as funcionalidades do sistema.
- `menu.py`: Arquivo que contém a lista de produtos do menu.

## Funcionalidades

### get_product_by_id

Esta função permite buscar um produto pelo seu ID. Caso o produto seja encontrado no menu, a função retorna o dicionário que o representa. Caso contrário, retorna um dicionário vazio.

**Exemplo de uso:**

```python
from management.product_handler import get_product_by_id

if __name__ == "__main__":
    print(get_product_by_id(28))
```

**Saída:**

```python
{
  '_id': 28,
  'description': 'Ricotta with berry and mint',
  'price': 27.81,
  'rating': 5,
  'title': 'Ricotta',
  'type': 'dairy'
}
```

### get_products_by_type

Esta função permite buscar produtos por tipo. Caso nenhum produto do tipo especificado seja encontrado, a função retorna uma lista vazia. Caso contrário, retorna uma lista contendo todos os produtos do tipo especificado.

**Exemplo de uso:**

```python
from management.product_handler import get_products_by_type

if __name__ == "__main__":
    print(get_products_by_type('drink'))
```

**Saída:**

```python
[
  {
    '_id': 32,
    'description': 'Mix of rum, lemon juice, mint, sugar and sparking water',
    'price': 27.61,
    'rating': 4,
    'title': 'Mojito',
    'type': 'drink'
},
  {
    '_id': 37,
    'description': 'Homemade cola drink with lemon juice and 2 ice cubes',
    'price': 28.96,
    'rating': 5,
    'title': 'Fresh Nuka-Cola',
    'type': 'drink'
  }
]
```

### add_product

A função `add_product` permite adicionar novos produtos ao menu. Ela gera um novo ID único para o produto adicionado e o armazena na chave "_id" do novo produto. O ID gerado é referente ao maior ID de produto do menu, somado com 1. Caso não haja produtos no menu, o ID gerado é 1. A função retorna apenas o produto adicionado com o ID gerado.

**Exemplo de uso:**

```python
from menu import products
from management.product_handler import add_product

if __name__ == "__main__":
    new_product = {
        "title": "X-Python",
        "price": 5.0,
        "rating": 5,
        "description": "Sanduíche de Python",
        "type": "fast-food"
    }
    print(add_product(products, **new_product))
```

**Saída:**

```python
{
  'title': 'X-Python',
  'price': 5.0,
  'rating': 5,
  'description': 'Sanduíche de Python',
  'type': 'fast-food',
  '_id': 103
}
```

### calculate_tab

A função `calculate_tab` calcula o subtotal do consumo de uma mesa com base em uma lista de dicionários representando os consumos. Cada dicionário contém a identificação ("_id") do produto consumido e a quantidade (amount) do produto consumida. A função retorna um dicionário com a chave "subtotal" contendo o valor total do consumo arredondado para duas casas decimais no máximo.

**Exemplo de uso:**

```python
from management.tab_handler import calculate_tab

if __name__ == "__main__":
    table_1 = [{"_id": 1, "amount": 5}, {"_id": 19, "amount": 5}]
    table_2 = [
        {"_id": 10, "amount": 3},
        {"_id": 20, "amount": 2},
        {"_id": 21, "amount": 5},
    ]

    print(calculate_tab(table_1))
    print(calculate_tab(table_2))
```

**Saída:**

```python
{'subtotal': '$216.1'}
{'subtotal': '$188.29'}
```

## Relatório do Menu

A função `menu_report` no módulo `product

_handler` gera um relatório sobre o menu de produtos com as seguintes informações:

- Total de produtos no menu.
- Preço médio de todos os produtos no menu (arredondado para duas casas decimais no máximo).
- Tipo mais comum de produto (o tipo com maior quantidade de produtos no menu).

**Exemplo de uso:**

```python
from management.product_handler import menu_report

if __name__ == "__main__":
    print(menu_report())
```

**Saída:**

```python
"Products Count: 51 - Average Price: $20.6 - Most Common Type: fruit"
```

## Contribuição

Este projeto foi desenvolvido como parte de um curso de programação na Kenzie Academy Brasil. Sinta-se à vontade para contribuir com melhorias ou correções. Basta criar um fork e enviar um pull request.
