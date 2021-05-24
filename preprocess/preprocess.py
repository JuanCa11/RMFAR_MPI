
from preprocess.utils import get_hour_interval, get_month_interval, get_day_of_month_interval, get_day_of_month_interval
from preprocess.settings import FUZZY_SETS,  CLUSTER_FEATURE
from fuzzy_ar.fuzzification import Fuzzification
import pandas as pd
from datetime import datetime


class Preprocess():
    def __init__(self) -> None:
        self._df_barrios_info = pd.read_csv("datasets/barrios_info.csv")
        self._dataset = pd.read_csv('datasets/dataset.csv')
    
    def preprocess_data(self, data):

        date_time = datetime.strptime(data['fecha'], '%Y-%m-%d %H:%M')

        hora_int = get_hour_interval(date_time.hour)
        mes_int = get_month_interval(date_time.month)
        dia_semana_int = get_day_of_month_interval(date_time.weekday())
        dia_mes_int = get_day_of_month_interval(date_time.day)

    
        data_row = self._df_barrios_info[self._df_barrios_info['BARRIOS']==data['barrio']]

        data_row = data_row.drop('BARRIOS', axis=1)
        data_row.insert(0, "MES", date_time.month)
        data_row.insert(0, "HORA_INT", hora_int)
        #data_row.insert(0, "MES_INT",mes_int)
        data_row.insert(0, "DIA_SEMANA_INT", dia_semana_int)
        data_row.insert(0, "DIA_MES_INT", dia_mes_int)
        data_row.insert(0, "GENERO", data['genero'])
        data_row.insert(0, "ACTIVIDAD", data['actividad'])
        data_row.insert(0, "DELITOS", '')
        data_row['SCA_AREA'] = data_row['SCA_AREA'].astype('float64')

        self._dataset = pd.concat([self._dataset, data_row], ignore_index=True)

    def fuzzify_data(self):
        fuzzification = Fuzzification(self._dataset, FUZZY_SETS, CLUSTER_FEATURE)
        fuzzification.fuzzify()
        return fuzzification.fuzzified_data.loc[len(fuzzification.fuzzified_data)-1,:]
