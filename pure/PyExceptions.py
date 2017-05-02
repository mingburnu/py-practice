# encoding: utf-8


def my_divide():
    # 會讓程式出錯,所以需要特別handle
    try:
        10 / 0

    except ZeroDivisionError:
        print("不能除以0!!!")
    else:
        print("沒有任何錯誤")
    finally:
        print("無論有沒有例外都會執行這一行")


my_divide()
