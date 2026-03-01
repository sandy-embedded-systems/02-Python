# 1.Given a voltage reading, print "Under Voltage", "Nominal", or "Over Voltage".
# (Nominal is between 3.0V and 3.3V inclusive.)
# Input: 3.35
# Output: Over Voltage
voltage=float(input("Enter voltage:"))
if voltage>=3.0 and voltage<=3.3:
    print("normal voltage")
else:
    print("Over voltage")
print()

#2.Take an 8-bit register value and print if the **MSB** (most significant bit) is set or not.
# Input: 0b10010010
# Output: MSB set
num=int(input("Enter binary value:"),2)
if num &(1<<7):
    print("MSB set")
else:
    print("MSB not set")
print()

#3. Enter a temperature and print "Overheat" (>75°C), "Normal" (25-75°C), or "Low Temp" (<25°C).
# Input: 18
# Output: Low Temp
temperature=int(input("Enter temperature:"))
if temperature>75: print("Over heat")
elif temperature>25 and temperature<75: print("Normal")
else: print("Low temp")
print()

#4. Given two pin logic levels (0 or 1), print the type of logic gate output if these were inputs to 
# an AND, OR, and XOR gate.
# Input: 1, 0
# Output: AND: 0, OR: 1, XOR: 1
pin1=bool(int(input("Enter pin1 state:")))
pin2=bool(int(input("Enter pin2 state:")))
print("AND:",pin1 and pin2)
print("OR:",pin1 or pin2)
print("XOR:",not (pin1 ^ pin2))
print()

#5.If a sensor value is outside the range 100–900, print "Sensor Fault". If within, print "Sensor OK".
# Input: 950
# Output: Sensor Fault
sensor_val=int(input("Enter sensor value:"))
if sensor_val>=100 and sensor_val<=900:
    print("Sensor OK")
else:
    print("Sensor FAULT")
print()

#6. Take an error code (integer). Print "Critical" if code ≥1000, "Warning" if 100–999, and "Info" if <100.
# Input: 230
# Output: Warning
errCode=int(input("Enter error code:"))
if errCode<100:print("Info")
elif errCode>=1000: print("Warning")
else: print("Critical")
print()

#7. Given three boolean flags: `power_on`, `overcurrent`, `overvoltage`, print:
# - "System Safe" if only `power_on` is True.
# - "Shut Down: Overcurrent" if `overcurrent` is True.
# - "Shut Down: Overvoltage" if `overvoltage` is True.
# - "Critical Failure" if both faults are True.
# Input: True, True, False
# Output: Shut Down: Overcurrent
power_flag=bool(input("Enter power flag:"))
overCur_flag=bool(input("Enter over current flag:"))
overVol=bool(input("Enter over voltage flag:"))
if power_flag==True and overCur_flag==False and overVol==False:
    print("System Safe")
elif power_flag==False and overCur_flag==True and overVol==False:
    print("Shut Down: Over current")
elif power_flag==False and overCur_flag==False and overVol==True:
    print("Shut Down: over voltage")
elif overCur_flag==True and overVol==True:
    print("Critical Failure")
print()

#8. Given a digital input value (0–255), determine and print which of 4 quadrants it falls into:
# - 0–63, 64–127, 128–191, 192–255
value=int(input("Enter digital value:"))
if value>=0 and value<=63:
    print("Quadrant 1")
elif value>=64 and value<=127:
    print("Quandrant 2")
elif value>=128 and value<=191:
    print("Quadrant 3")
else: print("Quadrant 4")
print()

#9. Enter a signal frequency (Hz). Print "Low Band" (<1000), "Mid Band" (1000–9999), "High Band" (10000–99999),
# or "Out of Range".
# Input: 8000
# Output: Mid Band
freq=int(input("Enter frequency:"))
if freq<1000: print("Low Band")
elif freq>=1000 and freq<10000:print("Mid Band")
elif freq>=10000 and freq<=99999:print("High Band")
else: print("Out of Range")
print()

#10. Given three sensor readings, print "Majority High" if at least two readings are above a threshold (e.g., 50),
# otherwise "Majority Low".
# Input: 40, 65, 70
# Output: Majority High
read1=int(input("Enter sensor reading 1:"))
read2=int(input("Enter sensor reading 2:"))
read3=int(input("Enter sensor reading 3:"))
if read2>50 and read3>50:
    print("Majority High")
else: print("Mejority Low")
print()

#11. Enter a 16-bit value and print if parity (number of 1s) is even or odd.
# Input: 0xAAAA
# Output: Parity: Even
num_16=int(input("Enter 16-bit value:"),16)
if num_16.bit_count()%2 ==0:
    print("Even parity")
else:
    print("Odd parity")
print()

#12. Given a voltage and current reading, print "Power OK" if both are in safe ranges, 
# otherwise print specific error:
# - Voltage out of 3.0–3.3V: "Voltage Error"
# - Current out of 10–500mA: "Current Error"
# - Both out: "Power Error"
voltage=int(input("Enter voltage:"))
current=int(input("Enter current:"))
if voltage>3.3 or voltage<3 and current<10 or current>500:
    print("Power Error")
elif voltage>3.3 or voltage<3:
    print("Voltage Error")
elif current<10 or current>500:
    print("Current Error")
else: print("Power OK")
print()

#13. Given the status of three LEDs (on/off as 1/0), print which LEDs are ON. If all are off, print 
# "All LEDs off".
# Input: 0, 1, 0
# Output: LED2 ON
led1=bool(input("LED1 status:"))
led2=bool(input("LED2 status:"))
led3=bool(input("LED3 status:"))
if (led1 and led2 and led3) == False:
    print("All LEDS are off")
elif led1:print("LED1 ON")
elif led2:print("LED2 ON")
elif led3: print("LED3 ON")
print()

#14. Accept a device mode value:
# - 0: "Standby"
# - 1: "Active"
# - 2: "Fault"
# - Any other: "Unknown mode"
mode=int(input("Enter device mode:"))
if mode==0: print("Standby")
elif mode==1: print("Active")
elif mode==2: print("Fault")
else: print("Unknown mode")
print()

#15.Enter two analog readings. Print "Match" if they are within 5 units of each other, "No Match" otherwise.
# Input: 98, 101
# Output: Match
read1=int(input("Enter sensor reading 1:"))
read2=int(input("Enter sensor reading 2:"))
if read1>read2:
    read1,read2=read2,read1
if (read2-read1)<=5:
    print("Match")
else:print("No Match")