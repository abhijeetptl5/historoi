import argparse

def infer_options():
    parser = argparse.ArgumentParser()
    help_str = "Path of WSI (/dir1/dir2/dir3/wsi.svs) " 
    help_str += "OR Path of directory containing WSIs (/dir1/dir2/dir3/) "
    help_str += "OR Paths with wildcards (/dir1/dir2/dir3/*.svs)"
    parser.add_argument("--wsis", help=help_str, type=str, metavar='')
    
    help_str = "Directory to save model probabilities in CSV format"
    parser.add_argument("--csv_dir", help=help_str, type=str, default='./csvs', metavar='')
    
    help_str = "Stride at 10x in X and Y direction. (stride=256 ==> no overlap)"
    parser.add_argument("--stride", help=help_str, type=int, default=128, metavar='')
    
    parser.add_argument("--device", help="cpu / cuda[gpu_ud]", type=str, default='cuda', metavar='')
    parser.add_argument("--batch_size", help="Batch size", type=int, default=256, metavar='')
    parser.add_argument("--workers", help="num_workers for data loader", type=int, default=4, metavar='')
    
    help_str = "Magnification at level 0. If provided through arguments, provided value is used otherwise fetched from WSI properties"
    parser.add_argument("--magni_0", help=help_str, type=int, default=None, metavar='')
    
    help_str = "If true, patches from level 0 are extracted, resized and given as input to model. magnification of other levels are not used."
    parser.add_argument("--use_level_0", help=help_str, action='store_true')
    
    help_str = "If true, geojson file compatible to QPath is generated"
    parser.add_argument("--vis", help=help_str, action='store_true')
    
    help_str = "Level corrosponding to 10x magnification .If provided, patches from given level are extracted without reading WSI properties."
    parser.add_argument("--level_10x", help=help_str, type=int, default=None, metavar='')
    
    help_str = "Checkpoint for six class classification model"
    model6_path = 'weights/model_6.pt'
    parser.add_argument("--model6", help=help_str, type=str, default=model6_path, metavar='')
    
    parser.add_argument("--skip_if_present", help=help_str, action='store_true')
    
    return parser.parse_args()
