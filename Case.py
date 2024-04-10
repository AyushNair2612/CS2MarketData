itemRarities = dict({
    "eb4b4b": "Covert",
    "d32ce6": "Classified",
    "8847ff": "Restricted",
    "4b69ff": "Milspec"
})

itemProbs = dict({
    "Covert": 0.0058,
    "Classified": 0.0288,
    "Restricted": 0.1438,
    "Milspec": 0.7193,
    "Extraordinary": 0.0023
})


class Case:
    def __init__(self, caseName):
        self.hashname = caseName
        self.itemDenoms = dict({
            "Covert": 0,
            "Classfied": 0,
            "Restricted": 0,
            "Milspec": 0,
            "Extraordinary": 0
        })
        self.items = []
        self.extraordinaries = []
        self.expectedVal = 0

