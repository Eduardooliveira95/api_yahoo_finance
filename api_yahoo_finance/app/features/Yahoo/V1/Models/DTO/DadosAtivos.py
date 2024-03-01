from datetime import datetime
from typing import List

from DateTime import DateTime
from pydantic import BaseModel


class DadosAtivos(BaseModel):
    nomeAtivo: str
    data: datetime
    abertura: float
    alta: float
    baixa: float
    fechamento: float
    volume: float
    dividendos: float
    divisaoDeAcoes: float
