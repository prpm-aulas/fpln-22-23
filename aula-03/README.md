# Aula 3 - Gerador de Ficheiros (continuação)

## Exercício

1. Melhore o `gerador.py` de forma a que aceite um conjunto de co-autores para além do autor principal.
   **O que fazer:**
   Criar um *input* que defina o nome de um co-autor.
   
   **Enquanto** <u>o *input* não for vazio</u>, ele deverá pedir repetidamente o nome de um co-autor, criando uma lista de autores.
   
   ```
   Insira um título: A Mensagem
   Insira o autor: Fernando Pessoa
   Insira um co-autor: Pedro
   Insira um co-autor: Tiago
   Insira um co-autor: Francisca
   Insira um co-autor: 
   Insira a data da publicação: 1934/12/01
   ```
   
   Deverá imprimir:
   
   ```yaml
   titulo: A Mensagem
   autor: Fernando Pessoa
   co-autores: Pedro; Tiago; Francisca;
   data: 1934/12/01
   ```

2. Estabeleça também um limite para o número de co-autores que uma obra pode ter (por exemplo: `5`). O programa deve pedir o nome dos co-autores enquanto este limite não for excedido ou o *input* de um co-autor não for vazio.
   
   O programa deverá ter o seguinte comportamento:
   
   ```
   Insira um título: A Mensagem
   Insira o autor: Fernando Pessoa
   Insira um co-autor (0/5): Pedro
   Insira um co-autor (1/5): Tiago
   Insira um co-autor (2/5): Francisca
   Insira um co-autor (3/5): Carolina
   Insira um co-autor (4/5): Guilherme
   AVISO: Limite de co-autores atingido (5/5)
   Insira a data da publicação: 1934/12/01
   ```

3. Melhore o `gerador.py` de forma a eliminar entradas repetidas de co-autores.
   
   ```
   Insira um título: A Mensagem
   Insira o autor: Fernando Pessoa
   Insira um co-autor (0/5): Pedro
   Insira um co-autor (1/5): Pedro
   AVISO: co-autor "Pedro" já existe!
   Insira um co-autor (1/5): Tiago
   Insira um co-autor (2/5): Francisca
   Insira um co-autor (3/5): Carolina
   Insira um co-autor (4/5): Francisca
   AVISO: co-autor "Francisca" já existe!
   Insira um co-autor (4/5): Guilherme
   AVISO: Limite de co-autores atingido (5/5)
   Insira a data da publicação: 1934/12/01
   ```

4. Melhore a formatação do campo dos co-autores nos ficheiros gerados.
   No caso do ficheiro ser YAML, o resultado deverá ser o seguinte:

   ```yaml
   titulo: A Mensagem
   autor: Fernando Pessoa
   co-autores:
     - Pedro
     - Tiago
     - Francisca
     - Carolina
     - Guilherme
   data: 1934/12/01


   ```

   No caso de ser JSON:
   ```json
   {
      "titulo": "A Mensagem",
      "autor": "Fernando Pessoa",
      "co-autores": [
         "Pedro",
         "Tiago",
         "Francisca",
         "Carolina",
         "Guilherme" 
      ],
      "data": "1934/12/01"
   }
   ```

   No caso de ser XML:
   ```xml
   <obra data="1934/12/01">
      <titulo>A Mensagem</titulo>
      <autor>Fernando Pessoa</autor>
      <co-autores>
         <co-autor>Pedro</co-autor>
         <co-autor>Tiago</co-autor>
         <co-autor>Francisca</co-autor>
         <co-autor>Carolina</co-autor>
         <co-autor>Guilherme</co-autor>
      </co-autores>
   </obra>
   ```
