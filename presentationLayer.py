import ListManager
import CheeseRecord

# Sean Di Rienzo
if __name__ == '__main__':

    csv_file = 'canadianCheeseDirectory.csv'
    database_file = 'canadianCheeseDirectory.sqlite'


    def presentation_loop():
        i = 0
        cheese_list = ListManager.ListManager(csv_file, database_file)

        while i == 0:

            print("Sean Di Rienzo - Assignment 3")
            print("Menu")

            user_input = input(
                "Choose An Option\n"
                "0 : Load Dataset From CSV\n"
                "1 : Write to CSV\n"
                "2 : Display all records\n"
                "3 : Create new record\n"
                "4 : Edit Record\n"
                "5 : Delete Record\n"
                "6 : Display Record at Index\n"
                "7 : Commit Changes and Close Connection\n"
            )

            if user_input == "0":
                cheese_list.csv_to_dataframe()
                cheese_list.dataframe_to_database_table()
                cheese_list.dataframe_to_list()
            elif user_input == "1":
                cheese_list.write_to_csv()
            elif user_input == "2":
                cheese_list.print_list()

            elif user_input == "3":
                cheese_list.add_record(CheeseRecord.CheeseRecord(
                    input("CheeseId: "), input("CheeseNameEN: "), input("ManufacturerNameEN: "),
                    input("ManufacturerProvCode: "), input("ManufacturingTypeEN: "), input("WebSiteEN: "),
                    input("FatContentPercent: "), input("MoisturePercent: "), input("ParticularitiesEN: "),
                    input("FlavourEN: "), input("CharacteristicsEn: "), input("RipeningEN: "), input("Organic: "),
                    input("CategoryTypeEN: "), input("MilkTypeEN: "), input("MilkTreatmentTypeEN: "),
                    input("RindTypeEN: "), input("LastUpdateDate: ")
                ))
                length = len(cheese_list.cheese_list) - 1
                cheese_list.print_at_index(length)


            elif user_input == "4":
                row_index = int(input("Enter Index of Record to Edit\n"))
                print(
                    "0:CheeseID, 1:CheeseNameEn, 2:ManufacturerNameEn, 3:ManufacturerProvCode, 4:ManufacturingTypeEn, "
                    "5:WebsiteEN, 6:FatContentPercent, 7:MoisturePercent, 8:ParticularitiesEn, 9:FlavourEN, "
                    "10:CharacteristicsEn, 11:RipeningEn, 12:Organic, 13:CategoryTypeEn, 14:MilkTypeEn, "
                    "15:MilkTreatmentTypeEn, 16:RindTypeEn, 17:LastUpdateDate ")
                column_index = int(input("Enter Index of Field to Edit \n"))
                cheese_list.edit_at_index(row_index, column_index, input("Enter value to write\n"))
            elif user_input == "5":
                cheese_list.delete_at_index(int(input("Enter the index of record to delete\n")))


            elif user_input == "6":
                cheese_list.print_at_index(int(input("Enter the Index of Record to Display\n")))

            elif user_input == "7":
                cheese_list.commit_and_close()
                pass
            else:
                pass


    presentation_loop()
