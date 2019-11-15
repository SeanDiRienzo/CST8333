import pandas as pd

import sqlite3
import sqlalchemy


class CheeseRecord:
    db_name = 'canadianCheeseDirectory.sqlite'
    master_table = 'cheeseDirectory'
    working_table = 'cheeseData'

    def __init__(self):
        self.setup()

    def edit_record(self, column, cheese_id, value):
        if column == 0:
            self.tempColumn = "CheeseId"
        elif column == 1:
            self.tempColumn = "CheeseNameEn"
        elif column == 2:
            self.tempColumn = "ManufacturerNameEn"
        elif column == 3:
            self.tempColumn = "ManufacturerProvCode"
        elif column == 4:
            self.tempColumn = "ManufacturingTypeEn"
        elif column == 5:
            self.tempColumn = "WebSiteEn"
        elif column == 6:
            self.tempColumn = "FatContentPercent"
        elif column == 7:
            self.tempColumn = "MoisturePercent"
        elif column == 8:
            self.tempColumn = "ParticularitiesEn"
        elif column == 9:
            self.tempColumn = "FlavourEn"
        elif column == 10:
            self.tempColumn = "CharacteristicsEn"
        elif column == 11:
            self.tempColumn = "RipeningEn"
        elif column == 12:
            self.tempColumn = "Organic"
        elif column == 13:
            self.tempColumn = "CategoryTypeEn"
        elif column == 14:
            self.tempColumn = "MilkTypeEn"
        elif column == 15:
            self.tempColumn = "MilkTreatmentTypeEn"
        elif column == 16:
            self.tempColumn = "RindTypeEn"
        elif column == 17:
            self.tempColumn = "LastUpdateDateEn"

        print(self.tempColumn)
        print(cheese_id)
        query = """UPDATE cheeseData SET {}={} WHERE CheeseId={}""".format(self.tempColumn, value, cheese_id)
        print(query)
        self.run_query(query, )

    def delete_record(self, cheese_id):

        query = 'DELETE FROM ' + self.working_table + " where CheeseId=" + cheese_id
        self.run_query(query, )

    def add_record(self, cheese_id, cheese_name_en, manufacturer_name_en,
                   manufacturer_prov_code, manufacturing_type_en, website_en,
                   fat_content_percent, moisture_percent, particularities_en, flavour_en,
                   characteristics_en, ripening_en, organic, category_type_en,
                   milk_type_en, milk_treatment_type_en, rind_type_en,
                   last_update_date):
        print(cheese_id)
        #  engine = sqlalchemy.create_engine('sqlite:///canadianCheeseDirectory.sqlite')
        #  connection = engine.connect()
        # connection.execute(self.working_table.insert(), name='Joe', age=20)
        sql_insert_query = '''INSERT INTO cheeseData(CheeseId, CheeseNameEn, ManufacturerNameEn,
                         ManufacturerProvCode, ManufacturingTypeEn, WebSiteEn,
                         FatContentPercent, MoisturePercent, ParticularitiesEn, FlavourEn,
                         CharacteristicsEn, RipeningEn, Organic, CategoryTypeEn,
                         MilkTypeEn, MilkTreatmentTypeEn, RindTypeEn,
                         LastUpdateDate)VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''

        parameters = (cheese_id, cheese_name_en, manufacturer_name_en,
                      manufacturer_prov_code, manufacturing_type_en, website_en,
                      fat_content_percent, moisture_percent, particularities_en, flavour_en,
                      characteristics_en, ripening_en, organic, category_type_en,
                      milk_type_en, milk_treatment_type_en, rind_type_en,
                      last_update_date)
        print("about to run query add in datacess")

        self.run_query(sql_insert_query, parameters)
        print("query succcessful")

    def setup(self):
        self.create_working_table()

    def get_table_all(self, table):
        query = 'SELECT * FROM ' + table
        db_rows = self.run_query(query, )
        return db_rows

    def create_working_table(self):
        engine = sqlalchemy.create_engine('sqlite:///canadianCheeseDirectory.sqlite')
        connection = engine.connect()
        df = pd.read_sql(self.master_table, con=connection)

        df = df.drop(['CheeseNameFr', 'ManufacturerNameFr', 'ManufacturingTypeFr', 'WebSiteFr', 'ParticularitiesFr',
                      'FlavourFr', 'CharacteristicsFr', 'RipeningFr', 'CategoryTypeFr', 'MilkTypeFr',
                      'MilkTreatmentTypeFr',
                      'RindTypeFr'], axis=1, inplace=False)

        df.to_sql(name='cheeseData', con=connection, if_exists='replace', index=False)

    def run_query(self, query, parameters=()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
            return result
