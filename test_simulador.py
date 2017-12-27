import simulador
from geopy.distance import vincenty
import threading, Queue
import time


contfog=0
FileName = 'qntd_enviado2'
RANGE_FOG = 300
list_qntd_enviados = []
list_fog_localization = []
fog_coord = [(-22.815538, -43.186481), (-22.883909, -43.494678), (-22.883881, -43.49474), (-22.884331, -43.496132), (-22.88393, -43.49472), (-22.883989, -43.494518), (-22.88402, -43.495708), (-22.884121, -43.495258), (-22.910837, -43.270172), (-22.91065, -43.269615), (-22.91065, -43.269615), (-22.910721, -43.27058), (-22.910875, -43.27058), (-22.910721, -43.270683), (-22.910738, -43.270668), (-22.910721, -43.270664), (-22.8144, -43.187374), (-22.910677, -43.270573), (-22.910633, -43.269493), (-22.814739, -43.188255)]

while contfog <= len(fog_coord):
	#for line in list_localidades_fog: 
	FileTemp = open(str(FileName) + ".tmp", 'a')	
	qntd_recebidos = 0
	cont = 0
	bus_test = simulador.Bus()
	fog_test = simulador.Fog()
	#fog_localization = fog_test.fog_localization(contfog)
	#print fog_localization
	for i in range(0,3600):

		distance = vincenty(bus_test.bus_request(i), fog_coord[contfog]).meters
		
		if (distance <= RANGE_FOG):
			#bus_test.send_data()
			qntd_recebidos = qntd_recebidos + 1
			#print qntd_recebidos
			
	
		#cont = cont + 1
		time.sleep(1)
		#print cont
		#print i
		
	print 'oi'
	FileTemp.write(str(fog_coord[contfog]) + " " + str(qntd_recebidos) + "\n")
	contfog = contfog + 1	
	
