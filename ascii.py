from PIL import Image, ImageDraw, ImageFont
import argparse
from helper import set_chars, getChar, arg_setup_string

#
# Developers:
# Robert Hunnicutt:   https://github.com/RobHunn
# Richard Iannucelli: https://github.com/konkrer
# Repo:               https://github.com/RobHunn/ascii-art-python3-cli
#


# Create command line argument parser.
parser = argparse.ArgumentParser(
    description="Turn any photo into ascii art from the Command Line."
)
#  Add all parser arguments from helper file
[eval(w) for w in arg_setup_string.split("|")]

# convert parser.parse_args() SimpleNamespace to dictionary for unpackability.
args = dict(vars(parser.parse_args()))

# Set charachters to use as pixels and reverse the order if reverse arg is true.
set_chars(args)


def ascii_art(charW, charH, scale, image, output):
    """Function to convert image into ascii art. Photo and text output."""
    im = Image.open(image)

    fnt = ImageFont.truetype("arial.ttf", 15)

    width, height = im.size
    im = im.resize(
        (int(scale * width), int(scale * height * (charW / charH)),), Image.NEAREST,
    )
    width, height = im.size
    pix = im.load()

    outputImage = Image.new("RGB", (charW * width, charH * height), color=(0, 0, 0))
    d = ImageDraw.Draw(outputImage)

    with open(f"{output}.txt", "w") as text_file:
        for i in range(height):
            for j in range(width):
                r, g, b = pix[j, i]
                h = int((r + g + b) / 3)
                # pix[j, i] = (h, h, h)  # WFT?? i dunno....
                char = getChar(h)
                text_file.write(char)
                d.text(
                    (j * charW, i * charH), char, font=fnt, fill=(r, g, b),
                )

            text_file.write("\n")

    outputImage.save(f"{output}.png")


if __name__ == "__main__":
    ascii_art(**args)
