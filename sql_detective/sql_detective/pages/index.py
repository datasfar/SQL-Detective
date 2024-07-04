import reflex as rx

from sql_detective.components.header import header
from sql_detective.components.console_input import console_input

from sql_detective.views.main_screen import main_creen

def index():
    return rx.container(
        rx.theme_panel(default_open=False),
        header(),
        main_creen(),
        console_input()
    )