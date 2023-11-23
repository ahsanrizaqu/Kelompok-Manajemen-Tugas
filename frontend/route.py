from frontend.content_view import *
from reference.ref import *

class Route:
    PAGE_TAMBAH_TUGAS = '/page_tambah_tugas'
    PAGE_DAFTAR_TUGAS = '/page_daftar_tugas'
    PAGE_PENTING = '/page_penting'
    PAGE_TENGGAT = '/page_tenggat'
    PAGE_HOME = '/page_home'

    # # SWITCH_CONTROL = {
    # #     PAGE_TAMBAH_TUGAS:ITEM_CONTROL_VIEW.CONTAINER_TAMBAH_TUGAS.current,
    # #     PAGE_DAFTAR_TUGAS:ITEM_CONTROL_VIEW.CONTAINER_DAFTAR_TUGAS.current,
    # #     PAGE_PENTING:ITEM_CONTROL_VIEW.CONTAINER_PENTING_TUGAS.current,
    # #     PAGE_TENGGAT:ITEM_CONTROL_VIEW.CONTAINER_TENGGAT_TUGAS.current,
    # #     PAGE_HOME:ITEM_CONTROL_VIEW.CONTAINER_HOME.current
    # # }

    SWITCH_CONTROL = {
        PAGE_TAMBAH_TUGAS:page_tambah_tugas(),
        PAGE_DAFTAR_TUGAS:page_daftar_tugas(),
        PAGE_PENTING:page_penting(),
        PAGE_TENGGAT:page_tenggat(),
        PAGE_HOME:page_home()
    }


    @staticmethod
    def switch_page(e, point, pg):
        print(point)
        
        for page in Route.SWITCH_CONTROL:     # for page in self.switch_control():
            print(f'page: {page}')

            if Route.SWITCH_CONTROL[page] is not None:
                Route.PAGE = pg
                Route.SWITCH_CONTROL[page].offset.x = 2
                Route.SWITCH_CONTROL[page].update()


        Route.SWITCH_CONTROL[point].offset.x = 0
        Route.SWITCH_CONTROL[point].data = pg
        Route.SWITCH_CONTROL[point].update()
