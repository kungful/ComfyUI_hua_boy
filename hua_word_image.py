from collections import Counter
from PIL import Image
import re
from .hua_icons import icons
class Huaword:
    def __init__(self):
        pass
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text1": ("STRING", {"multiline": True, "dynamicPrompts": True, "tooltip": "我是靓仔1全量字符串"}),
                "text2": ("STRING", {"multiline": True, "dynamicPrompts": True, "tooltip": "我是靓仔2指定字符串"}),
                "image1": ("IMAGE",),
                "image2": ("IMAGE",),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    OUTPUT_TOOLTIPS = ("在字符串中出现了你提到的词则会选在image1，如果没有就image2输出",)
    FUNCTION = "test"
    OUTPUT_NODE = True
    CATEGORY = icons.get("hua_boy_one")

    def test(self, text1, text2, image1, image2):
        text2_words = set(word.lower() for word in text2.split())
        words = re.findall(r'\b\w+\b', text1.lower())
        word_counts = Counter(words)
        total_count = sum(word_counts[word] for word in text2_words)
        
        if total_count > 0:
            output_images = image1
        else:
            output_images = image2
        
        print(f"目标单词 '{text2}' 总共出现了 {total_count} 次")
        # 添加打印语句
        return (output_images,)

NODE_CLASS_MAPPINGS = {
    "ComfyUI_hua_boy": Huaword
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ComfyUI_hua_boy": "布尔图片Boolean_image"
}
