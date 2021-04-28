from Factories.EasilyEnemyFactory import EasilyEnemyFactory
from Factories.HardEnemyFactory import HardEnemyFactory
from Factories.MiddleEnemyFactory import MiddleEnemyFactory

if __name__ == '__main__':

    levels = [EasilyEnemyFactory(), MiddleEnemyFactory(), HardEnemyFactory()]

    num_level = 1
    while True:
        try:
            num_level: int = int(input("Select difficulty level:\n1. Easily\n2. Middle\n3. Hard\n>  "))
            if 1 <= num_level <= 3:
                break
        except:
            pass

    level = levels[num_level-1]
    enemies = []
    num_enemies = 10

    print('\nLoading...')

    for i in range(0, num_enemies):
        enemies.append(level.create())
