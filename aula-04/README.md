# Aula 4 - Gerador de Ficheiros (continuação)

## Exercício

1. Melhore o `gerador.py` de forma a eliminar entradas repetidas de co-autores.
   
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

2. Melhore a formatação do campo dos co-autores nos ficheiros gerados.
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

3. Melhore o `gerador.py` de forma a imprimir os nomes dos co-autores por ordem alfabética.



