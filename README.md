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

Model weights can be downloaded from `weights` directory (set as default argument for `--model6`).

A typical command line for running the inference looks like
`python inference.py --wsis /path/to/wsis`


## Citation

If you use this work, please cite:

```bibtex
@article{patil2023efficient,
  title={Efficient quality control of whole slide pathology images with human-in-the-loop training},
  author={Patil, Abhijeet and Diwakar, Harsh and Sawant, Jay and Kurian, Nikhil Cherian and Yadav, Subhash and Rane, Swapnil and Bameta, Tripti and Sethi, Amit},
  journal={Journal of Pathology Informatics},
  pages={100306},
  year={2023},
  publisher={Elsevier}
}
