import requests, json, bs4

def metro():
	lineas = [f'linea-{x}' for x in range(1, 13)] + ['ramal'] + [f'ml{x}' for x in range(1,4)] #inicializamos todas las lineas para luego meterlas en la url

	data = [] #inicializamos una lista vacia
	for lin in lineas: #empezamos un for por cada linea de metro
		url = f'https://www.metromadrid.es/es/linea/{lin}' #formateamos el url de cada linea de metro
		r = requests.get(url) #hacemos request de la url
		soup = bs4.BeautifulSoup(r.text, 'html.parser') #parseamos el html para poder buscar cada etiqueta dentro
		eachLine = {} #creamos una linea vacia
		eachLine['linea'] = lin #asignamos lin a la linea
		listaBotones = soup.find_all('ul', attrs={'id': 'line-tabs', 'class':'vertical list__btnblue-lateral'}) #buscamos lo que queremos, en este caso cada ul con esos atributos
		botones = listaBotones[0].find_all('a') #dentro de eso buscamos todos los a
		circulacionHTML = soup.find_all('h3', attrs={'class':'tit__line-state'}) #buscamos la circulacion con los h3 y los atributos

		eachLine['circulacion'] = circulacionHTML[0].text.strip() #asignamos la primera de todos a ese atributo

		if len(botones) == 3: #si la longitud de los botones es 3 es que tiene incidencias
			descripcionHTML = soup.find_all('div', attrs={'class':'box__incidencias-incidencia'}) #buscamos la incidencia y se la asignamos con un color dependiendo de que tipo de circulacion tenga en esa linea
			eachLine['descripcion'] = descripcionHTML[-1].find('p').text.replace(".", ". ")
			eachLine['color'] = 'yellow' if eachLine['circulacion'] == 'Circulación Normal' else 'red'
			
		else:#si la longitud de botones no es 3 es que la linea no tiene ninguna incidencia
			eachLine['descripcion'] = 'No hay ninguna incidencia.'
			eachLine['color'] = 'green'

		data.append(eachLine) #añadimos la linea a la lista 
	jsonData = json.dumps(data)#creamos el json con los datos
	file = open('metro.txt','w') #creamos el archivo
	file.writelines(jsonData)#le metemos los datos
	file.close() #cerramos el archivo