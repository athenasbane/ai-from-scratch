import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

# hyperparameters
BATCH_SIZE = 64
LEARNING_RATE = 1e-3
EPOCHS = 5

# device 
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# data 
transform = transforms.ToTensor()

train_dataset = datasets.MNIST(
    root="data",
    train=True,
    transform=transform,
    download=True
)

test_dataset = datasets.MNIST(
    root="data",
    train=False,
    transform=transform,
    download=True
)

train_loader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=BATCH_SIZE)


# model 
model = nn.Sequential(
    nn.Flatten(),
    nn.Linear(784, 128),
    nn.ReLU(),
    nn.Linear(128, 64)
).to(device)

# loss and optimizer
loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=LEARNING_RATE)

# training loop
for epoch in range(EPOCHS):
    model.train()
    total_loss = 0
    for x, y in train_loader:
        x, y = x.to(device), y.to(device)

        logits = model(x)
        loss = loss_fn(logits, y)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        total_loss += loss.item()
    
    avg_loss = total_loss / len(train_loader)
    print(f"Epoch [{epoch+1}/{EPOCHS}], Loss: {avg_loss:.4f}")

# evaluation
model.eval()
correct, total = 0, 0

with torch.no_grad():
    for x, y in test_loader:
        x, y = x.to(device), y.to(device)
        logits = model(x)
        predictions = torch.argmax(logits, dim=1)

        correct += (predictions == y).sum().item()
        total += y.size(0)

accuracy = correct / total
print(f"Test Accuracy: {accuracy:.4f}")