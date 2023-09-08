from ttkbootstrap import* 
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *

class Interface(Window):
    def __init__(self,):
        super().__init__(themename="superhero",size=(900,500), title="Inventário de TI")
        self.widgets()

    def entry_label(self,frame,x,y,text):
        lbl = Label(frame,text = text,bootstyle= (PRIMARY) )
        lbl.place(x=x, y=y)

        entry = Entry(frame, bootstyle= (PRIMARY))
        entry.place(x=x+130, y=y)
        return entry
    
    def widgets(self):
        frame = Frame(self)
        frame.pack(side=TOP, fill=BOTH, expand=True)
        frame1 = Frame(self, bootstyle=INFO)
        frame1.place(x=5, y=0, width=290, height=490)
        lblframe1 = Labelframe(frame1, text="FORMULÁRIO", bootstyle=PRIMARY, padding=10)
        lblframe1.pack(side=TOP, fill=BOTH, expand=True)
    
        #Formulário
        self.usuario = self.entry_label(lblframe1,5,0, "Nome do Usuário:")
        self.departamento = self.entry_label(lblframe1,5,40, "Departamento:")
        self.unidade = self.entry_label(lblframe1,5,80, "Unidade:")
        self.tipo = self.entry_label(lblframe1,5,120, "Tipo ou Modelo:")
        self.nome = self.entry_label(lblframe1,5,160, "Nome do Dispositivo:")
        self.ender_ip = self.entry_label(lblframe1,5,200, "Endereço de IP:")
        self.ender_mac1 = self.entry_label(lblframe1,5,240, "Endereço MAC:")
        self.ender_mac2 = self.entry_label(lblframe1,5,280, "Endereço MAC Wi-Fi:")
        self.ant_v = self.entry_label(lblframe1,5,320, "Possui AV ? :")
        #Botão
        btn_salvar = Button(lblframe1, text="Salvar", command="/")
        btn_salvar.place(x=0,y=360, width=135)


        #Dados
        frame2 = Frame(frame, bootstyle=DANGER)
        frame2.place(x=300, y=0, height=490, width=590)
        lblframe2 = Labelframe(frame2, text="DADOS", bootstyle=SECONDARY, padding=10)
        lblframe2.pack(side= TOP, fill=BOTH, expand=True)

        tableview = Tableview(lblframe2,
                              paginated=True,
                              searchable=True,
                              bootstyle=(SUCCESS),
                              stripecolor=("cyan", None),
                              autoalign=True,
                              autofit=True,
                              height=15,
                              delimiter=";"
                              )
        tableview.pack(fill=BOTH, expand=True, padx=5, pady=5)

        #tabela
if __name__ == "__main__":
    app = Interface()
    app.mainloop()