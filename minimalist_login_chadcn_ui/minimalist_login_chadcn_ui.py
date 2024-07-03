import reflex as rx
from .pages.login_page import index as login_page

global_style = {
    "font_family": "Inter, sans-serif",
    "box_sizing": "border-box"
}

app = rx.App(stylesheets=[
    "https://fonts.googleapis.com/css2?family=Inter:wght@100..900&display=swap"
], style=global_style, theme=rx.theme(
    appearance="light"
))


app.add_page(login_page)
