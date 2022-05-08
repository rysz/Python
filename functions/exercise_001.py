#create a function
def say_hello():
  print('Hello World!')

say_hello()
print()

#create a funtiond with a parameter
def say_hello(name):
  print(f'Hello {name}!')

say_hello('Bob')
print()

#create a function with a default parameter
def say_hello(name='World'):
  print(f'Hello {name}!')

say_hello()
say_hello('Bob')
print()

#create a function with multiple parameters
#None is a special keyword that represents the NoneType object.
def say_hello(name='World', greeting=None):
  if greeting == None:
    print(f'Hello {name}!')
  else:
    print(f'{greeting} {name}!')

say_hello()
say_hello('Bob')
say_hello(greeting='Howdy')
say_hello('Bob', 'Howdy')
print()

print(type(None))
print()

#create a function that returns a list
def create_deck():
  suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
  ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
  deck = []

  for suit in suits:
    for rank in ranks:
      deck.append(f'{rank} of {suit}')

  return deck

my_deck = create_deck()
print(len(my_deck))
print()
