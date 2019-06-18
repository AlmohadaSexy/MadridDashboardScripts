import json, requests
lineas = [f'{x}' for x in range(1,13)] + [f'{x}' for x in range(14,80)] + [81, 82, 83, 85, 86, 87, 90, 93, 94, 96, 97, 98] + [f'{x}' for x in range(100,154)] + [155, 156, 160, 161, 162, 165, 171, 172, 173, 174, 175, 176, 177, 178, 180, 200, 210, 215, 247, 310] + [f'N{x}' for x in range(1, 27)] + ['N28']

def getToken():
	r = requests.get('https://openapi.emtmadrid.es/v1/mobilitylabs/user/login/', headers={"email":"almohadasexyfc@gmail.com", "password":"Sexy7890"})
	dataLogin = r.json()
	return dataLogin['data'][0]['accessToken']

def getEstaciones(accessToken):
	lineasDicc = {}
	for lin in lineas:
		rIda = requests.get(f'https://openapi.emtmadrid.es/v1/transport/busemtmad/lines/{lin}/stops/1/', headers={"accessToken":f"{accessToken}"})
		data1 = rIda.json()
		rVue = requests.get(f'https://openapi.emtmadrid.es/v1/transport/busemtmad/lines/{lin}/stops/2/', headers={"accessToken":f"{accessToken}"})
		data2 = rVue.json()
		if data1['code'] == '00' and data2['code'] == '00':
			dataIda = data1['data'][0]
			dataVue = data2['data'][0]
			linea = {}
			linea['lineaId'] = lin
			print(lin)
			try:
				linea['nombre'] = dataIda['timeTable'][0]['nameA'] + ' - ' + dataIda['timeTable'][0]['nameB']
			except Exception as e:
				linea['nombre'] = dataIda['timeTable'][0]['nameA']
			paradasIda = []
			for st in dataIda['stops']:
				sto = {}
				sto['nombre'] = st['name']
				sto['lat'] = st['geometry']['coordinates'][1]
				sto['lon'] = st['geometry']['coordinates'][0]
				sto['otrasLineas'] = st['dataLine']
				paradasIda.append(sto)
			linea['paradasIda'] = paradasIda
			paradasVue = []
			for st in dataVue['stops']:
				sto = {}
				sto['nombre'] = st['name']
				sto['lat'] = st['geometry']['coordinates'][1]
				sto['lon'] = st['geometry']['coordinates'][0]
				sto['otrasLineas'] = st['dataLine']
				paradasVue.append(sto)
			linea['paradasVue'] = paradasVue
			#lineasDicc.append(linea)
			lineasDicc[f'Linea_{lin}'] = linea
			
	jsonData = json.dumps(lineasDicc)
	file = open('lineasEMTPrueba.txt','w') #creamos el archivo
	file.writelines(jsonData)#le metemos los datos
	file.close() #cerramos el archivo

def LineasEMT(accessToken):
	lineasDicc = []
	for lin in lineas:
		r = requests.get(f'https://openapi.emtmadrid.es/v1/transport/busemtmad/lines/{lin}/stops/1/', headers={"accessToken":f"{accessToken}"})
		d = r.json()
		if d['code'] == '00': #and data2['code'] == '00':
			data = d['data'][0]
			linea = {}
			linea['lineaId'] = lin
			print(lin)
			try:
				linea['nombre'] = data['timeTable'][0]['nameA'] + ' - ' + data['timeTable'][0]['nameB']
			except Exception as e:
				linea['nombre'] = data['timeTable'][0]['nameA']
			lineasDicc.append(linea)
	jsonData = json.dumps(lineasDicc)
	file = open('lineasEMTLista.txt','w') #creamos el archivo
	file.writelines(jsonData)#le metemos los datos
	file.close() #cerramos el archivo