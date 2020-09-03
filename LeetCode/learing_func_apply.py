import pandas as pd
import numpy as np
import datetime as dt


# 正常定义函数
def can_divide_by_three(num):
    if num % 3 == 0:
        return True
    else:
        return False


# 执行获得可以整除3的数
selected_num = []
for number in range(1, 11):
    if can_divide_by_three(number):
        selected_num.append(number)
# print(selected_num)

# 使用lambda来简化函数
devide_modified = lambda x: True if x % 3 == 0 else False

selected_nums = []
for number in range(1, 11):
    if devide_modified(number):
        selected_nums.append(number)
# print(selected_nums)

# 从一个 list 中取出特定规则的数字， 只关注和设置这个规则，循环交给编程语言去处理
# filter(function, sequence)
# filter() 函数的功能：对 sequence 中的 item 依次执行 function(item)，
# 将结果为 True 的 item 组成一个 List/String/Tuple（取决于 sequence 的类型）并返回。
# 有了这个函数，上面的代码可以简化为：
devide_func_modified_two = lambda x: True if x % 3 == 0 else False
selected_nums_two = filter(devide_func_modified_two, range(1, 11))

# 将 lambda 表达式放在语句中
selected_numbers = filter(lambda x: x % 3 == 0, range(1, 11))

# Series.apply()
# pandas 的 apply() 函数可以作用于 Series 或者整个 DataFrame，
# 功能也是自动遍历整个 Series 或者 DataFrame, 对每一个元素运行指定的函数。
#
# 举一个例子，现在有这样一组数据，学生的考试成绩：
#
#   Name Nationality  Score
#    张           汉    400
#    李           回    450
#    王           汉    460


df = pd.DataFrame(data=[['张', '汉', 400], ["李", '回', 450], ['王', '汉', 460]],
                  columns=['Name', 'Nationality', 'Score'])
df['ExtraScore'] = df['Nationality'].apply(lambda x: 5 if x != '汉' else 0)
df['TotalScore'] = df['ExtraScore'] + df['Score']
# print(df)

# apply()也可执行python内置的函数，如得到Name这一列字符的个数，如用 apply()：
df['NameLen'] = df['Name'].apply(len)
# print(df)

# DataFrame.apply()
# DataFrame.apply() 函数则会遍历每一个元素，
# 对元素运行指定的 function。比如下面的示例：
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
df_square = pd.DataFrame(matrix, columns=list('xyz'), index=list('abc'))

# 对 df 执行 square() 函数后，所有的元素都执行平方运算：
df_square_all = df_square.apply(np.square)
print(df_square_all)

# 如果只想 apply() 作用于指定的行和列
# 可以用行或者列的 name 属性进行限定。比如下面的示例将 x 列进行平方运算：
df_square_column_x = df_square.apply(lambda x: np.square(x) if x.name == 'x' else x)
# print(df_square_column_x)

# 下面的示例对 x 和 y 列进行平方运算：
df_square_column_x_y = df_square.apply(lambda x: np.square(x) if x.name in ['x', 'y'] else x)
# print(df_square_column_x_y)

# 下面的示例对第一行 （a 标签所在行）进行平方运算
# 默认情况下 axis=0 表示按列，axis=1 表示按行。
df_row_first = df_square.apply(lambda x: np.square(x) if x.name == 'a' else x, axis=1)
# print(df_row_first)

# apply() 计算日期相减示例
# 平时我们会经常用到日期的计算，比如要计算两个日期的间隔，比如下面的一组关于 wbs 起止日期的数据
wbs = {
    "wbs": ["job1", "job2", "job3", "job4"],
    "date_from": ["2019-04-01", "2019-04-07", "2019-05-16", "2019-05-20"],
    "date_to": ["2019-05-01", "2019-05-17", "2019-05-31", "2019-06-11"]
}

# 日期间隔已经计算出来，但后面带有一个单位 days，
# 这是因为两个 datetime 类型相减，得到的数据类型是 timedelta64，如果只要数字，还需要使用 timedelta 的 days 属性转换一下。
df_dates = pd.DataFrame(wbs)
elapsed = df_dates['date_to'].apply(pd.to_datetime) - df_dates['date_from'].apply(pd.to_datetime)
df_dates['elapsed'] = elapsed.apply(lambda x: x.days)
print(df_dates)


# 使用 DataFrame.apply() 函数也能达到同样的效果，
# 我们需要先定义一个函数 get_interval_days() 函数的第一列是一个 Series 类型的变量，执行的时候，依次接收 DataFrame 的每一行。
def get_interval_days(arrLike, start, end):
    start_date = dt.datetime.strptime(arrLike[start], '%Y-%m-%d')
    end_date = dt.datetime.strptime(arrLike[end], '%Y-%m-%d')
    return (end_date - start_date).days


wbs = {
    "wbs": ["job1", "job2", "job3", "job4"],
    "date_from": ["2019-04-01", "2019-04-07", "2019-05-16", "2019-05-20"],
    "date_to": ["2019-05-01", "2019-05-17", "2019-05-31", "2019-06-11"]
}

df = pd.DataFrame(wbs)
df['elapsed'] = df.apply(get_interval_days, axis=1, args=('date_from', 'date_to'))
