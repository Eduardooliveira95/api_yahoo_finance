from datetime import datetime
from typing import List
from pydantic import BaseModel

from app.features.Yahoo.V1.Models.DTO.IndicadoresAtivo import IndicadoresAtivo


class DadosResponse(BaseModel):
    nome: str
    indicadores: List[IndicadoresAtivo]
