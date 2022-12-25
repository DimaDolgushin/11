from server.sql_base.db_manager import base_worker
from server.sql_base.models import Technic


def create_technic(technic: Technic):
    return base_worker.execute(
        query="INSERT INTO technics(manifacture_id, tech_name_id, batch_id, model, warranty, price) "
              "VALUES (?, ?, ?, ?, ?, ?) RETURNING id",
        args=(technic.manifacture_id, technic.tech_name_id, technic.tech_name_id,
              technic.batch_id, technic.model, technic.warranty, technic.price,))


def get_technic(technic_id: int):
    return base_worker.execute(query="SELECT id, manifacture_id, tech_name_id, batch_id, model, warranty, price "
                                     "FROM technics "
                                     "WHERE id = ?",
                               args=(technic_id,))


def get_all_technics():
    return base_worker.execute(query="SELECT id, manifacture_id, tech_name_id, batch_id, model, warranty, price "
                                     "FROM technics",
                               many=True)


def update_technic(technic_id: int, new_data: Technic):
    return base_worker.execute(
        query="UPDATE technics "
              "SET (manifacture_id, tech_name_id, batch_id, model, warranty, price) = (?, ?, ?, ?, ?, ?) "
              "WHERE id=?",
        args=(new_data.manifacture_id, new_data.tech_name_id, new_data.batch_id,
              new_data.model, new_data.warranty, new_data.price, technic_id))


def delete_technic(technic_id: int):
    return base_worker.execute(query="DELETE FROM technics WHERE id=? ",
                               args=(technic_id,))
