from abc import ABC
from traceback import print_tb


class Transport(ABC):

    def deliver(self):
        pass


# concreate objects..
class Truck(Transport):
    def deliver(self):
        return "Delivering by land in a box"

class Ship(Transport):
    def deliver(self):
        return "Delivering by sea in a container"

class Airplane(Transport):
    def deliver(self):
        return "Delivering by air in a package"


class Auto(Transport):
    def deliver(self):
        return "Delivering by road in a vehicle"

class TransportFactoryAbc(ABC):
    @staticmethod
    def create_transport(types):
        pass


class TransportFactory(TransportFactoryAbc):

    @staticmethod
    def create_transport(types):

        if types == "road":
            return Auto()
        elif types == "sea":
            return Ship()
        elif types == "air":
            return Airplane()

        else:
            return None


if __name__ == "__main__":
    transport_way = "sea"
    transport = TransportFactory.create_transport(transport_way)
    print(transport.deliver())