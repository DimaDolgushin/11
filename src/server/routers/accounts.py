import fastapi
from server.sql_base.models import Account
from server.resolvers.accounts import create_account, get_account, get_all_accounts, update_account, delete_account

accounts_router = fastapi.APIRouter(prefix="/accounts", tags=["Accounts"])


@accounts_router.get("/")
def start_page():
    return ""


@accounts_router.post("/create/")
def new_account(account: Account):
    return create_account(account)


@accounts_router.get("/get/{account_id}")
def search_account(account_id: int):
    return get_account(account_id)


@accounts_router.get("/get/")
def search_all_accounts():
    return get_all_accounts()


@accounts_router.put("/update/{account_id}")
def upd_account(account_id: int, new_data: Account):
    return update_account(account_id, new_data)


@accounts_router.delete("/delete/{account_id}")
def del_account(account_id: int):
    return delete_account(account_id)
