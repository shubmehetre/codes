import matplotlib.pyplot as plt


class Visualize:
    """main class"""

    def __init__(self) -> None:
        pass
        
    def main(self):
        """main function"""

        # some data set 
        values = [1,2,3,4,5,6]
        squares = [1,4,9,16,25,36]

        # fig - entire figure. ax - single plot
        fig, ax = plt.subplots()

        # creating a simple line graph
        ax.plot(values, squares, linewidth=3)

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
