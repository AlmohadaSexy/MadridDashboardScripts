import ftplib
#importamos las funciones de los archivos que tengo que ejecutar
from BiciMad import bici, getToken
from metro import metro
from TwitterTrends import twitter

def execAll(): # Funcion encargada de ejecutar las distintas scripts
	bici(getToken())
	metro()
	twitter()

def ftpME():
	ftp = ftplib.FTP() # Establecemos una conexion FTP para transferir los archivos al servidor web
	ftp.set_debuglevel(2)

	# Credenciales FTP para acceder al servidor web
	ftp.connect('', 21) #url ftp
	ftp.login("", "")#username and password
	ftp.cwd("")#directory

	ftp.storlines('STOR %s' % 'metro.txt', metro)	
	ftp.storlines('STOR %s' % 'twitter.txt', twitter)
	ftp.storbinary('STOR ' + 'bici.txt', bici)
	ftp.quit()

# Referencias a las scripts en el directorio relativo
execAll()
bici = open('bici.txt', 'rb')
twitter = open('twitter.txt', 'rb')
metro = open('metro.txt', 'rb')
ftpME()
