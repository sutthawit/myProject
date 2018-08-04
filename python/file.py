def main():
   # Create new file
   f=open("text1.txt", "w+")
   for i in range(10):
      f.write("This is line " + str(i) + "\r\n")
   f.close()

   # Append file
   f=open("text1.txt", "a")
   for i in range(10,20):
      f.write("This is line " + str(i) + "\r\n")
   f.close()

   # Ready file
   f=open("text1.txt", "r")
   if f.mode == 'r':
      contents = f.read()
      print(contents)
      f.close()

   # Ready file by line
   f=open("text1.txt", "r")
   if f.mode == 'r':
      line = f.readlines()
      print(line)
      for x in line:
         print(x)

if __name__ == "__main__":
   main()
