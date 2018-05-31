import datetime
import telepot
from telepot.loop import MessageLoop
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)

PIR_PIN = 8 #! change these numbers to your relevant pins on your gpio
LED = 12
BUZZ = 10
GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(BUZZ, GPIO.OUT)
GPIO.setup(LED, GPIO.OUT)

print ("PIR Telegram. CTRL+C to exit")

armed = 0

def handle(msg):
    global armed
    armed = 0
    global chat_id
    chat_id = #! PUT YOUR CHAT ID HERE#
    command = msg['text']

    print 'Got command: %s' % command

    if command == '/arm':
		              if armed == 0:
                            armed = 1
		                   	    bot.sendMessage(chat_id, "System now armed!")
			                      GPIO.output(BUZZ, 1)
                            time.sleep(1)
                            GPIO.output(BUZZ, 0)
                            time.sleep(0.5)
                            GPIO.output(BUZZ, 1)
                            time.sleep(0.5)
                            GPIO.output(BUZZ, 0)
		else:
			  bot.sendMessage(chat_id, "System already armed!")
			

    elif command == '/disarm':
                if armed == 1:
                        armed = 0
			                  bot.sendMessage(chat_id, "System has been disarmed")
			                  GPIO.output(BUZZ, 1)
                        time.sleep(1)
                        GPIO.output(BUZZ, 0)
                        time.sleep(0.5)
                        GPIO.output(BUZZ, 1)
                        time.sleep(0.5)
                        GPIO.output(BUZZ, 0)

		else:
			  bot.sendMessage(chat_id, "System is not armed")

    elif command == '/uptime':
                with open('/proc/uptime', 'r') as f:
                        uptime_seconds = float(f.readline().split()[0])
                        uptime_string = str(timedelta(seconds=uptime_seconds))
                        bot.sendMessage(chat_id, uptime_string)
                        print "%s said it want the uptime" % chat_id


def alarm():
	      if armed == 1:
		              bot.sendMessage(chat_id, "Motion Detected")
		              print 'Motion Detected'
	      else:
		          print 'Motion Detected but not armed'

bot = telepot.Bot('#! Put your bot id here')

MessageLoop(bot, handle).run_as_thread()
print 'I am listening ...'

while True:
           if GPIO.input(PIR_PIN):
                              if armed == 1:
		                          bot.sendMessage(chat_id, "Motion Detected")
					                    print 'Motion Detected'
					                    GPIO.output(BUZZ, 1)
					                    time.sleep(1)
                        	    GPIO.output(BUZZ, 0)
					                    time.sleep(5)
		        else:
					        print 'Motion Detected but not armed'
           		    time.sleep(10)
