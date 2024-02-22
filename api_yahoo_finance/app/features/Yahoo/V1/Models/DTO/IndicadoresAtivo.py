from datetime import datetime
from pydantic import BaseModel

class IndicadoresAtivo(BaseModel):
    data: datetime
    valorFechamentoDia: float