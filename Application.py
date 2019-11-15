import DataAccess


class DatabasePassThrough:

    def __init__(self):
        self.database_session = DataAccess.CheeseRecord()

    def delete_record(self, cheeseid):
        self.database_session.delete_record(cheeseid)

    def edit_record(self, column, cheeseid, value):
        self.database_session.edit_record(column, cheeseid, value)

    def get_all_records(self):
        db_rows = self.database_session.get_table_all(self.database_session.working_table)
        return db_rows

    def add_record(self, cheese_id, cheese_name_en, manufacturer_name_en,
                   manufacturer_prov_code, manufacturing_type_en, website_en,
                   fat_content_percent, moisture_percent, particularities_en, flavour_en,
                   characteristics_en, ripening_en, organic, category_type_en,
                   milk_type_en, milk_treatment_type_en, rind_type_en,
                   last_update_date):
        print("in application - add record")
        self.database_session.add_record(cheese_id, cheese_name_en, manufacturer_name_en,
                                         manufacturer_prov_code, manufacturing_type_en, website_en,
                                         fat_content_percent, moisture_percent, particularities_en, flavour_en,
                                         characteristics_en, ripening_en, organic, category_type_en,
                                         milk_type_en, milk_treatment_type_en, rind_type_en,
                                         last_update_date)
