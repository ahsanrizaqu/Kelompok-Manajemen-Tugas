import flet 
from flet import *
from frontend.route import Route


class SideBar(UserControl):

    def __init__(self, page):
        super().__init__()
        self.pg = page
        self.width = page.width * 20 / 100

    def build(self):
        self.side_bar_column = Column(
            spacing=10,
            controls=[
                Row(
                    controls=[
                        ElevatedButton(
                            icon=icons.ADD,
                            text='TAMBAH TUGAS',
                            expand=True,
                            on_click=lambda e: Route.switch_page(e, Route.PAGE_TAMBAH_TUGAS, self.pg)
                        )
                    ]
                ),

                Row(
                    controls=[
                        ElevatedButton(
                            icon=icons.BOOK,
                            text='DAFTAR TUGAS',
                            expand=True,
                            on_click=lambda e: Route.switch_page(e, Route.PAGE_DAFTAR_TUGAS, self.pg)
                        )
                    ]
                ),

                Row(
                    controls=[
                        ElevatedButton(
                            icon=icons.STAR,
                            text='PENTING',
                            expand=True,
                            on_click=lambda e: Route.switch_page(e, Route.PAGE_PENTING, self.pg)
                        )
                    ]
                ),

                Row(
                    controls=[
                        ElevatedButton(
                            icon=icons.ALARM,
                            text='TENGGAT',
                            expand=True,
                            # height=40,
                            on_click=lambda e: Route.switch_page(e, Route.PAGE_TENGGAT, self.pg)
                        )
                    ]
                )
            ]
        )

        return Container(
            # height=500,
            margin=margin.only(top=10),
            content=Row(
                spacing=0,
                controls=[
                    Container(
                        expand=True,
                        content=self.side_bar_column
                    ), 
                ]
            ),
        )
    