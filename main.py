import gemini


if __name__ == "__main__":
    model = 'gemini-1.5-flash-001'
    img_path = 'lamp.png'
    prompt = 'Краткое но информативное продающее описание товара с картинки для tumbler с хештегами'
    product_name = 'Лампа из дерева'
    result = gemini.generate_description(model, img_path, prompt, product_name)

    print(result)