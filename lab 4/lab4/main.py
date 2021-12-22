import sys
import math


def get_coef(index, prompt):
    try:
        # Пробуем прочитать коэффициент из командной строки
        coef_str = sys.argv[index]
    except:
        # Вводим с клавиатуры
        print(prompt)
        coef_str = input()
    # Переводим строку в действительное число
    try:
        coef = float(coef_str)
    except:
        return get_coef(index, prompt)
    return coef


def get_roots(a, b, c):
    result = []
    D = b * b - 4 * a * c
    if D == 0.0:
        root = -b / (2.0 * a)
        result.append(math.sqrt(root))
        result.append(-math.sqrt(root))
    elif D > 0.0:
        sqD = math.sqrt(D)
        root1 = (-b + sqD) / (2.0 * a)
        root2 = (-b - sqD) / (2.0 * a)
        if root1 > 0:
            result.append(math.sqrt(root1))
            result.append(-math.sqrt(root1))
        elif root1 == 0:
            result.append(root1)
        if root2 >= 0:
            result.append(math.sqrt(root2))
            result.append(-math.sqrt(root2))
        elif root2 == 0:
            result.append(root2)
    return result


def check_coef(a, b, c):
    if a != 0:
        return get_roots(a, b, c)
    else:
        if b != 0:
            if c != 0:
                return [-c / b]
            else:
                return [0]
        else:
            if c != 0:
                return []
            else:
                return ['infinity']


def main():
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')

    # Вычисление корней
    roots = check_coef(a, b, c)
    # Вывод корней
    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 1:
        print('{}'.format(roots[0]))
    elif len_roots == 2:
        print('{} и {}'.format(roots[0], roots[1]))
    elif len_roots == 3:
        print('{}, {} и {}'.format(roots[0], roots[1], roots[2]))
    elif len_roots == 4:
        print('{}, {}, {} и {}'.format(roots[0], roots[1], roots[2], roots[3]))


if __name__ == "__main__":
    main()
