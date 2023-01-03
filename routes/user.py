import asyncio

from fastapi import FastAPI
from typing import Optional
from fastapi import APIRouter
from config.db import db_conn
from config.db import cursor
from models.user import Student
from typing import Dict
import time

from schemas.user import users_entity, user_entity

use = APIRouter()


@use.post("/student")
async def add_data(request_data: Student):
    try:

        value = (request_data.name, request_data.mark)
        statement = "insert into register (name,mark) values (%s,%s)"
        print(statement)
        cursor.execute(statement, value)
        db_conn.commit()
        return {"msg": "data added successfully"}
    except Exception as e:
        return print(f"error :  {e}")


@use.get("/student")
async def find_all():
    try:
        print("find all")
        statement = "select * from register"
        cursor.execute(statement)
        return cursor.fetchall()
    except Exception as e:
        return {f"error : {e}"}


@use.get("/one_student")
async def find_one(id: int):
    try:
        print("find one")
        data = id
        statement = "select * from register where roll_no =%s"
        cursor.execute(statement, [data])
        return cursor.fetchone()
    except Exception as e:
        return {f"error : {e}"}


@use.put("/student")
async def update_mark(id: int, mark: int):
    try:
        data = mark
        statement = "update register set mark = %s where roll_no = %s"
        cursor.execute(statement, [data, id])
        db_conn.commit()
        return {f"mark updated successfully {id}"}
    except Exception as e:
        return {f"error : {e}"}


@use.delete("/student")
async def delete_data(id: int):
    try:
        statement = "delete from register where roll_no = %s"
        print([id])
        cursor.execute(statement, [id])
        db_conn.commit()
        return {f"data deleted successfully"}
    except Exception as e:
        return {f"error : {e}"}
