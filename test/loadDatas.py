from myDataset import MyDataset
from torch.utils.data import DataLoader

ds = MyDataset('csv.txt', 'csv.txt', '', '')
dataiter = DataLoader(ds, batch_size=3, shuffle=True)

for(i, j) in dataiter:
    print(i)
    print(j)
