import reflex as rx
import re
import pandas as pd
import pandasql as psql

class MainState(rx.State):
    """The app state."""

    columns = [
    {"title": "Nombre", "type": "str"},
    {"title": "Apellidos", "type": "str"},
    {"title": "Edad", "type": "int"},
    {"title": "Altura_cm", "type": "float"},
    {"title": "Complexión", "type": "str"},
    {"title": "Color_pelo", "type": "str"}
    ]

    data = [
    ["Ana", "López Martínez", 75, 192.55, "Atlético", "Pelirrojo"],
    ["Carlos", "Fernández López", 32, 159.09, "Delgado", "Rubio"],
    ["Pedro", "Martínez Álvarez", 49, 160.61, "Normal", "Castaño"],
    ["Elena", "López Navarro", 32, 189.89, "Robusto", "Negro"],
    ["Elena", "Fernández Hernández", 35, 167.02, "Normal", "Pelirrojo"],
    ["Luis", "Gutiérrez Rodríguez", 45, 194.02, "Normal", "Negro"],
    ["Ana", "Torres Pérez", 49, 185.06, "Delgado", "Castaño"],
    ["Teresa", "Domínguez Domínguez", 19, 163.81, "Normal", "Canoso"],
    ["José", "Gutiérrez Fernández", 42, 150.51, "Normal", "Negro"],
    ["David", "Gutiérrez Romero", 39, 197.4, "Robusto", "Negro"],
    ["Lucía", "Rodríguez Sánchez", 60, 154.28, "Atlético", "Rubio"],
    ["María", "Sánchez Romero", 61, 186.0, "Robusto", "Castaño"],
    ["Carlos", "Moreno Romero", 69, 174.43, "Robusto", "Castaño"],
    ["José", "Romero Alonso", 43, 187.91, "Normal", "Canoso"],
    ["Juan", "Martínez Sánchez", 64, 184.53, "Normal", "Castaño"],
    ["Elena", "Martínez Muñoz", 28, 182.3, "Robusto", "Negro"],
    ["Sergio", "Álvarez Sánchez", 71, 174.54, "Robusto", "Canoso"],
    ["Julia", "Fernández Rodríguez", 47, 189.65, "Normal", "Castaño"],
    ["Carlos", "Rodríguez Torres", 76, 154.65, "Atlético", "Canoso"],
    ["Teresa", "Alonso Pérez", 26, 161.08, "Atlético", "Castaño"],
    ["Juan", "Romero González", 80, 184.59, "Robusto", "Castaño"],
    ["Teresa", "Hernández Alonso", 57, 165.31, "Atlético", "Rubio"],
    ["Lucía", "Fernández López", 52, 179.08, "Robusto", "Castaño"],
    ["Elena", "Alonso Torres", 19, 173.66, "Delgado", "Canoso"],
    ["Raúl", "Sánchez Martínez", 76, 176.55, "Normal", "Negro"],
    ["David", "Torres García", 43, 171.28, "Robusto", "Rubio"],
    ["Pedro", "López Fernández", 55, 187.3, "Robusto", "Castaño"],
    ["Carlos", "González Romero", 54, 166.54, "Robusto", "Castaño"],
    ["Carmen", "Gutiérrez Gutiérrez", 60, 185.14, "Atlético", "Canoso"],
    ["Lucía", "Rodríguez Muñoz", 19, 163.55, "Robusto", "Rubio"],
    ["Miguel", "Martínez González", 23, 162.57, "Delgado", "Castaño"],
    ["Pedro", "Muñoz García", 59, 156.03, "Atlético", "Negro"],
    ["Luis", "Muñoz Hernández", 45, 159.63, "Normal", "Negro"],
    ["Juan", "Alonso Jiménez", 26, 155.98, "Delgado", "Castaño"],
    ["Miguel", "Romero Torres", 73, 176.79, "Robusto", "Negro"],
    ["Ana", "Gutiérrez Pérez", 47, 188.11, "Delgado", "Rubio"],
    ["José", "Rodríguez Jiménez", 29, 159.26, "Robusto", "Castaño"],
    ["Jorge", "Rodríguez Martínez", 21, 160.82, "Delgado", "Canoso"],
    ["Ana", "Domínguez Torres", 34, 174.21, "Atlético", "Rubio"],
    ["Isabel", "Martínez Álvarez", 42, 186.23, "Robusto", "Negro"],
    ["Isabel", "Martínez Martínez", 38, 198.83, "Atlético", "Castaño"],
    ["Julia", "Domínguez Gutiérrez", 31, 176.23, "Delgado", "Rubio"],
    ["Pedro", "Navarro Navarro", 47, 164.15, "Robusto", "Negro"],
    ["María", "González Martínez", 38, 155.03, "Normal", "Castaño"],
    ["Raúl", "Navarro López", 39, 159.71, "Normal", "Pelirrojo"],
    ["Teresa", "González López", 66, 161.37, "Robusto", "Canoso"],
    ["Ana", "Vázquez López", 74, 158.97, "Delgado", "Negro"],
    ["Jorge", "Fernández Muñoz", 42, 150.71, "Normal", "Negro"],
    ["José", "Sánchez Domínguez", 35, 176.71, "Robusto", "Pelirrojo"],
    ["Teresa", "Fernández Domínguez", 66, 163.72, "Normal", "Pelirrojo"],
    ["Laura", "Vázquez Martínez", 78, 198.71, "Robusto", "Rubio"],
    ["Julia", "Vázquez López", 71, 177.67, "Delgado", "Canoso"],
    ["Isabel", "Romero Domínguez", 44, 184.87, "Delgado", "Canoso"],
    ["David", "Domínguez Navarro", 34, 156.31, "Atlético", "Negro"],
    ["Juan", "Álvarez Hernández", 71, 193.42, "Normal", "Pelirrojo"],
    ["José", "Rodríguez Álvarez", 23, 174.54, "Atlético", "Canoso"],
    ["María", "Fernández Hernández", 48, 193.64, "Delgado", "Castaño"],
    ["Elena", "Muñoz Pérez", 19, 178.7, "Robusto", "Canoso"],
    ["Laura", "Jiménez Alonso", 65, 173.47, "Delgado", "Negro"],
    ["José", "Álvarez López", 52, 172.02, "Delgado", "Canoso"],
    ["Elena", "García Alonso", 21, 159.22, "Robusto", "Rubio"],
    ["Ana", "Vázquez Domínguez", 78, 152.57, "Atlético", "Pelirrojo"],
    ["Jorge", "Sánchez López", 40, 197.05, "Normal", "Negro"],
    ["Pedro", "Torres Rodríguez", 32, 173.89, "Delgado", "Negro"],
    ["Raúl", "Navarro Hernández", 59, 191.11, "Delgado", "Pelirrojo"],
    ["Isabel", "Pérez Moreno", 22, 170.04, "Normal", "Pelirrojo"],
    ["Carmen", "López Fernández", 67, 153.7, "Delgado", "Pelirrojo"],
    ["Isabel", "Moreno Jiménez", 79, 181.47, "Normal", "Negro"],
    ["Isabel", "González Alonso", 59, 152.68, "Normal", "Pelirrojo"],
    ["Juan", "Torres Jiménez", 20, 157.46, "Normal", "Pelirrojo"],
    ["Pedro", "Vázquez Navarro", 66, 178.14, "Robusto", "Negro"],
    ["José", "García Torres", 19, 165.19, "Atlético", "Negro"],
    ["Ana", "González Jiménez", 58, 186.86, "Atlético", "Pelirrojo"],
    ["David", "Moreno Gutiérrez", 21, 155.49, "Robusto", "Negro"],
    ["José", "Moreno Martínez", 51, 182.11, "Robusto", "Rubio"],
    ["Julia", "Gutiérrez Sánchez", 56, 160.06, "Atlético", "Castaño"],
    ["Laura", "González Gutiérrez", 65, 178.67, "Atlético", "Castaño"],
    ["Sergio", "Sánchez Martínez", 80, 172.38, "Delgado", "Canoso"],
    ["Elena", "García Gutiérrez", 61, 169.04, "Atlético", "Castaño"],
    ["Carlos", "Hernández Martínez", 73, 164.25, "Robusto", "Negro"],
    ["Teresa", "Hernández Jiménez", 65, 164.23, "Atlético", "Negro"],
    ["Carmen", "Torres Torres", 47, 193.25, "Robusto", "Negro"],
    ["Laura", "Hernández Sánchez", 39, 183.85, "Atlético", "Rubio"],
    ["Lucía", "Muñoz Sánchez", 45, 189.92, "Robusto", "Negro"],
    ["Jorge", "Martínez Gutiérrez", 66, 156.38, "Atlético", "Castaño"],
    ["Carlos", "Moreno Martínez", 68, 156.76, "Atlético", "Rubio"],
    ["David", "Gutiérrez Rodríguez", 59, 166.69, "Normal", "Castaño"],
    ["María", "García Martínez", 28, 184.52, "Robusto", "Rubio"],
    ["Isabel", "Muñoz López", 33, 155.49, "Normal", "Negro"],
    ["Teresa", "Sánchez Martínez", 43, 181.01, "Atlético", "Pelirrojo"],
    ["Elena", "Hernández Jiménez", 29, 180.69, "Robusto", "Castaño"],
    ["David", "Muñoz Domínguez", 49, 176.86, "Robusto", "Negro"],
    ["Ana", "González Gutiérrez", 68, 155.4, "Normal", "Rubio"],
    ["José", "Moreno Pérez", 70, 153.29, "Normal", "Castaño"],
    ["Carlos", "Hernández Sánchez", 67, 189.93, "Robusto", "Castaño"],
    ["Juan", "Sánchez Martínez", 39, 153.73, "Atlético", "Pelirrojo"],
    ["José", "Jiménez Sánchez", 51, 157.9, "Atlético", "Pelirrojo"],
    ["Julia", "Gutiérrez Pérez", 18, 169.88, "Atlético", "Negro"],
    ["Sergio", "Moreno Gutiérrez", 77, 174.82, "Atlético", "Castaño"],
    ["Lucía", "Domínguez Martínez", 53, 179.16, "Atlético", "Rubio"],
    ["María", "Muñoz Martínez", 64, 156.67, "Robusto", "Rubio"],
    ["Jorge", "Domínguez Gutiérrez", 51, 169.63, "Robusto", "Negro"],
    ["Carlos", "González Sánchez", 24, 159.84, "Atlético", "Rubio"],
    ["Ana", "Rodríguez Sánchez", 22, 188.97, "Robusto", "Rubio"],
    ["Julia", "Muñoz Domínguez", 26, 172.8, "Atlético", "Castaño"],
    ["Isabel", "Moreno López", 54, 172.98, "Robusto", "Negro"],
    ["Miguel", "Sánchez Martínez", 63, 184.61, "Atlético", "Castaño"],
    ["Teresa", "Gutiérrez Gutiérrez", 80, 181.83, "Delgado", "Rubio"],
    ["Sergio", "García Martínez", 79, 162.98, "Robusto", "Rubio"],
    ["Carmen", "Gutiérrez Pérez", 35, 165.89, "Atlético", "Rubio"],
    ["Ana", "Muñoz Sánchez", 47, 160.16, "Atlético", "Negro"],
    ["Carlos", "López Gutiérrez", 70, 170.29, "Atlético", "Rubio"],
    ["Lucía", "Hernández Gutiérrez", 24, 174.2, "Atlético", "Castaño"],
    ["Laura", "Jiménez Muñoz", 55, 160.96, "Delgado", "Rubio"],
    ["Jorge", "López Jiménez", 43, 177.94, "Atlético", "Rubio"],
    ["Laura", "Torres García", 78, 193.4, "Atlético", "Castaño"],
    ["Pedro", "Torres Jiménez", 55, 188.3, "Robusto", "Rubio"],
    ["María", "García Gutiérrez", 52, 180.6, "Robusto", "Rubio"],
    ["David", "García Martínez", 54, 154.97, "Robusto", "Negro"],
    ["Laura", "Torres Rodríguez", 45, 156.8, "Delgado", "Negro"],
    ["Julia", "Fernández Pérez", 42, 179.3, "Robusto", "Rubio"],
    ["Carlos", "Moreno Martínez", 75, 167.85, "Atlético", "Rubio"],
    ["Isabel", "Fernández Gutiérrez", 62, 164.36, "Delgado", "Rubio"],
    ["Juan", "Muñoz Pérez", 41, 169.36, "Atlético", "Rubio"],
    ["Carmen", "Sánchez López", 64, 176.01, "Delgado", "Rubio"],
    ["Miguel", "Fernández Gutiérrez", 21, 163.69, "Atlético", "Castaño"],
    ["David", "Muñoz Martínez", 55, 184.14, "Robusto", "Rubio"],
    ["Isabel", "González Sánchez", 31, 170.3, "Atlético", "Castaño"],
    ["Lucía", "Martínez López", 47, 191.68, "Robusto", "Rubio"],
    ["Ana", "Jiménez Gutiérrez", 59, 171.8, "Atlético", "Rubio"],
    ["José", "Martínez Muñoz", 51, 186.91, "Robusto", "Negro"],
    ["Juan", "González Pérez", 58, 164.93, "Atlético", "Castaño"],
    ["Teresa", "Fernández Sánchez", 58, 187.41, "Atlético", "Castaño"],
    ["Carlos", "Gutiérrez Gutiérrez", 44, 191.76, "Delgado", "Rubio"],
    ["Lucía", "Martínez Sánchez", 41, 193.06, "Delgado", "Rubio"],
    ["Miguel", "García López", 62, 158.34, "Delgado", "Rubio"],
    ["David", "Muñoz Muñoz", 45, 156.08, "Atlético", "Castaño"],
    ["Carlos", "Sánchez Muñoz", 44, 157.0, "Delgado", "Rubio"],
    ["Sergio", "González López", 25, 179.8, "Atlético", "Rubio"],
    ["José", "García Gutiérrez", 32, 186.57, "Atlético", "Rubio"],
    ["María", "Jiménez Martínez", 58, 184.72, "Atlético", "Rubio"],
    ["Isabel", "López Martínez", 38, 190.96, "Atlético", "Rubio"],
    ["Julia", "Moreno Jiménez", 59, 187.26, "Atlético", "Castaño"],
    ["Lucía", "Moreno López", 65, 167.07, "Atlético", "Castaño"],
    ["José", "García Pérez", 43, 176.55, "Atlético", "Rubio"],
    ["Ana", "Martínez Sánchez", 55, 158.54, "Atlético", "Rubio"],
    ["Jorge", "Jiménez Martínez", 41, 191.64, "Atlético", "Castaño"],
    ["Lucía", "Martínez Martínez", 62, 157.61, "Atlético", "Rubio"],
    ["Carlos", "González Jiménez", 54, 191.34, "Atlético", "Rubio"],
    ["Miguel", "Sánchez Sánchez", 54, 178.0, "Atlético", "Rubio"],
    ["Juan", "Gutiérrez Gutiérrez", 61, 176.61, "Atlético", "Rubio"],
    ["David", "Gutiérrez Pérez", 30, 157.08, "Atlético", "Rubio"],
    ["Ana", "García Muñoz", 68, 189.92, "Atlético", "Rubio"],
    ["Isabel", "Jiménez Gutiérrez", 45, 177.83, "Atlético", "Rubio"],
    ["Teresa", "Jiménez López", 48, 191.41, "Atlético", "Rubio"],
    ["Jorge", "González Gutiérrez", 18, 167.36, "Atlético", "Castaño"],
    ["Lucía", "García Gutiérrez", 56, 178.23, "Atlético", "Castaño"],
    ["Laura", "López Gutiérrez", 46, 184.55, "Atlético", "Castaño"],
    ["Pedro", "Hernández López", 63, 186.43, "Atlético", "Castaño"],
    ["Carlos", "González Martínez", 55, 155.99, "Atlético", "Rubio"],
    ["Sergio", "Martínez Gutiérrez", 40, 180.95, "Atlético", "Rubio"],
    ["María", "Fernández Gutiérrez", 47, 170.45, "Atlético", "Rubio"],
    ["José", "Jiménez Sánchez", 34, 174.69, "Atlético", "Rubio"],
    ["Ana", "Gutiérrez López", 42, 179.8, "Atlético", "Castaño"],
    ["Isabel", "Muñoz Sánchez", 62, 167.72, "Atlético", "Castaño"],
    ["Carlos", "Sánchez Gutiérrez", 67, 187.99, "Atlético", "Castaño"],
    ["Lucía", "Hernández Jiménez", 34, 153.57, "Atlético", "Castaño"],
    ["Jorge", "García Jiménez", 58, 178.64, "Atlético", "Castaño"],
    ["Laura", "Jiménez López", 46, 160.44, "Atlético", "Castaño"],
    ["David", "Sánchez López", 33, 192.19, "Atlético", "Castaño"],
    ["Isabel", "Gutiérrez Muñoz", 48, 187.56, "Atlético", "Castaño"],
    ["Juan", "Muñoz Martínez", 53, 181.49, "Atlético", "Castaño"],
    ["María", "Martínez Jiménez", 37, 172.7, "Atlético", "Castaño"],
    ["Ana", "Martínez López", 35, 176.41, "Atlético", "Castaño"],
    ["Teresa", "Jiménez Sánchez", 33, 160.09, "Atlético", "Castaño"],
    ["Lucía", "Sánchez Muñoz", 44, 168.01, "Atlético", "Castaño"],
    ["Pedro", "Gutiérrez Jiménez", 58, 181.85, "Atlético", "Castaño"],
    ["José", "Martínez Muñoz", 21, 178.7, "Atlético", "Castaño"],
    ["Julia", "Muñoz López", 32, 189.67, "Atlético", "Castaño"],
    ["Laura", "García Gutiérrez", 46, 188.76, "Atlético", "Castaño"],
    ["Carlos", "Jiménez Muñoz", 39, 168.66, "Atlético", "Castaño"],
    ["Ana", "Gutiérrez Gutiérrez", 23, 190.32, "Atlético", "Castaño"],
    ["David", "Jiménez López", 57, 161.84, "Atlético", "Castaño"],
    ["Lucía", "Muñoz Gutiérrez", 68, 181.53, "Atlético", "Castaño"],
    ["José", "García Gutiérrez", 68, 160.65, "Atlético", "Castaño"],
    ["Miguel", "Gutiérrez Jiménez", 53, 182.14, "Atlético", "Castaño"],
    ["Isabel", "Jiménez Martínez", 30, 188.72, "Atlético", "Castaño"],
    ["Julia", "Martínez Muñoz", 34, 158.61, "Atlético", "Castaño"],
    ["Juan", "Gutiérrez López", 52, 186.39, "Atlético", "Castaño"],
    ["Laura", "Jiménez Gutiérrez", 26, 190.41, "Atlético", "Castaño"],
    ["Sergio", "Sánchez Muñoz", 27, 173.08, "Atlético", "Castaño"],
    ["María", "García Jiménez", 40, 163.2, "Atlético", "Castaño"],
    ["Carlos", "García Martínez", 39, 192.83, "Atlético", "Castaño"],
    ["Ana", "García López", 23, 182.53, "Atlético", "Castaño"],
    ["David", "Jiménez Gutiérrez", 43, 184.24, "Atlético", "Castaño"],
    ["Lucía", "Muñoz Jiménez", 36, 169.47, "Atlético", "Castaño"],
    ["José", "Jiménez Gutiérrez", 39, 161.14, "Atlético", "Castaño"],
    ["Isabel", "Gutiérrez Muñoz", 57, 164.66, "Atlético", "Castaño"],
    ["Julia", "Jiménez López", 53, 165.62, "Atlético", "Castaño"],
    ["Juan", "Martínez Gutiérrez", 43, 156.98, "Atlético", "Castaño"],
    ["Laura", "Sánchez Muñoz", 59, 185.1, "Atlético", "Castaño"],
    ["Pedro", "García Gutiérrez", 55, 187.26, "Atlético", "Castaño"],
    ["María", "Jiménez Jiménez", 57, 161.2, "Atlético", "Castaño"],
    ["Carlos", "Jiménez Gutiérrez", 48, 158.9, "Atlético", "Castaño"],
    ["Lucía", "Muñoz Muñoz", 37, 163.52, "Atlético", "Castaño"],
    ["David", "García López", 46, 182.36, "Atlético", "Castaño"],
    ["Ana", "Gutiérrez Gutiérrez", 55, 160.03, "Atlético", "Castaño"],
    ["Isabel", "Jiménez Muñoz", 56, 158.34, "Atlético", "Castaño"],
    ["Julia", "Martínez López", 41, 163.85, "Atlético", "Castaño"],
    ["Juan", "García Muñoz", 47, 171.78, "Atlético", "Castaño"],
    ["Laura", "Gutiérrez Gutiérrez", 41, 170.22, "Atlético", "Castaño"],
    ["Sergio", "Gutiérrez López", 35, 188.04, "Atlético", "Castaño"],
    ["María", "García Gutiérrez", 34, 160.88, "Atlético", "Castaño"]]


    Personas = pd.DataFrame(data, columns=[col['title'] for col in columns])

    db_schema: list = []

    table_title: str = f" Personas "

    def create_schemas(self):
        """
        Crea el esquema de la base de datos a partir del DataFrame 'Personas'.
        Convierte los tipos de datos del DataFrame en tipos de datos compatibles con la base de datos.

        Args:
            None

        Returns:
            None
        """
        columnas_tipos = str(self.Personas.dtypes)
        patron = r'(\w+(?:\s*\(\w+\))?)\s+(\w+)'
        matches = re.findall(patron, columnas_tipos)
        resultados = [[columna, 'string' if tipo == 'object' else tipo] for columna, tipo in matches]
        self.db_schema = resultados
    
    def format_schemas(self):
        """
        Formatea el esquema de la base de datos para su presentación.
        Convierte cada columna y tipo de datos en una cadena formateada.

        Args:
            None

        Returns:
            None
        """
        formatted_schemas = [f"| {columna} | . . . . . . . . . | {tipo} |" for columna, tipo in self.db_schema]
        self.db_schema = formatted_schemas

    @rx.var
    def get_schemas(self) -> list:
        """
        Obtiene el esquema de la base de datos, creando y formateando el esquema según sea necesario.

        Args:
            None

        Returns:
            list: Lista del esquema de la base de datos formateado.
        """
        self.create_schemas()
        self.format_schemas()
        return self.db_schema
    
    
    def get_objetive(self):
        """
        Muestra un registro aleatorio del DataFrame 'Personas'.

        Args:
            None

        Returns:
            None
        """
        registro_aleatorio = self.Personas.sample(n=1)
        print(registro_aleatorio["Nombre"])
        return registro_aleatorio

    querry_result = []

    def submit_querry(self, querry):
        """
        Ejecuta una consulta SQL en el DataFrame 'Personas' y almacena el resultado.

        Args:
            querry (dict): Diccionario que contiene la consulta SQL con la clave 'querry'.

        Returns:
            None
        """
        Personas = self.Personas
        resultado = psql.sqldf(querry["querry"], locals())
        self.resultado = resultado

    
    # Cuando aun no se ha realiza ninguna consulta se hace una consulta de todo y se devuelve 
    # el dataframe en la varible resultado que cambiara al realizarle consultas

    query = "SELECT * FROM Personas"
    resultado = psql.sqldf(query, locals())


    ##########################################################################################
    # Generar misiones y pistas
    missions = []

    def generate_misions(self):
        self.missions = []
        random_record = self.get_objetive()
        print(random_record)

        # Ejemplo de misiones
        if random_record['Edad'].values[0] > 40:
            self.missions.append({
                'El usuario que buscamos es mayor de 40 años.',
                #'sql': 'SELECT * FROM df WHERE Edad > 40'
            })
        else:
            self.missions.append({
                'El usuario que buscamos es menor de 40 años.',
                #'sql': 'SELECT * FROM df WHERE Edad < 40'
            })

        if random_record['Altura_cm'].values[0] > 170:
            self.missions.append({
                'El usuario que buscamos mide más de 170 cm.',
                #'sql': 'SELECT * FROM df WHERE Altura_cm > 170'
            })
        else:
            self.missions.append({
                'El usuario que buscamos mide menos de 170 cm.',
                #'sql': 'SELECT * FROM df WHERE Altura_cm < 170'
            })

        if random_record['Complexión'].values[0] == 'Robusto':
            self.missions.append({
                'El usuario que buscamos tiene complexión robusta.',
                #'sql': "SELECT * FROM df WHERE Complexión = 'Robusto'"
            })

        if random_record['Color_pelo'].values[0] == 'Negro':
            self.missions.append({
                'El usuario que buscamos tiene el pelo negro.',
                #'sql': "SELECT * FROM df WHERE Color_pelo = 'Negro'"
            })

        # Más misiones basadas en otros atributos
        if random_record['Nombre'].values[0] == 'Carmen':
            self.missions.append({
                'El nombre del usuario que buscamos es Carmen.',
                #'sql': "SELECT * FROM df WHERE Nombre = 'Carmen'"
            })

        if 'Torres' in random_record['Apellidos'].values[0]:
            self.missions.append({
                'El usuario que buscamos tiene "Torres" en sus apellidos.',
                #'sql': "SELECT * FROM df WHERE Apellidos LIKE '%Torres%'"
            })

        if random_record['Complexión'].values[0] != 'Delgado':
            self.missions.append({
                'El usuario que buscamos no tiene complexión delgada.',
                #'sql': "SELECT * FROM df WHERE Complexión != 'Delgado'"
            })
        else:
            self.missions.append({
                'El usuario que buscamos tiene complexión delgada.',
                #'sql': "SELECT * FROM df WHERE Complexión = 'Delgado'"
            })


        # Mostrar misiones generadas
        print("Misiones generadas:")
        for mission in self.missions:
            print("Pista:", mission)
            print()