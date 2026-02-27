import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit
from PyQt6.QtCore import QUrl
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtGui import QFont, QIcon

def resource_path(relative_path):
    """Obtiene la ruta absoluta para recursos, funciona en desarrollo y en .exe"""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# CONFIGURACIÓN DEL ICONO EN WINDOWS (opcional)
try:
    from ctypes import windll
    myappid = 'vzla.colibri.browser.v1'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except Exception:
    pass

class ColibriBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        # Comprobación de existencia de icono; no da error si falta
        icon_path = resource_path("colibri.ico")
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))

        self.setWindowTitle("Colibrí Browser")
        self.setGeometry(200, 200, 1200, 800)

        fuente_grande = QFont("Arial", 14)
        self.setFont(fuente_grande)

        self.browser = QWebEngineView()

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        navbar = QWidget()
        navbar.setFixedHeight(50)
        nav_layout = QHBoxLayout()
        navbar.setLayout(nav_layout)

        # Botones de navegación
        back_btn = QPushButton("←")
        back_btn.clicked.connect(self.browser.back)
        nav_layout.addWidget(back_btn)

        forward_btn = QPushButton("→")
        forward_btn.clicked.connect(self.browser.forward)
        nav_layout.addWidget(forward_btn)

        reload_btn = QPushButton("⟳")
        reload_btn.clicked.connect(self.browser.reload)
        nav_layout.addWidget(reload_btn)

        home_btn = QPushButton("Inicio")
        home_btn.clicked.connect(lambda: self.browser.setUrl(QUrl("https://www.google.com")))
        nav_layout.addWidget(home_btn)

        self.url_bar = QLineEdit()
        self.url_bar.setFont(fuente_grande)
        self.url_bar.returnPressed.connect(self.load_url)
        nav_layout.addWidget(self.url_bar)

        main_layout.addWidget(navbar)
        main_layout.addWidget(self.browser)

        self.browser.urlChanged.connect(self.update_url)
        self.browser.setUrl(QUrl("https://www.google.com"))

    def load_url(self):
        url = self.url_bar.text()
        if not (url.startswith("http://") or url.startswith("https://")):
            url = "https://" + url
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setOrganizationName("ColibriProject")
    window = ColibriBrowser()
    window.show()
    sys.exit(app.exec())