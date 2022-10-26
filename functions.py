import os
import errno

class ProcesarData:

    def __int__(self):
        try:
            os.mkdir('data')
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
        try:
            os.mkdir('output/images')
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise


    def mes_to_month(self, df, var):
        mes_month = {'mes': ['Ene', 'Feb',
                     'Mar',  'Abr',
                     'May',  'Jun',
                     'Jul',  'Ago',
                     'Sep',  'Oct',
                     'Nov',  'Dic'],
                     'month': ['January','February',
                      'March', 'April',
                      'May',   'June',
                      'July',  'August',
                      'September', 'October',
                      'November',  'December']}
        df[var] = df[var].replace(mes_month['mes'], mes_month['month'])
        return df


    def remplazar_coma_punto(self, df, vars):
        if len(vars) > 1:
            for v in vars:
                df[v] = df[v].str.replace(',', '\.', regex=True)
        else:
            df[vars] = df[vars].str.replace(',', '\.', regex=True)

        return df


