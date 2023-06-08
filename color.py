blue = (0, 0, 255)
red = (250, 0, 0)
orange = (225, 100, 0)
sky_blue = (0, 200, 247)
cloud_light = (200, 200, 200)
cloud_dark = (125, 125, 125)
cloud_storm = (50, 50, 50)
rain = (40, 30, 220)
yellow = (225, 225, 25)
red_yellow = (250, 225, 25)


def blend(c1, c2, alpha):
    if alpha > 1:
        alpha = 1
    elif alpha < 0:
        alpha = 0
    r = (1 - alpha) * c1[0] + alpha * c2[0]
    g = (1 - alpha) * c1[1] + alpha * c2[1]
    b = (1 - alpha) * c1[2] + alpha * c2[2]
    return (int(r), int(g), int(b))
