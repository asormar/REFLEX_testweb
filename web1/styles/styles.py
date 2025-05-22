from enum import Enum
import reflex as rx


#Constants
MAX_WIDTH= "40%"
MARGIN_Y= "20px"

#Sizes
class Spacer(Enum):
    SMALL= "0.5em"
    MEDIUM= "0.8em"
    DEFAULT= "1em"
    BIG= "3em"

#Styles
BASE_STYLE= { #Aquí predefinimos los estilos
    rx.button :{
        "width":"100%",
        "height":"100%",
        "display":"block",
        "padding":Spacer.SMALL.value,
        "border_radius":Spacer.DEFAULT.value
    },

    rx.link :{
        "underline":"none",
        "color":"black",
        "_hover":{}
    }
}


button_title_style= dict(
    font_size=Spacer.DEFAULT.value
)

button_body_style= dict(
    font_size=Spacer.MEDIUM.value
)