from datetime import date
dateToday = date.today()

dateToday = str(dateToday)

yearNow = str(dateToday[0]) + str(dateToday[1]) + str(dateToday[2]) + str(dateToday[3])
monthNow = str(dateToday[5]) + str(dateToday[6])
dayNow = str(dateToday[8]) + str(dateToday[9])

print(monthNow,dayNow,yearNow)


class day:
  def __init__(self,month,day,year,data):
    self.m = month
    self.d = day
    self.y = year
    self.dat = data

day1 = day(monthNow,dayNow,yearNow,"This is a test of the data attribute")

feb = []
for d in range(1,29):
  feb.append(d)

showFeb = feb
counter = 0
for elm in range(0,len(feb)):
  if(counter == 5):
    print()
    counter = 0
  print(showFeb[elm],end="\t")
  counter += 1
print()

for d in range(0,len(feb)):
  feb[d] = day(monthNow,d,yearNow,"")
print()
print("#############")
print("#  Options  #")
print("#############")
print("1 - Add Event")
print("2 - View all events")
print("3 - Quit Pythonic Calendar")
opt = input("")
print()
print()

quitVar = False
while(quitVar == False):
  if opt == '1':
    dayIn = input("Enter the day of the month you would like to add an event to: ")
    dataIn = str(input("What time is the event: "))
    dataIn += " - "
    dataIn += str(input("Describe the event: "))
    feb[int(dayIn)].dat = dataIn
    

  if opt == '2':
    for elm in feb:
      print(elm.d + 1,end='\t')
      print(elm.dat)
    
  if opt == '3':
    print()
    print("Have a good day!")
    print()
    quitVar = True

  print()
  print("#############")
  print("#  Options  #")
  print("#############")
  print("1 - Add Event")
  print("2 - View all events")
  print("3 - Quit Pythonic Calendar")
  opt = input("")
  print()
  print()
