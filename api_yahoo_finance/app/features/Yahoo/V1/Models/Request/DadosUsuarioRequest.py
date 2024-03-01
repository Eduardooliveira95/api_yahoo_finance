from typing import List
from pydantic import BaseModel

from app.features.Yahoo.V1.Models.DTO.Ativos import Ativos


class DadosUsuarioRequest(BaseModel):
    nomeUsuario: str
    emailUsuario: str
    periodo: str
    isBrasil: bool
    ativos: List[Ativos]
