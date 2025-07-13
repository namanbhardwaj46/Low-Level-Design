from ComputerBuilder import ComputerBuilder
class Director:
    def __init__(self):
        self._builder = ComputerBuilder()

    def construct(self, ram, storage, gpu, cpu):
        try:
            self._builder.set_ram(ram).set_storage(storage).set_gpu(gpu).set_cpu(cpu)
            return self._builder.build()
        except ValueError as e:
            print(f"Error constructing computer: {e}")
            return None