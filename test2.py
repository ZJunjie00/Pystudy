import re
import time
from collections import Counter
start=time.time()
with open("sdxl.txt", "r", encoding="utf-8") as fd:
    texts = fd.read()  # 将文件的内容全部读取成一个字符串
    count = Counter(re.split(r"\W+", texts))  # 以单词为分隔

result = count.most_common(10)  # 统计最常使用的前10个
end=time.time()
print(result)
print("程序的运行时间为：{}".format(end-start))