pixel = input("Please provide a pixel value: ")
channel_pixel = input("Please provide channel values or pixel value: ")

pixel = pixel[2:]
value = int(pixel, 16)

red1 = (value & 0xFF0000) >> 16  # & = bitwise AND operator, >> = bitwise right shift operator
green1 = (value & 0x00FF00) >> 8
blue1 = (value & 0x0000FF) >> 0
if channel_pixel[1] == 'x':
    pixel_value = channel_pixel[2:]
    pixel_value = int(pixel_value, 16)

    pixel_red = (pixel_value & 0xFF0000) >> 16
    pixel_green = (pixel_value & 0x00FF00) >> 8
    pixel_blue = (pixel_value & 0x0000FF) >> 0
if channel_pixel[1] == 'x':
    red2 = red1 + int(pixel_red)
    green2 = green1 + int(pixel_green)
    blue2 = blue1 + int(pixel_blue)
else:
    channel_value = channel_pixel.split()
    red2 = red1 + int(channel_value[0])
    green2 = green1 + int(channel_value[1])
    blue2 = blue1 + int(channel_value[2])
    if red2 < 0:
        red2 += 256
    if green2 < 0:
        green2 += 256
    if blue2 < 0:
        blue2 += 256
    if red2 > 256:
        red2 -= 256
    if green2 > 256:
        green2 -= 256
    if blue2 > 256:
        blue2 -= 256

print("Your new pixel value is: 0x{0:02x}{1:02x}{2:02x}".format(red2, green2, blue2))