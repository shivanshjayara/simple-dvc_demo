## read the parameters
## process it
## return the data frame

import os
import yaml
import pandas as pd
import argparse

def read_params(config_path):      # func for reading the configuration  file i.e. .yaml file 
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config


def get_data(config_path):   # fun for getting the data  and passing the configuration path and reading those config
    config = read_params(config_path)
    print(config)
    data_path = config["data_source"]["s3_source"]
    df = pd.read_csv(data_path, encoding = 'utf-8')
    print(df.head())

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config",default="params.yaml")  #Default coz,so that if we forget the config, it will automatically take it from params.yaml
    parsed_args = args.parse_args()
    get_data(config_path=parsed_args.config)