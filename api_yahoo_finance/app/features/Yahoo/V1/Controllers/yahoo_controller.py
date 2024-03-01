from pathlib import Path

from fastapi import APIRouter, HTTPException
from typing import List
from fastapi.responses import FileResponse
from app.features.Yahoo.V1.Models.Request.DadosUsuarioRequest import DadosUsuarioRequest
from app.features.Yahoo.V1.Models.Response.DadosResponse import DadosResponse
from app.features.Yahoo.V1.Services.yahoo_service import YahooService

router = APIRouter()
yahoo_service = YahooService()

@router.get("/dadosFechamento", response_model=List[DadosResponse])
async def buscar_dados(dados: DadosUsuarioRequest, skip: int = 0, limit: int = 10):
    return yahoo_service.buscarDadosFechamentoAtivos(dados, skip=skip, limit=limit)

@router.get("/dadosFechamento/excel")
async def buscar_dados_excel(dados : DadosUsuarioRequest, skip : int = 0, limit : int = 10):
    excel = yahoo_service.buscarDadosFechamentoAtivosExcel(dados, skip=skip, limit=limit)
    return FileResponse(path=excel, media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

@router.get("/dadosFechamento/teste")
async def teste(dados : DadosUsuarioRequest):
    return yahoo_service.buscaDadosAtivos(dados)