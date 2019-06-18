import json, urllib, requests

def getToken():
	r = requests.get('https://openapi.emtmadrid.es/v1/mobilitylabs/user/login/', headers={"email":"almohadasexyfc@gmail.com", "password":"Sexy7890"})
	dataLogin = r.json()
	return dataLogin['data'][0]['accessToken']

def bici(accessToken):
	r = requests.get('https://openapi.emtmadrid.es/v1/transport/bicimad/stations/', headers={"accessToken":f"{accessToken}"})
	data = r.json()
	estaciones = []
	for st in data['data']: #empezamos un for para cada una de las estaciones en la API
		stat = {} #creamos una linea vacia y metemos en ella todos los datos que nos interesan
		stat['lat'] = st['geometry']['coordinates'][1]
		stat['lon'] = st['geometry']['coordinates'][0]
		stat['nombre'] = st['name']
		stat['direccion'] = st['address']
		stat['bases'] = st['total_bases']
		stat['ancladas'] = st['dock_bikes']
		stat['vacias'] = st['free_bases']
		stat['operativo'] = 'No' if st['no_available'] == 1 else 'Si'
		estaciones.append(stat) #introducimos la linea en la lista que hemos inicializado antes
	jsonData = json.dumps(estaciones) #formateamos la lista para que sea formato JSON
	file = open('bici.txt','w') #creamos nuestro txt para meter los datos
	file.writelines(jsonData) #metemos los datos
	file.close() #y cerramos el archivo
