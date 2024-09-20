import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    predict = np.random.randint(1, 101)
    print(f"number - {number}")
    print(f"predict - {predict}")

    while number != predict:
        count += 1
        if number > predict:
            predict += 10
        else:
            predict -= 10
            if number > predict:
                predict += 5
                if number > predict:
                    predict += 3
                    if number > predict:
                        predict += 1
        # elif number < predict:
        #     predict -= 10
        #     if number > predict:
        #         predict += 5
        #         if number < predict:
        #             predict -= 1
        print(predict, count)
    return count


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = []  # список для сохранения количества попыток
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))  # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return (score)


if __name__ == '__main__':
    score_game(random_predict)