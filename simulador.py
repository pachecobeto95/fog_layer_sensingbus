import requests
import client3
import fog_agent_new_tests
import time
class Bus(object):

	def __init__(self):
		#self.bus_line = bus_line
		self.URL = 'http://dadosabertos.rio.rj.gov.br/apiTransporte/apresentacao/rest/index.cfm/obterTodasPosicoes'
		self.URL2 = 'https://www.google.com.br/'
		self.IP = '127.0.0.1'
		self.PORT = 50000
		

	def bus_request(self, cont):
		try:
			str_bus = requests.get(self.URL)
			json_bus = str_bus.json()
			bus_datahora = json_bus['DATA'][cont][0]
			bus_ordem = json_bus['DATA'][cont][1]
			bus_line = json_bus['DATA'][cont][2]
			bus_latitude = json_bus['DATA'][cont][3]
			bus_longitude = json_bus['DATA'][cont][4]
		except (requests.exceptions.ChunkedEncodingError) as e:
			time.sleep(1)
			r = requests.get(self.URL2)
			bus_latitude = 0
			bus_longitude = 0
			time.sleep(30)
		return bus_latitude, bus_longitude

		
		
	def send_data(self):
		
		client3.cloud_client(self.IP, self.PORT)	
		
		




class Fog(object):		
	def __init__(self):
		self.URL = 'http://dadosabertos.rio.rj.gov.br/apiTransporte/apresentacao/rest/index.cfm/obterTodasPosicoes'
		self.IP = '127.0.0.1'
		self.PORT = 50000
		#self.list_coord= []
		

	def receiving_data(self):
		
		fog_agent_new_tests.run(server_class=HTTPServer, handler_class=fog_agent_new_tests.S, port=50000)

	def fog_localization(self, cont):

		str_fog = requests.get(self.URL)
		json_fog = str_fog.json()
		fog_latitude = json_fog['DATA'][cont][3]
		fog_longitude = json_fog['DATA'][cont][4]
		#self.list_coord.append(str(fog_latitude) + "," + str(fog_longitude)) 
		#cont = cont + 1

		return fog_latitude, fog_longitude
		
		 





