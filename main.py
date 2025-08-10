import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import os

# Configurações
CAMINHO_PLANILHA = 'alunos.csv'
CAMINHO_MODELO = 'modelo_certificado.png'
FONTE_CAMINHO = 'GreatVibes-Regular.ttf'
FONTE_TAMANHO = 100
PRESENCA_MINIMA = 70
PASTA_SAIDA = 'certificados_gerados'

os.makedirs(PASTA_SAIDA, exist_ok=True)

df = pd.read_csv(CAMINHO_PLANILHA)

for _, row in df.iterrows():
    nome = row['Nome']
    presenca = row['Presenca']

    if presenca >= PRESENCA_MINIMA:
        img = Image.open(CAMINHO_MODELO)
        draw = ImageDraw.Draw(img)
        fonte = ImageFont.truetype(FONTE_CAMINHO, FONTE_TAMANHO)

        texto = nome
        bbox = fonte.getbbox(texto)
        w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
        W, H = img.size
        x = (W - w) / 2 # Ajuste Horizontal
        y = H * 0.47 # Ajuste vertical

        draw.text((x, y), texto, fill='black', font=fonte)

        saida = os.path.join(PASTA_SAIDA, f'certificado_{nome}.pdf')
        img_rgb = img.convert('RGB') 
        img_rgb.save(saida)

        print(f'✅ Gerado: {saida}')
    else:
        print(f'❌ {nome} – presenca {presenca}% (abaixo de {PRESENCA_MINIMA}%)')
