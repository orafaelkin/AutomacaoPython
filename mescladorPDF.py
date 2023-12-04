import PyPDF2
import os #ler arquivos

merger = PyPDF2.PdfMerger() #""mesclador

lista_arquivos = os.listdir("MesclarPDF/arquivos")
lista_arquivos.sort()  #ordenar
print(lista_arquivos)

for arquivo in lista_arquivos:
    if ".pdf" in arquivo: 
        merger.append(f"MesclarPDF/arquivos/{arquivo}") #append = adicionar

merger.write("PDF Mesclado.pdf")        

