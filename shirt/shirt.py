from PIL import Image
from PIL import ImageOps
from sys import argv
from os import path

if len(argv) == 3:
    ext_one = path.splitext(argv[1])
    ext_two = path.splitext(argv[2])
    if ext_one[-1] == ext_two[-1]:
        if ext_two[-1] == ".jpg" or ext_two[-1] == ".png":
            try:
                with Image.open("shirt.png") as fg:
                    with Image.open(argv[1]) as bg:
                        new_bg = ImageOps.fit(bg, fg.size, centering = (0.5, 0.5))
                        new_bg.paste(fg, fg)
                    new_bg.save(argv[2])
            except FileNotFoundError:
                exit("Input does not exist")
        else:
            exit("Invalid output")
    else:
        exit("Input and output have different extensions")

elif len(argv) < 3:
    exit("Too few command-line arguments")

else:
    exit("Too many command-line arguments")