print('run start')
import RPi.GPIO as GPIO

LSBFIRST = 1
MSBFIRST = 2

dataPin = 7 #DS pin of 74HC595 (Pin 14)
latchPin = 11 #ST_CP or RCLK Pin of 74HC595 (Pin12)
clockPin = 13 #CH_CP Pin of 74HC595 (Pin11)
currentState = 0b00000000

def setup_relay_board_pins():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(dataPin, GPIO.OUT)
    GPIO.setup(latchPin, GPIO.OUT)
    GPIO.setup(clockPin, GPIO.OUT)
    write_state(currentState)

def write_state(data):
    GPIO.output(latchPin, GPIO.LOW)
    for i in range(8):
        GPIO.output(dataPin, (data >> (7-i)) & 0x01)
        GPIO.output(clockPin, GPIO.HIGH)
        GPIO.output(clockPin, GPIO.LOW)
    GPIO.output(latchPin, GPIO.HIGH) #Latch high to update outputs

def toggle_relay(relay):
    tState = my_dict[relay]
    nState = 0
    cState = currentState
    binString = str(bin(cState))
    tString = str(bin(tState))
    tStringLen = len(tString)
    binStringLength = len(binString)
    nState = 0
    print('--- trying to toggle with ' + str(bin(tState)))
    print('cstate ' + str(cState))
    for i in range(0,8):
        #check if current state should be toggled
        #check if bit is sig
        print('check if current state is bigger than ' + str(2**i))
        if(cState >= 2**i):
            #get val of current bit
            currentBit = binString[binStringLength-(i+1)]
            if(currentBit == '1'):
                #relay is definitely set to 1, check toggle value
                print('circuit state 1')
                if(tState >= 2**i):
                    tBit = tString[tStringLen-(i+1)]
                    print('toggle bit '+ tBit)
                    if(tBit == '1'):
                        #relay is 1 and toggle true
                        nState += 0
                    else:
                        #relay is 1 and toggle false
                        nState += 2**i
                else:
                    #relay is 1 and toggle false
                    print('toggle bit 0')
                    nState += 2**i
            else:
                #relay is definitely set to 0, check toggle value
                print('circuit state 0')
                if(tState >= 2**i):
                    tBit = tString[tStringLen-(i+1)]
                    print('toggle bit '+ tBit)
                    if(tBit == '1'):
                        #relay is 0 and toggle is true
                        nState += 2**i
                else:
                    print('toggle bit 0')
        else:
            print('circuit state 0')
            if(tState >= 2**i):
                tBit = tString[tStringLen-(i+1)]
                print('toggle bit '+ tBit)
                if(tBit == '1'):
                    #relay is 0 and toggle is true
                    nState += 2**i
            else:
                print('toggle bit 0')
    write_state(nState)
    return nState
    

my_dict = {
    "a" : 128,
    "b" : 64,
    "c" : 32,
    "d" : 16,
    "e" : 8,
    "f" : 4,
    "g" : 2,
    "h" : 1,
}
