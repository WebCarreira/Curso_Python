import PySimpleGUI as sg
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# Função para criar o PDF
def create_pdf(data, filename):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4
    
    c.setFont("Helvetica", 12)
    y_position = height - 40
    
    for key, value in data.items():
        text = f"{key}: {value}"
        c.drawString(40, y_position, text)
        y_position -= 20  # Move down for next line
    
    c.save()

# Layout da GUI
layout = [
    [sg.Text('Nome'), sg.InputText(key='Nome')],
    [sg.Text('Idade'), sg.InputText(key='Idade')],
    [sg.Text('Email'), sg.InputText(key='Email')],
    [sg.Text('Endereço'), sg.InputText(key='Endereço')],
    [sg.Button('Gerar PDF'), sg.Button('Cancelar')]
]

window = sg.Window('Recolha de Dados', layout)

while True:
    event, values = window.read()
    
    if event == sg.WINDOW_CLOSED or event == 'Cancelar':
        break
    if event == 'Gerar PDF':
        if all(values.values()):
            create_pdf(values, "dados_recolhidos.pdf")
            sg.popup('PDF criado com sucesso!')
        else:
            sg.popup('Por favor, preencha todos os campos.')
    
window.close()
