from openslide import OpenSlide
import numpy as np
from pathlib import Path
import torch
from torchvision import models
from torchvision import transforms
from utils import filtered_patches
from utils import get_metadata
from torch.utils.data import DataLoader
from tqdm import tqdm
from dataset import WSIDataset
import sys
from args import infer_options
from glob import glob
import os
from visualization import make_geojson

args = infer_options()

device = args.device

model6 = models.resnet18().to(device)
model6.fc = torch.nn.Linear(512, 6).to(device)
model6.load_state_dict(torch.load(args.model6, map_location=device))
model6.eval()

sm = torch.nn.Softmax(dim=1)
bs = args.batch_size
wsis = sorted(glob(args.wsis))

for w in wsis:
    if True:
    # try:
        print()
        print(f'processing {w}...')
        wsi = OpenSlide(w)
        csv_path = Path(args.csv_dir) / f"{Path(w).stem}.csv"

        if args.skip_if_present and csv_path.is_file(): continue

        level, ps = get_metadata(wsi, args)
        df = filtered_patches(wsi, args)
        print(f'batches = {1+len(df)//args.batch_size}')
        base_transform = transforms.Compose([transforms.Resize(256), transforms.ToTensor()])
        ds = WSIDataset(df, wsi, base_transform, level=level, ps=ps)
        dl = DataLoader(ds, batch_size=bs, shuffle=False, num_workers=args.workers)
        probs = np.zeros((len(ds), 6))
        with torch.no_grad():
            for i, data in tqdm(enumerate(dl)):
                out = model6(data.to(device))
                probs[bs*i:bs*i+data.shape[0], :6] = sm(out).cpu().numpy()


        names = ['Epithelial', 'Stroma', 'Adipose', 'Artefact', 'Miscelleneous', 'Lymphocytes']
        maps = {idx:name for idx, name in enumerate(names)}
        df['preds'] = np.argmax(probs, axis=1)
        df['preds'] = df['preds'].map(maps)

        if not Path(args.csv_dir).is_dir(): os.makedirs(args.csv_dir)
        df.to_csv(csv_path, index=False)
        if args.vis:
            make_geojson(csv_path)
