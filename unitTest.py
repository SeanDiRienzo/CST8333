import unittest
import CheeseRecord
import ListManager


"""Sean Di Rienzo"""

class MyTestCase(unittest.TestCase):

    def test_database_same_as_list(self):
        """ test that the database table has been created"""
        index = 1
        list_object = ListManager.ListManager('canadianCheeseDirectory.csv', 'canadianCheeseDirectory.sqlite')
        list_object.csv_to_dataframe()
        list_object.dataframe_to_database_table()
        list_object.dataframe_to_list()
        cursor = list_object.conn.cursor()
        cursor.execute('''Select CheeseId from cheeseData where rowid=?''', (index,))
        row = cursor.fetchone()
        test_int = row[0]

        """ test that the value of the CheeseId at index is the same in my list as it is in the database"""
        self.assertEqual(list_object.cheese_list[index - 1].CheeseId, test_int)
        print("Sean Di Rienzo Test 1 Complete")

    def test_add_database_record(self):
        list_object = ListManager.ListManager('canadianCheeseDirectory.csv', 'canadianCheeseDirectory.sqlite')
        list_object.csv_to_dataframe()
        list_object.dataframe_to_list()
        list_object.dataframe_to_database_table()

        """add a new record"""
        list_object.add_record(
            CheeseRecord.CheeseRecord(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18))

        cursor = list_object.conn.cursor()
        cursor.execute('''SELECT * FROM cheeseData ORDER BY rowid DESC''')
        row = cursor.fetchone()
        tempCheeseId = row[0]
        tempLastUpdateDate = row[17]
        index = len(list_object.cheese_list) - 1

        """test that the value of the last record (most recently added) fields are equal to the fields of my cheeseRecord object in memory 
        """
        self.assertEqual(list_object.cheese_list[index].CheeseId, int(tempCheeseId))
        self.assertEqual(list_object.cheese_list[index].LastUpdateDate, int(tempLastUpdateDate))
        print("Sean Di Rienzo Test 2 Complete")

if __name__ == '__main__':
    unittest.main()
