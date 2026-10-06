"""Создаёт заглушку picture.png и logo.png 100x100."""
from PIL import Image, ImageDraw
import os

# Создаём папку resources, если её нет
os.makedirs("resources", exist_ok=True)

# Заглушка для фото
img = Image.new("RGB", (100, 100), color="#CCCCCC")
draw = ImageDraw.Draw(img)
draw.rectangle([0, 0, 99, 99], outline="#999999", width=2)
draw.text((25, 45), "NO PHOTO", fill="#666666")
img.save("resources/picture.png")

# Логотип (для ДЗ)
logo = Image.new("RGB", (100, 100), color="#D2F6E7")
draw2 = ImageDraw.Draw(logo)
draw2.text((25, 45), "LOGO", fill="#70B2AF")
logo.save("resources/logo.png")

print("✅ Создано: resources/picture.png, resources/logo.png")