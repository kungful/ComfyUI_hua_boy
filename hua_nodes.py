#---------------------------------------------------------------------------------------------------------------------#
#节点作者：hua   代码地址：https://github.com/kungful/ComfyUI_hua_boy.git
#---------------------------------------------------------------------------------------------------------------------#
from .hua_icons import icons
import typing as tg



#---------------------------------------------------------------------------------------------------------------------#
class Hua_gradio_Seed:

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {
            "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff})}}

    RETURN_TYPES = ("INT", "STRING", )
    RETURN_NAMES = ("seed", "show_help", )
    FUNCTION = "hua_seed"
    OUTPUT_NODE = True
    CATEGORY = icons.get("hua_boy_one")

    @staticmethod
    def hua_seed(seed):
        show_help = "https://github.com/kungful/ComfyUI_hua_boy.git"
        return (seed, show_help,)
#---------------------------------------------------------------------------------------------------------------------#