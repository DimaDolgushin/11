from server.sql_base.db_manager import base_worker
from server.sql_base.models import Sale


def create_sale(sale: Sale):
    return base_worker.execute(
        query="INSERT INTO sales(account_id, tech_id, quantity, discount) VALUES (?, ?, ?, ?) RETURNING id",
        args=(sale.account_id, sale.tech_id, sale.quantity, sale.discount,))


def get_sale(sale_id: int):
    return base_worker.execute(query="SELECT id, account_id, tech_id, quantity, discount FROM sales WHERE id = ?",
                               args=(sale_id,))


def get_all_sales():
    return base_worker.execute(query="SELECT id, account_id, tech_id, quantity, discount FROM sales",
                               many=True)


def update_sale(sale_id: int, new_data: Sale):
    return base_worker.execute(
        query="UPDATE sales SET (account_id, tech_id, quantity, discount) = (?, ?, ?, ?) WHERE id=?",
        args=(new_data.account_id, new_data.tech_id, new_data.quantity, new_data.discount, sale_id))


def delete_sale(sales_id: int):
    return base_worker.execute(query="DELETE FROM sales WHERE id=? ",
                               args=(sales_id,))
