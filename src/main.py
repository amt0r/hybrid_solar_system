import pandas
import tkinter

from insolation_api import InsolationAPI
from hybrid_system import HybridSystem
from seaborn_plotter import Plotter
from main_window import MainWindow
from csv_save import CsvSave


def main():
    root = tkinter.Tk()
    gui = MainWindow(root)

    gui.run()
    latitude, longitude, year_usage, generate, year, kW_price = gui.get_user_inputs()
    if not(year_usage): return
    
    insolation_data = InsolationAPI().get_insolation(latitude, longitude, year)
    hybrid_system = HybridSystem(year_usage, generate, kW_price)
    
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Avg']

    calculated_usage_data = hybrid_system.calculate_usage_months()
    calculated_generated_data = hybrid_system.calculate_generated_energy(insolation_data)
    calculated_efficency_data = [(gen / use) * 100 for use, gen in zip(calculated_usage_data, calculated_generated_data)]
    calculated_usage_price_data = hybrid_system.calculate_usage_price()
    calculated_saved_money_data = hybrid_system.calculate_saved_money()
    calculated_efficency_money_data = [(gen / use) * 100 if use!=0 else 0 for use, gen in zip(calculated_usage_price_data, calculated_saved_money_data)]

    data_usage = {
        "Months": months,
        "kW": calculated_usage_data
    }
    data_generated = {
        "Months": months,
        "kW": calculated_generated_data
    }
    data_price = {
        "Months": months,
        "Money": calculated_usage_price_data
    }
    data_efficency = {
        "Months": months,
        "%": calculated_efficency_data
    }
    data_saved_money = {
        "Months": months,
        "Money": calculated_saved_money_data
    }
    data_money_efficency = {
        "Months": months,
        "%": calculated_efficency_money_data
    }

    df_usage = pandas.DataFrame(data_usage)
    df_generated = pandas.DataFrame(data_generated)
    df_price = pandas.DataFrame(data_price)
    df_efficency = pandas.DataFrame(data_efficency)
    df_saved_money = pandas.DataFrame(data_saved_money)
    df_money_efficency = pandas.DataFrame(data_money_efficency)

    print(df_usage, df_generated, df_price, df_saved_money, df_efficency, df_money_efficency, sep="\n\n")
    
    to_csv = CsvSave()
    to_csv.add_save(df_usage, "Used_energy_kW")
    to_csv.add_save(df_generated, "Solar_panel_genetated_kW")
    to_csv.add_save(df_price, "Price_per_month")
    to_csv.add_save(df_saved_money, "Saved_money")
    to_csv.add_save(df_efficency, "Percent_of_generated_energy")
    to_csv.add_save(df_money_efficency, "Percent_of_saved_money")
    to_csv.save()

    plotter = Plotter()
    plotter.add_plot(df_usage, "Months", "kW", "Used energy")
    plotter.add_plot(df_generated, "Months", "kW", "Solar panel genetated")
    plotter.add_plot(df_efficency, "Months", "%", "Percent of generated energy")
    plotter.add_plot(df_price, "Months", "Money", "Price per month")
    plotter.add_plot(df_saved_money, "Months", "Money", "Saved money")
    plotter.add_plot(df_money_efficency, "Months", "%", "Percent of saved money")
    plotter.show_plots()


if __name__ == "__main__":
    main()