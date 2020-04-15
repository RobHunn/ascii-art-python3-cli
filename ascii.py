from PIL import Image, ImageDraw, ImageFont
import math
import argparse
#
# Developers:
# Robert Hunnicutt:   https://github.com/RobHunn
# Richard Iannucelli: https://github.com/konkrer
# Repo:               https://github.com/RobHunn/ascii-art-python3-cli
#


# grab command line arguments
parser = argparse.ArgumentParser(
    description="Turn any photo into ascii art from the Command Line."
)
parser.add_argument(
    "image", type=str,
    default=None,
    help="The image to convert to ascii art. Required."
)
parser.add_argument(
    "--output",
    type=str,
    default='output',
    help='The name of the file to save the png and text output. Eg - img1. Optional (default is "output")',
)
parser.add_argument(
    "--charW",
    type=int,
    default=12,
    help='The width of a single character Type=int default=12',
)
parser.add_argument(
    "--charH",
    type=int,
    default=18,
    help='The height of a single character Type=Int default=18',
)
parser.add_argument(
    "--scale",
    type=float,
    default=.10,
    help='The scale of image Type=float default=.10',
)
# convert parser.parse_args() SimpleNamespace to dictionary.
# Remove keys with value of None.
args = {k: v for k, v in vars(parser.parse_args()).items() if v != None}
print(args)
chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]

charArray = list(chars)
charLength = len(charArray)
interval = charLength / 256


def getChar(inputInt):
    return charArray[math.floor(inputInt * interval)]


def ascii_art(charW, charH, scale, image, output, output_txt="output"):
    if not image:
        return
    text_file = open(f"{output}.txt", "w")

    im = Image.open(image)
    # You may have to chage this line to a font on your system too work this is my relative path
    fnt = ImageFont.truetype("arial.ttf", 15)

    width, height = im.size
    im = im.resize(
        (
            int(scale * width),
            int(scale * height * (charW / charH)),
        ),
        Image.NEAREST,
    )
    width, height = im.size
    pix = im.load()

    outputImage = Image.new(
        "RGB", (charW * width, charH * height), color=(0, 0, 0)
    )
    d = ImageDraw.Draw(outputImage)

    for i in range(height):
        for j in range(width):
            r, g, b = pix[j, i]
            h = int(r / 3 + g / 3 + b / 3)
            pix[j, i] = (h, h, h)
            text_file.write(getChar(h))
            d.text(
                (j * charW, i * charH),
                getChar(h),
                font=fnt,
                fill=(r, g, b),
            )

        text_file.write("\n")

    outputImage.save(f"{output}.png")


if __name__ == "__main__":
    ascii_art(**args)
