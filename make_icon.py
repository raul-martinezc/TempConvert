from PIL import Image, ImageDraw, ImageFont
import math

SIZE = 1024
img = Image.new("RGBA", (SIZE, SIZE), (255, 255, 255, 255))
draw = ImageDraw.Draw(img)

# Colors
RED = (220, 50, 50)
DARK = (40, 40, 40)
LIGHT_RED = (240, 180, 180)

# Thermometer body
bulb_cx, bulb_cy = SIZE // 2, 750
bulb_r = 100
tube_w = 60
tube_top = 160
tube_bottom = bulb_cy - bulb_r + 20

# Tube outline
draw.rounded_rectangle(
    [bulb_cx - tube_w // 2 - 8, tube_top - 8, bulb_cx + tube_w // 2 + 8, tube_bottom + 8],
    radius=20, fill=DARK
)
# Tube fill (white interior)
draw.rounded_rectangle(
    [bulb_cx - tube_w // 2, tube_top, bulb_cx + tube_w // 2, tube_bottom],
    radius=14, fill=(255, 255, 255)
)
# Mercury fill
mercury_top = 300
draw.rounded_rectangle(
    [bulb_cx - tube_w // 2 + 10, mercury_top, bulb_cx + tube_w // 2 - 10, tube_bottom],
    radius=10, fill=RED
)

# Bulb outline
draw.ellipse(
    [bulb_cx - bulb_r - 8, bulb_cy - bulb_r - 8, bulb_cx + bulb_r + 8, bulb_cy + bulb_r + 8],
    fill=DARK
)
# Bulb fill
draw.ellipse(
    [bulb_cx - bulb_r, bulb_cy - bulb_r, bulb_cx + bulb_r, bulb_cy + bulb_r],
    fill=RED
)

# Tick marks
for i in range(6):
    y = mercury_top + i * ((tube_bottom - mercury_top) // 5)
    tick_w = 30 if i % 2 == 0 else 18
    draw.line(
        [bulb_cx + tube_w // 2 + 4, y, bulb_cx + tube_w // 2 + 4 + tick_w, y],
        fill=DARK, width=5
    )

img.save("icon.png")
print("icon.png saved")

# Convert to icns
import subprocess, os

os.makedirs("icon.iconset", exist_ok=True)
sizes = [16, 32, 64, 128, 256, 512, 1024]
for s in sizes:
    resized = img.resize((s, s), Image.LANCZOS)
    resized.save(f"icon.iconset/icon_{s}x{s}.png")
    if s <= 512:
        resized2 = img.resize((s * 2, s * 2), Image.LANCZOS)
        resized2.save(f"icon.iconset/icon_{s}x{s}@2x.png")

subprocess.run(["iconutil", "-c", "icns", "icon.iconset", "-o", "icon.icns"])
print("icon.icns saved")
