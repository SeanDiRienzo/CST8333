import csv
#Sean Di Rienzo

class CheeseRecord:
    """ CheeseRecord object """

    def __init__(self, cheese_id, CheeseNameEn, ManufacturerNameEn,
                 ManufacturerProvCode, ManufacturingTypeEn, WebSiteEn,
                 FatContentPercent, MoisturePercent, ParticularitiesEn, FlavourEn,
                 CharacteristicsEn, RipeningEn, Organic, CategoryTypeEn,
                 MilkTypeEn, MilkTreatmentTypeEn, RindTypeEn,
                 LastUpdateDate):
        """Constructor , taking in parameters for the desired fields from the csv"""

        self.CheeseId = cheese_id
        self.CheeseNameEn = CheeseNameEn
        self.ManufacturerNameEn = ManufacturerNameEn
        self.ManufacturerProvCode = ManufacturerProvCode
        self.ManufacturingTypeEn = ManufacturingTypeEn
        self.WebSiteEn = WebSiteEn
        self.FatContentPercent = FatContentPercent
        self.MoisturePercent = MoisturePercent
        self.ParticularitiesEn = ParticularitiesEn
        self.FlavourEn = FlavourEn
        self.CharacteristicsEn = CharacteristicsEn
        self.RipeningEn = RipeningEn
        self.Organic = Organic
        self.CategoryTypeEn = CategoryTypeEn
        self.MilkTypeEn = MilkTypeEn
        self.MilkTreatmentTypeEn = MilkTreatmentTypeEn
        self.RindTypeEn = RindTypeEn
        self.LastUpdateDate = LastUpdateDate



    def convert_to_string(self):
        """ Returns a string with the CheeseObject's data """
        cheese_record_string = " "
        cheese_record_string += str(self.CheeseId) + " | "
        cheese_record_string += str(self.CheeseNameEn) + " | "
        cheese_record_string += str(self.ManufacturerNameEn) + " | "
        cheese_record_string += str(self.ManufacturerProvCode) + " | "
        cheese_record_string += str(self.ManufacturingTypeEn) + " | "
        cheese_record_string += str(self.WebSiteEn) + " | "
        cheese_record_string += str(self.FatContentPercent) + " | "
        cheese_record_string += str(self.MoisturePercent) + " | "
        cheese_record_string += str(self.ParticularitiesEn) + " | "
        cheese_record_string += str(self.FlavourEn) + " | "
        cheese_record_string += str(self.CharacteristicsEn) + " | "
        cheese_record_string += str(self.RipeningEn) + " | "
        cheese_record_string += str(self.Organic) + " | "
        cheese_record_string += str(self.CategoryTypeEn) + " | "
        cheese_record_string += str(self.MilkTypeEn) + " | "
        cheese_record_string += str(self.MilkTreatmentTypeEn) + " | "
        cheese_record_string += str(self.RindTypeEn) + " | "
        cheese_record_string += str(self.LastUpdateDate)

        return cheese_record_string
