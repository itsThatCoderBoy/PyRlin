def perleanate_no_edges(sizex, sizey, noise=np.array([])):
    if noise.size == 0:
        noise = np.random.randint(1, 101, (sizex, sizey))
    else:
        noise = noise
    noise = noise.astype(float)
    final = noise
    x = 0
    y = 0
    for i in range(sizex * sizey):
        if x == 0 and y == 0:
            final[x, y] = 0

        elif x == 0 and y != 0 and y != sizey - 1:
            final[x, y] = 0

        elif x == sizex - 1 and y == 0:
            final[x, y] = 0

        elif x == sizex - 1 and y != 0 and y != sizey - 1:
            final[x, y] = 0

        elif x == sizex - 1 and y == sizey - 1:
            final[x, y] = 0

        elif x != 0 and x != sizex - 1 and y == sizey - 1:
            final[x, y] = 0

        elif x == 0 and y == sizey - 1:
            final[x, y] = 0

        elif x == 0 and y != 0 and y != sizey - 1:
            final[x, y] = 0

        else:
            final[x,
                  y] = (noise[x, y] + noise[x, y + 1] + noise[x + 1, y + 1] +
                        noise[x + 1, y] + noise[x + 1, y - 1] +
                        noise[x, y - 1] + noise[x - 1, y - 1] +
                        noise[x - 1, y] + noise[x - 1, y + 1]) / 9

        x += 1
        if x == sizex:
            y += 1
            x = 0

    return final


def perleanate(sizex, sizey, noise=np.array([])):
    if noise.size == 0:
        noise = np.random.randint(1, 101, (sizex, sizey))
    else:
        noise = noise
    noise = noise.astype(float)
    final = noise
    x = 0
    y = 0
    for i in range(sizex * sizey):
        if x == 0 and y == 0:
            final[x, y] = (noise[x, y] + noise[x, y + 1] +
                           noise[x + 1, y + 1] + noise[x + 1, y]) / 4

        elif x == 0 and y != 0 and y != sizey - 1:
            final[x, y] = (noise[x, y] + noise[x, y + 1] +
                           noise[x + 1, y + 1] + noise[x + 1, y] +
                           noise[x + 1, y - 1] + noise[x, y - 1]) / 6

        elif x == sizex - 1 and y == 0:
            final[x, y] = (noise[x, y] + noise[x, y + 1] + noise[x - 1, y] +
                           noise[x - 1, y + 1]) / 4

        elif x == sizex - 1 and y != 0 and y != sizey - 1:
            final[x, y] = (noise[x, y] + noise[x, y + 1] + noise[x, y - 1] +
                           noise[x - 1, y - 1] + noise[x - 1, y] +
                           noise[x - 1, y + 1]) / 6

        elif x == sizex - 1 and y == sizey - 1:
            final[x, y] = (noise[x, y] + noise[x, y - 1] +
                           noise[x - 1, y - 1] + noise[x - 1, y]) / 4

        elif x != 0 and x != sizex - 1 and y == sizey - 1:
            final[x, y] = (noise[x, y] + noise[x + 1, y] +
                           noise[x + 1, y - 1] + noise[x, y - 1] +
                           noise[x - 1, y - 1] + noise[x - 1, y]) / 6

        elif x == 0 and y == sizey - 1:
            final[x, y] = (noise[x, y] + noise[x + 1, y] +
                           noise[x + 1, y - 1] + noise[x, y - 1]) / 4

        elif x == 0 and y != 0 and y != sizey - 1:
            final[x, y] = (noise[x, y] + noise[x, y + 1] +
                           noise[x + 1, y + 1] + noise[x + 1, y] +
                           noise[x + 1, y - 1] + noise[x, y - 1]) / 6

        else:
            final[x,
                  y] = (noise[x, y] + noise[x, y + 1] + noise[x + 1, y + 1] +
                        noise[x + 1, y] + noise[x + 1, y - 1] +
                        noise[x, y - 1] + noise[x - 1, y - 1] +
                        noise[x - 1, y] + noise[x - 1, y + 1]) / 9

        x += 1
        if x == sizex:
            y += 1
            x = 0

    return final


def multiple_perleanate(sizex, sizey, iterations):
    final = perleanate_no_edges(sizex, sizey)
    for i in range(iterations - 1):
        final = perleanate_no_edges(sizex, sizey, final)

    return final


def round_noise(noise):
    final = noise.astype(int)
    x = 0
    y = 0

    for num in noise:

        for num2 in num:
            final[x, y] = int(num2)
            y += 1
        x += 1
        y = 0

        # noise[index] = int(num2)

    return final


def rounded_perleanate(sizex, sizey):
    round_noise(perleanate_no_edges(sizex, sizey))


def split_noise(noise, splitPoint=50):
    final = noise.astype(int)
    x = 0
    y = 0

    for num in noise:

        for num2 in num:
            if noise[x, y] >= splitPoint:
                final[x, y] = 0
            else:
                final[x, y] = 1
            y += 1
        x += 1
        y = 0

    return final


def make_map(sizex, sizey, iterations, splitPoint=50):
    noise = split_noise(multiple_perleanate(sizex, sizey, iterations),
                        splitPoint)
    final = noise.astype(str)
    x = 0
    y = 0

    for num in noise:
        for num2 in num:
            if noise[x, y] == 0:
                final[x, y] = f"{CLR.RED}██"
            else:
                final[x, y] = f"{CLR.WHITE}██"
            y += 1
        x += 1
        y = 0

    return final


def new_map_chunk(sizex,
                  sizey,
                  iterations,
                  splitPoint=50,
                  edge1=np.array([]),
                  edge2=np.array([]),
                  edge3=np.array([]),
                  edge4=np.array([])):
    pass
