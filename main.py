from flet import *
import flet as ft
from frontend.appbar_view import appbar_widget
from frontend.gabungan_view import show_content_merge



def main(page: Page):
    page.appbar = appbar_widget(page)

    page.add(
        show_content_merge(page)
    )
    
    # page.update()

ft.app(target=main)
