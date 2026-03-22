![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![PyQt6](https://img.shields.io/badge/PyQt6-41CD52?style=for-the-badge&logo=qt&logoColor=white)

# 🐦 Colibrí Browser

### 📝 Descripción
Un navegador web de código abierto, ligero y eficiente, desarrollado íntegramente en **Python**. Diseñado para ofrecer una experiencia de navegación fluida en equipos con recursos de hardware limitados, priorizando la velocidad y el bajo consumo de memoria.

### 🚀 Características
* **Motor WebEngine:** Renderizado moderno de páginas web.
* **Interfaz Minimalista:** Sin distracciones, enfocada en la velocidad.
* **Optimizado:** Ideal para procesadores de doble núcleo y sistemas con poca RAM.
* **Portable:** Fácil de ejecutar sin instalaciones complejas.

### 🛠️ Tecnologías utilizadas
* **Lenguaje:** Python
* **Interfaz Gráfica:** PyQt6
* **Motor de Navegación:** QtWebEngine

### ⚙️ Instalación y Uso
1. Descarga el repositorio o el archivo ejecutable.
2. Asegúrate de tener instaladas las dependencias (si corres el script `.py`).
3. Ejecuta `colibri.exe` (o `python main.py`) y comienza a navegar.

---
> **Nota del autor:** Este proyecto demuestra que con lógica clara y Python se pueden crear herramientas robustas para el día a día.
```bash
pip install PyQt6 PyQt6-WebEngine
```

---

## Modo de uso

1. Descarga `colibri_browser.py` y colócalo junto a `colibri.ico` si quieres que se muestre el icono.
2. Ejecuta el programa:
    ```bash
    python colibri_browser.py
    ```

---

## Empaquetar como ejecutable

Para compartir tu navegador con usuarios sin Python:

1. Instala PyInstaller:
    ```bash
    pip install pyinstaller
    ```
2. Empaqueta:
    ```bash
    pyinstaller --onefile --add-data "colibri.ico;." colibri_browser.py
    ```
3. El ejecutable estará en la carpeta `dist/`.

---

## Código principal

Mira el siguiente archivo para ver el código completo o para modificarlo según tus necesidades:

```python
# colibri_browser.py
import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit
# ... resto del código ...
```

---

## Preguntas frecuentes

- **¿No aparece el icono?**  
  El navegador funciona igual; sólo coloca `colibri.ico` junto al script para mostrar el icono.

- **¿Problemas con PyQt6-WebEngine?**  
  Instala la dependencia con `pip install PyQt6-WebEngine`.

- **¿Errores en Linux/Mac?**  
  Asegúrate de tener los paquetes de QtWebEngine según la distribución (puedes usar Homebrew en Mac).

---

## Créditos

Hecho por javier43000.  
Inspirado en la libertad de aprender y compartir software.

---

¿Tienes sugerencias, ideas o encontraste un bug?  

¡Abre un issue o comenta aquí!
