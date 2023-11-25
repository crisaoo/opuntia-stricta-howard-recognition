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


## Anotação das imagens e construção do dataset inicial

Para a anotação de imagens, usamos o software especializado LabelImg. Cada imagem foi anotada com sua classe correspondente, indicando se é "corte" ou "nao-corte". Esse processo é crucial para fornecer rótulos aos dados e treinar o  modelo.

Além da anotação, organizamos as imagens e seus arquivos de anotação de maneira estruturada. Criamos uma hierarquia de pastas bem organizada para armazenar as imagens e seus respectivos arquivos de anotação da seguinte forma:

- data

    -  label
        
        - marked_images
        
            - corte
            - nao-corte

Esse dataset com as anotações está localizado no seguinte drive: https://drive.google.com/drive/folders/1LP2fwRDOkpU33mrahcR7Tl33cSbVDlqk?usp=sharing 