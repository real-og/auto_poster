import os
import io
import google.generativeai as genai
import PIL.Image


GOOGLE_API_KEY = str(os.environ.get('GEMINI_TOKEN'))  

genai.configure(api_key=GOOGLE_API_KEY)


def transform_img_to_byte_array(img_path):
    try:
        image = PIL.Image.open(img_path)
        # Конвертация изображения в байты, как того требует Gemini API
        img_byte_arr = io.BytesIO()
        image.save(img_byte_arr, format='PNG')  #  Используйте JPEG или PNG
        img_byte_arr = img_byte_arr.getvalue()
        return img_byte_arr
    except FileNotFoundError:
        return "Ошибка: Изображение не найдено."
    except Exception as e:
        return f"Ошибка при открытии изображения: {e}"


def generate_description(model_name: str, image_path: str, prompt: str, product_name: str) -> str:
    model = genai.GenerativeModel(model_name)  
    img_byte_array = transform_img_to_byte_array(image_path)
    prompt = prompt + f'/n Название товара - {product_name}'

    try:
        response = model.generate_content(
            contents=[prompt, {"mime_type": "image/jpeg", "data": img_byte_array}],
        )
    except Exception as e:
        return f"Ошибка при запросе к Gemini: {e}"
    
    if response.text:
        return response.text
    else:
        return "Не удалось сгенерировать описание."

