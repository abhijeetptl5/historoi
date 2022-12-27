# historoi
contains inference codes for historoi, training data used for historoi and tcga-tissue dataset


This repository provides inference code for histoROI model.
HistoROI is a six class classification model with classes:
1. Epithelial region
2. stromal region
3. Adipose / Scattered stroma, etc
4. Artefacts
5. Miscelleneous
6. Lymphocyte dense region

'inference.py' generates a CSV file with 3 columns, 2 columns for xy coordinates of WSI and third column corrosponds to prediction of a model for patch around xy coordinates

To run a model, run:
**inference.py** by passing the following arguments:
*  `--wsis`: Path of WSI (/dir1/dir2/dir3/wsi.svs) OR Path of directory containing WSIs (/dir1/dir2/dir3/) OR Paths with wildcards (/dir1/dir2/dir3/*.svs)
*  `--csv_dir`: Directory to save model probabilities in CSV format
*  `--stride`: Stride at 10x in X and Y direction. (stride=256 ==> no overlap)
*  `--batch_size`: batch_size
*  `--workers`: workers
*  `--magni_0`: Magnification at level 0. If provided through arguments, provided value is used otherwise fetched from WSI properties
*  `--use_level_0`: If true, patches from level 0 are extracted, resized and given as input to model. magnification of other levels are not used.
*  `--vis`: If true, geojson file compatible to QPath is generated
*  `--level_10x`: Level corrosponding to 10x magnification .If provided, patches from given level are extracted without reading WSI properties.
*  `--model6`: weights for HistoROI model

Model can be downloaded from [here](https://drive.google.com/file/d/1-nFuLI55PjI_v_0liRIka8PpuhGqO72a/view?usp=sharing).

A typical command line for running the inference looks like
`python inference.py --wsis /path/to/wsis`
