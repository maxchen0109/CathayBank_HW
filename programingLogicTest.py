def print_triangle(n):
    """
    輸入值(n)為整數型別
    輸出為*符號且邊長為輸入數字的空心正三角形

    邏輯說明：
    1. 先判斷輸入值是否為整數型別，若是，才能進行空心正三角形的輸出
    2. 進行 1~ (n+1) 輸出控制三角形形狀的空格數與 * 個數
    """
    if type(n) != int: 
        print('輸入值須為整數')
    else:
        for i in range(1, n+1):
            print(''.join([' '*(n-i), '* '*(i)]))


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
        print('輸入值不可含非數字')
    else:
        print(''.join(sorted([s2 for s2 in list(str(numbers)) if int(s2)%2 != 0],reverse=True)+sorted([s1 for s1 in list(str(numbers)) if int(s1)%2 == 0])))


#測試案例：
print_triangle(3)
print_triangle(4)
print_triangle('3')
print_triangle('a')
sort_numbers('417324689435')
sort_numbers('s256sfsaf')