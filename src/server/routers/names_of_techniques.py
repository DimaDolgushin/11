import fastapi
from server.sql_base.models import NameTechnic
from server.resolvers.names_of_techniques import create_name_technic, get_name_technic, get_all_name_technics, update_name_technic, delete_name_technic

name_technics_router = fastapi.APIRouter(prefix="/technics/names", tags=["TechnicsNames"])


@name_technics_router.get("/")
def start_page():
    return ""


@name_technics_router.post("/create/")
def new_name_technic(name_technic: NameTechnic):
    return create_name_technic(name_technic)


@name_technics_router.get("/get/{name_technic_id}")
def search_name_technic(name_technic_id: int):
    return get_name_technic(name_technic_id)


@name_technics_router.get("/get/")
def search_all_name_technics():
    return get_all_name_technics()


@name_technics_router.put("/update/{name_technic_id}")
def upd_name_technic(name_technic_id: int, new_data: NameTechnic):
    return update_name_technic(name_technic_id, new_data)


@name_technics_router.delete("/delete/{name_technic_id}")
def del_name_technic(name_technic_id: int):
    return delete_name_technic(name_technic_id)
