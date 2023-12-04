import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title="Selecione uma pasta") #lista o caminho da pasta

lista_arquivos = os.listdir(caminho) #lista os aruivos da pasta

locais = {   #aqui cria-se as pastas a serem criasda e as extensoes de cada uma que seram inseridas
    "imagens": [".png",".jpg",".gif"],
    "planilhas": [".xls",".xlsx",".csv"],
    "pdfs": [".pdf"],
}  #lista

for arquivo in lista_arquivos:
    nome,extensao = os.path.splitext(f"{caminho}/{arquivo}") #usado para extrair a extensao
    for pasta in locais:
        if extensao in locais[pasta]: #pasta selecionada
            if not os.path.exists(f"{caminho}/{pasta}"): #se nao existir a pasta
                os.mkdir(f"{caminho}/{pasta}")  #criar a pasta 
            #os.rename(f"{caminho}/{nome_antigo} , "caminho/nome_novo")     
            os.rename(f"{caminho}/{arquivo}" , f"{caminho}/{pasta}/{arquivo}") # tirando o arquivo de uma pasta e colocando na nova criada       
