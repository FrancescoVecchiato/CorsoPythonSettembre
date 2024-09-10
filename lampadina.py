class Lampadina :

    def __init__(self):

        self.stato = "spenta"
        self.taratura = 0
        self.click_attuali = 0

    def __str__(self):

        return f"Stato attuale: {self.stato}, Taratura: {self.taratura}"

    def click(self):

        if self.click_attuali >= self.taratura :

            self.click_attuali += 1
            self.stato = "rotta"

        elif self.stato == "spenta":

            self.stato = "accesa"
            self.click_attuali += 1

        else:

            self.stato = "spenta"
            self.click_attuali += 1

    def visualizza_stato(self):

       return self.stato