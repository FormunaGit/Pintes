import pintes

# Create a new Pintes object
pint = pintes.createPint()

# Create the root body variable
root = pint.generate_body()

# Create an H1 tag
pint.create(root, 'Hello, World!', tag='h1')

# Not specifying a tag will default to a paragraph "p" tag.
pint.create(root, 'I am a paragraph tag')

# Creating an anchor tag (`a` tag) can't be done with the `create()` function for now. Instead, use `create_anchor()`.
pint.create_anchor(root, 'Click me!', 'https://example.com')

# Creating a div tag is a bit more complex. You need to create a new "root pint" and use that as the root for the div's children, similar to TKinter.
divRoot = pint.generate_body()
pint.create(divRoot, 'I am inside a div tag!')

# Now, update the root body variable with the div tag. Should be right above the export function.
pint.div_update(root, divRoot)

# Now, to export this.
# NOTE: Do not simply print the root variable. Instead, it's recommended to use Pintes's built-in export function.
#export = pint.export_to_html(root)
#print(export)

# You can also export to a file.
# NOTE: This will overwrite the file if it already exists.
pint.export_to_html_file(root, 'index.html')
