import os
import errno

def crear_dir_data():
    try:
        os.mkdir('data')
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise


def mes_to_month(df, var):
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


def remplazar_coma_punto(df):
    df['dolar'] = df.dolar.str.replace(',', '.')
    df['prom'] = df.prom.str.replace(',', '.')
    return df
