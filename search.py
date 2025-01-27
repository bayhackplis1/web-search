import requests
from bs4 import BeautifulSoup
from termcolor import colored

def buscar_en_duckduckgo(query, num_resultados):
    """
    Realiza una búsqueda en DuckDuckGo y devuelve una lista de URLs.
    """
    resultados = []
    url = "https://html.duckduckgo.com/html/"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        data = {"q": query}
        response = requests.post(url, headers=headers, data=data, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        for link in soup.find_all("a", {"class": "result__a"}):
            href = link.get("href")
            if href.startswith("http"):
                resultados.append(href)
                if len(resultados) >= num_resultados:
                    break
        return resultados
    except Exception as e:
        print(colored(f"[X] Error en DuckDuckGo: {e}", "red"))
        return []

def buscar_en_bing(query, num_resultados):
    """
    Realiza una búsqueda en Bing y devuelve una lista de URLs.
    """
    resultados = []
    url = "https://www.bing.com/search"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        params = {"q": query, "count": num_resultados}
        response = requests.get(url, headers=headers, params=params, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        for link in soup.find_all("a"):
            href = link.get("href")
            if href and href.startswith("http") and "bing.com" not in href:
                resultados.append(href)
                if len(resultados) >= num_resultados:
                    break
        return resultados
    except Exception as e:
        print(colored(f"[X] Error en Bing: {e}", "red"))
        return []

def buscar_en_yahoo(query, num_resultados):
    """
    Realiza una búsqueda en Yahoo y devuelve una lista de URLs.
    """
    resultados = []
    url = "https://search.yahoo.com/search"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        params = {"p": query}
        response = requests.get(url, headers=headers, params=params, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        for link in soup.find_all("a"):
            href = link.get("href")
            if href and href.startswith("http") and "yahoo.com" not in href:
                resultados.append(href)
                if len(resultados) >= num_resultados:
                    break
        return resultados
    except Exception as e:
        print(colored(f"[X] Error en Yahoo: {e}", "red"))
        return []

def combinar_resultados(resultados_totales, num_resultados):
    """
    Combina resultados de múltiples motores de búsqueda y elimina duplicados.
    """
    resultados_unicos = list(dict.fromkeys(resultados_totales))
    return resultados_unicos[:num_resultados]

def mostrar_banner():
    banner = """
    ██████╗ ███████╗████████╗███████╗██╗     █████╗ ██████╗ ███████╗
    ██╔══██╗██╔════╝╚══██╔══╝██╔════╝██║    ██╔══██╗██╔══██╗██╔════╝
    ██████╔╝█████╗     ██║   █████╗  ██║    ███████║██████╔╝███████╗
    ██╔══██╗██╔════╝     ██║   ██╔══╝  ██║    ██╔══██║██╔══██╗╚════██╗
    ██████╔╝███████╗    ██║   ███████╗███████╗██║  ██║██║  ██║██████╔╝
    ╚═════╝ ╚══════╝    ╚═╝   ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ 
    """
    print(colored(banner, "cyan"))

def realizar_busqueda():
    """
    Función que maneja la búsqueda y muestra los resultados.
    """
    print(colored("Bienvenido al Buscador Mejorado con Múltiples Motores", "green"))
    print(colored("Este programa realiza búsquedas en DuckDuckGo, Bing y Yahoo para ampliar los resultados.\n", "yellow"))

    try:
        # Pedir al usuario el término de búsqueda y la cantidad de resultados
        query = input(colored("¿Qué tipo de páginas deseas buscar? (Ejemplo: páginas con Pterodactyl instalado): ", "magenta")).strip()
        num_resultados = int(input(colored("¿Cuántos resultados deseas obtener? (Ejemplo: 10): ", "magenta")))

        if num_resultados <= 0:
            print(colored("[!] La cantidad de resultados debe ser mayor a 0.", "red"))
            return

        # Realizar búsquedas en los diferentes motores
        print(colored("\n[*] Iniciando búsquedas...", "yellow"))
        resultados_totales = []
        motores = {
            "DuckDuckGo": buscar_en_duckduckgo,
            "Bing": buscar_en_bing,
            "Yahoo": buscar_en_yahoo
        }

        for nombre, funcion in motores.items():
            print(colored(f"[*] Buscando en {nombre}...", "blue"))
            resultados = funcion(query, num_resultados)
            resultados_totales.extend(resultados)
            print(colored(f"    [+] {len(resultados)} resultados obtenidos de {nombre}", "green"))

        # Combinar y filtrar resultados
        resultados_finales = combinar_resultados(resultados_totales, num_resultados)

        # Mostrar los resultados
        if resultados_finales:
            print(colored("\n=== Resultados Combinados ===", "cyan"))
            for i, url in enumerate(resultados_finales, 1):
                print(f"{i}. {url}")
            print(colored("==============================", "cyan"))
        else:
            print(colored("[!] No se encontraron resultados en los motores de búsqueda.", "red"))
    except ValueError:
        print(colored("[!] Por favor, introduce un número válido para la cantidad de resultados.", "red"))
    except KeyboardInterrupt:
        print(colored("\n[X] Búsqueda cancelada por el usuario.", "red"))
    except Exception as e:
        print(colored(f"[X] Error inesperado: {e}", "red"))

def main():
    """
    Función principal que interactúa con el usuario y gestiona la ejecución del script.
    """
    mostrar_banner()

    while True:
        realizar_busqueda()
        
        # Preguntar si el usuario quiere realizar otra búsqueda
        respuesta = input(colored("\n¿Deseas realizar otra búsqueda? (s/n): ", "cyan")).strip().lower()
        if respuesta != "s":
            print(colored("\nGracias por usar el buscador. ¡Hasta luego!", "green"))
            break

if __name__ == "__main__":
    main()
