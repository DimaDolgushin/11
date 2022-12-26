from server.sql_base.db_manager import base_worker
from router import routers
from fastapi import FastAPI
import uvicorn


app = FastAPI()

[app.include_router(router) for router in routers]


if __name__ == "__main__":
    base_worker.create_base("../sql/dolgushin_tables.sql")
    uvicorn.run("start_server:app", reload=True, host="127.0.0.1", port=8000)
