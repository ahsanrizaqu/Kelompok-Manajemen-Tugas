from flet import *
import flet
from frontend.sidebar_view import SideBar
from frontend.content_view import *
from reference.ref import *

def show_content_merge(page):
    return Container(
        ref=GABUNGANVIEW.CONTAINER_UTAMA,
        data=page,
        height=page.height,
        content=Row(
            controls=[
                SideBar(
                    page
                ),
                Container(
                    margin=margin.only(top=10),
                    expand=True,
                    content=Stack(
                        controls=[
                            # page_tenggat(),
                            # page_penting(),
                            # page_daftar_tugas(),
                            # page_tambah_tugas(),
                            # page_home()
                            
                            ITEM_CONTROL_VIEW.CONTAINER_TENGGAT_TUGAS.current,
                            ITEM_CONTROL_VIEW.CONTAINER_PENTING_TUGAS.current,
                            ITEM_CONTROL_VIEW.CONTAINER_DAFTAR_TUGAS.current,
                            ITEM_CONTROL_VIEW.CONTAINER_TAMBAH_TUGAS.current,
                            ITEM_CONTROL_VIEW.CONTAINER_HOME.current
                        ]
                    )
                )
            ]
        ),
    )
