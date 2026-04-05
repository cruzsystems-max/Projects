# 📸 Foto Quiosco con Detección de Guiño

Aplicación de escritorio desarrollada en Python que permite capturar fotografías automáticamente mediante la detección de rostros y el guiño de un ojo utilizando visión por computadora.

## 👨‍💻 Autor
- **Cristian Cruz**  
- 🎥 Demo: [https://youtu.be/MKwdiutVYjU](https://youtu.be/MKwdiutVYjU)

  <img width="1563" height="774" alt="image" src="https://github.com/user-attachments/assets/4f9c1120-bb6d-4089-9db8-3cab781414f4" />


---

## 🧠 Descripción

Este proyecto implementa un sistema de captura de imágenes tipo “quiosco”, que:

- Detecta rostros en tiempo real usando **Haar Cascades**.
- Detecta ojos dentro del rostro.
- Captura una foto automáticamente cuando el usuario guiña un ojo.
- Permite guardar o descartar la imagen capturada.

Todo esto se muestra en una interfaz gráfica construida con **Tkinter**.


## 🚀 Instalación

1. Clona este repositorio o descarga el código.
2. Instala las dependencias necesarias:

```bash
pip install opencv-python pillow
