import pintes
pint = pintes.createPint()
root = pint.generate_body()
ulRoot = pint.generate_body()
pint.create(root, 'This is a motherfucking website.', tag='h1')
pint.create(root, 'And it\'s fucking perfect.')
pint.create(root, 'Seriously, what the fuck else do you want?', tag='h2')
pint.create(root, 'You probably build websites and think your shit is special. You think your 13 megabyte parallax-ative home page is going to get you some fucking Awwward banner you can glue to the top corner of your site. You think your 40-pound jQuery file and 83 polyfills give IE7 a boner because it finally has box-shadow. Wrong, motherfucker. Let me describe your perfect-ass website:')
pint.create(ulRoot, 'Shit\'s lightweight and loads fast', tag='li')
pint.create(ulRoot, 'Fits on all your shitty screens', tag='li')
pint.create(ulRoot, 'Looks the same in all your shitty browsers', tag='li')
pint.create(ulRoot, 'The motherfucker\'s accessible to every asshole that visits your site', tag='li')
pint.create(ulRoot, 'Shit\'s legible and gets your fucking point across (if you had one instead of just 5mb pics of hipsters drinking coffee)', tag='li')


pint.div_update(root, ulRoot, tag='ul')
pint.export_to_html_file(root, 'tiamfw.html')
