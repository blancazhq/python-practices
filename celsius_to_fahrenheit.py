#Prompt the user for a number in degrees Celsius, and convert the value to degrees in Fahrenheit and display it to the user. 

temp_c = float(raw_input("temprature in C"))

temp_f = temp_c*1.8+32

print "%.1f F" % temp_f
