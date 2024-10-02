import torch
import torch.nn as nn

class LeNet_v1(nn.Module):
    def __init__(self, ) -> None:
        super().__init__()
        self.net = nn.Sequential(
            nn.Conv2d(1, 6, 5),
            nn.Sigmoid(),
            nn.MaxPool2d(2, 2),
            nn.Conv2d(6, 16, 5),
            nn.Sigmoid(),
            nn.MaxPool2d(2, 2),
            nn.Flatten(),
            nn.LazyLinear(120),
            nn.Sigmoid(),
            nn.Linear(120, 84),
            nn.Sigmoid(),
            nn.Linear(84, 10),
        )

    def forward(self, x):
        return self.net(x)
    

class LeNet_v2(nn.Module):
    def __init__(self, ) -> None:
        super().__init__()
        self.conv1 = nn.Conv2d(1, 6, 5)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.pool = nn.MaxPool2d(2, 2)
        self.flattener = nn.Flatten()
        self.fc1 = nn.LazyLinear(120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)
    
    def forward(self, x):
        x = self.pool(nn.functional.sigmoid((self.conv1(x))))
        x = self.pool(nn.functional.sigmoid((self.conv2(x))))
        x = self.flattener(x)
        x = nn.functional.sigmoid(self.fc1(x))
        x = nn.functional.sigmoid(self.fc2(x))
        x = self.fc3(x)
        return x
    

if __name__ == '__main__':
    x = torch.randn(1, 1, 28, 28)
    model1 = LeNet_v1()
    model2 = LeNet_v2()
    print(model1(x).shape)
    print(model2(x).shape)