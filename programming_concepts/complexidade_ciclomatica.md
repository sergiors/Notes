---
title: Complexidade ciclomática
---

Complexidade ciclomática
------------------------

**"Quantidade de caminhos percorrido até o fim do algoritmo."**

Tem como base a teoria de grafos.

Teste de caixa branca ou estrutural: verifica os procedimentos de um sistema testado
Teste de caixa preta: testa apenas a entradas e saídas

# Teoria dos grafos

8 vertices (círculos)
12 arestas (traços)

*Cada escolha tomada é um nó, ou seja, todos elementos que vão usar da lógica para decidir o caminho.*

**V(G) = E - N + 2**
**V(G)** número ciclomático
**E** quantidade de arestas
**N** quantidade de nós

```php
// 19 é maior ou igual a 18, é válido
// 18 é maior ou igual a 18, é válido
// 17 é maior ou igual a 18, é inválido

// E = 5
// N = 5
// V(G) = 5 - 5 + 2
// V(G) = 2

function legal_age(int $yr_old): bool
{
    if ($yr_old >= 18) {
        return true;
    } else {
        return false;
    }
}
```


```php
// E = 6
// N = 6
// V(G) = 6 - 6 + 2
// V(G) = 2

function legal_age(int $yr_old): bool
{
    if ($yr_old >= 18) {
        return true;
    }

    if ($yr_old < 18)
        return false;
    }
}
```

```php
// E = 3
// N = 4
// V(G) = 3 - 4 + 2
// V(G) = 1

function legal_age(int $yr_old): bool
{
    if ($yr_old >= 18) {
        return true;
    }

    return false;
}
```

```php
function legal_age(int $yr_old): bool
{
    return $yr_old >= 18
}
```