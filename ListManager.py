import pandas as pd
import numpy as np
import sqlite3
import csv
import CheeseRecord


# Sean Di Rienzo


class ListManager:
    """ ListManagement class to perform function on the list of records """
    cheese_list = []
    target_database = 'database.sqlite'
    cheese_frame = pd.DataFrame
    tempColumn = ""

    def __init__(self, csv_location, database_location):

        self.csv_location = csv_location
        self.database_location = database_location
        self.conn = sqlite3.connect(database_location)

    """ constructor """

    def csv_to_dataframe(self):
        """ Function to parse csv file for desired columns, stores them in a Pandas Dataframe """
        try:
            self.cheese_frame = pd.read_csv(self.csv_location,
                                            usecols=['CheeseId', 'CheeseNameEn', 'ManufacturerNameEn',
                                                     'ManufacturerProvCode',
                                                     'ManufacturingTypeEn', 'WebSiteEn', 'FatContentPercent',
                                                     'MoisturePercent',
                                                     'ParticularitiesEn', 'FlavourEn', 'CharacteristicsEn',
                                                     'RipeningEn',
                                                     'Organic',
                                                     'CategoryTypeEn', 'MilkTypeEn', 'MilkTreatmentTypeEn',
                                                     'RindTypeEn',
                                                     'LastUpdateDate'])
        except IOError as e:
            print(e)

        print("CSV Loaded to Memory and Stored in a Pandas Dataframe")

    def dataframe_to_list(self):
        """ Function to create a list of cheeseRecord objects """

        """ replace pandas null field (nan) with whitespace"""
        self.cheese_frame.replace(np.nan, '', regex=True)
        """iterate over reach row and create CheeseRecord object using the csv fields """
        for index, rows in self.cheese_frame.iterrows():
            temp_record = CheeseRecord.CheeseRecord(rows[0], rows[1], rows[2], rows[3], rows[4], rows[5], rows[6],
                                                    rows[7],
                                                    rows[8],
                                                    rows[9], rows[10], rows[11], rows[12], rows[13], rows[14], rows[15],
                                                    rows[16],
                                                    rows[17])
            self.cheese_list.append(temp_record)
            """add newly created record to the list"""
        print("Pandas DataFrame converted to List of CheeseRecord Objects")

    def dataframe_to_database_table(self):
        """function to dump the pandas dataframe into a table in my database, if the table already exists overwrite
        it """
        self.cheese_frame.to_sql(name='cheeseData', con=self.conn, if_exists='replace', index=False)
        print("Database Table cheeseData Created in canadianCheeseDirectory.sqlite")

    def add_record(self, cheese_record):
        """function to add a record"""
        """first add to list in memory"""
        self.cheese_list.append(cheese_record)
        print("record added to end of list")
        """then add to database table"""
        self.add_database_record(cheese_record)
        print("Record added to database table")

    def return_list_object(self):
        return self

    def new_record(self, Cheese_id, CheeseNameEn, ManufacturerNameEn,
                   ManufacturerProvCode, ManufacturingTypeEn, WebSiteEn,
                   FatContentPercent, MoisturePercent, ParticularitiesEn, FlavourEn,
                   CharacteristicsEn, RipeningEn, Organic, CategoryTypeEn,
                   MilkTypeEn, MilkTreatmentTypeEn, RindTypeEn,
                   LastUpdateDate):
        """function that feeds a new cheeserecord object to higher layers"""
        return CheeseRecord.CheeseRecord(Cheese_id, CheeseNameEn, ManufacturerNameEn,
                                         ManufacturerProvCode, ManufacturingTypeEn, WebSiteEn,
                                         FatContentPercent, MoisturePercent, ParticularitiesEn, FlavourEn,
                                         CharacteristicsEn, RipeningEn, Organic, CategoryTypeEn,
                                         MilkTypeEn, MilkTreatmentTypeEn, RindTypeEn,
                                         LastUpdateDate)

    def print_list(self):

        """function to print out list of cheese records"""

        for index in self.cheese_list:
            print(index.convert_to_string())

    def print_at_index(self, index):

        """function to print cheese record at index"""
        print(self.cheese_list[index].convert_to_string())

    def delete_at_index(self, index):

        """function to delete cheese record at index"""
        """first delete from list in memory"""
        self.cheese_list.pop(index)
        print("item at index " + str(index) + " deleted")
        """then delete from database"""
        self.delete_database_record(index)
        print("record deleted from array of objects in memory")

    def write_to_csv(self):

        """function to write list from memory to data.csv"""
        with open('data.csv', 'w', ) as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['cheese_id', 'CheeseNameEn', 'ManufacturerNameEn',
                             'ManufacturerProvCode', 'ManufacturingTypeEn', 'WebSiteEn',
                             'FatContentPercent', 'MoisturePercent', 'ParticularitiesEn', 'FlavourEn',
                             'CharacteristicsEn', 'RipeningEn', 'Organic', 'CategoryTypeEn',
                             'MilkTypeEn', 'MilkTreatmentTypeEn', 'RindTypeEn',

                             'LastUpdateDate'])
            for index in self.cheese_list:
                writer.writerow(
                    [str(index.CheeseId), index.CheeseNameEn, index.ManufacturerNameEn, index.ManufacturerProvCode,
                     index.ManufacturingTypeEn, index.WebSiteEn, index.FatContentPercent, index.MoisturePercent,
                     index.ParticularitiesEn, index.FlavourEn, index.CharacteristicsEn, index.RipeningEn, index.Organic,
                     index.CategoryTypeEn, index.MilkTypeEn, index.MilkTreatmentTypeEn, index.RindTypeEn,
                     index.LastUpdateDate])
        print("Dataset written to data.csv\n")

    def edit_at_index(self, index: int, row: int, value: str):
        """function to edit cheese record instance field at index, row"""

        if row == 0:
            self.cheese_list[index].CheeseId = value
        elif row == 1:
            self.cheese_list[index].CheeseNameEn = value
        elif row == 2:
            self.cheese_list[index].ManufacturerNameEn = value
        elif row == 3:
            self.cheese_list[index].ManufacturerProvCode = value
        elif row == 4:
            self.cheese_list[index].ManufacturingTypeEn = value
        elif row == 5:
            self.cheese_list[index].WebSiteEn = value
        elif row == 6:
            self.cheese_list[index].FatContentPercent = value
        elif row == 7:
            self.cheese_list[index].MoisturePercent = value
        elif row == 8:
            self.cheese_list[index].ParticularitiesEn = value
        elif row == 9:
            self.cheese_list[index].FlavourEn = value
        elif row == 10:
            self.cheese_list[index].CharacteristicsEn = value
        elif row == 11:
            self.cheese_list[index].RipeningEn = value
        elif row == 12:
            self.cheese_list[index].Organic = value
        elif row == 13:
            self.cheese_list[index].CategoryTypeEn = value
        elif row == 14:
            self.cheese_list[index].MilkTypeEn = value
        elif row == 15:
            self.cheese_list[index].MilkTreatmentTypeEn = value
        elif row == 16:
            self.cheese_list[index].RindTypeEn = value
        elif row == 17:
            self.cheese_list[index].LastUpdateDate = value
        print("Value Updated in memory array of objects\n")
        print(self.cheese_list[index].convert_to_string())

    def edit_database_field(self, index, column, value):
        """function to update the field in the database table"""

        """find string column name from int currentRow() fed when called"""
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

        editcursor = self.conn.cursor()
        print(self.tempColumn)
        """Time to update the database"""
        editcursor.execute(
            """UPDATE cheeseData SET {}=? WHERE ROWID = ?""".format(self.tempColumn),
            (value, (index + 1)))
        print ("Field :" + self.tempColumn + " Updated to database table")

    def add_database_record(self, cheese_record):
        """function to add a new record to the database"""
        cursor = self.conn.cursor()
        sql_insert_query = '''INSERT INTO cheeseData(CheeseId, CheeseNameEn, ManufacturerNameEn,
                 ManufacturerProvCode, ManufacturingTypeEn, WebSiteEn,
                 FatContentPercent, MoisturePercent, ParticularitiesEn, FlavourEn,
                 CharacteristicsEn, RipeningEn, Organic, CategoryTypeEn,
                 MilkTypeEn, MilkTreatmentTypeEn, RindTypeEn,
                 LastUpdateDate)VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
        row_data = (cheese_record.CheeseId, cheese_record.CheeseNameEn, cheese_record.ManufacturerNameEn,
                    cheese_record.ManufacturerProvCode, cheese_record.ManufacturingTypeEn, cheese_record.WebSiteEn,
                    cheese_record.FatContentPercent, cheese_record.MoisturePercent, cheese_record.ParticularitiesEn,
                    cheese_record.FlavourEn, cheese_record.CharacteristicsEn, cheese_record.RipeningEn,
                    cheese_record.Organic, cheese_record.CategoryTypeEn, cheese_record.MilkTypeEn,
                    cheese_record.MilkTreatmentTypeEn, cheese_record.RindTypeEn, cheese_record.LastUpdateDate)
        cursor.execute(sql_insert_query, row_data)

        cursor.close()

        print ("New Record Added to database table")

    def delete_database_record(self, index):
        """function to delete a database record at index"""
        delete_cursor = self.conn.cursor()
        delete_cursor.execute('''DELETE from cheeseData where rowid=?''', (index + 1,))
        print("Record in Database deleted at rowid = " + str(index + 1))
        delete_cursor.close()


    def commit_and_close(self):
        self.conn.commit()