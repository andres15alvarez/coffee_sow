import torch
import torch.nn as nn

class Classificator(nn.Module):

    def __init__(self):
        super(Classificator, self).__init__()
        
        self.layer1 = nn.Linear(5, 10)
        self.layer2 = nn.Linear(10, 20)
        self.layer3 = nn.Linear(20, 15)
        self.output = nn.Linear(15, 1)
        self.leaky_relu = nn.LeakyReLU()
        self.dropout = nn.Dropout(p=0.5)
        
    def forward(self, X):
        x = self.leaky_relu(self.layer1(X))
        x = self.dropout(x)
        x = self.leaky_relu(self.layer2(x))
        x = self.dropout(x)
        x = self.leaky_relu(self.layer3(x))
        x = self.dropout(x)
        x = self.output(x)      
        return x

def predict(temperature, humidity, altitude, rain, sunshine):
    model = Classificator()
    model.load_state_dict(torch.load('app/coffee_sow_nn.pt'))
    model.eval()
    x = torch.tensor([temperature, humidity, altitude, rain, sunshine])
    y = torch.round(torch.sigmoid(model(x))).item() 
    return y
