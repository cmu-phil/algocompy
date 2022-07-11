

class task:
    def __init__(self, alg, id):
        self.alg = alg
        self.id = id

    def run(self, data, G):
        return self.alg.run(data, G)

    def get_id(self):
        return self.id

    def __str__(self):
        return str(self.alg)
