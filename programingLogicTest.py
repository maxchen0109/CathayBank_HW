def print_triangle(n):
    """
    輸入值(n)為整數型別
    輸出為*符號且邊長為輸入數字的空心正三角形

    邏輯說明：
    1. 先判斷輸入值是否為整數型別或是大於1，若是，才能進行空心正三角形的輸出
    2. 列印空格，為每行建立所需的縮排，每行的縮排會遞減
    3. 透過 prev 變數來決定非頭、尾行的空格數量。
    """
    if not isinstance(n, int) or n <= 1:
        print("輸入值須為整數且大於1")
    else:
        prev = 0
        for i in range(n):
            if i == 0:
                print(''.join([' ' * (n - i - 1), ' *', ' ' * (i)]))
            elif i < n-1:
                print(''.join([' ' * (n - i - 1), ' *', ' ' * (i + prev), '*']))
                prev += 1
            else:
                print(''.join([' *' * (i +1)]))


def sort_numbers(numbers):
    """
    輸入值(numbers)為字串型別
    輸出為依照” 奇數都在偶數前面”，且”偶數升冪排序”，”奇數降冪排序” 的字串型別

    邏輯說明：
    1. 先判斷輸入值是否包含『非整數』的值，若沒有，才能進行數字排序
    2. 分別將，不能被2整除的數取出存入串列裡並進行降冪排序，能被2整除的數取出存入串列裡並進行排序
    3. 將兩個串列裡的值進行合併
    """
    if False in list(map(lambda i: i.isdigit(), list(str(numbers)))):
        print("輸入值不可含非數字")
    else:
        print(
            "".join(
                sorted(
                    [s2 for s2 in list(str(numbers)) if int(s2) % 2 != 0], reverse=True
                )
                + sorted([s1 for s1 in list(str(numbers)) if int(s1) % 2 == 0])
            )
        )


# 測試案例：
print_triangle(1)
print_triangle(3)
print_triangle(6)
print_triangle("3")
print_triangle("a")
sort_numbers("417324689435")
sort_numbers("s256sfsaf")
