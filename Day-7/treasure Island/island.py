import achi

print(achi.welcome)
print()
print('In this Treasure Island Your job is to find Treasure, but remember there are many dangers things here so be '
      'careful')
print()

print(achi.begins)
print()
print(achi.lake)

lives = 4

cross_lake = input('There is a Lake in front of you, what should you choose! (Swim or Boat): ').capitalize()

if cross_lake == 'Boat':
    print('Wow You successfully reached to Island 😍')
    print()
    print(achi.island)
    direction = input('Now there are two ways to go either North or South: ').capitalize()
    if direction == 'North':
        pass
    elif direction == 'South':
        print(achi.hills)
        print('You fell from the hill')
        print('You lose')
        lives -= 1
    else:
        print(f'Sorry There is no direction {direction}')

elif cross_lake == 'Swim':
    print(achi.island)
    print()
    direction = input('Now there are two ways to go either East or West: ').capitalize()
    if direction == 'East':
        print('There is a crocodile living in the each. He eat you')
        print('You lose')
    elif direction == 'West':
        room = input('You have 2 rooms blue and red choose one: ').capitalize()
        if room == 'Red':
            print('There is a Fire in the room. You dead')
            print('You lose!')
            lives -= 1
        elif room == 'Blue':
            print('Congrajulations you find the treasure!')
            print()
            print(achi.treasure)

    else:
        print(f'Sorry There is no direction {direction}')

