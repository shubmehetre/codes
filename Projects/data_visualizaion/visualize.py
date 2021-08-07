import matplotlib.pyplot as plt


class Visualize:
    """main class"""

    def __init__(self) -> None:
        pass
        
    def main(self):
        """main function"""

        # some data set 
        x_values = range(1, 1001)
        squares = [x**2 for x in x_values]

        # use styles pre-defined inside matplotlib.pyplot.style
        plt.style.use('seaborn')

        # fig - entire figure. ax - single plot
        fig, ax = plt.subplots()

        # scatter() - plot points 

        ax.scatter(x_values,squares,c=squares,cmap=plt.cm.Blues, s=10)
                

        # plot - creates a line graph
        ax.plot(x_values, squares, linewidth=1)

        # set viewer title and label axes
        ax.set_title("Random shit", fontsize=20)
        ax.set_xlabel("Value number", fontsize=12)
        ax.set_ylabel("my data", fontsize=12)

        # tick labels
        ax.tick_params(axis='both', labelsize=14)


        self.display_viewer()


    def display_viewer(self):
        """display the screen"""
        # show the matplotlib viewer
        plt.show()

if __name__ == "__main__":
    """call main if this program is run"""
    visual = Visualize()
    visual.main()
