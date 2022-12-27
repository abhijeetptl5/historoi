from torch.utils.data import Dataset

class WSIDataset(Dataset):
    def __init__(self, df, wsi, transform, level, ps):
        self.wsi = wsi
        self.transform = transform
        self.df = df
        self.level = level
        self.ps = ps

    def __len__(self):
        return len(self.df)

    def __getitem__(self, idx):
        x, y = self.df.iloc[idx, 0]-512, self.df.iloc[idx, 1]-512
        if x<0: x=0
        if y<0: y=0
        patch = self.wsi.read_region((x, y), self.level, (self.ps, self.ps))
        patch = self.transform(patch.convert('RGB'))
        return patch
