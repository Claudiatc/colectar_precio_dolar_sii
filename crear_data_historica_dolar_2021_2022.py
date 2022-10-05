
from ColectDolarSII import *
from functions import *

crear_dir_data()

"""
el objetivo del script es crear tablas con formato largo por medio de la recopilación 
del valor histórico del dolar de la web sii.cl
"""

metadata = {'info':
   """PENDIENTE:
   Desde home de sii, se puede seleccionar dólar y llegar a un menú de filtros para meses y años.
   Al seleccionar año, se actualiza el drive y quedan obsoletos los elementos.
   Intenté con iframe, pero no hay iframe a la vista.
   Intenté con for e ir actualizando los elementos, pero el mensaje de error igual aparece:
   element is not attached to the page document 
   SOLUCIÓN TEMPORAL: usar url específicos al valor de dólar por día.
   """,
    'web': 'https://www.sii.cl/valores_y_fechas/dolar/dolar',

    'web_ext': '.htm',
    'path': '/usr/bin/chromedriver_linux/chromedriver',
    'id_sel_mes': 'sel_mes',
    'valor_mes': 'todos',
    'year': '//*[@id="my-wrapper"]/div[2]/div[1]/div/div/div[2]/div[1]/div/div[2]/div/div/button/span[1]',
    'encabezados': '//*[@id="table_export"]/thead/tr/th',
    'valores': '//*[@id="table_export"]/tbody/tr'
}

anios = ['2021', '2022']
dolar = ColectDolarSII(name='Clau', metadata=metadata)
ws = dolar.construir_pag_web(anios)
df = dolar.colectar_remodelar_dolar(ws)

# en este caso se remplazan los valores de mes en español al inglés por necesidades particulares del proyecto
df = mes_to_month(df, 'month')


df = remplazar_coma_punto(df)
#

df.to_feather('data/dolar_hist.feather')


#%%
