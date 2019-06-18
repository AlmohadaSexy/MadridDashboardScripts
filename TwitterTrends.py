# Script Scrapping Tendencias Twitter

# Librerias y Header
import requests, json
from bs4 import BeautifulSoup

def twitter():
	r = requests.get('https://trends24.in/spain/madrid/') # Recurso para obtener las ultimas tendencias de Madrid
	soup = BeautifulSoup(r.text, 'html.parser') # Recurso para convertir la informacion en un objeto manipulable
	results = soup.find('ol', attrs={'class':'trend-card__list'}) # Lista con las tendencias obtenidas

	datos = []

	for result in results:
		
		texto = result.find('a').text # Dentro de "result" buscamos la etiqueta html "a" y devolvemos su texto
		direccion = result.find('a')['href'] # Devolvemos el valor de la etiqueta "href"
		
		datos.append({'texto': texto ,'direccion': direccion}) # Guardamos en el conjunto de datos las variables obtenidas

	jsonData = json.dumps(datos) # Hacemos un volcado del conjunto de datos en un archivo con formato JSON
	file = open('twitter.txt','w')
	file.writelines(jsonData)
	file.close()