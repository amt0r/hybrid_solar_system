from system import System


class HybridSystem(System):
    def __init__(self, year_usage, rated_power_solar, kW_price):
        super().__init__(year_usage, kW_price)
        self.rated_power_solar = rated_power_solar
        self.generate_by_month = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def calculate_generated_energy(self, insolation_by_month):
        self.generate_by_month = [30 * self.rated_power_solar * insolation for insolation in insolation_by_month]
        return self.generate_by_month
    
    def calculate_saved_money(self):
        price_by_month_saved=[]

        for month_genetated, month_price in zip(self.generate_by_month, self.price_by_month):
            money_saved = self.price_kilowatt_hour * month_genetated
            price_by_month_saved.append(min(money_saved, month_price))
        
        return price_by_month_saved
    