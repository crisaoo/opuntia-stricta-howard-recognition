# Opuntia Stricta Howard Recognition

Esse projeto tem como objetivo principal desenvolver um dataset de imagens de palmas do tipo orelha de elefante, uma planta amplamente cultivada na região Nordeste do Brasil. 

O objetivo do dataset é saber quando uma folha de palma deve ser cortada ou não. 

O dataset será usado para treinar e avaliar um algoritmo de aprendizado de máquina no reconhecimento de quando uma folha de palma deve ser cortada com base em imagens.


## Pré-Processamento

O pré-processamento de imagens busca criar um conjunto de dados consistente e enriquecido para treinar e testar algoritmos de aprendizado de máquina, especificamente para a classificação das palmas. 

Esse processo inclui a padronização do tamanho das imagens, normalização das cores para eliminar variações indesejadas, augmentação de dados para diversificar o conjunto, e segmentação para isolar áreas de interesse, como as palmas. 

O objetivo é garantir que o modelo seja treinado com dados limpos e representativos, promovendo sua eficácia na tarefa desejada.

Para fazer isso, basta executar o código abaixo no terminal:

``` 
python image_preprocessing.py
```


Como resultado, teremos duas pastas localizada no diretório **/data/no_label: resized_data e segmented_dir.**

- resized_data: contém as imagens redimensionadas;
- segmented_dir: contém as imagens segmentadas.