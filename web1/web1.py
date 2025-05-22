import reflex as rx
from web1.components.navbar import navbar #así modularizamos el código importando componentes
from web1.components.footer import footer
from web1.views.header.header import header
from web1.views.links.links import links
import web1.styles.styles as styles

class State(rx.State): #Esto es para añadir el back en algún momento
    pass


def index() -> rx.Component:
    return rx.box(
        navbar(),

        rx.center( # para centrar cualquier cosa (en la pantalla)
            rx.vstack(
                header(),
                links(),
                max_width=styles.MAX_WIDTH,
                width="100%", #para que el contenido ocupe todo lo que pueda dentro del 50%
                margin_y=styles.Spacer.DEFAULT,
                align="center"
            )
        ),

        
        footer(),
    )

app= rx.App(
    style= styles.BASE_STYLE
)
app.add_page(index)

