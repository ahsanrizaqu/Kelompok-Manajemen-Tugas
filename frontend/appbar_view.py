import flet 
from flet import *


def appbar_widget(page):
    return AppBar(
            leading=Container(
                content= Text(
                value='Tasking',
                color=colors.WHITE,
                size=20
                ),
                alignment=alignment.center,
                margin=margin.only(left=20)
            ),    
            leading_width=100,
            bgcolor=colors.BLUE_900,
            actions=[
                Container(
                    content=TextField(
                        prefix_icon=icons.SEARCH,
                        label='Cari Tugas Anda',
                        height=40,
                        border_radius=100,
                        bgcolor='white'
                    ),
                    margin=Margin(
                        left=10,
                        right=10,
                        bottom=10,
                        top=10
                    )
                      
                )
            ]
        )
