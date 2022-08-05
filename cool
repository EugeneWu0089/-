## 字符串和常用數據結構

### 使用字符串

第二次世界大戰促使了現代電子計算機的誕生，最初的目的用計算機來快速的完成導彈彈道的計算，因此在計算機剛剛誕生的那個年代，計算機處理的信息基本上都是數值型的信息，而世界上的第一臺電子計算機ENIAC每秒鐘能夠完成約5000次浮點運算。隨著時間的推移，雖然數值運算仍然是計算機日常工作中最為重要的事情之一，但是今天的計算機更多的時間需要處理的數據可能都是以文本的方式存在的，如果我們希望通過Python程序操作本這些文本信息，就必須要先了解字符串類型以及與它相關的知識。

所謂**字符串**，就是由零個或多個字符組成的有限序列，一般記為![$${\displaystyle s=a_{1}a_{2}\dots a_{n}(0\leq n \leq \infty)}$$](./res/formula_5.png)。

我們可以通過下面的代碼來了解字符串的使用。

```Python
def main():
    str1 = 'hello, world!'
    # 通過len函數計算字符串的長度
    print(len(str1))  # 13
    # 獲得字符串首字母大寫的拷貝
    print(str1.capitalize())  # Hello, world!
    # 獲得字符串變大寫後的拷貝
    print(str1.upper())  # HELLO, WORLD!
    # 從字符串中查找子串所在位置
    print(str1.find('or'))  # 8
    print(str1.find('shit'))  # -1
    # 與find類似但找不到子串時會引發異常
    # print(str1.index('or'))
    # print(str1.index('shit'))
    # 檢查字符串是否以指定的字符串開頭
    print(str1.startswith('He'))  # False
    print(str1.startswith('hel'))  # True
    # 檢查字符串是否以指定的字符串結尾
    print(str1.endswith('!'))  # True
    # 將字符串以指定的寬度居中並在兩側填充指定的字符
    print(str1.center(50, '*'))
    # 將字符串以指定的寬度靠右放置左側填充指定的字符
    print(str1.rjust(50, ' '))
    str2 = 'abc123456'
    # 從字符串中取出指定位置的字符(下標運算)
    print(str2[2])  # c
    # 字符串切片(從指定的開始索引到指定的結束索引)
    print(str2[2:5])  # c12
    print(str2[2:])  # c123456
    print(str2[2::2])  # c246
    print(str2[::2])  # ac246
    print(str2[::-1])  # 654321cba
    print(str2[-3:-1])  # 45
    # 檢查字符串是否由數字構成
