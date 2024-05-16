#Esta version genera un gif
import os
import pydicom
import matplotlib.pyplot as plt
from PIL import Image

def load_dicom_images(folder_path):
    dicom_files = [file for file in os.listdir(folder_path) if file.endswith('.dcm')]
    dicom_files.sort()
    dicom_images = [pydicom.dcmread(os.path.join(folder_path, file)) for file in dicom_files]
    return dicom_images

def create_gif_from_dicom_images(dicom_images, output_gif_path):
    images = []
    temp_file_paths = []  # Lista para almacenar los nombres de archivo temporales
    for idx, image in enumerate(dicom_images):
        plt.imshow(image.pixel_array, cmap=plt.cm.gray)
        plt.axis('off')
        plt.title('DICOM image')
        temp_file_path = f'temp_{idx}.png'
        plt.savefig(temp_file_path)  # Guardar imagen temporalmente como PNG
        temp_file_paths.append(temp_file_path)  # Agregar nombre de archivo temporal a la lista
        images.append(Image.open(temp_file_path))
        plt.clf()

    # Guardar todas las imágenes como un GIF animado
    images[0].save(output_gif_path, save_all=True, append_images=images[1:], optimize=False, duration=500, loop=0)

    # Eliminar todos los archivos temporales al final del proceso
    for temp_file_path in temp_file_paths:
        os.remove(temp_file_path)

folder_path = 'Informatica-2/Taller-3/archivosDCM'  # Ruta de la carpeta que contiene las imágenes DICOM
output_gif_path = 'Informatica-2/Taller-3/rodilla.gif'  # Ruta del archivo GIF de salida
dicom_images = load_dicom_images(folder_path)
create_gif_from_dicom_images(dicom_images, output_gif_path)
