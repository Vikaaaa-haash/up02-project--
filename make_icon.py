"""Создаёт иконку icon.ico и icon.png."""
from PIL import Image, ImageDraw

# Создаём картинку 64x64
img = Image.new("RGB", (64, 64), color="#70B2AF")
draw = ImageDraw.Draw(img)

# Рисуем простую иконку — белый круг с буквой A
draw.ellipse([8, 8, 56, 56], fill="#D2F6E7", outline="#FFFFFF", width=2)

try:
    from PIL import ImageFont
    font = ImageFont.truetype("arial.ttf", 30)
except Exception:
    font = None

if font:
    draw.text((22, 18), "A", font=font, fill="#70B2AF")
else:
    draw.text((25, 25), "A", fill="#70B2AF")

# Сохраняем в .ico и .png
img.save("resources/icon.ico", format="ICO")
img.save("resources/icon.png", format="PNG")

print("✅ Созданы resources/icon.ico и resources/icon.png")
