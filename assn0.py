import os
import sys
from enum import Enum

def celsius_to_fahrenheit(celsius):
#""Convert temperature from Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def file_read(file_name):
  file_open = open(file_name,r)
  line_read = file_open.readlines()
  line = line_read.split('/n')
  for i in line:
      print(celcius_to_fahrenheit(i))
      
def main():
  if len(sys.argv) > 1:
      file_read(sys.argv[1])
  else:    
      celsius_temperature = float(input("Enter temperature in Celsius: "))
      fahrenheit_temperature = celsius_to_fahrenheit(celsius_temperature)
      print("Temperature in Fahrenheit:", fahrenheit_temperature)
  # Print the value of the environment variable CSN if it exists
  csn = os.getenv("CSN")
  if csn is None or csn == '':
      print('CSN is empty    FAIL')
  else:
      print("CSN is {}".format(csn))
      
if __name__ == "__main__":
  main()
               
