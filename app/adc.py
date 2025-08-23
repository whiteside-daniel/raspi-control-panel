import spidev
import time

#Setup SPI
spi = spidev.SpiDev()
spi.open(0,0) #Bus 0 device 0
spi.max_speed_hz = 1000000

#Constants
VREF = 5.3
R1 = 10000.0
R2 = 2000.0
VDRATIO = 1 + (R1 / R2)

def read_mcp3008(channel):
    #Setup SPI
    spi = spidev.SpiDev()
    spi.open(0,0) #Bus 0 device 0
    spi.max_speed_hz = 1000000
    if(channel < 0 or channel > 7):
        return 0
    
    #Send 3 bytes: start bit, mode/channel, and dont care
    adc_response = spi.xfer2([0x01 , (0x80 + (channel << 4)), 0x00])
    
    #Extract 10-bit result
    adc_value = ((adc_response[1] & 0x03) << 8) + adc_response[2]
    adc_voltage = adc_value * VREF / 1024
    battery_voltage = adc_voltage * VDRATIO
    spi.close()
    return round(battery_voltage, 2)

vtg = read_mcp3008(0)
print(f"{vtg:.2f}")