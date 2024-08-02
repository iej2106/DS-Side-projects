from PIL import Image
import pytesseract
import os

def apply_ocr(image_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(image_folder):
        if filename.endswith('.png'):
            image_path = os.path.join(image_folder, filename)
            text = pytesseract.image_to_string(Image.open(image_path))
            
            # Save the OCR result
            with open(os.path.join(output_folder, f'{filename}.txt'), 'w') as f:
                f.write(text)
            
            print(f"OCR applied to {filename} and result saved.")

# Example usage
image_folder = 'paystubs_images'
output_folder = 'paystubs_text'
apply_ocr(image_folder, output_folder)
