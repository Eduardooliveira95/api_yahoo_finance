from typing import List
from pydantic import BaseModel

class Ativos(BaseModel):
    nomeAtivo : str
    categoriaAtivo : str
    quantidadeAtivo : int