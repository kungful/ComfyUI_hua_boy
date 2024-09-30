from collections import Counter
import re

def count_word_occurrences(text, target_words):
    """
    统计目标单词在文本中出现的次数，并返回总次数。

    :param text: 输入的文本
    :param target_words: 目标单词列表（可以是字符串或列表）
    :return: 目标单词在文本中出现的总次数
    """
    # 将目标单词列表转换为小写
    target_words = [word.lower() for word in target_words]
    
    # 使用正则表达式将文本分割成单词列表，并将所有单词转换为小写
    words = re.findall(r'\b\w+\b', text.lower())
    
    # 使用Counter统计每个单词出现的次数
    word_counts = Counter(words)
    
    # 初始化总次数为0
    total_count = 0
    
    # 遍历目标单词列表，累加它们的出现次数
    for word in target_words:
        total_count += word_counts.get(word, 0)
    
    return total_count

# 获取输入的文本和目标单词列表
text = inputs["0_string"]
target_words = inputs["1_output_0"].split()


# 获取目标单词的出现总次数
total_word_count = count_word_occurrences(text, target_words)

# 将结果存储在 outputs[0] 中
outputs[0] = [total_word_count]

# 如果 total_word_count 大于零，将 outputs[0] 设置为 inputs["0_image"]
if total_word_count > 0:
    outputs[1] = inputs["2_image"]
else:
    outputs[1] = inputs["3_image"]


# 打印结果
print(f"目标单词 '{target_words}' 总共出现了 {total_word_count} 次")