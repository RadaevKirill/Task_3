import os
import random

from sklearn.model_selection import train_test_split
import pandas as pd


def generate_data(num_days: int, procent_test: float):
    total = []
    for i in range(num_days):
        day = []
        day.append(random.randint(20, 30))  # Температура
        day.append(random.choice(['Sunny', 'Clouds', 'Rain']))  # Погода
        day.append(random.randint(0, 5))  # Ветер
        day.append(random.choice(['N', 'NW', 'W', 'SW', 'S', 'SE', 'E', 'NE']))  # Направление
        day.append(random.randint(730, 760))  # Давление

        total.append(day)
    train, test = train_test_split(pd.DataFrame(total,
                                   columns=['Temperature', 'Sky', 'Wind', 'Direction', 'Pressure']),
                                   test_size=procent_test)
    train.to_csv('./data/train/train.csv', index=False)
    test.to_csv('./data/test/test.csv', index=False)


if __name__ == '__main__':
    procent_test = 0.2
    num_days = 1000

    os.makedirs('data', exist_ok=True)
    os.makedirs('data/train', exist_ok=True)
    os.makedirs('data/test', exist_ok=True)

    generate_data(num_days, procent_test)
