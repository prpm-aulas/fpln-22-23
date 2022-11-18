## Trabalho Prático

Deve ser feito em grupos de 2 elementos.

Entrega: 20 Janeiro (código + relatório)

# Lista telefónica

Este trabalho prático consiste em criar uma ferramenta para gerir uma lista de contactos.


## Dados

Um contacto deve ser composto, no mínimo, por:
* `id` - um número único que serve como identificador do contacto;
* `nome`- nome do contacto;
* `numeros` - lista de números telefónicos associado àquele contacto;

> **Nota**: Estejam à vontade para modificar a estrutura dos vossos contactos. Por exemplo: 
> - podem decidir colocar `primeiro_nome` e `ultimo_nome` em vez de apenas `nome`; 
> - adicionar campos adicionais: `email`, `notas`, etc.; 
> - a lista de números pode incluir um pequeno campo para identificar o que é um número específico: `telefone de casa`, `telemóvel da empresa`, etc;

## Funcionalidades

A ferramenta deve ter as seguintes funcionalidades:

### Adicionar um novo contacto

```bash
python3 contactos.py adicionar
```

### Editar um contacto

```bash
python3 contactos.py editar [id]
```

### Apagar um contacto

```bash
python3 contactos.py apagar [id]
```

### Apresentar a lista de contactos por ordem alfabética

```bash
python3 contactos.py lista
```

### Pesquisar por um determinado contacto

```bash
python3 contactos.py pesquisar [padrao]
```

---
## Funcionalidades Extra

### Imprimir um texto de ajuda para a utilização da ferramenta.
```bash
python3 contactos.py ajuda
```
Deverá imprimir, por exemplo:
```
Utilização:
  python3 contactos.py [comando] [argumentos...]
  
  Comandos:
    adicionar             Adiciona um novo contacto
    editar [id]           Edita o contacto com o identificador [id]
    apagar [id]           Elimina o contacto com o identificador [id]
    lista                 Apresenta a lista total de contactos por ordem alfabética
    pesquisar [padrao]    Pesquisa e apresenta os resultados da procura por [padrao] na lista
```

### Importar uma lista de contactos de um ficheiro.
```bash
python3 contactos.py importar [ficheiro]
```

### Extrair a lista de contactos para um ficheiro com um determinado formato.
```
python3 contactos.py extrair [formato] [ficheiro]
```




