import cv2 
import os
from PIL import Image
import numpy as np

# Indicar o caminho do dataset com as imagens originais e onde ficarão armazenadas as imagens modificadas
root_dir = './data/no_label'
source_dir = os.path.join(root_dir, 'collected_images')
resized_dir = os.path.join(root_dir, 'resized_data')    
segmented_dir = os.path.join(root_dir, 'segmented_dir')    


# Realizar o calculo da media dos valores da altura e largura das imagens
# para redimensionar todas imagens para um mesmo tamanho
width = []
height = []

for file in os.listdir(source_dir):
    img_path = os.path.join(source_dir, file)

    image = Image.open(img_path)
    w, h = image.size

    width.append(w)
    height.append(h)

width_mean = sum(width) / len(width)
height_mean = sum(height) / len(height)

print(f"Média de largura: {int(width_mean)}")
print(f"Média de altura: {int(height_mean)}")

# Definir a largura e a altura para qual as imagens serão redimensionadas
dim = (width_mean, height_mean)


# Criar a pasta para armazenar as imagens redimensionadas (caso nao exista)
if not os.path.exists(resized_dir):
    os.makedirs(resized_dir)

# Identificar e redimensionar as imagens seguindo o padrao definido anteriormente
for filename in os.listdir(source_dir):
    if filename.endswith('.jpg'):
        img = cv2.imread(os.path.join(source_dir, filename))
        img_resized = cv2.resize(img, dim, cv2.INTER_AREA)
        cv2.imwrite(os.path.join(resized_dir, filename), img_resized)
    else:
        ...
        
# Criar a pasta para armazenar as imagens segmentadas caso nao exista)
if not os.path.exists(segmented_dir):
    os.makedirs(segmented_dir)
        
for filename in os.listdir(resized_dir):

    img = cv2.imread(os.path.join(resized_dir, filename))

    # Converter a imagem de RGB para HSV
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Definir intervalo de verde para criar a máscara
    lower = np.array([35, 10, 10])  # Verde mais escuro
    upper = np.array([80, 200, 200])# Verde mais claro

    # Criar uma máscara usando o intervalo de cor
    mask = cv2.inRange(img_hsv, lower, upper)

    # Aplicar a máscara à imagem original
    imageSegmented = cv2.bitwise_and(img, img, mask=mask)

    # Salvar na pasta criada anteriormente as novas imagens segmentadas
    cv2.imwrite(os.path.join(segmented_dir, filename), imageSegmented)   