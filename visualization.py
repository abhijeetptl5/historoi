import pandas as pd
from glob import glob
from pathlib import Path
import numpy as np
import numpy as np

    
def make_geojson(csv_path):
    colors = {'Artefact':-65536, 
              'Stroma':-16776961, 
              'Epithelial':-16711681, 
              'Adipose':-65281, 
              'Miscelleneous':-16777216, 
              'Lymphocytes':-15053542
             }
    df = pd.read_csv(csv_path)
    out_name = f'visualizations/{Path(csv_path).stem}.geojson'

    lines = "{\n"
    lines += '"type": "FeatureCollection",\n'
    lines += '"features": [\n'

    for idx, name in enumerate(df['preds'].unique()):
        lines += '{\n'
        lines += '"type": "Feature",\n'
        lines += '"geometry": {\n'
        lines += '"type": "MultiPoint",\n'
        lines += '"coordinates": [\n'

        df_ = df[df['preds']==name]
        coords = df_.values[:, :2]
        for x, y in coords[:-1]:
            lines += (f"[{x}, {y}],\n")
        lines += f"[{x}, {y}]\n"

        lines += ']\n'
        lines += '},\n'
        lines += '"properties": {\n'
        lines += '"object_type": "annotation",\n'
        lines += '"classification": {\n'
        lines += f'"name": "{name}",\n'
        lines += f'"colorRGB": {colors[name]} \n'
        lines += '},\n'
        lines += '"isLocked": false \n'
        lines += '} \n'
        if idx==df['preds'].nunique()-1:
            lines += '}\n'
        else: lines += '},\n'

    lines += ']\n'
    lines += '}\n'

    with open(out_name, 'w') as f:
        f.write(lines)
