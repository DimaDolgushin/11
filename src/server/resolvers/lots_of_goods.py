from server.sql_base.db_manager import base_worker
from server.sql_base.models import LotOfGood


def create_lot_of_good(lot_of_good: LotOfGood):
    return base_worker.execute(query="INSERT INTO lots_of_goods(supplier_id, time_date) VALUES (?, ?) RETURNING id",
                               args=(lot_of_good.supplier_id, lot_of_good.time_date))


def get_lot_of_good(lot_of_good_id: int):
    return base_worker.execute(query="SELECT id, supplier_id, time_date FROM lots_of_goods WHERE id = ?",
                               args=(lot_of_good_id,))


def get_all_lot_of_goods():
    return base_worker.execute(query="SELECT id, supplier_id, time_date FROM lots_of_goods",
                               many=True)


def update_lot_of_good(lot_of_good_id: int, new_data: LotOfGood):
    return base_worker.execute(query="UPDATE lots_of_goods SET (supplier_id, time_date) = (?, ?) WHERE id=?",
                               args=(new_data.supplier_id, new_data.time_date, lot_of_good_id))


def delete_lot_of_good(lot_of_good_id: int):
    return base_worker.execute(query="DELETE FROM lots_of_goods WHERE id=? ",
                               args=(lot_of_good_id,))
