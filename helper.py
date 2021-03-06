
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


def check_interactive(args):
    """If image is None or -i flag was entered query user for input."""
    if not args["image"]:
        interactive = True
    else:
        interactive = args["i"] 
    del args["i"]

    if not interactive:
        return args

    # if args are default values query user for new values
    new = {k: input(verboser[k]) for k, v in args.items() if v == default[k]}
    # if no user input use default value. if input convert it to float if it is a number argument.
    new = {k: default[k] 
            if v == '' else 
            float(v) if k in num_args else v 
            for k, v in new.items()}

    return {**args, **new}
    

def get_hrgb(pixel):
    """Fuction to get r, g, b output plus h.
       h is average of r, g, b.
       If pixel is integer image is grayscale. set r,g,b = pixel.
       Output: h, r, g, b
    """
    if isinstance(pixel, int):
        return pixel, pixel, pixel, pixel
    r, g, b, *_ = pixel
    return int((r + g + b) / 3), r, g, b


arg_setup_string = """
parser.add_argument(
    "image",
    type=str,
    default=None,
    nargs="?",
    help="The image to convert to ascii art. Required.",
)|
parser.add_argument(
    "-i",
    action="store_true",
    help='Interactive. User will be queried for input.',
)|
parser.add_argument(
    "--output",
    type=str,
    default="output",
    help='The name of the file to save the png and text output. Eg - img1. Optional (default is "output")',
)|
parser.add_argument(
    "--font-size",
    type=int,
    default=15,
    dest="font_size",
    help="Font size used for pixel. Type=int default=15",
)|
parser.add_argument(
    "--charW",
    type=int,
    default=12,
    help="The width of a single character spot. Type=int default=12",
)|
parser.add_argument(
    "--charH",
    type=int,
    default=18,
    help="The height of a single character spot. Type=Int default=18",
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


verboser = {
        "image": "Image file to process: ",
        "output": 'Output files name (leave blank for default "output"): ',
        "font_size": "Font size to use as pixel (leave blank for default 15): ",
        "charW": "Character width (leave blank for default 12): ",
        "charH": "Character height (leave blank for default 18): ",
        "scale": "Scale for image (leave blank for default scale 0.10): ",
        "rev": "Invert character scheme for white background image? (leave blank default): "
        }

default = {
    "image": None,
    "output": "output",
    "font_size": 15,
    "charW": 12,
    "charH": 18,
    "scale": 0.1,
    "rev": False
    }
    
num_args = ["font_size", "charW", "charH", "scale"]
