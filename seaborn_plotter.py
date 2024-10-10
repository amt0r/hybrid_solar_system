import seaborn as sns
import matplotlib.pyplot as plt


class Plotter:
    def __init__(self):
        sns.set_style("darkgrid", {"axes.facecolor": "black", "grid.color": "gray"})

        plt.rcParams['axes.labelcolor'] = 'white'
        plt.rcParams['xtick.color'] = 'white'
        plt.rcParams['ytick.color'] = 'white'
        plt.rcParams['text.color'] = 'white'
        plt.rcParams['axes.titlecolor'] = 'white'
        plt.rcParams['figure.facecolor'] = 'black'
        plt.rcParams['axes.facecolor'] = 'black'

        self.plots = []

    def add_plot(self, data, x, y, title):
        self.plots.append((data, x, y, title))

    def show_plots(self):
        num_plots = len(self.plots)
        if num_plots < 2:
            data, x, y, title = self.plots[0]
            sns.barplot(x=x, y=y, data=data)
            plt.title(title)
            plt.show()
        else:
            cols = 2
            rows = (num_plots + 1) // cols

            fig, axs = plt.subplots(cols, rows, figsize=(5 * rows, 5 * cols))
            axs = axs.flatten()
            
            for ax, (data, x, y, title) in zip(axs, self.plots):
                sns.barplot(x=x, y=y, data=data, ax=ax, color='pink')
                ax.set_title(title)
            
            for ax in axs[num_plots:]:
                ax.axis('off')

            plt.tight_layout()
            plt.show()