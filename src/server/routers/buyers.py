import fastapi
from server.sql_base.models import Buyer
from server.resolvers.buyers import create_buyer, get_buyer, get_all_buyers, update_buyer, delete_buyer

buyers_router = fastapi.APIRouter(prefix="/buyers", tags=["Buyers"])


@buyers_router.get("/")
def start_page():
    return ""


@buyers_router.post("/create/")
def new_buyer(buyer: Buyer):
    return create_buyer(buyer)


@buyers_router.get("/get/{buyer_id}")
def search_buyer(buyer_id: int):
    return get_buyer(buyer_id)


@buyers_router.get("/get/")
def search_all_buyers():
    return get_all_buyers()


@buyers_router.put("/update/{buyer_id}")
def upd_buyer(buyer_id: int, new_data: Buyer):
    return update_buyer(buyer_id, new_data)


@buyers_router.delete("/delete/{buyer_id}")
def del_buyer(buyer_id: int):
    return delete_buyer(buyer_id)
