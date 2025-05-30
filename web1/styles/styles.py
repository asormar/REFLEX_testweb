from enum import Enum
import reflex as rx
import reflex_chakra as rc
from .colors import Colors as Colors
from .colors import TextColor as TextColor
from .fonts import Font as Font
from .fonts import FontWeight as FontWeight


#Constants
MAX_WIDTH= "35%"
MARGIN_Y= "20px"

#Sizes
class Spacer(Enum):
    SMALL= "0.5em"
    MEDIUM= "0.8em"
    DEFAULT= "1em"
    LARGE= "1.5em"
    VERY_LARGE="2.5em"
    BIG= "3em",
    VERY_BIG="7em"

STYLESHEETS= [
    "https://fonts.googleapis.com/css2?family=Poppins:wght@300;500&display=swap",
    "https://fonts.googleapis.com/css2?family=WDXL+Lubrifont+TC&display=swap"
]

#Styles
BASE_STYLE= { #Aquí predefinimos los estilos con css
    "background_color": Colors.BACKGROUND,
    "font_family":Font.DEFAULT,
    "font_weight":FontWeight.LIGHT,

    rx.heading:{
        "color":TextColor.HEADER,
        "font_family":Font.TITLE.value,
        "font_weight":FontWeight.BOLD,
    },

    rx.button and rc.button:{
        "width":"100%",
        "height":"100%",
        "display":"block",
        "padding":Spacer.SMALL.value,
        "border_radius":Spacer.DEFAULT.value,
        "color":TextColor.HEADER,
        "background_color": Colors.CONTENT,
        "_hover":{
            "background_color": Colors.SECONDARY
        } #modifier that appear when mouse is on the element
    },

    rx.link and rc.link :{
        "underline":"none",
        "_hover":{}
    },
}


navbar_title_style= {
    "font_family": Font.LOGO,
    "font_size":Spacer.LARGE,
    "font_weight":FontWeight.MEDIUM,
}

title_style= {
    "width":"100%",
    "padding_top":Spacer.DEFAULT.value,
    "color":TextColor.HEADER,
    "font_family":Font.TITLE.value,
    "font_weight":FontWeight.MEDIUM,
}

button_title_style= {
    "font_size":Spacer.DEFAULT.value,
    "color":TextColor.HEADER,
    "font_family":Font.TITLE.value,
    "font_weight":FontWeight.MEDIUM,
}

button_body_style= {
    "font_size":Spacer.MEDIUM.value,
    "color":TextColor.BODY,
    "font_weight":FontWeight.LIGHT
}