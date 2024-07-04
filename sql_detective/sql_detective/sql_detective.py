import reflex as rx

# Imports pages
from sql_detective.pages.index import index


# Imports styles
import sql_detective.styles.styles as styles

app = rx.App(
    theme=rx.theme(
        appearance="dark", has_background=True, radius="none", accent_color="orange", gray_color="slate"
    ),
    stylesheets=styles.STYLESHEETS,
    style=styles.MAIN_STYLES
)


app.add_page(index)