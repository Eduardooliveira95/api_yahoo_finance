from fastapi import APIRouter, HTTPException
from typing import List
from app.features.Yahoo.V1.Models.Request.DadosUsuarioRequest import DadosUsuarioRequest
from app.features.Yahoo.V1.Models.Response.DadosResponse import DadosResponse
from app.features.Yahoo.V1.Services.yahoo_service import YahooService


router = APIRouter()
yahoo_service = YahooService()

@router.post("/dados", response_model=List[DadosResponse])
async def buscar_dados(dados: DadosUsuarioRequest, skip: int = 0, limit: int = 10):
    return yahoo_service.chamarAPiYahoo(dados, skip=skip, limit=limit)

#@router.get("/users/", response_model=List[UserUpdate])
#async def read_users(skip: int = 0, limit: int = 10):
#    return user_service.get_users(skip=skip, limit=limit)