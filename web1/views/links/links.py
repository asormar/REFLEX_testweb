import reflex as rx
from web1.components.link_button import link_button
from web1.components.title import title

def links() -> rx.Component:
    return rx.vstack(
        title("ABOUT ME"),
        
        link_button("Linkedin",
                    "Explore my academic journey, skills, and projects",
                    "icons/linkedin.png",
                    "https://www.youtube.com/watch?v=AzG9n77SkBU"),

        link_button("Github",
                    "A log of my programming projects and collaborative development",
                    "icons/github.png",
                    "https://www.youtube.com/watch?v=AzG9n77SkBU"),

        link_button("Curriculum",
                    "What I’ve done, what I know, and how I can contribute",
                    "icons/cv.png",
                    "https://www.youtube.com/watch?v=AzG9n77SkBU"),

        width="100%" #hace que los botones ocupen el max_width del center de web1.py

        

    )