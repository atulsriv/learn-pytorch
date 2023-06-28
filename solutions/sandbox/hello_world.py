import torch
def print_version():
    print(f'torch version: {torch.__version__}')


def random_torch():
    x = torch.rand(5, 3)
    print(x)


if __name__ == "__main__":
    print_version()
    random_torch()
