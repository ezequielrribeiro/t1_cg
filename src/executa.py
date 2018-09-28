from src.LerArquivo import Ler_Arquivo

"""
conj_pontos = {}
with open('pontos.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        obj = Ponto(row['x'], row['y'], row['z'])
        conj_pontos[row['label']] = obj

    print(conj_pontos)
"""

leArquivo = Ler_Arquivo("pontos.csv", "desenha_linhas.csv")
ObjDesenho = leArquivo.ler_arquivo()
print(ObjDesenho.__dict__)
