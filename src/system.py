class System:
    def __init__(self, year_usage):
        self.month_coefficients_usage = [1.46, 1.28, 1.10, 0.91, 0.73, 0.66, 0.59, 0.62, 0.80, 1.02, 1.28, 1.54, 1]
        self.price_kilowatt_hour = 4.32
        self.year_usage = year_usage
        self.usage_by_month = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.price_by_month = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def calculate_usage_months(self):
        average_month_usage = self.year_usage/12
        self.usage_by_month = [average_month_usage * coeff for coeff in self.month_coefficients_usage]
        return self.usage_by_month
    
    def calculate_usage_price(self):
        self.price_by_month = [self.price_kilowatt_hour * month_usage for month_usage in self.usage_by_month]
        return self.price_by_month