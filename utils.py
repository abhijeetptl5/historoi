import numpy as np
from torchvision import transforms
import pandas as pd

def ccrop(crop_size):
    transforms_ =  transforms.Compose([
            transforms.CenterCrop(crop_size),
            transforms.ToTensor()
    ])
    return transforms_

def filtered_patches(wsi, args):
    h, w = wsi.dimensions
    if args.magni_0: magni_0 = args.magni_0
    else: magni_0 = round(10/float(wsi.properties['openslide.mpp-x']))
    stride = round(args.stride*(magni_0/10))
    thumb = np.array(wsi.get_thumbnail((h//stride, w//stride)).convert('L'))
    arr = np.logical_and(thumb < 240, thumb > 20)
    df = pd.DataFrame(columns=['dim1', 'dim2'])
    df['dim1'], df['dim2'] = stride*np.where(arr)[1]+(stride//2), stride*np.where(arr)[0]+(stride//2)
    return df

def get_metadata(wsi, args):
    if args.level_10x: return args.level_10x, 256
    if args.magni_0: magni_0 = args.magni_0
    else: magni_0 = round(10/float(wsi.properties['openslide.mpp-x']))
    if args.use_level_0: 
        level = 0
        ps = round(256*magni_0/10)
        return level, ps
    ds = round(1/float(wsi.properties['openslide.mpp-x']))
    level = wsi.get_best_level_for_downsample(ds+0.1)
    level_ds = float(wsi.properties[f'openslide.level[{level}].downsample'])
    ps = round((256*magni_0/10)/level_ds)
    return level, ps
