class Asset:
    def __init__(self, worth):
        self.worth = worth

    def calculate_tax(self):
        return 0


class Apartment(Asset):
    def __init__(self, worth):
        super().__init__(worth)

    def calculate_tax(self):
        return self.worth / 1000


class Car(Asset):
    def __init__(self, worth):
        super().__init__(worth)

    def calculate_tax(self):
        return self.worth / 200


class CountryHouse(Asset):
    def __init__(self, worth):
        super().__init__(worth)

    def calculate_tax(self):
        return self.worth / 500


assets_worth = float(input("Введите стоимость вашего имущества: "))

apartment = Apartment(assets_worth)
car = Car(assets_worth)
country_house = CountryHouse(assets_worth)

taxes = [asset.calculate_tax() for asset in [apartment, car, country_house]]

total_tax = sum(taxes)

for asset, tax in zip([apartment, car, country_house], taxes):
    print(f"Налог на {asset.worth}: {tax}")

print(f"Общий налог: {total_tax}")

money = float(input("Введите количество ваших денег: "))

if money < total_tax:
    print(f"Вам не хватает {total_tax - money} денег")
else:
    print("У вас достаточно денег для уплаты налогов")