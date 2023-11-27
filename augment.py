import cv2 
import os

root_dir = './dataset'
resized_dir = os.path.join(root_dir, 'resized_data')    
augmented_dir = os.path.join(root_dir, 'augmented_data')

def change_brightness_contrast(image, alpha, beta):
    
    # Aplicar a transformação linear para alterar brilho e contraste
    result = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
    return result

for filename in os.listdir(resized_dir):

    imageSelected2 = cv2.imread(os.path.join(resized_dir, filename))

    # Definir os parâmetros de brilho e contraste desejados
    alpha = 1.15 # Fator de contraste (1.0 significa sem alteração)
    beta = 30    # Fator de brilho

    # Alterar brilho e contraste
    modifiedImage = change_brightness_contrast(imageSelected2, alpha, beta)

    # Exibir as imagens original e alterada
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite(os.path.join(augmented_dir, filename), modifiedImage)