import RPi.GPIO as GPIO
import time as time
#import time

LSBFIRST = 1
MSBFIRST = 2

dataPin = 7 #DS pin of 74HC595 (Pin 14)
latchPin = 11 #ST_CP or RCLK Pin of 74HC595 (Pin12)
clockPin = 13 #CH_CP Pin of 74HC595 (Pin11)
invertPin = 15 #control pin, powers inverter which switches shift register on/off
currentState = 0b00000000

my_dict = {
    "A" : 128,
    "B" : 64,
    "C" : 32,
    "D" : 16,
    "E" : 8,
    "F" : 4,
    "G" : 2,
    "H" : 1,
}


def setup_relay_board_pins(dp=7, lp=11, cp=13):
    global currentState
    global invertPin
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(dp, GPIO.OUT)
    GPIO.setup(lp, GPIO.OUT)
    GPIO.setup(cp, GPIO.OUT)
    write_state(currentState)



def write_state(data, dp=7, lp=11, cp=13):
    GPIO.output(lp, GPIO.LOW)
    for i in range(8):
        GPIO.output(dp, (data >> (7-i)) & 0x01)
        GPIO.output(cp, GPIO.HIGH)
        GPIO.output(cp, GPIO.LOW)
    GPIO.output(lp, GPIO.HIGH) #Latch high to update outputs
    
    
    
def read_relay_state():
    state_map = {}
    global currentState
    checkState = currentState
    print(checkState)
    if(checkState >= 128):
        state_map.update({"A" : True})
        checkState -= 128
    else:
        state_map.update({"A" : False})
    
    if(checkState >= 64):
        state_map.update({"B" : True})
        checkState -= 64
    else:
        state_map.update({"B" : False})
    
    if(checkState >= 32):
        state_map.update({"C" : True})
        checkState -= 32
    else:
        state_map.update({"C" : False})
    
    if(checkState >= 16):
        state_map.update({"D" : True})
        checkState -= 16
    else:
        state_map.update({"D" : False})
    
    if(checkState >= 8):
        state_map.update({"E" : True})
        checkState -= 8
    else:
        state_map.update({"E" : False})
    
    if(checkState >= 4):
        state_map.update({"F" : True})
        checkState -= 4
    else:
        state_map.update({"F" : False})
    
    if(checkState >= 2):
        state_map.update({"G" : True})
        checkState -= 2
    else:
        state_map.update({"G" : False})
    
    if(checkState >= 1):
        state_map.update({"H" : True})
        checkState -= 1
    else:
        state_map.update({"H" : False})
    #Return checked values
    print(state_map)
    return state_map


def toggle_relay(relay):
    global currentState
    tState = my_dict[relay]
    nState = 0
    cState = currentState
    binString = str(bin(cState))
    tString = str(bin(tState))
    tStringLen = len(tString)
    binStringLength = len(binString)
    nState = 0
    print('--- trying to toggle '+relay+' with ' + str(bin(tState)))
    print('cstate ' + str(cState))
    for i in range(0,8):
        #check if current state should be toggled
        #check if bit is sig
        #print('check if current state is bigger than ' + str(2**i))
        if(cState >= 2**i):
            #get val of current bit
            currentBit = binString[binStringLength-(i+1)]
            if(currentBit == '1'):
                #relay is definitely set to 1, check toggle value
                #print('circuit state 1')
                if(tState >= 2**i):
                    tBit = tString[tStringLen-(i+1)]
                    #print('toggle bit '+ tBit)
                    if(tBit == '1'):
                        #relay is 1 and toggle true
                        nState += 0
                    else:
                        #relay is 1 and toggle false
                        nState += 2**i
                else:
                    #relay is 1 and toggle false
                    #print('toggle bit 0')
                    nState += 2**i
            else:
                #relay is definitely set to 0, check toggle value
                #print('circuit state 0')
                if(tState >= 2**i):
                    tBit = tString[tStringLen-(i+1)]
                    #print('toggle bit '+ tBit)
                    if(tBit == '1'):
                        #relay is 0 and toggle is true
                        nState += 2**i
                #else:
                    #print('toggle bit 0')
        else:
            #print('circuit state 0')
            if(tState >= 2**i):
                tBit = tString[tStringLen-(i+1)]
                #print('toggle bit '+ tBit)
                if(tBit == '1'):
                    #relay is 0 and toggle is true
                    nState += 2**i
            #else:
                #print('toggle bit 0')
    write_state(nState)
    currentState = nState
    return currentState

def run_relay_test():
    setup_relay_board_pins()
    toggle_relay("A")
    time.sleep(1)
    toggle_relay("B")
    time.sleep(1)
    toggle_relay("C")
    time.sleep(1)
    toggle_relay("D")
    time.sleep(1)
    toggle_relay("E")
    time.sleep(1)
    toggle_relay("F")
    time.sleep(1)
    toggle_relay("G")
    time.sleep(1)
    toggle_relay("H")
    time.sleep(1)
    read_relay_state()
    toggle_relay("A")
    time.sleep(1)
    toggle_relay("B")
    time.sleep(1)
    toggle_relay("C")
    time.sleep(1)
    toggle_relay("D")
    time.sleep(1)
    toggle_relay("E")
    time.sleep(1)
    toggle_relay("F")
    time.sleep(1)
    toggle_relay("G")
    time.sleep(1)
    toggle_relay("H")
    time.sleep(1)
    read_relay_state()
    toggle_relay("A")
    time.sleep(1)
    toggle_relay("B")
    time.sleep(1)
    toggle_relay("C")
    time.sleep(1)
    toggle_relay("D")
    time.sleep(1)
    toggle_relay("E")
    time.sleep(1)
    toggle_relay("F")
    time.sleep(1)
    toggle_relay("G")
    time.sleep(1)
    toggle_relay("H")
    time.sleep(1)
    read_relay_state()
    toggle_relay("A")
    time.sleep(1)
    toggle_relay("B")
    time.sleep(1)
    toggle_relay("C")
    time.sleep(1)
    toggle_relay("D")
    time.sleep(1)
    toggle_relay("E")
    time.sleep(1)
    toggle_relay("F")
    time.sleep(1)
    toggle_relay("G")
    time.sleep(1)
    toggle_relay("H")
    time.sleep(1)
    read_relay_state()
    
def testControlPin():
    GPIO.setmode(GPIO.BOARD)
    global invertPin
    GPIO.setup(invertPin, GPIO.OUT)
    GPIO.output(invertPin, GPIO.HIGH)
    time.sleep(8)
    GPIO.output(invertPin, GPIO.LOW)
    
#run_relay_test()
#testControlPin()