from server.sql_base.db_manager import base_worker
from server.sql_base.models import Buyer


def create_buyer(buyer: Buyer):
    return base_worker.execute(
        query="INSERT INTO buyers(surname, name, patronymic, telephone) VALUES (?, ?, ?, ?) RETURNING id",
        args=(buyer.surname, buyer.name, buyer.patronymic, buyer.phone))


def get_buyer(buyer_id: int):
    return base_worker.execute(query="SELECT id, surname, name, patronymic, telephone FROM buyers WHERE id = ?",
                               args=(buyer_id,))


def get_all_buyers():
    return base_worker.execute(query="SELECT id, surname, name, patronymic, telephone FROM buyers",
                               many=True)


def update_buyer(buyer_id: int, new_data: Buyer):
    return base_worker.execute(
        query="UPDATE buyers SET (surname, name, patronymic, telephone) = (?, ?, ?, ?) WHERE id=?",
        args=(new_data.surname, new_data.name, new_data.patronymic, new_data.phone, buyer_id))


def delete_buyer(buyer_id: int):
    return base_worker.execute(query="DELETE FROM buyers WHERE id=? ",
                               args=(buyer_id,))
