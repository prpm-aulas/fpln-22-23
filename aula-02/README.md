# Aula 2 - Geração de um ficheiro a partir de inputs

## Exercício

1. Criar um programa `gerador.py` que lê do terminal um _título_, um _autor_ e um _ano de publicação_, e de seguida imprime os valores lidos de acordo com um formato.
   
   **O que fazer**:
   
   Correr o programa
   
   ```bash
   python3 gerador.py
   ```
   
   deverá pedir os seguintes inputs (*os valores passados são exemplos*),
   
   ```
   Insira um título: A Mensagem
   Insira o autor: Fernando Pessoa
   Insira a data da publicação: 1934/12/01
   ```
   
   e de seguida deverá imprimir o seguinte,
   
   ```yaml
   titulo: A Mensagem
   autor: Fernando Pessoa
   data: 1934/12/01
   ```

2. O texto que imprimimos no exercício anterior está escrito no formato [YAML](https://yaml.org/). Para além do YAML, existem outros formatos, como o [JSON](https://www.json.org/json-en.html) ou o [XML](https://pt.wikipedia.org/wiki/XML).
   Acrescente ao programa `gerador.py` a possibilidade de escolhermos em que formato (YAML ou JSON) é que queremos imprimir o conteúdo final.
   
   **O que fazer**:
   
   Para além dos *inputs* que já passávamos no exercício anterior, vamos acrescentar um novo *input* que definirá o formato do texto final.
   
   ```
   Insira o formato: ...
   ```
   
   **Se** o <u>formato for o YAML</u>, **então** o texto continuará a ser:
   
   ```yaml
   titulo: A Mensagem
   autor: Fernando Pessoa
   data: 1934/12/01
   ```
   
   **Senão**, no caso de ser JSON, deverá imprimir:
   
   ```json
   {
       "titulo": "A Mensagem",
       "autor": "Fernando Pessoa",
       "data": "1934/12/01"
   }
   ```

3. Atualize o `gerador.py` de forma a poder especificar um ficheiro para guardar o texto que gera.
   
   **O que fazer**:
   
   Acrescentar um novo *input* ao programa.
   
   ```
   Insira o nome do ficheiro onde quer guardar o resultado: ...
   ```
   
   Por exemplo, imaginemos que o nome do ficheiro introduzido foi `mensagem`. Se o formato for YAML, o programa deverá criar um ficheiro chamado `mensagem.yml`. Se for JSON, o ficheiro deverá chamar-se `mensagem.json`.

## Extra

1. Alguns parâmetros podem ser opcionais, i.e. o utilizador pode decidir não escrever nada. Por exemplo,
   
   - se o utilizador não passar nenhuma data, não queremos colocar o campo `data` no resultado final;
   
   - caso não passe nenhum formato, o programa deverá assumir o formato YAML por *default*;
   
   - se não passar nenhum nome de ficheiro, o programa deverá utilizar o título da obra como nome do ficheiro resultante;
   
   - o título e o autor deverão ser obrigatórios. Isto é, caso o utilizador não passe um ou outro, o programa deverá imprimir uma mensagem de erro (por exemplo: `ERRO: Título não pode ser vazio!`) e parar.
   
   Melhore o `gerador.py` de forma a que consiga lidar com *inputs* inválidos ou incompletos.

2. Implemente também o formato XML.
   
   `mensagem.xml`
   
   ```xml
   <obra data="1934/12/01">
       <titulo>A Mensagem</titulo>
       <autor>Fernando Pessoa</autor>
   </obra>
   ```
