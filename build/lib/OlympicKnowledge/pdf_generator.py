from fpdf import FPDF
import pandas as pd

class CustomPDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Olympic Handball Medalists', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def add_image(self, img_path, x, y, w, h):
        self.image(img_path, x, y, w, h)

def generate_pdf_Y(content, filename="output.pdf", title="Olympic Knowlege 1.0"):
    pdf = CustomPDF()
    
    
    pdf.add_page()  
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, title, 0, 1, 'C')
    pdf.ln(10)  

    for section, results in content.items():
        pdf.add_page()  
        pdf.set_font('Arial', 'B', 12)
        pdf.cell(0, 10, section, 0, 1, 'L')
        
        if isinstance(results, pd.DataFrame):
            pdf.set_font('Arial', '', 12)
            if results.empty:
                pdf.multi_cell(0, 10, "No medals found.\n")
            else:
                pdf.multi_cell(0, 10, results.to_string(index=False) + "\n")
        elif isinstance(results, dict):
            for medal, names in results.items():
                pdf.set_font('Arial', 'B', 12)
                pdf.cell(0, 10, txt=medal + ":", ln=True)
                pdf.set_font('Arial', '', 12)
                if not names:
                    pdf.cell(0, 10, txt=f"No {medal.lower()} medals.", ln=True)
                else:
                    for name in names:
                        encoded_name = name.encode('latin-1', 'replace').decode('latin-1')
                        pdf.cell(200, 6, txt=encoded_name, ln=True)
                pdf.ln()
    
    pdf.output(filename)
    print(f"PDF generated: {filename}")



def generate_pdf_G(content, filename="output.pdf", title="Olympic Knowledge"):
    pdf = CustomPDF()
    pdf.add_page()

    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, title, 0, 1, 'C')
    pdf.ln(10) 

    for item in content:
        if isinstance(item, str):
            pdf.set_font('Arial', '', 12)
            pdf.multi_cell(0, 10, item)
            pdf.ln()
        elif isinstance(item, dict) and 'image' in item:
            pdf.add_image(item['image'], x=10, y=pdf.get_y(), w=100, h=75)
            pdf.ln(80)  

    pdf.output(filename)
    print(f"PDF generated: {filename}")



def generate_pdf_C(content, filename):
    pdf = CustomPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, 'Handball Medalists', 0, 1, 'C')
    pdf.ln(10)

    for section, data in content.items():
        pdf.add_page()
        pdf.set_font('Arial', 'B', 14)
        pdf.cell(0, 10, section, 0, 1, 'L')
        pdf.ln(10)

        for medal_type, df in data.items():
            pdf.set_font('Arial', 'B', 12)
            pdf.cell(0, 10, medal_type, 0, 1, 'L')
            pdf.set_font('Arial', '', 12)
            if df.empty:
                pdf.cell(0, 10, f'No {medal_type.lower()} medals.', 0, 1, 'L')
            else:
                for line in df.to_string(index=False).split('\n'):
                    pdf.cell(0, 10, line, 0, 1, 'L')
            pdf.ln(5)
    
    pdf.output(filename)

def generate_pdf_F(country, leagues, filename="output.pdf", title="Handball Leagues Report"):
    filename = f"{country.capitalize()}_Leagues.pdf" 

    pdf = CustomPDF()
    pdf.add_page()
    
    
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, title, 0, 1, 'C')
    pdf.ln(10) 
    
    
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(0, 10, f"Country: {country.capitalize()}", 0, 1, 'L')
    pdf.ln(10)
    
    
    pdf.set_font('Arial', '', 12)
    for league in leagues:
        pdf.cell(0, 10, f"- {league}", 0, 1, 'L')
    
    pdf.output(filename)
    print(f"PDF report saved as: {filename}")



def generate_pdf_A(content, filename="output.pdf", title="Olympic Knowledge 1.0"):
    pdf = CustomPDF()
    
    
    pdf.add_page()  
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, title, 0, 1, 'C')
    pdf.ln(10)  

    for section, results in content.items():
        pdf.add_page()  
        pdf.set_font('Arial', 'B', 12)
        pdf.cell(0, 10, section, 0, 1, 'L')
        
        if isinstance(results, pd.DataFrame):
            pdf.set_font('Arial', '', 12)
            if results.empty:
                pdf.multi_cell(0, 10, "No medals found.\n")
            else:
                for index, row in results.iterrows():
                    pdf.multi_cell(0, 10, f"Year: {row['Year']}, Medal Type: {row['Medal Type']}")
                    if 'Wikipedia Page' in row and row['Wikipedia Page']:
                        wikipedia_link = row['Wikipedia Page']
                        pdf.cell(0, 10, f"Wikipedia Page: {wikipedia_link}", ln=True, link=wikipedia_link)
                    pdf.ln(10)
        elif isinstance(results, dict):
            for medal, names in results.items():
                pdf.set_font('Arial', 'B', 12)
                pdf.cell(0, 10, txt=medal + ":", ln=True)
                pdf.set_font('Arial', '', 12)
                if not names:
                    pdf.cell(0, 10, txt=f"No {medal.lower()} medals.", ln=True)
                else:
                    for name in names:
                        encoded_name = name.encode('latin-1', 'replace').decode('latin-1')
                        pdf.cell(200, 6, txt=encoded_name, ln=True)
                pdf.ln()
    
    pdf.output(filename)
    print(f"PDF generated: {filename}")
