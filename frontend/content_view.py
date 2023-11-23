from flet import *
import flet
from frontend.item_control_view import *
from reference.ref import *
from backend.database import list_of_item


##############3 TAMBAH TUGAS PAGE
def page_tambah_tugas():
    Container(
        ref=ITEM_CONTROL_VIEW.CONTAINER_TAMBAH_TUGAS,
            content=Tambah_ItemView(),
        offset=transform.Offset(0,0),
        animate_offset=animation.Animation(500, AnimationCurve.DECELERATE),
        expand=True,
        bgcolor=colors.BLUE_50,
    )

    # page.add(ITEM_CONTROL_VIEW.CONTAINER_TAMBAH_TUGAS.current)

    return ITEM_CONTROL_VIEW.CONTAINER_TAMBAH_TUGAS.current
    

def page_daftar_tugas():
    Container(
        ref=ITEM_CONTROL_VIEW.CONTAINER_DAFTAR_TUGAS,
        content=ListView(
            ref=CONTENT_VIEW.LISTVIEW_DAFTAR_TUGAS,
            controls=[
                DaftarTugas_ItemView(x.nama_tugas, x.deskripsi_tugas) for x in list_of_item
            ]
        ),
        offset=transform.Offset(0,0),
        animate_offset=animation.Animation(500, AnimationCurve.DECELERATE),
        expand=True,
        bgcolor=colors.BLUE_50,
    )

    # page.add(ITEM_CONTROL_VIEW.CONTAINER_DAFTAR_TUGAS.current)

    return ITEM_CONTROL_VIEW.CONTAINER_DAFTAR_TUGAS.current

def page_penting():
    Container(
        ref=ITEM_CONTROL_VIEW.CONTAINER_PENTING_TUGAS,
            content=ListView(
            ref=CONTENT_VIEW.LISTVIEW_PENTING_TUGAS,
            controls=[
                Penting_ItemView(x.nama_tugas, x.deskripsi_tugas, w + 1) for w, x in enumerate(list_of_item)
            ]
        ),
        offset=transform.Offset(0,0),
        animate_offset=animation.Animation(500, AnimationCurve.DECELERATE),
        expand=True,
        bgcolor=colors.BLUE_50,
    )

    # page.add(ITEM_CONTROL_VIEW.CONTAINER_PENTING_TUGAS.current)

    return ITEM_CONTROL_VIEW.CONTAINER_PENTING_TUGAS.current

def page_tenggat():
    Container(
        ref=ITEM_CONTROL_VIEW.CONTAINER_TENGGAT_TUGAS,
        content=ListView(
            ref=CONTENT_VIEW.LISTVIEW_TENGGAT_TUGAS,
            controls=[
                Tenggat_ItemView(x.nama_tugas, x.deskripsi_tugas) for x in list_of_item
            ]
        ),
        offset=transform.Offset(0,0),
        animate_offset=animation.Animation(500, AnimationCurve.DECELERATE),
        expand=True,
        bgcolor=colors.BLUE_50,
    )

    # page.add(ITEM_CONTROL_VIEW.CONTAINER_TENGGAT_TUGAS.current)

    return ITEM_CONTROL_VIEW.CONTAINER_TENGGAT_TUGAS.current


def page_home():
    Container(
        ref=ITEM_CONTROL_VIEW.CONTAINER_HOME,
        content=ListView(
        expand=True,
        ref=ITEM_CONTROL_VIEW.LISTVIEW_HOME,
        ),
        offset=transform.Offset(0,0),
        animate_offset=animation.Animation(500, AnimationCurve.DECELERATE),
        bgcolor=colors.GREY_300
    )

    # page.add(ITEM_CONTROL_VIEW.CONTAINER_HOME.current)

    return ITEM_CONTROL_VIEW.CONTAINER_HOME.current
