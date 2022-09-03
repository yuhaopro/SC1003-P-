# Have a list of colour r g b
# Check r g b must be integers, and values between 0 to 255

# Have a float variable for speed
# Check Input must be float, and between 0.05 and 1

_QUITPROGRAM = 400
_RED = "red"
_GREEN = "green"
_BLUE = "blue"

_MESSAGE = "message"
_BACKGROUND = "background"

def CheckMessageColor(string_color, string_usage):
    counter = 0
    while counter < 3:
        try:
            _colourvalue = int(input("Enter the " + string_usage + " color value for " + string_color + " : "))
            if (_colourvalue < 0 or _colourvalue > 255 ):
                print("Value has to be between 0 and 255 (",counter + 1, ")")
                counter+=1
                continue
            else:
                return _colourvalue
        except:
            print("Invalid - use number only (",counter + 1, ")")
            counter+=1
    else:
        print("You have exceeded the number of trials allowed. Bye!")
        quit()

def CheckSpeed():
    counter = 0
    while counter < 3:
        try:
            _speedvalue = float(input("Enter the message speed value: "))
            if (_speedvalue < 0.05 or _speedvalue > 1 ):
                print("Value has to be between 0.05 and 1 (",counter + 1, ")")
                counter+=1
                continue
            else:
                return _speedvalue
        except:
            print("Invalid - use number only (",counter + 1, ")")
            counter+=1
    else:
        print("You have exceeded the number of trials allowed. Bye!")
        quit()
    


r = CheckMessageColor(_RED, _MESSAGE)
g = CheckMessageColor(_GREEN, _MESSAGE)
b = CheckMessageColor(_BLUE, _MESSAGE)
message_color = [r, g, b]

r = CheckMessageColor(_RED, _BACKGROUND)
g = CheckMessageColor(_GREEN, _BACKGROUND)
b = CheckMessageColor(_BLUE, _BACKGROUND)
background_color = [r ,g, b]

speed_value = CheckSpeed()
print("Message_Colours: " + message_color)
print("Background_Colours: " + background_color)
print("Speed_Value: " + speed_value)