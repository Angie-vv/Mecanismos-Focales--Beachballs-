# Mecanismos Focales - Región de Valparaíso, Chile

## Descripción

Este proyecto descarga, procesa y visualiza mecanismos focales sísmicos de la región de Valparaíso utilizando datos del catálogo GCMT. Se filtran eventos según su ubicación, se clasifican según régimen tectónico, y se grafican en un mapa usando diagramas tipo *beachball*.

---

## Contenido del Proyecto

- `1_Filter.py`: Descarga y filtra eventos sísmicos por ubicación.
- `2_Creacion de Mapa.py`: Clasifica mecanismos focales según tensor de momento y Genera el mapa con diagramas *beachball* coloreados.
- `valparaiso_focal_mechanisms (1).csv`: Datos procesados y clasificados.


---

## Requisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

---

## Instalación de Dependencias

Para instalar todas las librerías necesarias, primero asegúrate de tener Python y pip instalados. Luego, desde la terminal o consola, ejecuta:


```bash
pip install obspy pandas numpy matplotlib cartopy
Nota: En sistemas Windows, la instalación de cartopy puede requerir algunos paquetes adicionales o usar un entorno como Anaconda para evitar problemas.


##Uso
Ejecuta los scripts en orden para obtener el resultado final:

python 1_download_and_filter.py
python 2_classify_regime.py
python 3_plot_beachballs.py

##Resultados
Archivo CSV con mecanismos focales clasificados: beachballs_classified_Tarapaca.csv.

Mapa que muestra los mecanismos focales con colores según el régimen tectónico:

Azul: Extensión

Rojo: Compresión

Naranja: Oblicuo

##Licencia
Este proyecto utiliza la licencia Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0).
Consulta aquí para más detalles.

##Contacto
Para dudas o sugerencias, contáctame en:

Email: a.varas28@gmail.com

GitHub: Angie-vv

¡Gracias por tu interés en el proyecto!