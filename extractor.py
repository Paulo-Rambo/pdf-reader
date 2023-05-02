import PyPDF2


class PdfReader:
    def __init__(self, pdf_file):
        self.__pdf_file = pdf_file

    new_user_data = ""

    @property
    def get_graduation(self):
        new_text = ""
        word = "Graduation:"
        last_word = ":"
        with open(self.__pdf_file, "rb") as arquivo_pdf:
            pdf_reader = PyPDF2.PdfReader(arquivo_pdf)

            num_paginas = len(pdf_reader.pages)

            for num in range(num_paginas):
                pdf_page = pdf_reader.pages[num]
                texto = pdf_page.extract_text()
                new_text = ""
                graduation_index = 0
                last_word_index = 0
                dot_index = 0
                if word in texto:
                    graduation_index = texto.index(word)
                    last_word_index = texto.find(last_word, graduation_index + len(word))
                if last_word_index != -1:
                    new_text = texto[graduation_index + len(word):last_word_index + len(last_word)]
                    dot_index = new_text.rfind(".")
                if dot_index != -1:
                    new_text = new_text[0: dot_index + 1].replace("\n", "").split("●")
                    new_text.pop(0)
                    new_user_data = new_text
                    return new_text
      
    def create_new_page(self):
        page = PyPDF2.PageObject.create_blank_page(pdf=None, width=595, height=842)
        # reader = PyPDF2.PdfReader("Currículo.pdf")
        # page = reader.pages[0]
        writer = PyPDF2.PdfWriter()
        writer.add_page(page)

        text = "Testando"
        writer.write(text)
        
        with open("annotate15.pdf", "wb") as fp:
            writer.write(fp)


curriculo1 = PdfReader("Currículo (8).pdf")
print(curriculo1.get_graduation)
curriculo1.create_new_page()