import cs50
#loop ask for number of 1-8
while True:
    height = cs50.get_int("height:")
    if height >0 and height <= 8:
        break
#end of loop, formula for pyramid, spaces and hashes.
for i in range(height):
    print (' ' * (height-1-i) , end = "")
    print ('#' * (i+1));