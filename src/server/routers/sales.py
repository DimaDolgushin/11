import fastapi
from server.sql_base.models import Sale
from server.resolvers.sales import create_sale, get_sale, get_all_sales, update_sale, delete_sale

sales_router = fastapi.APIRouter(prefix="/sales", tags=["Sales"])


@sales_router.get("/")
def start_page():
    return ""


@sales_router.post("/create/")
def new_sale(sale: Sale):
    return create_sale(sale)


@sales_router.get("/get/{sale_id}")
def search_sale(sale_id: int):
    return get_sale(sale_id)


@sales_router.get("/get/")
def search_all_sales():
    return get_all_sales()


@sales_router.put("/update/{sale_id}")
def upd_sale(sale_id: int, new_data: Sale):
    return update_sale(sale_id, new_data)


@sales_router.delete("/delete/{sale_id}")
def del_sale(sale_id: int):
    return delete_sale(sale_id)
