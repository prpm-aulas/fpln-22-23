import re

text = """
Todas as cartas de amor são
Ridículas.
Não seriam cartas de amor se não fossem
Ridículas.Também escrevi em meu tempo cartas de amor,
Como as outras,
Ridículas.As cartas de amor, se há amor,
Têm de ser
Ridículas.Mas, afinal,
Só as criaturas que nunca escreveram
Cartas de amor
É que são
Ridículas.Quem me dera no tempo em que escrevia
Sem dar por isso
Cartas de amor
Ridículas.A verdade é que hoje
As minhas memórias
Dessas cartas de amor
É que são
Ridículas.(Todas as palavras esdrúxulas,
Como os sentimentos esdrúxulos,
São naturalmente
Ridículas).
"""


words_list = re.findall(r'\w+', text)

words_counter = {}
for word in words_list:
    if word not in words_counter:
        words_counter[word] = 1
        continue
    
    words_counter[word] += 1

words_counter = dict(sorted(words_counter.items(), key=lambda item: item[1], reverse=True))
print(words_counter)

