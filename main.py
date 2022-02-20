import requests
print('\n\n\t  iiii                       iiii                      ffffffffffffffff                \n'
'\t i::::i                     i::::i                    f::::::::::::::::f               \n'
'\t  iiii                       iiii                    f::::::::::::::::::f              \n'
'\t                                                     f::::::fffffff:::::f              \n'
'\tiiiiiiippppp   ppppppppp   iiiiiiinnnn  nnnnnnnn     f:::::f       ffffffooooooooooo   \n'
'\ti:::::ip::::ppp:::::::::p  i:::::in:::nn::::::::nn   f:::::f           oo:::::::::::oo \n'
'\t i::::ip:::::::::::::::::p  i::::in::::::::::::::nn f:::::::ffffff    o:::::::::::::::o\n'
'\t i::::ipp::::::ppppp::::::p i::::inn:::::::::::::::nf::::::::::::f    o:::::ooooo:::::o\n'
'\t i::::i p:::::p     p:::::p i::::i  n:::::nnnn:::::nf::::::::::::f    o::::o     o::::o\n'
'\t i::::i p:::::p     p:::::p i::::i  n::::n    n::::nf:::::::ffffff    o::::o     o::::o\n'
'\t i::::i p:::::p     p:::::p i::::i  n::::n    n::::n f:::::f          o::::o     o::::o\n'
'\t i::::i p:::::p    p::::::p i::::i  n::::n    n::::n f:::::f          o::::o     o::::o\n'
'\ti::::::ip:::::ppppp:::::::pi::::::i n::::n    n::::nf:::::::f         o:::::ooooo:::::o\n'
'\ti::::::ip::::::::::::::::p i::::::i n::::n    n::::nf:::::::f         o:::::::::::::::o\n'
'\ti::::::ip::::::::::::::pp  i::::::i n::::n    n::::nf:::::::f          oo:::::::::::oo \n'
'\tiiiiiiiip::::::pppppppp    iiiiiiii nnnnnn    nnnnnnfffffffff            ooooooooooo   \n'
'\t        p:::::p                                                                        \n'
'\t        p:::::p                                                                        \n'
'\t       p:::::::p                                                                       \n'
'\t       p:::::::p                                                                       \n'
'\t       p:::::::p                                                                       \n'
'\t       ppppppppp                                                                       \n\n'.expandtabs(3))

while True:
    ipdata = []
    x = input("\tWhat is the IP address?: ".expandtabs(2))
    page = requests.get(f'https://api.iplocation.net/?ip={x}')
    print(f'\n\tInformation about {x} IP address:\n'.expandtabs(1))
    page = str(page.text)
    page = page.strip('{}')
    page = page.replace('"', '')
    page = page.replace('_', ' ')
    page = page.split(",")
    for i in page:
        i = i.split(":")
        ipdata.append([i[0], i[1]])
    for i in ipdata:
        print("\t", end = "".expandtabs(1))
        print(f'{i[0]}\t{i[1]}'.expandtabs(20))
    print("\n\t--------------------------------------------------------\n".expandtabs(1))
