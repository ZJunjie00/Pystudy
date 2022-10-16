import re
import time

start=time.time()
with open("sdxl.txt", "r", encoding="utf-8") as fd:
    word_list = []
    word_dict = {}
    for line in fd.readlines():
        for word in line.strip().split(" "):
            word_list.append(re.sub(r"[.|!|,]", "", word.lower()))
    word_sets = list(set(word_list))
    word_dict = {word: word_list.count(word) for word in word_sets if word}
result = sorted(word_dict.items(), key=lambda d: d[1], reverse=True)[:10]
print(result)
end=time.time()
print("程序的运行时间为：{}".format(end-start))


