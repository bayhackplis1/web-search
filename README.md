Buscador Web con Múltiples Motores
Este script en Python permite realizar búsquedas web utilizando DuckDuckGo, Bing y Yahoo de manera simultánea, combinando los resultados obtenidos y presentándolos de forma organizada. Es una herramienta sencilla pero poderosa para obtener una mayor variedad de resultados en la web.

Funcionalidades
Búsqueda en tres motores: Realiza búsquedas en DuckDuckGo, Bing y Yahoo.
Combinación de resultados: Los resultados de cada motor se combinan en una sola lista, eliminando duplicados para que solo veas enlaces únicos.
Interactividad: Al finalizar cada búsqueda, el script pregunta si deseas realizar otra búsqueda, permitiendo un flujo continuo sin tener que reiniciar el programa.
Interfaz atractiva: El script incluye un diseño colorido para facilitar su uso en la terminal, con un banner de bienvenida y resultados destacados en colores.
Requisitos
Python 3.x
Librerías: requests, beautifulsoup4, termcolor.
Instala las dependencias con:




pip install requests beautifulsoup4 termcolor
Uso
Clona el repositorio en tu máquina local:

bash
Copiar
Editar
git clone https://github.com/bayhackplis1/web-search
Ejecuta el script:




python3 search.py
Ingresa el término de búsqueda y la cantidad de resultados que deseas obtener.

El script mostrará los resultados obtenidos de los tres motores de búsqueda.

Al finalizar, te preguntará si deseas realizar otra búsqueda. Si respondes "s", el proceso se repite; si respondes "n", el programa terminará.
