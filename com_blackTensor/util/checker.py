import datetime
import os

class Checker:
    @staticmethod
    def check_covid_date_type(date):
        
        try:
            if(date is not None):
                date = datetime.datetime.strptime(date, '%Y%m%d')
                return True
            else:
                return False
        except ValueError:
            return False

    @staticmethod
    def check_folder_path(path):
        return os.path.isdir(Checker.get_abs_path(path))

    @staticmethod
    def get_abs_path(path):
        return os.path.abspath(path)