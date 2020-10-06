t = "temp"
temp = 0
a = 90
b = 70
c = 50
d = 32

temp = int(input("Please enter the current temperature: "))

if temp >= a:
    print ("Wear Shorts")

if temp < a:
    if temp >= b:
        print ("Short Sleeves are fine")
    
if temp < b:
    if temp >= c:
        print ("Wear a jacket")

if temp < c:
    if temp >= d:
        print ("Wear a heavy coat")

if temp < d:
    print ("Stay Inside")


