
CHARS = list(
    """ .'`^",:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"""
)
INTERVAL = len(CHARS) / 256


def set_chars(args):
    """Function to reverse CHARS if rev flag set."""
    if args["rev"]:
        CHARS.reverse()
    del args["rev"]


def getChar(val):
    """Function to convert val 0-255 to one of available charachters."""
    return CHARS[int(val * INTERVAL)]


arg_setup_string = """
parser.add_argument(
    "image",
    type=str,
    # default=None,  # I think this is unneccesarry. Get same message with or without default when image is omitted.
    help="The image to convert to ascii art. Required.",
)|
parser.add_argument(
    "--output",
    type=str,
    default="output",
    help='The name of the file to save the png and text output. Eg - img1. Optional (default is "output")',
)|
parser.add_argument(
    "--charW",
    type=int,
    default=12,
    help="The width of a single character Type=int default=12",
)|
parser.add_argument(
    "--charH",
    type=int,
    default=18,
    help="The height of a single character Type=Int default=18",
)|
parser.add_argument(
    "--scale",
    type=float,
    default=0.10,
    help="The scale of image Type=float default=.10",
)|
parser.add_argument(
    "--rev",
    type=bool,
    default=False,
    help="Reverse the order of charachter maping to color input.",
)"""
