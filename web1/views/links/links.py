import reflex as rx
from web1.components.link_button import link_button
from web1.components.title import title

def links() -> rx.Component:
    return rx.vstack(
        title("TÍTULO 1"),

        link_button("Hinata","Es malo", "https://www.youtube.com/watch?v=AzG9n77SkBU"),
        link_button("Kageyama", "Es bueno", "https://www.youtube.com/watch?v=P6xGAV87ttw"),
        link_button("Tsuki", "Es alto", "https://www.youtube.com/watch?v=8hPJyxlk8_s"),
        link_button("Daichi", "Es mayor", "https://www.youtube.com/watch?v=qjeMc9tBz9c"),


        title("TÍTULO 2"),

        link_button("Hinata","Es malo", "https://www.youtube.com/watch?v=AzG9n77SkBU"),
        link_button("Kageyama", "Es bueno", "https://www.youtube.com/watch?v=P6xGAV87ttw"),
        link_button("Tsuki", "Es alto", "https://www.youtube.com/watch?v=8hPJyxlk8_s"),
        link_button("Daichi", "Es mayor", "https://www.youtube.com/watch?v=qjeMc9tBz9c"),
        width="100%" #hace que los botones ocupen el max_width del center de web1.py

        

    )