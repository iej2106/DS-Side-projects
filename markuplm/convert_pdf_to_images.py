from pdf2image import convert_from_path
import os

def convert_pdf_to_images(pdf_folder, output_folder):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Process each PDF in the folder
    for filename in os.listdir(pdf_folder):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(pdf_folder, filename)
            images = convert_from_path(pdf_path)
            
            # Save images
            for i, image in enumerate(images):
                image.save(os.path.join(output_folder, f'{filename}_page_{i}.png'), 'PNG')
            
            print(f"Converted {filename} to images and saved in {output_folder}")

# Example usage
pdf_folder = 'paystubs'
output_folder = 'paystubs_images'
convert_pdf_to_images(pdf_folder, output_folder)
