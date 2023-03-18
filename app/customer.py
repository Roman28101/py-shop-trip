from dataclasses import dataclass


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: list[int]
    money: float

    def customer_info(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    def shop_visit(self, shop_name: str, cost: float) -> None:
        print(f"{self.name}'s trip to the {shop_name} costs {cost}")

    def change_location(self, destination: list) -> None:
        self.location = destination

    def come_back_home(self, spent_money: float) -> None:
        print(f"{self.name} rides home\n"
              f"{self.name} now has {self.money - spent_money} dollars\n")