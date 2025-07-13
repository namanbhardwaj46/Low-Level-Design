

if __name__ == '__main__':

    ram = 10
    storage = "1TB SSD"
    gpu = "NVIDIA RTX 3080"
    cpu = "Intel Core i9-11900K"

    import Director
    computer = Director.Director().construct(ram, storage, gpu, cpu)

    print(computer)

