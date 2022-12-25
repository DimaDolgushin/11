import fastapi
from server.sql_base.models import Technic
from server.resolvers.technics import create_technic, get_technic, get_all_technics, delete_technic, update_technic

technics_router = fastapi.APIRouter(prefix="/technics", tags=["Technics"])


@technics_router.get("/")
def start_page():
    return ""


@technics_router.post("/create/")
def new_technic(technic: Technic):
    return create_technic(technic)


@technics_router.get("/get/{technic_id}")
def search_technic(technic_id: int):
    return get_technic(technic_id)


@technics_router.get("/get/")
def search_all_technics():
    return get_all_technics()


@technics_router.put("/update/{technic_id}")
def upd_technic(technic_id: int, new_data: Technic):
    return update_technic(technic_id, new_data)


@technics_router.delete("/delete/{technic_id}")
def del_technic(technic_id: int):
    return delete_technic(technic_id)
