from parser import scrap_all_pages, URL

scrapper = ''
run = 0

while scrapper != ('y') or scrapper != ('n'):
    scrapper = input('Do you want to start parsing {}? (y/n) \n'.format(URL))
    if scrapper == 'y':
        scrap_all_pages(URL)
    elif scrapper == 'n':
        break
    else:
        scrapper = input('Invalid choice! Type "y" or "n" \n')

while run != 'exit':
    run = input('Type author id (or "exit"): \n')
    print(run)
