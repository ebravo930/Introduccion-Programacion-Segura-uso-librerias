from sqlalchemy import create_engine, MetaData, Table, Column, Integer, select, NVARCHAR
from sqlalchemy.orm import Session  # Importamos Session para manejar la conexión de forma más eficiente

# Configuración de conexión a la base de datos MS-SQL usando SQLAlchemy
DATABASE_URI = 'mssql+pyodbc://sa:Passw0rdInacap@localhost,1433/Libreria?driver=ODBC+Driver+17+for+SQL+Server'

engine = create_engine(DATABASE_URI, echo=True)
metadata = MetaData()

# Definición de la tabla 'Usuarios'
usuarios = Table('Usuarios', metadata,
                 Column('Id', Integer, primary_key=True),
                 Column('Nombre', NVARCHAR(50)),
                 Column('Edad', Integer),
                 autoload_with=engine)

# Creación de la tabla en la base de datos si no existe
metadata.create_all(engine)

# Utilizamos una sesión para manejar la consulta
with Session(engine) as session:
    # Preparar la sentencia SQL de selección utilizando la ORM API para facilitar el manejo de los resultados
    select_statement = select(usuarios)  # Seleccionamos la tabla entera
    result = session.execute(select_statement)

    # Imprimir los resultados accediendo a los nombres de las columnas
    for row in result.mappings():
        print(f"Id: {row['Id']}, Nombre: {row['Nombre']}, Edad: {row['Edad']}")

# El uso de Session aquí facilita la gestión de transacciones y el contexto de conexión
