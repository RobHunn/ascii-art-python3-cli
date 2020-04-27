from PIL import Image, ImageDraw, ImageFont
import argparse
from helper import arg_setup_string, check_interactive, set_chars, getChar, get_hrgb

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
#  Add all parser arguments from helper file.
[eval(w) for w in arg_setup_string.split("|")]

# convert parser.parse_args() SimpleNamespace to dictionary for unpackability.
args = dict(vars(parser.parse_args()))

# check for interactive input.
args = check_interactive(args)

# Set charachters to use as pixels and reverse the order if reverse arg is true.
set_chars(args)


def ascii_art(image, font_size, scale, charW, charH, output):
    """Function to convert image into ascii art. Photo and text output."""
    im = Image.open(image)

    fnt = ImageFont.truetype("arial.ttf", int(font_size))

    width, height = im.size
    im = im.resize(
        (int(scale * width), int(scale * height * (charW / charH)),), Image.NEAREST,
    )
    width, height = im.size
    pix = im.load()

    outputImage = Image.new(
        "RGB", (int(charW * width), int(charH * height)), color=(0, 0, 0)
    )
    d = ImageDraw.Draw(outputImage)

    with open(f"{output}.txt", "w") as text_file:
        for i in range(height):
            for j in range(width):
                h, r, g, b, = get_hrgb(pix[j, i])
                char = getChar(h)
                text_file.write(char)
                d.text(
                    (int(j * charW), int(i * charH)), char, font=fnt, fill=(r, g, b),
                )

            text_file.write("\n")

    outputImage.save(f"{output}.png")


if __name__ == "__main__":
    ascii_art(**args)
