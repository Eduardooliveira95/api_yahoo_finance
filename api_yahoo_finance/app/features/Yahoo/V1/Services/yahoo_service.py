from typing import List

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import date, datetime, timedelta
import yfinance as yf
import warnings
import pandas as pd
from pathlib import Path

from app.features.Yahoo.V1.Models.DTO.IndicadoresAtivo import IndicadoresAtivo
from app.features.Yahoo.V1.Models.Request.DadosUsuarioRequest import DadosUsuarioRequest
from app.features.Yahoo.V1.Models.Response.DadosResponse import DadosResponse
from app.features.Yahoo.V1.Models.DTO.DadosAtivos import DadosAtivos

warnings.filterwarnings("ignore", category=FutureWarning)


class YahooService:


    def buscaDadosAtivos(self, dados : DadosUsuarioRequest, null=None) -> List[DadosAtivos]:
        dadosRetorno: List[DadosAtivos] = []
        for ativo in dados.ativos:
            dadosAtivo = DadosAtivos
            if dados.isBrasil:
                aapl = yf.Ticker(ativo.nomeAtivo + '.SA').history(period=dados.periodo + 'mo')
            else :
                aapl = yf.Ticker(ativo.nomeAtivo).history(period=dados.periodo+'mo')
            for index, row in aapl.iterrows():
                dadosAtivo = DadosAtivos(
                    data=index.strftime('%Y-%m-%d'),
                    abertura=row['Open'],
                    alta=row['High'],
                    baixa=row['Low'],
                    fechamento=row['Close'],
                    volume=row['Volume'],
                    dividendos=row['Dividends'],
                    divisaoDeAcoes=row['Stock Splits']
                )
                dadosRetorno.append(dadosAtivo)
            return dadosRetorno


    def buscarDadosFechamentoAtivos(self, dados: DadosUsuarioRequest, null=None, skip: int = 0, limit: int = 100) -> \
        List[DadosResponse]:
        lista_de_ativos = dados.ativos
        periodo: str = dados.periodo
        dados: List[DadosResponse] = []
        for ativo in lista_de_ativos:
            dadosBolsa = DadosResponse(nome=ativo.nomeAtivo, indicadores=[])
            aapl = yf.Ticker(ativo.nomeAtivo).history(period=periodo+'mo')
            fechamentosBolsa = aapl['Close'].values
            dataAcao = list(aapl['Close'].index)
            dadosBolsa.nome = ativo.nomeAtivo
            for valor, data in zip(fechamentosBolsa, dataAcao):
                indicador = IndicadoresAtivo(data=data, valorFechamentoDia=valor)
                dadosBolsa.indicadores.append(indicador)
            dados.append(dadosBolsa)
        return dados

    def buscarDadosFechamentoAtivosExcel(self, dados, skip, limit) -> str:
        buscarDados = self.buscarDadosFechamentoAtivos(dados)
        df = pd.DataFrame(buscarDados)
        dadosFechamentoBolsa = Path.home() / "Downloads" / "dados_fechamento_bolsa.xlsx"
        df.to_excel(dadosFechamentoBolsa, index=False)
        return str(dadosFechamentoBolsa)
