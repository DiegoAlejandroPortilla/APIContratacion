from typing import Optional
from pydantic import BaseModel

class Tennant(BaseModel):
    tennantid:str
    tennantname:str
    tennantlastname:str
    tennantbirthdate:str
    tennantusername:str
    tennantpassword:str
    tennantemail:str
    tennantscore:float

    