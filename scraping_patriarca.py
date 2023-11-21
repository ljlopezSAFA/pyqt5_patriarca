#requests
import requests
#bs4
import bs4


def obtener_contenido_web():

    pagina_web = requests.get("https://www.elpatriarca.com/comprar-dulces/polvorones/").content

    soup = bs4.BeautifulSoup(pagina_web, "html.parser")

    return soup


def extraer_informacion():


    producto_plantilla = {
        "url" : "",
        "nombre": "",
        "precio" : 0.0,
        "descripcion" : ""
    }

    lista_productos = []


    soup = obtener_contenido_web()

    elemento_principal = soup.find("ul", {"class": "products columns-4"})

    elementos = elemento_principal.find_all("li")

    for elemento in elementos:

        #url_imagen
        url = elemento.find("img")["src"]
        #nombre del producto
        producto = elemento.find("h2").text
        #precio
        precio = float(elemento.find("bdi").text[:-1].replace(",", "."))

        #enlace pagina de detalles
        enlace_detalles = elemento.find("a")["href"]
        pagina_detalles = requests.get(enlace_detalles).content
        soup_detalles = bs4.BeautifulSoup(pagina_detalles,"html.parser")


        #descripcion producto
        descripcion = soup_detalles.find("div", {"class","et_pb_row et_pb_row_1_tb_body"}).find_all("p")[1].text


        #Construir el diccionario de producto
        nuevo_producto = producto_plantilla.copy()
        nuevo_producto["url"] = url
        nuevo_producto["nombre"] = producto
        nuevo_producto["precio"] = precio
        nuevo_producto["descripcion"] = descripcion

        lista_productos.append(nuevo_producto)





    return lista_productos



