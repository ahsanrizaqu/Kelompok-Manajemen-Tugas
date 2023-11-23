from datetime import datetime
from flet import *
import flet
from model.model import Tugas
from reference.ref import *
from backend.database import list_of_item

################ TAMBAH TUGAS ITEM
class Tambah_ItemView(UserControl):
    def build(self):
        return Container(
            margin=margin.all(10),
            content=Row(
            controls=[
                TextField(
                    ref=ITEM_CONTROL_VIEW.TEXTFIELD_NAMA_TUGAS_TAMBAH_JADWAL,
                    hint_text='Nama Tugas',
                    border_radius=70,
                    bgcolor='white',
                ),

                TextField(
                    ref=ITEM_CONTROL_VIEW.TEXTFIELD_DESKRIPSI_TUGAS_TAMBAH_JADWAL,
                    hint_text='Deskripsi Tugas Anda',
                    border_radius=50,
                    bgcolor='white',
                ),

                IconButton(
                    icon=icons.ADD,
                    tooltip='Tambahkan ke DB',
                    on_click=lambda e: self.insert_data_to_db(
                        e,
                        ITEM_CONTROL_VIEW.TEXTFIELD_NAMA_TUGAS_TAMBAH_JADWAL.current.value,
                        ITEM_CONTROL_VIEW.TEXTFIELD_DESKRIPSI_TUGAS_TAMBAH_JADWAL.current.value
                    )
                )
            ]
        ),
        expand=True,
        offset=transform.Offset(0,0),
        animate_offset=animation.Animation(500, AnimationCurve.DECELERATE),
        bgcolor=colors.BLUE_50,
    )

    def insert_data_to_db(self, e, nama_tugas, deskripsi_tugas):
        list_of_item.append(
            Tugas(nama_tugas, deskripsi_tugas)
        )
        print("DATA BERHASIL MASUK KE DATABASE")
        print(f'ISI : {list_of_item}')

        self.clear_text_field()
        self.show_daftar_tugas()
        self.show_penting_tugas()
        self.show_tenggat_tugas()

    def clear_text_field(self):
        ITEM_CONTROL_VIEW.TEXTFIELD_NAMA_TUGAS_TAMBAH_JADWAL.current.value = ""
        ITEM_CONTROL_VIEW.TEXTFIELD_DESKRIPSI_TUGAS_TAMBAH_JADWAL.current.value = ""

        ITEM_CONTROL_VIEW.TEXTFIELD_NAMA_TUGAS_TAMBAH_JADWAL.current.update()
        ITEM_CONTROL_VIEW.TEXTFIELD_DESKRIPSI_TUGAS_TAMBAH_JADWAL.current.update()

    def show_daftar_tugas(self):
        CONTENT_VIEW.LISTVIEW_DAFTAR_TUGAS.current.controls = [DaftarTugas_ItemView(x.nama_tugas, x.deskripsi_tugas) for x in list_of_item]
        CONTENT_VIEW.LISTVIEW_DAFTAR_TUGAS.current.update()

    def show_penting_tugas(self):
        CONTENT_VIEW.LISTVIEW_PENTING_TUGAS.current.controls = [Penting_ItemView(x.nama_tugas, x.deskripsi_tugas, w + 1) for w, x in enumerate(list_of_item)]
        CONTENT_VIEW.LISTVIEW_PENTING_TUGAS.current.update()

    def show_tenggat_tugas(self):
        CONTENT_VIEW.LISTVIEW_TENGGAT_TUGAS.current.controls = [Tenggat_ItemView(x.nama_tugas, x.deskripsi_tugas) for x in list_of_item]
        CONTENT_VIEW.LISTVIEW_TENGGAT_TUGAS.current.update()


################### DAFTAR TUGAS
class DaftarTugas_ItemView(UserControl):
    def __init__(self, nama_tugas, deskripsi_tugas):
        super().__init__()
        self.nama_tugas = nama_tugas
        self.deskripsi_tugas = deskripsi_tugas
        

    def build(self):
        return Container(
                content=Row(
                    controls=[
                        Text(f'\t\t{self.nama_tugas[0]}\t\t:', weight=FontWeight.BOLD),
                        Text(f'\t{self.deskripsi_tugas}', weight=FontWeight.BOLD)
                    ]
                ),
                border_radius=100,
        offset=transform.Offset(0,0),
        animate_offset=animation.Animation(500, AnimationCurve.DECELERATE),
        expand=True,
        bgcolor=colors.WHITE,
        margin=margin.only(left=10, top=10),
        height=40
    )



############## PENTING TUGAS
class Penting_ItemView(UserControl):
    def __init__(self, nama_tugas, deskripsi_tugas, nomor):
        super().__init__()
        self.nama_tugas = nama_tugas
        self.deskripsi_tugas = deskripsi_tugas
        self.nomor = nomor
    

    def build(self):
        return Container(
                content=Row(
                    controls=[
                        Text(f'\t\t{self.nama_tugas[0]}\t:', weight=FontWeight.BOLD),
                        Text(f'\t{self.deskripsi_tugas}\t\t\t-->', weight=FontWeight.BOLD),
                        Text(f'\tTugas penting ke {self.nomor}', weight=FontWeight.BOLD)
                    ]
                ),
                border_radius=100,
        offset=transform.Offset(0,0),
        animate_offset=animation.Animation(500, AnimationCurve.DECELERATE),
        expand=True,
        bgcolor=colors.WHITE,
        margin=margin.only(left=10, top=10),
        height=40
    )
   

############### TENGGAT TUGAS
class Tenggat_ItemView(UserControl):
    def __init__(self, nama_tugas, deskripsi_tugas):
        super().__init__()
        self.nama_tugas = nama_tugas
        self.deskripsi_tugas = deskripsi_tugas

    def build(self):
        return Container(
                content=Row(
                    controls=[
                        Text(f'\t\t{self.nama_tugas[0]}\t\t:', weight=FontWeight.BOLD),
                        Text(f'\t{self.deskripsi_tugas}\t\t\t-->', weight=FontWeight.BOLD),
                        Text(f'\ttenggat tangal {datetime.now().date()}', weight=FontWeight.BOLD)
                    ]
                ),
                border_radius=100,
        offset=transform.Offset(0,0),
        animate_offset=animation.Animation(500, AnimationCurve.DECELERATE),
        expand=True,
        bgcolor=colors.WHITE,
        margin=margin.only(left=10, top=10),
        height=40
    )
   