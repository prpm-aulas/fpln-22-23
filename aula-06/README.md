# Aula 6 - Processamento de Texto

## Exercícios

O ficheiro `texto.txt` contém um exemplo de um texto para ser utilizado nos próximos exercícios.

1. Crie uma função `conta` que recebe como argumento uma `string` que representa o nome de um ficheiro, lê o conteúdo desse ficheiro, e devolva o número de palavras que estão nesse conteúdo.
> Sugestão: Utilizar a função das *strings* `split`

Exemplo:
```python
n = conta("texto.txt")
print(n)

---

653
```

2. Melhore a função `conta` de forma a que devolva uma estrutura com o número de ocorrências de cada palavra no texto.

3. Crie uma função `limpa`, que recebe uma `string` como argumento, remove todos os sinais de pontuação do argumento, e retorna então uma nova `string` sem os sinais de pontuação.
Use esta função `limpa` para melhorar também a função `conta` de modo a evitar a ocorrência de palavras com sinais.
> Sugestão: Utilizar a função das *strings* `replace`

Exemplo:
```python
t = limpa("Hello, world!")
print(t)

---

"Hello world"
```

4. Muitas das palavras que estão no texto não têm muita "importância", como por exemplo os determinantes, as preposições, ou as conjunções. Estas palavras normalmente são chamadas de *stop words*.
Crie uma função `remove_stop_words` que recebe uma lista de palavras, e retorna uma nova lista sem as *stop words*.

Acrescente esta função à função `conta`.


5. Crie agora uma função `desenha_nuvem` que gera uma imagem com uma nuvem de palavras.
Para isto, deverá utilizar a biblioteca `wordcloud` que pode ser instalada através do comando
```bash
pip3 install wordcloud
```

Exemplo de utilização da biblioteca:
```python
from wordcloud import WordCloud

d = {'hello': 3, 'world': 1, 'Olá': 2, 'mundo': 10, 'adeus': 3}

# gerar a nuvem
wordcloud = WordCloud().generate_from_frequencies(d)

# desenhar a nuvem
image = wordcloud.to_image()
image.show()
```

