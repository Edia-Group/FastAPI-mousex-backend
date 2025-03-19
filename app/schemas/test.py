from pydantic import BaseModel, ValidationError
from datetime import datetime
from typing import Optional, Dict
from app.schemas.domande import Pagina

class TestBase(BaseModel):
    idTest: int
    dataOraInizio: Optional[datetime] = None
    tipo: str = 'Normale'
    inSequenza: bool = False
    nrGruppo: int = 0
    secondiRitardo: int = 5
    utente_id: int
    dataOraFine: Optional[datetime] = None
    dataOraInserimento: datetime
    nrTest: int = 0
    malusF5: bool = False
    numeroErrori: int = 0
    tempo_impiegato: float 
    is_validate: bool 

    class Config:
        from_attributes = True

class TestResponse(TestBase):
    pass

class TestCreate(BaseModel):
    utente_id: int


class TestCreateRequest(BaseModel):
    tipo: str
    secondi_ritardo: int = 5
    group_id: Optional[int] = None

class FormattedTest(BaseModel):
    formattedTest: Dict[str, Pagina]