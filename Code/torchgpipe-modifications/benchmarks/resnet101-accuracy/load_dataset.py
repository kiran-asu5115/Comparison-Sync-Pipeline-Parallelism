import torchvision
from torch.utils.data import DataLoader
import os


def load():
    post_transforms = torchvision.transforms.Compose([
        torchvision.transforms.ToTensor(),
        torchvision.transforms.Normalize(mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225)),
    ])

    data_transform = torchvision.transforms.Compose([
        torchvision.transforms.RandomResizedCrop(224, scale=(0.08, 1.0)),
        torchvision.transforms.RandomHorizontalFlip(),
        post_transforms,
    ])

    imagenet_directory = os.path.join(os.getcwd(), "imagenet")
    train_dir = os.path.join(imagenet_directory, "train")
    test_dir = os.path.join(imagenet_directory, "val")

    train_data = torchvision.datasets.ImageFolder(root=train_dir, transform=data_transform)
    test_data = torchvision.datasets.ImageFolder(root=test_dir, transform=data_transform)

    class_names = train_data.classes

    # Turn train and test Datasets into DataLoaders
    train_dataloader = DataLoader(dataset=train_data,
                                  batch_size=1,  # how many samples per batch?
                                  num_workers=1,  # how many subprocesses to use for data loading? (higher = more)
                                  shuffle=True)  # shuffle the data?

    test_dataloader = DataLoader(dataset=test_data,
                                 batch_size=1,
                                 num_workers=1,
                                 shuffle=False)  # don't usually need to shuffle testing data

    return train_dataloader, test_dataloader


if __name__ == '__main__':
    load()
