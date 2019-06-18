import json, urllib, requests

with urllib.request.urlopen('https://gist.githubusercontent.com/tdreyno/4278655/raw/7b0762c09b519f40397e4c3e100b097d861f5588/airports.json') as url:
	data = json.loads(url.read().decode())
myDict = {}
for lin in data:
	myDict[lin['code']] = lin['name']

jsonDep = json.dumps(myDict)
file = open('AirportNames.txt','w') #creamos el archivo
file.writelines(jsonDep)#le metemos los datos
file.close() #cerramos el archivo