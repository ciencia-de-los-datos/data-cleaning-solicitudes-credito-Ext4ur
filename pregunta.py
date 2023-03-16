"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")

    df.drop(columns=['Unnamed: 0'], inplace=True)

    # Verificacion tipo de datos

    df['fecha_de_beneficio'] = pd.to_datetime(df.fecha_de_beneficio, dayfirst = True)

    # Verificacion de rangos numericos y de fecha

    # Manejo de categorias

    # Registros duplicados

    df = df.drop_duplicates().dropna()

    # Unificacion de cadenas de texto

    ## Sexo

    df['sexo'] = df['sexo'].str.lower()

    ## Tipo de emprendimiento

    df['tipo_de_emprendimiento'] = df['tipo_de_emprendimiento'].str.lower()

    ## Idea de negocio

    df['idea_negocio'] = df['idea_negocio'].str.lower()

    df['idea_negocio'] = df['idea_negocio'].replace(' |-', '_', regex=True)

    ## Barrio

    df['barrio'] = df['barrio'].str.lower()
    df['barrio'] = df['barrio'].replace(' |-', '_', regex=True)

    ## Linea de credito

    df['línea_credito'] = df['línea_credito'].str.lower()
    df['línea_credito'] = df['línea_credito'].replace(' |-', '_', regex=True)


    ## Monto del credito

    df['monto_del_credito'] = df['monto_del_credito'].replace('\$| |,|\.00', '', regex=True)

    # Formato de fechas

    #print(df['estrato'].value_counts())

    #df.to_csv('Prueba.csv', index=False)

    return df
