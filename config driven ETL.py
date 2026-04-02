import json
import pandas as pd



def run_pipeline(config_file):
    with open(config_file) as f:
        config = json.load(f)

    df = pd.read_csv(config["source"])

    # Transformations
    if config.get("drop_columns"):
        df = df.drop(columns=config["drop_columns"])

    if config.get("filter_column"):
        col = config["filter_column"]
        df = df[df[col] >= 0]

    # Output
    df.to_csv(config["output"], index=False)

run_pipeline("config.json")