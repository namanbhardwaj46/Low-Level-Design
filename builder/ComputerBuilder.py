from Computer import Computer

class ComputerBuilder:
    def __init__(self):
        self.gpu = None
        self.cpu = None
        self.ram = None
        self.storage = None

    def set_gpu(self, gpu):
        self.gpu = gpu
        return self

    def set_cpu(self, cpu):
        self.cpu = cpu
        return self

    def set_ram(self, ram):
        self.ram = ram
        return self

    def set_storage(self, storage):
        self.storage = storage
        return self

    def validate(self):
        if self.ram is None or self.ram <= 0:
            raise ValueError("RAM must be a positive integer")
        if self.ram > 64:
            raise ValueError("RAM cannot exceed 64GB")

    def build(self):
        self.validate()
        computer = Computer()
        computer.set_gpu(self.gpu)
        computer.set_cpu(self.cpu)
        computer.set_ram(self.ram)
        computer.set_storage(self.storage)
        return computer