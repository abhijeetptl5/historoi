import json
import pandas as pd
from pathlib import Path


def make_geojson(csv_path):
    colors = {
        'Artefact': -65536,
        'Stroma': -16776961,
        'Epithelial': -16711681,
        'Adipose': -65281,
        'Miscelleneous': -16777216,
        'Lymphocytes': -15053542
    }
    
    df = pd.read_csv(csv_path)

    features = []
    for label, group in df.groupby('preds'):
        coords = group.iloc[:, :2].values.tolist()
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "MultiPoint",
                "coordinates": coords
            },
            "properties": {
                "object_type": "annotation",
                "classification": {
                    "name": label,
                    "colorRGB": colors[label]
                },
                "isLocked": False
            }
        }
        features.append(feature)

    geojson = {
        "type": "FeatureCollection",
        "features": features
    }

    out_path = Path("visualizations")
    out_path.mkdir(parents=True, exist_ok=True)
    out_file = out_path / f"{Path(csv_path).stem}.geojson"

    with open(out_file, "w") as f:
        json.dump(geojson, f, indent=4)
