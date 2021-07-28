import csv
from PIL import Image
import torch
from torchvision import transforms
from torch.utils.data import DataLoader
import torch.nn as nn 
import torch.nn.functional as F
import torchvision.models as models

class LeafResnet(nn.Module):
    def __init__(self):
        super().__init__()

        # get Restnet
        self.resnet50 = models.resnet50(pretrained=False)
        num_ftrs = self.resnet50.fc.in_features
        self.resnet50.fc = nn.Linear(num_ftrs, 1024)

        self.cate_model = nn.Sequential(
			nn.Linear(1024, 1024),
			nn.BatchNorm1d(1024),
			nn.ReLU(),
			nn.Dropout(),
			#total 10 categorys
			nn.Linear(1024, 10),
	 		nn.Softmax(dim = 1)
	    )
        
    def forward(self, x): 
        if not isinstance(x, torch.Tensor):
            print(x)
            x = torch.Tensor(x)
        out = self.resnet50(x)
        out = self.cate_model(out)
        return out

class LeafData(torch.utils.data.Dataset):
    def __init__(self, path):
        self.path = path
        self.leaf_transforms = transforms.Compose([ transforms.ToTensor(),])

    def __getitem__(self, index):
        data = Image.open(self.path)
        data = self.leaf_transforms(data)
        return data
    
    def __len__(self):
        return 1

def get_idxtoclass():
    idx_to_class = {}
    with open('../leafmodel/Tomato_class_to_idx.csv', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            idx_to_class[row['idx']] = row['category']
    return idx_to_class

def leaf_predict(path):
    leafset = LeafData(path)
    leaf_loader = DataLoader(leafset , batch_size=1)
    device = torch.device('cpu')
    model = LeafResnet()
    model.load_state_dict(torch.load('../leafmodel/leafillness.pt', map_location=device))
    model.eval()
    idx_to_class = get_idxtoclass()
    with torch.no_grad():
        for image in leaf_loader:
            out = model(image)
            #_, max_cate = torch.max(out.data, 1)
            res = {idx_to_class[str(idx)] : round(value.item(),6) for idx, value in enumerate(out.squeeze())}
    return res


if __name__ == '__main__':
    
    res = leaf_predict('leaf.JPG')
    for k, v in res.items():
        print(f'{k} -> {round(v,5)}')