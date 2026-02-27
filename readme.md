# Colibrí Browser

**Colibrí Browser** es un navegador web ligero y universal creado con PyQt6 y QtWebEngine. Hecho para aprender, experimentar y navegar sin complicaciones. ¡Listo para Windows, Linux y Mac!

---

## Características

- Navegación fácil: atrás, adelante, recargar, ir a inicio (Google).
- Barra de direcciones intuitiva.
- Código universal, sin dependencias de sistema adicionales salvo PyQt6/PyQt6-WebEngine.
- Icono opcional (`colibri.ico`). Si no está, el navegador funciona igual.

---

## Requisitos

- **Python 3.8+**
- **PyQt6**
- **PyQt6-WebEngine**

Instala dependencias:
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
