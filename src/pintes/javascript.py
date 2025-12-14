"""
Pintes JavaScript Module.

An even worse amalgamation.
Made to give the user Python functions that replicate JS functions.
"""


class PJS:
    """
    An even worse amalgamation.

    Allows Pintes pages to use JavaScript functions in a more Python-like way.
    """

    def __init__(self, RootPint):
        """
        Idk why I need to add a docstring here, Emacs is annoying but fun.

        Also why do I have to add a period to every sentence in it?
        """
        self.rootclass = RootPint

    def alert(self, message: str):
        """
        PJS.Alert().

        Takes in a string of text in the message variable and
        directly injects JavaScript code into the pint.
        """
        self.rootclass.top_js.append(f'alert("{message}")')


# Creating an instance with an argument
instance = PJS(RootPint="Formuna")

print(instance.rootclass)  # Output: Formuna
