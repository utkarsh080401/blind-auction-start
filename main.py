logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
from replit import clear
print("Welcome to the mini auction")
auct= {}
again = False
while(not again):
  print(logo)
  name= input("What's your name?")
  bid = int(input("What's your bid(in dollars)"))
  auct[name]= bid
  another = input("Someone left?")
  if another.lower() != 'yes':
    again= True
  clear()
print(auct)
max1= max(auct.values())
position= list(auct.values()).index(max1)
max_bidder= list(auct.keys())[position]
print(f'And the winner is {max_bidder} Ji')





#HINT: You can call clear() to clear the output in the console.