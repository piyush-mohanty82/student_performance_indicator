import os
import sys
import numpy as np
import pandas as pd
import dill

from src.exception import CustomException

def  save_object(file_path,obj):
    try:
        dir_path = os.path.dirname(file_path)
        #Extracts the directory from the file path.
        #Example: From 'models/model.pkl', it gets 'models'.

        os.makedirs(dir_path,exist_ok=True)
        # Creates the folder(s) if they don’t already exis
        #exist_ok=True prevents an error if the folder is already there.



        with open(file_path,"wb") as file_obj: #Opens the file in binary write mode ("wb")
            dill.dump(obj,file_obj) # Uses dill.dump() to save the object to the file.
    except Exception as e:
        raise CustomException(e,sys)
