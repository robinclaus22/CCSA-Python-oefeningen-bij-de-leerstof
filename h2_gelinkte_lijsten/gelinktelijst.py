class LinkedLIst:
    def __init__(self):
        self.eerste = None

    def zoek(self, x):
        ref = self.eerste
        while ref != None and ref.data != None:
            ref = ref.volgende 
        return ref

    def verwijder(self, ref):
        x = ref.volgende.data
        ref.volgende = ref.volgende.volgende
        return x

    def print(self):
        ref = self.eerste
        while ref != None:
            print(ref.data)
            ref = ref.volgende
        print("None")

    def voegToe(self, ref, x):
        hulp = Knoop()
        hulp.data = x
        hulp.volgende = ref.volgende
        ref.volgende = hulp

class Knoop:
    def __init__(self):
        self.data = None
        self.volgende = None

lijst = LinkedLIst()

knoop3 = Knoop()
knoop3.data = 'C'

knoop2 = Knoop()
knoop2.data = 'B'
knoop2.volgende = knoop3

knoop1 = Knoop()
knoop1.data = 'A'
knoop1.volgende = knoop2

lijst.eerste = knoop1

lijst.voegToe(lijst.eerste, 'E')

lijst.print()

