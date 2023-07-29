from fastapi import APIRouter
from config.db import connection
from schemas.Tennant import Tennant
import methods.TennantMethods as TennantMethods

APITennant = APIRouter()

@APITennant.get('/tennant')
def get_tennants():
    cur = connection.cursor()
    cur.execute('SELECT * FROM tennant')
    result = cur.fetchall()
    print(result)
    return result

@APITennant.post('/tennant')
def create_tennant(tennant: Tennant):
    new_tennant = {
        "tennantname": tennant.tennantname,
        "tennantlastname": tennant.tennantlastname,
        "tennantbirthdate": tennant.tennantbirthdate,
        "tennantusername": tennant.tennantusername,
        "tennantpassword": tennant.tennantpassword,
        "tennantemail": tennant.tennantemail,
        "tennantscore": tennant.tennantscore
    }
    if TennantMethods.validate_username(tennant.tennantusername) == True:
        new_tennant["tennantid"] = TennantMethods.create_id()
        cur = connection.cursor()
        cur.execute('INSERT INTO tennant (tennantid, tennantname, tennatlastname, tennantbirthdate, tennantusername, tennantpassword, tennantemail, tennnantscore) VALUES (%(tennantid)s, %(tennantname)s, %(tennantlastname)s, %(tennantbirthdate)s, %(tennantusername)s, %(tennantpassword)s, %(tennantemail)s, %(tennantscore)s)', new_tennant)
        connection.commit()
        return "Tennant created successfully"
    else:
        return "Username already exists"
    
@APITennant.get('/tennant/{tennantusername}')
def validate_tennant_user(tennantusername: str):
    cur = connection.cursor()
    cur.execute('SELECT tennantusername, tennantpassword FROM tennant WHERE tennantusername = %s', (tennantusername,))
    result = cur.fetchall()
    return result


    