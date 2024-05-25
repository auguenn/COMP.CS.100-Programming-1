"""
COMP.CS.100 tehtävä
Tekijä: Enna Augustin
Opiskelijanumero: 050235634
"""


from tkinter import *


class Userinterface:
    """
    fghjkgjhbknlm
    grhtfguhjklöcghvjbknlmögvjhbknklm
    hkjlölbkj kjlölhjkl
    """

    def __init__(self):
        """
        gvjhbknlhbkjnklm
        gvjhbknlmhbkjnlml-
        """
        self.__mainwindow = Tk()

        self.__labelA = Label(self.__mainwindow, text="weight (kg):")
        self.__labelB = Label(self.__mainwindow, text="height (cm):")

        # TODO: Create an Entry-component for the weight.
        self.__weight_value = Entry()


        # TODO: Create an Entry-component for the height.
        self.__height_value = Entry()



        # TODO: Create a Button that will call the calculate_BMI-method.
        # TODO: Change the colour of the Button to something else than
        #       the default colour.
        self.__calculate_button = Button(self.__mainwindow, text='calculate',
                                         background = 'pink', foreground = 'blue',
                                         command=self.calculate_BMI)


        # TODO: Create a Label that will show the decimal value of the BMI
        #      after it has been calculated.
        self.__result_text = Label(self.__mainwindow, text="")


        # TODO: Create a Label that will show a verbal description of the BMI
        #       after the BMI has been calculated.
        self.__explanation_text = Label(self.__mainwindow)


        # TODO: Create a button that will call the stop-method.
        self.__stop_button = Button(self.__mainwindow, text='stop', command=self.stop)


        # TODO: Place the components in the GUI as you wish.
        # If you read the Gaddis book, you can use pack here instead of grid!
        self.__weight_value.grid(row=0, column=1)
        self.__labelA.grid(row=0, column=0)
        self.__labelB.grid(row=0, column=2)
        self.__height_value.grid(row=0, column=3)
        self.__calculate_button.grid(row=1, column=2)
        self.__stop_button.grid(row=4, column=5)
        self.__result_text.grid(row=2, column=2)
        self.__explanation_text.grid(row=3, column=3)

    # TODO: Implement this method.
    def calculate_BMI(self):
        """
        Part b) This method calculates the BMI of the user and
        displays it. First the method will get the values of
        height and weight from the GUI components
        self.__height_value and self.__weight_value.  Then the
        method will calculate the value of the BMI and show it in
        the element self.__result_text.

        Part e) Last, the method will display a verbal
        description of the BMI in the element
        self.__explanation_text.
        """
        try:
            weight=int(self.__weight_value.get())
            height=int(self.__height_value.get())
            if weight <= 0 or height <= 0:
                self.__explanation_text['text'] = "Error: height and weight must be positive."
                self.reset_fields()
                return
            else:
                BMI = weight / (height / 100) ** 2
                self.__result_text['text'] = str(round(BMI,2))
        except ValueError:
            self.__explanation_text['text'] = "Error: height and weight must be numbers."
            self.reset_fields()
            return


        if BMI >= 18.5 and BMI <= 25:
            self.__explanation_text['text'] = "Your weight is normal."
        elif BMI > 25:
            self.__explanation_text['text'] = "You are overweight."
        else:
            self.__explanation_text['text'] = "You are underweight."

    # TODO: Implement this method.
    def reset_fields(self):
        """
        In error situations this method will zeroize the elements
        self.__result_text, self.__height_value, and self.__weight_value.
        """
        #self.__result_text['text'] = ""
        #self.__explanation_text['text'] = ''
        self.__height_value.delete(0, 'end')
        self.__weight_value.delete(0, 'end')

    def stop(self):
        """
        Ends the execution of the program.
        """

        self.__mainwindow.destroy()

    def start(self):
        """
        Starts the mainloop.
        """
        self.__mainwindow.mainloop()


def main():
    # Notice how the user interface can be created and
    # started separately.  Don't change this arrangement,
    # or automatic tests will fail.
    ui = Userinterface()
    ui.start()


if __name__ == "__main__":
    main()