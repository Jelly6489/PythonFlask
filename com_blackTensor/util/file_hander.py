import logging
import pandas as pd
import os

from com_blackTensor.util.checker import Checker

class FileHandler:
    
    @staticmethod
    def save_to_csv(savePath, saveData, columnsList, encodingStr):
        df = pd.DataFrame(saveData, columns=columnsList)
        df.to_csv(Checker.get_abs_path(savePath), index=False, encoding=encodingStr)

    @staticmethod
    def load_to_csv(filePath, encodingStr):
        return pd.read_csv(Checker.get_abs_path(filePath), encoding=encodingStr, index_col=[0])
    
    @staticmethod
    def crete_folder(path):
        os.mkdir(Checker.get_abs_path(path))