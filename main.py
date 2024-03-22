import random
import art
from game_data import data
from replit import clear

print(art.logo)

score=0

kplay=True
print()
a=random.randint(0, len(data)-1)
b=random.randint(0, len(data)-1)

while kplay:
  while b==a:
    b=random.randint(0, len(data)-1)
  if a==b:
    continue
  print(f"Compare A: {data[a]['name']}, {data[a]['description']}, from {data[a]['country']}")
  print(art.vs)
  print(f"Against B: {data[b]['name']}, {data[b]['description']}, from {data[b]['country']}")
  inp=input("Who has more followers? Type 'A' or 'B': ").lower()
  clear()
  print(art.logo)
  if data[a]['follower_count'] > data[b]['follower_count']:
    comp="a"
  elif data[a]['follower_count'] < data[b]['follower_count']:
    comp="b"
  else:
    comp=inp
  if inp!=comp:
    kplay=False
    print(f"Sorry, that's wrong. Final score: {score}")
  else:
    score+=1
    print(f"You're right! Current score: {score}.")
    a=b
  
    
    
  
