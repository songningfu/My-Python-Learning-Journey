# -*- coding: utf-8 -*-
"""
Spyder 编辑器

这是一个临时脚本文件。
"""
import random
# 生成1-100的随机整数
secret_number = random.randint(1, 100)
guess_count = 0  # 记录猜测次数

while True:
    # 获取用户输入并转换为整数
    user_guess = int(input("请输入1-100之间的数字："))
    guess_count += 1
    
    if user_guess > secret_number:
        print("大了！")
    elif user_guess < secret_number:
        print("小了！")
    else:
        print(f"恭喜猜对了！你一共猜了{guess_count}次。")
        break  # 猜对后跳出循环
