class BoxOccupiedError(Exception):
    "Raise exception when user input a occupied box"

"""Module providing the input functionality: Only receives number from 1 to 9"""
def player_input(occupied_boxes, player_name):
    number = 0
    while True:
        try:
            number = int(input("{pname}'s turn: Please choose your next move - index position, remember that it must be a number between 1 and 9, and that the box must be available: ".format(pname = player_name)))
            if(number not in range(1,10)):
                raise ValueError("Must be a number between the range of 1-9") 
            if(number in occupied_boxes):
                raise BoxOccupiedError()       
        except BoxOccupiedError:
            print("Box is already occupied. Please look at the board and input an index position that be free")
        except ValueError:
            print("Please input a number that be between the range of 1-9")
        else:
            break
    
    return number       
