import flet
from flet import *


class REF_TAMBAH_TUGAS_VIEW:
    LIST_VIEW = Ref[ListView]()

class CONTENT_VIEW:
    LISTVIEW_TENGGAT_TUGAS = Ref[ListView]()
    LISTVIEW_PENTING_TUGAS = Ref[ListView]()
    LISTVIEW_DAFTAR_TUGAS = Ref[ListView]()

class ITEM_CONTROL_VIEW:
    CONTAINER_TAMBAH_TUGAS = Ref[Container]()
    CONTAINER_DAFTAR_TUGAS = Ref[Container]()
    CONTAINER_PENTING_TUGAS = Ref[Container]()
    CONTAINER_TENGGAT_TUGAS = Ref[Container]()
    CONTAINER_HOME = Ref[Container]()
    LISTVIEW_TAMBAH_TUGAS = Ref[ListView]()
    LISTVIEW_DAFTAR_TUGAS = Ref[ListView]()
    LISTVIEW_PENTING_TUGAS = Ref[ListView]()
    LISTVIEW_TENGGAT_TUGAS = Ref[ListView]()
    LISTVIEW_HOME = Ref[ListView]()
    TEXTFIELD_NAMA_TUGAS_TAMBAH_JADWAL = Ref[TextField]()
    TEXTFIELD_DESKRIPSI_TUGAS_TAMBAH_JADWAL = Ref[TextField]()

class GABUNGANVIEW:
    CONTAINER_UTAMA = Ref[Container]()
