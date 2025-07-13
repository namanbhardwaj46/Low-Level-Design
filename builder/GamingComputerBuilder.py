from .Computer import Computer

class GamingComputerBuilder:
    def __init__(self):
        self.gpu = None
        self.cpu = None
        self.ram = None
        self.storage = None

    def set_gpu(self, gpu):
        if gpu is None and self.gpu<"2gb":
            raise ValueError("GPU must be specified for a gaming computer")
        self.gpu = gpu
        return self

    def set_cpu(self, cpu):
        self.cpu = cpu
        return self

    def set_ram(self, ram):
        if ram is None or ram <= 0:
            raise ValueError("RAM must be a positive integer")
        if ram > 64:
            raise ValueError("RAM cannot exceed 64GB")
        self.ram = ram
        return self

    def set_storage(self, storage):
        self.storage = storage
        return self

    def build(self):
        computer = Computer()
        computer.set_gpu(self.gpu)
        computer.set_cpu(self.cpu)
        computer.set_ram(self.ram)
        computer.set_storage(self.storage)
        return computer