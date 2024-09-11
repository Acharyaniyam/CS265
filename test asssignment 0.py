#!/usr/bin/env python3
#*****************************************************
# stack.c -- implementation of the stack functions
#Niyam Acharya 
#April 2024
#
# python3 (macOs 13.0 (22A380)) 
# GNU/Linux 5.4.0-100-generic x86_64
#**************************************************/

import os
import sys
from enum import Enum

def celsius_to_fahrenheit(celsius):
#""Convert temperature from Celsius to Fahrenheit."""
    return float((float(celsius) * 9/5) + 32)

def file_read(file_name):
  file_open = open(file_name)
  while True:
    line_read = file_open.readline()
    print(celsius_to_fahrenheit(line_read))
      
def main():
    while True:
        try:
            if len(sys.argv) > 1:
                file_read(sys.argv[1])
            else:    
                celsius_temperature = float(input("Enter temperature in Celsius: "))
                fahrenheit_temperature = celsius_to_fahrenheit(celsius_temperature)
                print("Temperature in Fahrenheit:", fahrenheit_temperature)
        except ValueError:
            print()
        # Print the value of the environment variable CSN if it exists
    csn = os.getenv("CSN")
    if csn is None or csn == '':
        print('CSN is empty    FAIL')
    else:
        print("CSN is {}".format(csn))
      
if __name__ == "__main__":
  main()