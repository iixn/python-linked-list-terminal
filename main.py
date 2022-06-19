from os import system
from time import sleep
from sys import exit
import signal
import platform

def clearTerm():
    if platform.system() == "Windows":
        system("cls")
    elif platform.system() == "Linux":
        system("clear")

def signal_handler(signal, frame):

    print("\n\n\033[1;33mBye")
    exit()

signal.signal(signal.SIGINT, signal_handler)

class node:

  def __init__(self, data = None, next = None):

    self.data = data
    self.next = next

class linkedList:

  def __init__(self):

    self.head = None

  def isEmpty(self):
    
    if self.head == None:

      print("\n\033[1;31mThe list is empty!")

    else:

      print("\n\033[1;32mThe list has items!")
      
  def addEnd(self, data):

    if not self.head:

      self.head = node(data=data)
      return

    curr = self.head

    while curr.next:

      curr = curr.next

    curr.next = node(data=data)

  def addFirts(self, data):

    self.head = node(data=data, next=self.head) 

  def printList(self):
    
    node = self.head

    if node == None:

      print("\033[1;31mThere is no node!")
      return
    
    while node != None:
      
      print("\033[1;34m{}".format(node.data), end ="\033[1;36m -> ")
      node = node.next

      if node == None:

        print("\033[1;31mEND")
  
  def delNode(self, key):
    
    curr = self.head
    prev = None
    while curr and curr.data != key:
            
      prev = curr
      curr = curr.next
    
    if prev is None:
            
      self.head = curr.next
        
    elif curr:
      
      prev.next = curr.next
      curr.next = None

lklst = linkedList()

def option1():

  lklst.isEmpty()

def option2(number):

  lklst.addEnd(data=number)

def option3(number):

  lklst.addFirts(data=number)

def option4(number):

  lklst.delNode(key=number)

def option5():

  lklst.printList()

def options():

  clearTerm()

  try:
    option = int(input("""
\033[1;36mPython       List           NULL
\033[1;36m     ↘     ↗     ↘        ↗
\033[1;36m      Linked       Terminal 

\033[34mBy iixn\n
\033[35m[1] Is Empty List
[2] Add Last Node
[3] Add First Node
[4] Delete Node
[5] Print List

[*] Choose an option > """))

    if option == 1:

      option1()
      sleep(2)
      options()

    elif option == 2:

      try:

        number = int(input("\n\033[1;34mIntroduce a number > "))
        option2(number)
        print("\n\033[1;32mAdded Successfully!")
        sleep(2)
        options()

      except ValueError:

        print("\n\033[1;31mOnly Numbers!")
        sleep(2)
        options()

    elif option == 3:

      try:

        number = int(input("\n\033[1;34mIntroduce a number > "))
        option3(number)
        print("\n\033[1;32mAdded Successfully!")
        sleep(2)
        options()

      except ValueError:

        print("\n\033[1;31mOnly Numbers!")
        sleep(2)
        options()

    elif option == 4:

      try:
        
        number = int(input("\n\033[1;34mIntroduce the node you want remove > "))
        option4(number)
        print("\n\033[1;32mRemoved Successfully")
        sleep(2)
        options()

      except ValueError:

        print("\n\033[1;31mOnly Numbers!")
        sleep(2)
        options()

      except AttributeError:

        print("\n\033[1;31mThe node does not exist!")
        sleep(2)

      options()

    elif option == 5:

      print("")
      option5()
      input("\n\033[1;34mPress ENTER to continue")
      options()

    else:

      print("\n\033[1;31mChoose a correct option!")
      sleep(2)
      options()

  except ValueError:

    print("\n\033[1;31mOnly Numbers!")
    sleep(2)
    options()

options()
