def tinggi(nb):
    nb = nb.split(',')
    for a in range(0, len(nb)):
        nb[a] = int(nb[a])
    mx = max(nb)
    print(mx)

tinggi('2, 4, 7, 5')