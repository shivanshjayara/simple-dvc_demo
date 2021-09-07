# read the data from the data source
# save it in the data/raw fro further process
# there are some gaps or space in between the words of features name

import os
import pandas as pd
from get_data import read_params, get_data
import argparse

def load_and_save(config_path):
    config = read_params(config_path)
    df = get_data(config_path)
    new_cols = [col.replace(' ','_') for col in df.columns] #creating list of the new feature columns

    # we need to save it into raw data sub folde which is in data folder
    raw_data_path = config["load_data"]["raw_dataset_csv"]
    
    df.to_csv(raw_data_path,sep=",",index=False, header=new_cols)
    


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config",default="params.yaml")  #Default coz,so that if we forget the config, it will automatically take it from params.yaml
    parsed_args = args.parse_args()
    load_and_save(config_path=parsed_args.config)
