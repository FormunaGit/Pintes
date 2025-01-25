import pintesrework

root = pintesrework.CreatePint()

root.create('Hello, World!', tag='h1')
root.create('I am a paragraph tag')
root.create_anchor('Click me!', 'https://example.com')

root.export_to_html_file('rework.html')
