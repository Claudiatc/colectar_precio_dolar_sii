import os
import errno

def crear_dir_data():
    try:
        os.mkdir('data')
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise


def mes_to_month(df):
    mes_month = {'Ene': 'January',
                 'Feb': 'February',
                 'Mar': 'March',
                 'Abr': 'April',
                 'May': 'May',
                 'Jun': 'June',
                 'Jul': 'July',
                 'Ago': 'August',
                 'Sep': 'September',
                 'Oct': 'October',
                 'Nov': 'November',
                 'Dic': 'December'}
    df['month'] = df.month.replace(mes_month, inplace=True)


def remplazar_coma_punto(df):
    df['dolar'] = df.dolar.str.replace(',', '.')
    df['mean'] = df.mean.str.replace(',', '.')
    return df

#%%
