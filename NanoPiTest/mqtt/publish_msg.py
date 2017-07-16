# script to send 
import paho.mqtt.publish as publish
import time 

host_name = "192.168.120.84"
topic_name = "test/dev1"

def main_loop():
    while 1:
        publish.single(topic_name, 121, hostname=host_name)
        time.sleep(1)

if __name__ == '__main__':
    try:
        main_loop()
    except KeyboardInterrupt:
        print >> sys.stderr, '\nExiting by user request.\n'
        sys.exit(0)    

