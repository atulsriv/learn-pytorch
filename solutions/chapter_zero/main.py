import torch

def create_tensor():
    scalar = torch.Tensor(7)
    print(scalar.name)
    print(scalar.item())







if __name__ == "__main__":
    create_tensor()