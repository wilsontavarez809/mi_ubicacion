import webbrowser
import os

# Ruta al archivo HTML
ruta_html = os.path.abspath("index.html")

# Abre el archivo HTML en el navegador
webbrowser.open(f"file://{ruta_html}")
