#!/usr/bin/env python3

options = [
  "1: Kilometres to Miles",
  "2: Miles to Kilometres",
  "3: Celsius to Fahrenheit",
  "4: Fahrenheit to Celsius"
]

def km_mi(inputnum):
  outputnum = inputnum / 1.609
  return outputnum

def mi_km(inputnum):
  outputnum = inputnum * 1.609344
  return outputnum

def ce_fa(inputnum):
  outputnum = (inputnum * 9/5) + 32
  return outputnum

def fa_ce(inputnum):
  outputnum = (inputnum - 32) * 5/9
  return outputnum


def main():
  number = float(input("Enter the number you want to convert: "))
  for option in options:
    print(option)
  choice = int(input("Type the number of the option you wish to use: "))
  if choice == 1:
    output = km_mi(number)
    print(f"Kilometres to Miles: {number} ----> {output}".format(number, output))
  elif choice == 2:
    output = mi_km(number)
    print(f"Miles to Kilometres: {number} ----> {output}".format(number, output))
  elif choice == 3:
    output = ce_fa(number)
    print(f"Celsius to Fahrenheit: {number} ----> {output}".format(number, output))
  elif choice == 4:
    output = fa_ce(number)
    print(f"Fahrenheit to Celsius: {number} ----> {output}".format(number, output))
  else:
    print("Invalid choice. Restarting Program.\n-----------------------")
    main()

if __name__ == "__main__":
  main()