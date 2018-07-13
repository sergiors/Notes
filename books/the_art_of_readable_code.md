---
title: The Art of Readable Code
---

The Art of Readable Code
------------------------

### Teorema fundamental de legibilidade
> Deve ser escrito para minimizar o tempo necessário para sua compreensão.

### Criação de nomes informativos
* Valores com unidades.
* Palavras especificas.
* Prefira nomes concretos, capaz de descrições mais detalhadas.
* Nome pequenos em escopos pequenos.

> Para expressões, menos linhas, tokens pode ser ruim.

### Nomes que não podem ser mal interpretados
Para intervalos inclusivos start e stop (stop não diz que ta incluso) -> last begin e end p/ inclusivo/exclusivo.
     
Para definir limite superior ou inferior: `max` e `min`.

Nome boolean, evite métodos negados e prefira utilizar: is, has, can ou should para deixar claro que é um boolean.

Exemplo: `disable_ssl` -> `use_ssl`

`get()` e `size()` no geral se espera como métodos leveis.

`size` vs `countSize`, o problema esta em não mostrar o que size faz, enquanto countSize deixa claro que ele será contado, evitando uma operação O(n2).

```javascript
while (list.size() > max_size)
```


```php
// off by one
10 >= 10

// fixed
10 > 10
```
[off-by-one - excedido-por-um](https://en.wikipedia.org/wiki/Off-by-one_error)

### Estética
- Métodos podem eliminar irregularidades (código duplicado)
- Alinhar em colunas podem ajudar a identificar erro de digitação (quando há variáveis semelhantes)
- Separar os “parágrafos" do código em blocos lógicos

### Comentários
- Comentário-muleta: que compensa código ruim.
- A história do valor de uma constante. O motivo por que aquele valor.
- Exemplos para entrada e saída de funções. (docblock)

> **Simplificar o código é minimizar o trabalho mental.** Quanto mais esforço mental, mais bugs podem passar despercebidos.

### Expressões gigantes

```javascript
// Variáveis de explicação

username = line.split(':')[0].strip()
if (username == 'root') {
    // ...
}
```

```javascript
// Variáveis de resumo

userOwnsDocument = req.user.id == doc.owner_id
```

- Quanto mais variáveis forem utilizadas mais difícil será monitora-las.
- Quanto maior o escopo, mais longo será monitora-las intervalo de tempo que você terá de monitorar.
- Quanto mais alterações, mais difícil será monitorar seu valor atual.

### Variáveis e legibilidade
- Para variáveis de fluxo dentro de loop, a transferencia de código pode auxiliar e também ajudar para ter um alinhamento menor. (Object Calisthenics)
- Em muitos casos é possível eliminar variáveis de resultados intermediários. ( extract method)
- Reduzir escopo de variáveis:
- Delegação para classes menores.

> - Quanto maior o escopo da variável, maior change de mudança (estado) acidental.
> - Variáveis em escopo menores auxilia na imutabilidade.
> - Quanto mais alterar a variável, possivelmente, maior a complexidade ciclomática

### Extração de subproblemas não relacionados
- Divide responsabilidade
- Auxilia em testes unitário, manutenção e object calisthenics ([Rule 1: Only One Level Of Indentation Per Method](http://refactoring.com/catalog/extractMethod.html))

### Transforme seus pensamentos em código
- Descreve o que seu código tem que fazer em linguagem simples
- Preste atenção as palavras-chaves e essenciais
- Escreve o código de acordo com essa descrição
- Rubber duck, explique seu problema ao pato de borracha para destravar o chakra

### Escreva menos código
- O melhor código é aquele que não existe
- Conheça sua ferramentas (linguagem)
- Código novo implica novas responsabilidades, como teste, documentação e gerenciamento (manutenção).

### Links
- https://martinfowler.com/bliki/FunctionLength.html
- https://gist.github.com/marcelgsantos/78837adf48491a05e42f0fee1530d650
- http://journal.stuffwithstuff.com/2009/06/05/naming-things-in-code/