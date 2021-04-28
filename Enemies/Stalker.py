from IEnemy import IEnemy


class Stalker(IEnemy):

    def __init__(self):
        self.spawn()

    def spawn(self):
        print(self.get_name() + ' is spawn')

    def kill(self):
        print(self.get_name() + ' is dead')

    def get_name(self):
        return 'Stalker'