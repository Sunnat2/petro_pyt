from abc import ABC, abstractmethod
from collections import deque

class QueueBehaviour(ABC):
    @abstractmethod
    def take_in_queue(self, person):
        pass

    @abstractmethod
    def release_from_queue(self):
        pass

    @abstractmethod
    def process_queue(self):
        pass

class MarketBehaviour(ABC):
    @abstractmethod
    def accept_order(self, order):
        pass

    @abstractmethod
    def deliver_order(self):
        pass

class Market(QueueBehaviour, MarketBehaviour):
    def init(self):
        self.queue = deque()
        self.orders = []

    def take_in_queue(self, person):
        self.queue.append(person)
        print(f"{person} added to queue")

    def release_from_queue(self):
        if self.queue:
            person = self.queue.popleft()
            print(f"{person} removed from queue")
            return person
        else:
            print("Queue is empty")
            return None

    def process_queue(self):
        if self.queue:
            person = self.queue[0]
            print(f"Processing {person} in queue")
            # Simulate processing
        else:
            print("Queue is empty")

    def accept_order(self, order):
        self.orders.append(order)
        print(f"Order {order} accepted")

    def deliver_order(self):
        if self.orders:
            order = self.orders.pop(0)
            print(f"Order {order} delivered")
            return order
        else:
            print("No orders to deliver")
            return None

    def update(self):
        print("Updating market state...")
        self.process_queue()
        self.deliver_order()

# Пример использования класса Market
if __name__ == "main":
    market = Market()
    
    # Работа с очередью
    market.take_in_queue("Alice")
    market.take_in_queue("Bob")
    market.process_queue()
    market.release_from_queue()
    
    # Работа с заказами
    market.accept_order("Order1")
    market.accept_order("Order2")
    market.deliver_order()
    
    # Обновление состояния магазина
    market.update()
    market.update()