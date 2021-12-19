import torch
from torch.utils.data import Dataset
import pandas as pd


class MyDataset(Dataset):
    def __init__(self, csv_file, txt_file, root_dir, other_file):
        self.csv_data = pd.read_csv(csv_file)
        with open(txt_file, 'r') as f:
            data_list = f.readlines()
        self.txt_data = data_list
        self.root_dir = root_dir

    def __len__(self):
        return len(self.csv_data)

    def __getitem__(self, item):
        data = (self.txt_data[item], self.txt_data[item])
        return data
