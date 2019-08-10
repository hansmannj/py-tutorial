import colorsys

n = 8
for i in range(1, n + 1):
    rgb = "#" + "".join(["{:02x}".format(int(v * 255)) for v in colorsys.hsv_to_rgb(180, i / 8., 1)])
    print(rgb)
