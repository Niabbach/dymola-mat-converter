import json
import os

def export_all(df, static, name):
    os.makedirs("data/csv", exist_ok=True)
    os.makedirs("data/parquet", exist_ok=True)
    os.makedirs("data/json", exist_ok=True)

    df.to_csv(f"data/csv/{name}.csv", index=False)
    df.to_parquet(f"data/parquet/{name}.parquet", index=False)

    # paramètres statiques
    with open(f"data/json/{name}_static.json", "w") as f:
        json.dump(static, f, indent=2)

    # résultats temporels
    timeseries_json = {
        "time": df["time"].tolist(),
        "signals": {
            col: df[col].tolist()
            for col in df.columns if col != "time"
        }
    }

    with open(f"data/json/{name}_timeseries.json", "w") as f:
        json.dump(timeseries_json, f, indent=2)

