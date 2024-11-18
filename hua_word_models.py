from collections import Counter
from PIL import Image
import re
from .hua_icons import icons
class Modelhua:
    def __init__(self):
        pass
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text1": ("STRING", {"multiline": True, "dynamicPrompts": True, "tooltip": "我是靓仔1全量字符串"}),
                "text2": ("STRING", {"multiline": True, "dynamicPrompts": True, "tooltip": "我是靓仔2指定字符串"}),
                "model1": ("MODEL",),
                "model2": ("MODEL",),
            },
        }

    RETURN_TYPES = ("MODEL",)
    OUTPUT_TOOLTIPS = ("在字符串中出现了你提到的词则会选在model1，如果没有就model2输出",)
    FUNCTION = "load_model_hua"
    OUTPUT_NODE = True
    CATEGORY = icons.get("hua_boy_one")

    def load_model_hua(self, text1, text2, model1, model2):
        text2_words = set(word.lower() for word in text2.split())
        words = re.findall(r'\b\w+\b', text1.lower())
        word_counts = Counter(words)
        total_count = sum(word_counts[word] for word in text2_words)
        
        if total_count > 0:
            model_options = model1
        else:
            model_options = model2
        
        print(f"目标单词 '{text2}' 总共出现了 {total_count} 次")
        # 添加打印语句
        return (model_options,)

NODE_CLASS_MAPPINGS = {
    "小字体说明：我是comfyui_hua_boy的model": Modelhua
} 

NODE_DISPLAY_NAME_MAPPINGS = {
    "小字体说明：我是comfyui_hua_boy的model": "布尔模型Boolean_model"
}
