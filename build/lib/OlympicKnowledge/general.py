import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import re
from pdf_generator import CustomPDF, generate_pdf_G

def General():
    wikipedia_url = "https://en.wikipedia.org/wiki/Handball"

    try:
        response = requests.get(wikipedia_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        main_content_div = soup.find('div', class_='mw-parser-output')
        paragraphs = main_content_div.find_all('p')
        
        content_list = []  
        
        description = None
        for paragraph in paragraphs:
            if paragraph.text.strip():
                text_without_superscript = ' '.join(paragraph.stripped_strings)
                text_without_superscript = re.sub(r'\[3\]\s*', '', text_without_superscript)
                description = text_without_superscript
                content_list.append(description)  
                break
            
        if not description:
            print("Failed to fetch description from Wikipedia.")
            return None
        
        image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fb/SAP_Arena_Handball_ausverkauft.jpg/300px-SAP_Arena_Handball_ausverkauft.jpg"
        
        try:
            image_response = requests.get(image_url)
            image = Image.open(BytesIO(image_response.content))
            
            image_path = "handball_image.jpg"
            image.save(image_path)

            content_list.append({'image': image_path})

        except Exception as e:
            print("An error occurred while fetching or displaying the image:", e)
        
        generate_pdf_G(content_list, filename="Handball_Info.pdf") 

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    General()
