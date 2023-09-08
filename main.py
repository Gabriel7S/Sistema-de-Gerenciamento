import customtkinter as ctk
from reportlab.pdfgen import canvas
import openpyxl

class Application(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1920x1080")
        self.create_widgets()
        self.inventario = []
    #exportador

        # Criação de um botão para exportar em PDF ou Excel
        self.exportar = ctk.CTkButton(self, text="Exportar em PDF ou Excel", command=self.exportar_dados)
        self.exportar.pack(pady=10)

    def exportar_dados(self):
        # Cria um novo arquivo PDF
        pdf = canvas.Canvas("inventario.pdf")

        # Adiciona os dados do inventário ao arquivo PDF
        pdf.drawString(100, 750, "Equipamento da Empresa ou Locado?: " + self.equipamento.get())
        pdf.drawString(100, 700, "Nome do Dispositivo: " + self.dispositivo.get())
        pdf.drawString(100, 650, "Usuário: " + self.usuario.get())
        pdf.drawString(100, 600, "Processador: " + self.processador.get())
        pdf.drawString(100, 550, "Memória RAM (GB): " + self.memoria.get())
        pdf.drawString(100, 500, "HD (Tamanho): " + self.hd.get())
        pdf.drawString(100, 450, "SSD (Tamanho): " + self.ssd.get())
        pdf.drawString(100, 400, "Está no Domínio?: " + self.dominio.get())
        pdf.drawString(100, 350, "Estado (Em Uso ou Parado): " + self.estado.get())
        pdf.drawString(100, 300, "Modelo: " + self.modelo.get())
        pdf.drawString(100, 250, "Endereço MAC: " + self.mac.get())
        pdf.drawString(100, 200, "Endereço MAC Wi-Fi: " + self.mac_wifi.get())
        pdf.drawString(100, 150, "Possui Webex?: " + self.webex.get())
        pdf.drawString(100, 100, "Ramal do Webex: " + self.ramal_webex.get())
        pdf.drawString(100, 50, "Possui Biosystem?: " + self.biosystem.get())

        # Salva o arquivo PDF
        pdf.save()

        # Cria um novo arquivo Excel
        wb = openpyxl.Workbook()
        sheet = wb.active

        # Adiciona os dados do inventário à planilha do Excel
        sheet["A1"] = "Equipamento da Empresa ou Locado?"
        sheet["B1"] = self.equipamento.get()
        sheet["A2"] = "Nome do Dispositivo"
        sheet["B2"] = self.dispositivo.get()
        sheet["A3"] = "Usuário"
        sheet["B3"] = self.usuario.get()
        sheet["A4"] = "Processador"
        sheet["B4"] = self.processador.get()
        sheet["A5"] = "Memória RAM (GB)"
        sheet["B5"] = self.memoria.get()
        sheet["A6"] = "HD (Tamanho)"
        sheet["B6"] = self.hd.get()
        sheet["A7"] = "SSD (Tamanho)"
        sheet["B7"] = self.ssd.get()
        sheet["A8"] = "Está no Domínio?"
        sheet["B8"] = self.dominio.get()
        sheet["A9"] = "Estado (Em Uso ou Parado)"
        sheet["B9"] = self.estado.get()
        sheet["A10"] = "Modelo"
        sheet["B10"] = self.modelo.get()
        sheet["A11"] = "Endereço MAC"
        sheet["B11"] = self.mac.get()
        sheet["A12"] = "Endereço MAC Wi-Fi"
        sheet["B12"] = self.mac_wifi.get()
        sheet["A13"] = "Possui Webex?"
        sheet["B13"] = self.webex.get()
        sheet["A14"] = "Ramal do Webex"
        sheet["B14"] = self.ramal_webex.get()
        sheet["A15"] = "Possui Biosystem?"
        sheet["B15"] = self.biosystem.get()

        # Salva o arquivo Excel
        wb.save("inventario.xlsx")

app = Application()
app.mainloop()

#TABELAS+PESQUISA
coldata = [
    {"text": "LicenseNumber", "stretch": False},
    "CompanyName",
    {"text": "UserCount", "stretch": False},
]

rowdata = [
    ('A123', 'IzzyCo', 12),
    ('A136', 'Kimdee Inc.', 45),
    ('A158', 'Farmadding Co.', 36)
]

dt = Tableview(
    coldata=coldata,
    rowdata=rowdata,
    paginated=True,
    searchable=True,
    bootstyle=PRIMARY,
)

dt.pack(fill=BOTH, expand=YES, padx=10, pady=10)
