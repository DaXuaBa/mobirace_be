from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session

def get_districts_list(db: Session, province: str):
    try:
        connection = db.connection().connection
        cursor = connection.cursor()
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Cannot connect to database.')
    try:
        if province is not None:
            sql_query = "SELECT DISTRICT, NAME FROM mobirace.AREA where NOT AREA.DISTRICT =\"\" AND AREA.PROVINCE = %s AND AREA.PRECINCT =\"\" AND STATUS = 1;"
            cursor.execute(sql_query,(province,))
            result = cursor.fetchall()
            return result
        else: return []
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Execution fail.')
    finally:
        cursor.close()
        connection.close()

def get_provinces_list(db: Session):
    try:
        connection = db.connection().connection
        cursor = connection.cursor()
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Cannot connect to database.')
    try:
        sql_query = "SELECT PROVINCE, NAME FROM mobirace.AREA where AREA.DISTRICT =\"\" AND AREA.PRECINCT =\"\" AND STATUS = 1;"
        cursor.execute(sql_query)
        result = cursor.fetchall()
        return result
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Execution fail.')
    finally:
        cursor.close()
        connection.close()

def get_wards_list(db: Session, province: str, district: str):
    try:
        connection = db.connection().connection
        cursor = connection.cursor()
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Cannot connect to database.')
    try:
        if province is not None and district is not None:
            sql_query = "SELECT PRECINCT, NAME FROM mobirace.AREA where AREA.DISTRICT =%s AND AREA.PROVINCE = %s AND NOT AREA.PRECINCT =\"\" AND STATUS = 1;"
            cursor.execute(sql_query,(district,province))
            result = cursor.fetchall()
            return result
        elif district is None:
            sql_query = "SELECT PRECINCT, NAME FROM mobirace.AREA where AREA.PROVINCE = %s AND NOT AREA.PRECINCT =\"\" AND STATUS = 1;"
            cursor.execute(sql_query,(province,))
            result = cursor.fetchall()
            return result
        elif province is None: return []
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Execution fail.')
    finally:
        cursor.close()
        connection.close()