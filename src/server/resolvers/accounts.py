from server.sql_base.db_manager import base_worker
from server.sql_base.models import Account


def create_account(account: Account):
    return base_worker.execute(
        query="INSERT INTO accounts(buyer_id, discount, date_time, amount) VALUES (?, ?, ?, ?) RETURNING id",
        args=(account.buyer_id, account.discount, account.discount, account.amount))


def get_account(account_id: int):
    return base_worker.execute(query="SELECT id, buyer_id, discount, date_time, amount FROM accounts WHERE id = ?",
                               args=(account_id,))


def get_all_accounts():
    return base_worker.execute(query="SELECT id, buyer_id, discount, date_time, amount FROM accounts",
                               many=True)


def update_account(account_id: int, new_data: Account):
    return base_worker.execute(
        query="UPDATE accounts SET (buyer_id, discount, date_time, amount) = (?, ?, ?, ?) WHERE id=?",
        args=(new_data.buyer_id, new_data.discount, new_data.date_time, new_data.amount, account_id))


def delete_account(account_id: int):
    return base_worker.execute(query="DELETE FROM accounts WHERE id=? ",
                               args=(account_id,))
