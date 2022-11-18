# Aula 8 - Meteorologista

1. Criar um programa que recebe como argumento um local e diz as previsões meteorológicas desse local para os 5 dias seguintes.



## Funcionalidades

### Previsões para um determinado local
```bash
python3 meteo.py [local] [data]
```

Se a `data` não for passada, então imprime a previsão para os 5 dias.


#### Exemplo
```bash
python3 meteo.py Braga 1
````
Isto deve imprimir a previsão do primeiro dia dos 5 que existem.


### Imprimir um texto de ajuda
```bash
python3 meteo.py ajuda
```
Isto deve imprimir
```
Utilização:
  python3 meteo.py [local] [dia]
  
  Argumentos:
    [local] - Local do qual queremos ir buscar as previsões (obrigatório)
    [dia] - Dia específico de uma previsão (opcional)
```

### Imprimir as localidades com a temperatura máxima mais alta e mais baixa
```
python3 meteo.py max
```

### Imprimir as localidades com a temperatura mínima mais alta e mais baixa
```
python3 meteo.py min
```
