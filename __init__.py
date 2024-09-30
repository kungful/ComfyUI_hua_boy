from collections import Counter
from PIL import Image
import re
from .hua_word_image import Huaword
from .hua_word_models import Modelhua

NODE_CLASS_MAPPINGS = {
    "小字体说明：我是comfyui_hua_boy": Huaword,
    "小字体说明：我是comfyui_hua_boy的model": Modelhua
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "小字体说明：我是comfyui_hua_boy": "布尔图片Boolean_image",
    "小字体说明：我是comfyui_hua_boy的model": "布尔模型Boolean_model"
}

shit = """

██████╗ ██████╗ ██████╗ ██████╗ ██████╗ ██████╗ ██████╗ ██████╗ ██████╗ 
██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗
██████╔╝██████╔╝██████╔╝██████╔╝██████╔╝██████╔╝██████╔╝██████╔╝██████╔╝
██╔═══╝ ██╔═══╝ ██╔═══╝ ██╔═══╝ ██╔═══╝ ██╔═══╝ ██╔═══╝ ██╔═══╝ ██╔═══╝ 
██║     ██║     ██║     ██║     ██║     ██║     ██║     ██║     ██║     
╚═╝     ╚═╝     ╚═╝     ╚═╝     ╚═╝     ╚═╝     ╚═╝     ╚═╝     ╚═╝     

"""
print(shit)
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", ]