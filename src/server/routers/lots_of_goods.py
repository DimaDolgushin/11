import fastapi
from server.sql_base.models import LotOfGood
from server.resolvers.lots_of_goods import create_lot_of_good, get_all_lot_of_goods, get_lot_of_good, update_lot_of_good, delete_lot_of_good

lots_of_goods_router = fastapi.APIRouter(prefix="/lot_of_goods", tags=["Lot_of_goods"])


@lots_of_goods_router.get("/")
def start_page():
    return ""


@lots_of_goods_router.post("/create/")
def new_lot_of_good(lot_of_good: LotOfGood):
    return create_lot_of_good(lot_of_good)


@lots_of_goods_router.get("/get/{lot_of_good_id}")
def search_lot_of_good(lot_of_good_id: int):
    return get_lot_of_good(lot_of_good_id)


@lots_of_goods_router.get("/get/")
def search_all_lot_of_goods():
    return get_all_lot_of_goods()


@lots_of_goods_router.put("/update/{lot_of_good_id}")
def upd_lot_of_good(lot_of_good_id: int, new_data: LotOfGood):
    return update_lot_of_good(lot_of_good_id, new_data)


@lots_of_goods_router.delete("/delete/{lot_of_good_id}")
def del_lot_of_good(lot_of_good_id: int):
    return delete_lot_of_good(lot_of_good_id)
