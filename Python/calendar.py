# COMMAND LINE CALENDAR
# Functions of the program include:
#	- View the calendar
# - Add an event to the calendar
#	-	Update an existing event
#	-	Delete an existing event

# Module imports
from time import sleep, strftime

# Take Username from user
user_name = raw_input("Enter your username: ") + "\n"

# Calendar dictionary to store dates as keys and events as values
calendar = {}

def welcome():
  print "Welcome to Command Line Calendar, " + user_name + "!\n"
  print "Initiating calendar..."
  sleep(1)
  print "Today is " + strftime("%A %B %d, %Y")
  print "Current time is " + strftime("%H:%M:%S")
  sleep(1)
  print "Select one of the following options"
  
def start_calendar():
  welcome()
  start = True
  while start:
    print_choice = "A - Add" + "\n" + "U - Update" + "\n" + "V - View" + "\n" + "D - Delete" + "\n" + "Q - Quit" + "\n"
    user_choice = raw_input(print_choice)
    user_choice = user_choice.upper()
    # Checking for View (V) option
    if (user_choice == "V"):
      # Checking for present events in the Calendar
      if (len(calendar.keys()) == 0 ):
        print "Calendar is empty"
      else :
        print calendar
    
    # Checking for Update (U) option
    elif (user_choice == "U"):
      date = raw_input("Enter date: ") 
      update = raw_input("Enter the update: ")
      calendar[date] = update
      print "Update successful" 
      print calendar
    
    # Checking for Add (A) option
    elif (user_choice == "A"):
      event = raw_input("Enter event:")
      date = raw_input("Enter date (MM/DD/YYYY)")
      if (len(date) > 10 or int(date[6:]) < int(strftime("%Y"))):
        print "Invalid date, please check if the date is correct and of this year"
        try_again = raw_input("Try again? (Y/N)")
        try_again = try_again.upper()
        if (try_again == 'Y'):
        	continue
        else:
          start = False
      else:
        calendar[date] = event
        print "Addition successful"
        print calendar
    
    # Checking for Delete (D) option
    elif(user_choice == "D"):
      print calendar.values()
      if len(calendar.keys()) < 1:
        print "Calendar is empty, can not delete any events"
      else:
        event = raw_input("Enter the event")
        for date in calendar.keys():
          if event == calendar[date]:
            del calendar[date]
            print "Event deletion successful" 
            print calendar
        else:
          print "Incorrect event specified, please try again."
    
    # Checking for Quit (Q) option 
    elif (user_choice == "Q"):
      print "Exiting Calendar..." + "\n"  + "Have a great day!"
      start = False
    
    # Checking for incorrect random specified option
    else:
      print "Invalid command entered, please try again."
  
# Main section
start_calendar()
