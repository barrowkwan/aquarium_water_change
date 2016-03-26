#!/usr/bin/env python

import time
import pifacedigitalio as pfd

p = pfd.PiFaceDigital()

pump_water = 0
fill_water = 0

try:
  if p.input_pins[0].value == 1 :
    print "Start pump @ ", time.strftime("%m/%d/%Y %H:%M:%S")
    p.output_pins[0].turn_on()
    p.output_pins[1].turn_off()
    time.sleep(5)
    p.output_pins[7].turn_on()
    pump_water = 1
    time.sleep(2)
  else:
    print "Fill tank @ ", time.strftime("%m/%d/%Y %H:%M:%S")
    p.output_pins[7].turn_off()
    time.sleep(2)
    p.output_pins[0].turn_off()
    p.output_pins[1].turn_on()
    fill_water = 1
    time.sleep(2)
      
  while True:
    time.sleep(1) 
    if pump_water == 1 and p.input_pins[0].value == 0:
      print "Stop Pump and fill tank @ ", time.strftime("%m/%d/%Y %H:%M:%S")
      p.output_pins[7].turn_off()
      time.sleep(2) 
      p.output_pins[0].turn_off()
      p.output_pins[1].turn_on()
      time.sleep(1) 
      fill_water = 1
      pump_water = 0
    elif fill_water == 1 and p.input_pins[1].value == 1:
      print "Stop filling tank @ ", time.strftime("%m/%d/%Y %H:%M:%S")
      p.output_pins[7].turn_off()
      time.sleep(2) 
      p.output_pins[0].turn_on()
      p.output_pins[1].turn_off()
      time.sleep(1) 
      break
    else:
      continue 


  print "All done @ ", time.strftime("%m/%d/%Y %H:%M:%S")
  time.sleep(1) 
  p.output_pins[7].turn_off()
  time.sleep(2) 
  p.output_pins[0].turn_on()
  p.output_pins[1].turn_off()
  time.sleep(5) 
  p.output_pins[7].turn_off()
  time.sleep(2) 
  p.output_pins[0].turn_off()
  p.output_pins[1].turn_off()

except KeyboardInterrupt as e:
  p.output_pins[7].turn_off()
  time.sleep(2)
  p.output_pins[0].turn_off()
  p.output_pins[1].turn_off()
  print "Bye Bye!!"
except:
  p.output_pins[7].turn_off()
  time.sleep(2)
  p.output_pins[0].turn_off()
  p.output_pins[1].turn_off()
  print "Unexpected Error:", sys.exc_info()[0]



