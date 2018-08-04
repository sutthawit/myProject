import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

def main():
   print(os.name)
   print("Item exists: " + str(path.exists("text1.txt")))
   print("Item is a file: " + str(path.isfile("text1.txt")))
   print("Item is a directory: " + str(path.isdir("text1.txt")))
   print("Item path: " + str(path.realpath("text1.txt")))
   print("Item path and name: " + str(path.split(path.realpath("text1.txt"))))


   t = time.ctime(path.getmtime("text1.txt"))
   #print("Last modify time of " + str(path.realpath("text1.txt")) + " is " + t)
   print(t)

   #print("Last modify time of " + str(path.realpath("text1.txt")) + " is " + str(datetime.datetime.fromtimestamp(path.getmtime("text1.txt"))))
   print(datetime.datetime.fromtimestamp(path.getmtime("text1.txt")))

   td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("text1.txt"))
   print("It has been " + str(td) + " since the file was modified")
   print ("or, " + str(td.total_seconds()) + " seconds")
 
if __name__ == "__main__":
   main()
