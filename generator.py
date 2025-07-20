from PIL import Image, ImageDraw, ImageFont
import requests

def create_story_template(product: dict) -> str:
    response = requests.get(product["image_url"], stream=True)
    img = Image.open(response.raw).convert("RGB")
    img = img.resize((1080, 1920))
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    draw.text((50, 1600), f"{product['title']}
{product['price_kzt']} ₸
Размеры: {product['sizes_kz']}", fill="white", font=font)
    path = "/mnt/data/story_result.jpg"
    img.save(path)
    return path