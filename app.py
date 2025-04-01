from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Reemplaza con tu token OAuth válido para el entorno sandbox
EBAY_OAUTH_TOKEN = "v^1.1#i^1#r^0#f^0#I^3#p^3#t^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"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        instrumento = request.form.get('instrumento')
        resultados = buscar_instrumento(instrumento)
        return render_template('resultados.html', resultados=resultados, busqueda=instrumento)
    return render_template('index.html')

def buscar_instrumento(termino):
    url = "https://api.sandbox.ebay.com/buy/browse/v1/item_summary/search?"
    headers = {
        "Authorization": f"Bearer {EBAY_OAUTH_TOKEN}",
        "Content-Type": "application/json"
    }
    # Los parámetros se pueden enviar en la URL
    params = {
        "q": termino,
        "limit": "10"
    }
    response = requests.get(url, headers=headers, params=params)
    
    # Depuración: imprime la respuesta completa
    data = response.json()
    print(data)
    
    items = []
    # La estructura de la respuesta de la API de Browse es distinta. Por ejemplo:
    try:
        for item in data.get("itemSummaries", []):
            detalle = {
                "titulo": item.get("title", "Sin título"),
                "precio": item.get("price", {}).get("value", "0"),
                "moneda": item.get("price", {}).get("currency", ""),
                # En la API de Browse, la imagen principal puede venir en la propiedad "image" o similar.
                "imagen": item.get("image", {}).get("imageUrl", ""),
                "link": item.get("itemWebUrl", ""),
                "condicion": item.get("condition", "Desconocido")
            }
            items.append(detalle)
    except Exception as e:
        print("Error procesando la respuesta:", e)
    return items

if __name__ == '__main__':
    app.run(debug=True)
