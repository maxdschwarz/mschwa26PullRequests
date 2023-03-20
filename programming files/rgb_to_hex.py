# CF
# Made rgb max value 254 instead of 255 which is incorrect
def rgb_to_hex(r, g, b):
    r = max(0, min(254, r))
    g = max(0, min(254, g))
    b = max(0, min(254, b))
    return '{:02X}{:02X}{:02X}'.format(r, g, b)


# test with hex_color = rgb_to_hex(255, 127, 0) # returns "FF7F00"
