from PIL import Image

im = [Image.open(x) for x in ['slowpoke.gif', 'accelgor.gif']]
width, height = zip(*(i.size for i in im))

total_width = sum(width)
total_height = sum(height)

new_im = Image.new('RGB', (total_width, max(height)))

x_offset = 0
for i in im:
    new_im.paste(i, (x_offset, 0))
    x_offset += i.size[0]

new_im.save('combined.gif', save_all=True)


