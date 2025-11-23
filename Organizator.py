import os
import shutil

pasta_alvo = os.path.join(os.path.expanduser("~"), "Downloads")

categorias = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Executaveis": [".exe", ".msi", ".bat"],
    "Compactados": [".zip", ".rar", ".7z"]
}

def organizar():
    print(f"Organizando a pasta: {pasta_alvo}...")

    for arquivo in os.listdir(pasta_alvo):
        full_path = os.path.join(pasta_alvo, arquivo)

        if os.path.isdir(full_path):
            continue

        movido = False

        for pasta, extensoes in categorias.items():

            if arquivo.lower().endswith(tuple(extensoes)):
                pasta_destino = os.path.join(pasta_alvo, pasta)
                if not os.path.exists(pasta_destino):
                    os.makedirs(pasta_destino)

                shutil.move(full_path, os.path.join(pasta_destino,arquivo))
                print(f"Movido: {arquivo} -> {pasta}")
                movido = True
                break

            if not movido:
                print(f"Ignorado(sem categoria): {arquivo}")




if __name__ == "__main__":
    organizar()
    print("Concluido!")