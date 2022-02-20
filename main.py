import requests
while True:
    ipdata = []
    x = input("What is the IP address?: ")
    page = requests.get(f'https://api.iplocation.net/?ip={x}')
    print(f'\nInformation about {x} IP address:\n')
    page = str(page.text)
    page = page.strip('{}')
    page = page.replace('"', '')
    page = page.replace('_', ' ')
    page = page.split(",")
    for i in page:
        i = i.split(":")
        ipdata.append([i[0], i[1]])
    for i in ipdata:
        print(f'{i[0]}\t{i[1]}'.expandtabs(20))
    print("\n----------------------------\t\n")
