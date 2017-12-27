
import fog_agent_new_tests
import threading, Queue
qntd_fogs = [600]
r_s = None
q = Queue.Queue()
COMPRESSION_LEVEL=1
WORD_SIZE_BITS=-15
MAX_MEASURES=100
MEM_LEVEL=9
STOP_ID = 1
OFFSET=1
def generateData (max_gathering):
    dataList = []

    for line in range (0, max_gathering):
        dataList.append(Data().data)

    return dataList


def createMessage(sensing_node, data):
    message = {}

    message["node_id"] = sensing_node
    message["type"] = 'data'
    message["header"] = "datetime,lat,lng,light,temperature,humidity,rain"
    message["load"] = data

    return message
def send_thread(thread_name,q):
    """Sends periodically stored data"""
    while True:
        output = {}
        output['stop_id'] = STOP_ID
        output['batches'] = []
        if not q.empty():
            while not q.empty():
                b = q.get()
                if ( b is not None):
                    output['batches'].append(b)
	    message = fog_agent_new_tests.compressMessage(output)
	    print message
	    
            #print cloud_client(message)    
            time.sleep(30)

def do_POST(message): 
        """Receives data from Arduino and sends to Cloud"""
    	input_batches = {}
    
    	input_batches['node_id'] = message['node_id'][0]
    	for line in message['load']:
        	tmp = line.split('\n')
	#print tmp
	#sizetmp = float(len(tmp))
	#print sizetmp
	#print '_______________'
	#hot_island.cartridge(tmp)
	#module = Module.module(tmp)
	#module.controller()
	#cloud_client(module.get_payload())	                
    	input_batches['type'] = str(message['type'][0])
    	input_batches['header'] = str(message['header'][0])
    	input_batches['received'] = str(datetime.datetime.now())
    	input_batches['load'] = tmp[0:-1] #the last line is always empty 
    	q.put(input_batches)
	#self.send_response(200)
  


if __name__ == "__main__":
	data = []
	messageText = ""
	r_s = None
	count = 0
	FileName = 'tamanho_msg_'
 
	for nr_fog in qntd_fogs:
		FileTemp = open(str(FileName) + str(nr_fog) + '.tmp', 'r')
		#handler_class = fog_agent_new_tests.S
		t = threading.Thread(send_thread, args=('alt', q))
    		t.daemon = True
    		
    
		for line in FileTemp.readlines():
			line_list = line.split()
		    	sensingNode = line_list[4] 
		    	data = generateData (int(sensingNode))
			print data
			message = createMessage(sensingNode, data)
			

			t.start()
			do_POST(message)
			t.join()
	
			

	
			
		

	    	   



		


