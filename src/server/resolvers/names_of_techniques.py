from server.sql_base.db_manager import base_worker
from server.sql_base.models import NameTechnic


def create_name_technic(name_tech: NameTechnic):
    return base_worker.execute(
        query="INSERT INTO names_of_the_technique(video_card, cooler, motherboard) VALUES (?, ?, ?) RETURNING id",
        args=(name_tech.video_card, name_tech.cooler, name_tech.motherboard))


def get_name_technic(name_tech_id: int):
    return base_worker.execute(
        query="SELECT id, video_card, cooler, motherboard FROM names_of_the_technique WHERE id = ?",
        args=(name_tech_id,))


def get_all_name_technics():
    return base_worker.execute(query="SELECT id, video_card, cooler, motherboard FROM names_of_the_technique",
                               many=True)


def update_name_technic(name_tech_id: int, new_data: NameTechnic):
    return base_worker.execute(
        query="UPDATE names_of_the_technique SET (video_card, cooler, motherboard) = (?, ?, ?) WHERE id=?",
        args=(new_data.video_card, new_data.cooler, new_data.motherboard, name_tech_id))


def delete_name_technic(name_tech_id: int):
    return base_worker.execute(query="DELETE FROM names_of_the_technique WHERE id=? ",
                               args=(name_tech_id,))
