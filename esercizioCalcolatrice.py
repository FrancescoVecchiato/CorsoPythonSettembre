'''

Creare tramite l’interfaccia grafica wx una calcolatrice.
La finestra deve avere due campi di input e quattro pulsanti
uno per l’addizione, uno per la sottrazione, uno per la divisione e uno per la moltiplicazione
quando l’utente preme il pulsante il programma resituisce un messagebox con il risultato dell’operazione

'''

import wx

class Myapp(wx.App):

    def OnInit(self):

        frame = wx.Frame(None, title = "Calcolatrice", size = (500, 400))

        panel = wx.Panel(frame)
        vbox = wx.BoxSizer(wx.VERTICAL)

        self.label = wx.StaticText(panel, label="Inserisci un numero")
        vbox.Add(self.label, flag=wx.LEFT, border=5)

        self.text_ctrl = wx.TextCtrl(panel)
        vbox.Add(self.text_ctrl, flag=wx.LEFT, border=5)
        self.text_ctrl.GetParent().Layout()

        self.label1 = wx.StaticText(panel, label="Inserisci un numero")
        vbox.Add(self.label1, flag=wx.LEFT, border=5)

        self.text_ctrl1 = wx.TextCtrl(panel)
        vbox.Add(self.text_ctrl1, flag=wx.LEFT, border=5)
        self.text_ctrl1.GetParent().Layout()

        button_a = wx.Button(panel, label="Somma")
        vbox.Add(button_a, flag=wx.LEFT, border=5)
        button_a.GetParent().Layout()

        button_b = wx.Button(panel, label="Sottrai")
        vbox.Add(button_b, flag=wx.LEFT, border=5)
        button_b.GetParent().Layout()

        button_c = wx.Button(panel, label="Dividi")
        vbox.Add(button_c, flag=wx.LEFT, border=5)
        button_c.GetParent().Layout()

        button_d = wx.Button(panel, label="Moltiplica")
        vbox.Add(button_d, flag=wx.LEFT, border=5)
        button_d.GetParent().Layout()

        button_a.Bind(wx.EVT_BUTTON, self.somma)
        button_b.Bind(wx.EVT_BUTTON, self.sottrazione)
        button_c.Bind(wx.EVT_BUTTON, self.divisione)
        button_d.Bind(wx.EVT_BUTTON, self.moltiplicazione)

        panel.SetSizer(vbox)
        frame.Show()

        return True

    def somma(self, event):

        num = int(self.text_ctrl.GetValue())
        num1 = int(self.text_ctrl1.GetValue())

        wx.MessageBox(f"Il risultato è {num + num1}", "Somma", wx.OK | wx.ICON_INFORMATION)

    def sottrazione(self, event):

        num = int(self.text_ctrl.GetValue())
        num1 = int(self.text_ctrl1.GetValue())

        wx.MessageBox(f"Il risultato è {num - num1}", "Sottrazione", wx.OK | wx.ICON_INFORMATION)

    def divisione(self, event):

        num = int(self.text_ctrl.GetValue())
        num1 = int(self.text_ctrl1.GetValue())

        wx.MessageBox(f"Il risultato è {num / num1}", "Divisione", wx.OK | wx.ICON_INFORMATION)

    def moltiplicazione(self, event):

        num = int(self.text_ctrl.GetValue())
        num1 = int(self.text_ctrl1.GetValue())

        wx.MessageBox(f"Il risultato è {num * num1}", "Moltiplicazione", wx.OK | wx.ICON_INFORMATION)

if __name__ == "__main__":
    app = Myapp()
    app.MainLoop()