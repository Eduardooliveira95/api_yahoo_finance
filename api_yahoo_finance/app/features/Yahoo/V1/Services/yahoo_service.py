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
            else:
                aapl = yf.Ticker(ativo.nomeAtivo).history(period=dados.periodo+'mo')
            for index, row in aapl.iterrows():
                dadosAtivo = DadosAtivos(
                    nomeAtivo=ativo.nomeAtivo,
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
        dadosBrutos = self.buscaDadosAtivos(dados)
        dadosRetorno: List[DadosResponse] = []
        for dadosBusca in dadosBrutos:
            indicador = IndicadoresAtivo(data=dadosBusca.data, valorFechamentoDia=dadosBusca.fechamento)
            dadosBolsaTeste = DadosResponse(nome=dadosBusca.nomeAtivo, indicadores=[indicador])
            dadosRetorno.append(dadosBolsaTeste)
        return dadosRetorno

    def buscarDadosFechamentoAtivosExcel(self, dados, skip, limit) -> str:
        buscarDados = self.buscarDadosFechamentoAtivos(dados)
        datas = []
        fechamentos = []
        for dados in buscarDados:
            for indicador in dados.indicadores:
                datas.append(indicador.data)
                fechamentos.append(indicador.valorFechamentoDia)

        df = pd.DataFrame({"Datas": datas[0], "Fechamentos": fechamentos})
        df = df.set_index("Datas", drop=True)

        dadosFechamentoBolsa = Path.home() / "Downloads" / "dados_fechamento_bolsa.xlsx"
        df.to_excel(dadosFechamentoBolsa, index=False)
        return str(dadosFechamentoBolsa)
