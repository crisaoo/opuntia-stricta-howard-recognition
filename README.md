# Opuntia Stricta Howard Recognition

Esse projeto tem como objetivo principal desenvolver um dataset de imagens de palmas do tipo orelha de elefante, uma planta amplamente cultivada na região Nordeste do Brasil. 

O objetivo do dataset é saber quando uma folha de palma deve ser cortada ou não. 

O dataset será usado para treinar e avaliar um algoritmo de aprendizado de máquina no reconhecimento de quando uma folha de palma deve ser cortada com base em imagens.

&nbsp;

## Pré-Processamento

O pré-processamento de imagens busca criar um conjunto de dados consistente e enriquecido para treinar e testar algoritmos de aprendizado de máquina, especificamente para a classificação das palmas. 

Esse processo inclui a padronização do tamanho das imagens, normalização das cores para eliminar variações indesejadas, augmentação de dados para diversificar o conjunto, e segmentação para isolar áreas de interesse, como as palmas. 

O objetivo é garantir que o modelo seja treinado com dados limpos e representativos, promovendo sua eficácia na tarefa desejada.

O dataset inicial utilizado para esse pré-processamento está localizado no seguinte endereço: https://drive.google.com/drive/folders/1kQzHtsae0YAnpXPsKB_rKxU-cLprAdic?usp=sharing. 

Para fazer isso, basta executar o código abaixo no terminal:

``` 
python image_preprocessing.py
```


Como resultado, teremos duas pastas localizada no diretório **/data/no_label: resized_data e segmented_dir.**

- resized_data: contém as imagens redimensionadas
- segmented_dir: contém as imagens segmentadas.

Os seguintes datasets resultantes podem ser encontradas nos seguintes links respectivamentes:

- https://drive.google.com/drive/folders/1HutWMJoTdyaSudXX48aJrUQCahMh9jDC?usp=sharing
- https://drive.google.com/drive/folders/1qF-X2w2N-W8e91k52-LCiSSbReS-TN24?usp=sharing 



&nbsp;


## Augmentação de dados

A fim de diversificar o dataset devido as condições não ideais para a coleta de dados, fez-se necessário a utilização de algum método para augmentar o dataset.

Para isso, foi utilizado o script `augment.py`. O objetivo principal desse algoritmo é alterar o contraste e brilho das imagens coletadas para simular um dia mais ensolarado. 

Para executar o código, basta executar o código abaixo no terminal:

```
python augment.py
```

Como resultado, o dataset foi populado com algumas imagens, o que resultou em um conjunto de dados composto por 200 imagens.


&nbsp;


## Anotação das imagens e construção do dataset inicial

Para a anotação de imagens, usamos o software especializado LabelImg. Cada imagem foi anotada com sua classe correspondente, indicando se é "corte" ou "nao-corte". Esse processo é crucial para fornecer rótulos aos dados e treinar o  modelo.

Além da anotação, organizamos as imagens e seus arquivos de anotação de maneira estruturada. Criamos uma hierarquia de pastas bem organizada para armazenar as imagens e seus respectivos arquivos de anotação da seguinte forma:

- data

    -  label
        
        
        - corte
        - nao-corte

Esse dataset com as anotações está localizado no seguinte drive: https://drive.google.com/drive/folders/1LP2fwRDOkpU33mrahcR7Tl33cSbVDlqk?usp=sharing 


&nbsp;


## Treinamento e Avaliação do Modelo
Este tópico aborda o código responsável pelo treinamento e avaliação de um modelo de aprendizado de máquina, usando um conjunto de dados anotado e pré-processado. 

O modelo em questão é um classificador Random Forest, e o conjunto de dados é composto por imagens de palmas anotadas com as classes "corte" ou "nao-corte".

### Carregamento e Pré-processamento dos Dados

O código começa carregando as anotações do conjunto de dados YOLO a partir de arquivos de texto. As anotações incluem informações sobre a classe (corte ou nao-corte) e as coordenadas associadas à localização da palma na imagem. As classes e coordenadas são armazenadas nos arrays labels e features, respectivamente.

### Divisão dos Dados e Treinamento do Modelo
Em seguida, os dados são divididos em conjuntos de treinamento e teste, utilizando 70% dos dados para treinamento e 30% para teste. Isso é feito usando a função train_test_split do scikit-learn. Um classificador Random Forest é criado e treinado usando o conjunto de treinamento.

### Avaliação do Modelo
Após o treinamento, o modelo é testado no conjunto de teste, e métricas de avaliação são calculadas. As métricas incluem:

- Acurácia: A porcentagem de previsões corretas em relação ao total de previsões.
- F1 Score: Uma média ponderada da precisão e da revocação, fornecendo um equilíbrio entre ambas.
- Precisão: A porcentagem de verdadeiros positivos em relação ao total de previsões positivas.
- Revocação: A porcentagem de verdadeiros positivos em relação ao total de casos positivos.

A matriz de confusão é calculada para avaliar o desempenho do modelo em diferentes classes.

### Visualização dos Resultados


Por fim, são exibidos os resultados em termos de métricas de avaliação e uma matriz de confusão. Além disso, são apresentados gráficos para visualizar as métricas de avaliação, incluindo um gráfico de barras e um gráfico de matriz de confusão.

Para isso, execute o seguinte código no terminal:

```
python random_forest.py
```