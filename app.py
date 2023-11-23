from flask import Flask, render_template, request
import requests
import folium
from folium import plugins
import webbrowser

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mostrar_mapa', methods=['POST'])
def mostrar_mapa():
    ip = request.form['ip']
    dados = obter_localizacao(ip)

    try:
        lat, lon = map(float, dados['loc'].split(','))
    except KeyError:
        return "Não foi possível obter a localização."

    mapa = folium.Map(location=[lat, lon], zoom_start=12)
    folium.Marker([lat, lon], popup=f"Localização do IP: {ip}").add_to(mapa)

    fullscreen = plugins.Fullscreen()
    mapa.add_child(fullscreen)

    mapa.save('static/mapa_interativo.html')

    return render_template('mostrar_mapa.html', lat=lat, lon=lon, ip=ip)

def obter_localizacao(ip):
    url = f"https://ipinfo.io/{ip}/json"
    resposta = requests.get(url)
    dados = resposta.json()
    return dados

if __name__ == '__main__':
    webbrowser.open_new('http://127.0.0.1:5000/')
    app.run(debug=True)
