from parser import scrap_all_pages, URL, converting, saved_data_list, \
    print_authors

# interface to make scrapping
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

converting(saved_data_list)  # convert parsed data to file

# interface to take info about authors
ids = []
nums = 1
while nums > 0:
    nums = int(input('How many authors you need? (press "0" to exit)\n'))
    for num in range(0, nums):
        id = int(input('Type author id (1-100)\n'))
        ids.append(id)
    nums -= 1
    if nums == 0:
        break

    print_authors(ids)  # printing data about authors
