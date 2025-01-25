"""
Pintes
~~~~~~~~~~~~~~~~
*An amalgamation of horror.*
Pintes is a Python module designed to generate static HTML pages.
"""
# Imports (none yet :3)

# Variables
__author__ = "Formuna"
__version__ = "0.1:PRERELEASE"

# Classes
class Pint:
    def __init__(self):
        print('What are you doing?')
    @staticmethod
    def test():
        """
        Test if Pintes is working + get the version.
        """
        print(f'Pintes v{__version__} by {__author__}')
    @staticmethod
    def generate_body(parent: list = []):
        """
        Generate an empty list for the body of the HTML page.
        """
        vanillapageBODY: list = []
        return vanillapageBODY
    # Here is where the tag creation functions will go.
    @staticmethod
    def div_update(root: list, divRoot: list, tag: str = 'div'): # TODO: remove this if possible
        """
        Update the root body variable with a div tag.
        `root` is the root body variable. (creatable with `generate_body()`)
        `divRoot` is the root body variable for the div tag. (also creatable with `generate_body()`)
        """
        root.append(f'<{tag}>{"".join(divRoot)}</{tag}>')
    @staticmethod
    def create(root: list, text: str = 'UNNAMED', className: str = '', tag: str = 'p'):
        """
        Create an H1 tag.
        `root` is the root body variable. (creatable with `generate_body()`)
        `text` is the text inside the H1 tag.
        `className` is the class of the H1 tag. Optional.
        """
        root.append(f'<{tag} class={className}>{text}</{tag}>')
    @staticmethod
    def create_anchor(root: list, text: str = 'UNNAMED', href: str = '#', className: str = ''):
        """
        Create an anchor tag.
        `root` is the root body variable. (creatable with `generate_body()`)
        `text` is the text inside the anchor tag.
        `href` is the href of the anchor tag.
        `className` is the class of the anchor tag. Optional.
        """
        root.append(f'<a href={href} class={className}>{text}</a>')


    # Export function
    @staticmethod
    def export_to_html(root: list):
        """
        Export the root body variable to HTML.
        This will return a string, good for PyWebview.
        If you want to write to a file, use `export_to_html_file()`.
        `root` is the root body variable. (creatable with `generate_body()`)
        """
        html = ''.join(root)
        return f'<!DOCTYPE html><html><head></head><body> {html} </body></html>'
    @staticmethod
    def export_to_html_file(root: list, filename: str = 'index.html'):
        """
        Export the root body variable to an HTML file.
        `root` is the root body variable. (creatable with `generate_body()`)
        `filename` is the name of the file. Default is `index.html`.
        """
        html = ''.join(root)
        with open(filename, 'w') as file:
            file.write(f'<!DOCTYPE html><html><head></head><body> {html} </body></html>')
        print(f'Exported to {filename}!')

# Functions
def createPint():
    return Pint

# Just in case someone wants to run this file.
if __name__ == '__main__':
    print('What are you doing? Run demo.py instead.')
