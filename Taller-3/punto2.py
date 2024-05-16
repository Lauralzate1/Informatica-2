#Esta version muestra una ventana emergente con las imagenes de la rodilla en estilo (gif)
import os
import pydicom
import matplotlib.pyplot as plt

def load_dicom_images(folder_path):
    dicom_files = [file for file in os.listdir(folder_path) if file.endswith('.dcm')]
    dicom_files.sort()
    dicom_images = [pydicom.dcmread(os.path.join(folder_path, file)) for file in dicom_files]
    return dicom_images

def display_dicom_images(dicom_images):
    fig, ax = plt.subplots()
    index = 0

    def on_close(event):
        plt.close()
        display_dicom_images.running = False

    fig.canvas.mpl_connect('close_event', on_close)

    while index < len(dicom_images) and display_dicom_images.running:
        ax.imshow(dicom_images[index].pixel_array, cmap=plt.cm.gray)
        ax.set_title('Dicom image')
        ax.axis('off')
        plt.pause(0.5) 
        plt.draw()
        index += 1

    plt.close()

#Ejemplo de uso
folder_path = 'Informatica-2/Taller-3/archivosDCM'
dicom_images = load_dicom_images(folder_path)
display_dicom_images.running = True  # Variable para controlar la ejecución
display_dicom_images(dicom_images)