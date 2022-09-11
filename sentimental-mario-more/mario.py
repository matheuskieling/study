while True:
    try:
        height = int(input("Height: "))
        # pyramid must be between 1 and 8 inclusive
        if height >= 1 and height < 9:
            # if okay, break out of the loop
            break
        else:
            raise ValueError
    # if input is not an integer
    except ValueError:
        pass

# iniciate blocks to be 1
blocks = height - (height - 1)
# iniciate spaces to be height - 1(this "1" is a block)
spaces = height - 1
# loop to print spaces + blocks + two spaces + blocks
for line in range(height):
    print(f"{spaces*' '}{blocks*'#'}  {blocks*'#'}")
    # update the number of blocks and spaces
    blocks += 1
    spaces -= 1
