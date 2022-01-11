from PIL import Image
import torch
import torchvision
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable
from torchvision import transforms, utils
import matplotlib.pyplot as plt

# Hyper Parameters
EPOCH = 10                    # use data to train with EPOCH times
BATCH_SIZE = 100
LEARNING_RATE = 0.001
DOWNLOAD_MNIST = True

train_data_path = './dataset/train_data'
test_data_path = './dataset/test_data'

train_data = torchvision.datasets.ImageFolder(train_data_path,
                                            transform=torchvision.transforms.Compose([torchvision.transforms.Grayscale(), 
                                                                                      torchvision.transforms.ToTensor()])
                                            )
test_data = torchvision.datasets.ImageFolder(test_data_path,
                                            transform=torchvision.transforms.Compose([torchvision.transforms.Grayscale(), 
                                                                                      torchvision.transforms.ToTensor()])
                                            )
 
train_loader = torch.utils.data.DataLoader(train_data, batch_size=BATCH_SIZE, shuffle=True, num_workers = 2)
test_loader = torch.utils.data.DataLoader(test_data, batch_size=50, shuffle=True, num_workers = 2)

print('Number of training images:\n'+ str(len(train_data)) + '\n')
print('Number of testing images:\n'+ str(len(train_loader)) + '\n')

print('Number of training batches:\n' + str(len(test_data)) + '\n')
print('Number of testing batches:\n' + str(len(test_loader)) + '\n')

def show_batch(imgs):
    grid = utils.make_grid(imgs,nrow=10)
    plt.imshow(grid.numpy().transpose((1, 2, 0)))
    plt.title('Batch from dataloader')
    
# dataset visualization
for i, (batch_x, batch_y) in enumerate(train_loader):
    if(i<4):
        print(batch_x.size(), '\n', batch_y.size(), '\n')
        print(batch_y[:20])
 
        show_batch(batch_x)
        plt.axis('off')
        plt.show()

# network architecture

class CNN(nn.Module):    
    # layers
    def __init__(self):
        super(CNN, self).__init__()
        
        self.conv1 = nn.Sequential(
            nn.Conv2d(
                in_channels = 1,
                out_channels = 16,
                kernel_size = 5,
                stride = 1,
                padding = 1,
            ),
            nn.ReLU(),
            nn.MaxPool2d(
                kernel_size = 2,
            ),
        )
        
        self.conv2 = nn.Sequential(
            nn.Conv2d(16, 32, 5, 1, 2),
            nn.ReLU(),
            nn.MaxPool2d(2),
        )
        
        self.out = nn.Linear(32 * 12 * 12, 4)
    
    # connections
    def forward(self, x):
        x = self.conv1(x)
        x = self.conv2(x)
        x = x.view(x.size(0), -1)
        output = self.out(x)
        return output     

# network instantiation and visualization
cnn = CNN()
print(cnn)

# training
counter = 0
plot_x = []
plot_loss = []
accu = []
plot_accuracy = []

optimizer = torch.optim.Adam(cnn.parameters(), lr = LEARNING_RATE)
#scheduler = torch.optim.lr_scheduler.ExponentialLR(optimizer, gamma=0.8) # exponential decent learning rate
loss_func = nn.CrossEntropyLoss()

for epoch in range(EPOCH):
    for step, (x, y) in enumerate(train_loader):
        batch_x = Variable(x)
        batch_y = Variable(y)
        
        output = cnn(batch_x)
        loss = loss_func(output, batch_y)
        optimizer.zero_grad()                  # clear gradients for this training step
        loss.backward()                        # back propagation, compute gradients
        optimizer.step()
        #scheduler.step()
        
        if step%10 == 0:
            for (test_x, test_y) in (test_loader):
                test_output = cnn(test_x)
                prediction_y = torch.max(test_output, 1)[1].data.squeeze()
                accuracy = sum(prediction_y == test_y).numpy()/test_y.size(0)
                accu.append(accuracy)
                print('Epoch:', epoch, '| train loss: %.4f' % loss.item(), '| test accuracy: %4f' % accuracy)
        if step%10 == 0:
            plot_x.append(counter)
            plot_loss.append(loss.item())
            plot_accuracy.append(sum(accu)/len(accu)) # record average accuracy
            
        counter = counter + 1

print('Training complete')

# visualization
fig,ax1 = plt.subplots()
ax2 = ax1.twinx()           # mirror
ax1.plot(plot_x, plot_loss, 'r-')
ax2.plot(plot_x, plot_accuracy, 'b-')
 
ax1.set_xlabel('training step')    #x label title
ax1.set_ylabel('loss',color = 'r')   #y1 label title
ax2.set_ylabel('accuracy',color = 'b')   #y2 label title

# save model
torch.save(cnn, 'net.pkl')