#---------------------------------------------------------------------------------------------------------------------#
#节点作者：hua   代码地址：https://github.com/kungful/ComfyUI_hua_boy.git
#---------------------------------------------------------------------------------------------------------------------#
from .hua_icons import icons
import typing as tg
import json
import os
import random
import numpy as np  # 用于处理图像数据
from PIL import Image, ImageOps, ImageSequence, ImageFile
from PIL.PngImagePlugin import PngInfo
import folder_paths  # 假设这是一个自定义模块，用于处理文件路径
from comfy.cli_args import args


OUTPUT_DIR = folder_paths.get_output_directory()


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

class Hua_gradio_jsonsave:
    def __init__(self):
        self.output_dir = folder_paths.get_output_directory()
        self.type = "output"
        self.prefix_append = ""
        self.compress_level = 4

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "images": ("IMAGE", {"tooltip": "The images to save."}),
                "filename_prefix": ("STRING", {"default": "apijson", "tooltip": "The prefix for the file to save. This may include formatting information such as %date:yyyy-MM-dd% or %Empty Latent Image.width% to include values from nodes."})
            },
            "hidden": {
                "prompt": "PROMPT", "extra_pnginfo": "EXTRA_PNGINFO"
            },
        }


    RETURN_TYPES = ()
    RETURN_NAMES = ()
    FUNCTION = "autosavejson"
    OUTPUT_NODE = True
    CATEGORY = icons.get("hua_boy_one")
    DESCRIPTION = "保存api格式json工作流到input文件夹下"

    def autosavejson(self, images, filename_prefix="apijson", prompt=None, extra_pnginfo=None):
        filename_prefix += self.prefix_append
        full_output_folder, filename, counter, subfolder, filename_prefix = folder_paths.get_save_image_path(filename_prefix, self.output_dir, images[0].shape[1], images[0].shape[0])
        results = list()
        # results = []
        counter = 0  # 初始化计数器
        for i, image in enumerate(images):
            imagefilename = f"{filename_prefix}_{i}.png"
            results.append({
                "imagefilename": imagefilename,
            })

            # Save JSON file
            filename_with_batch_num = f"{filename_prefix}"
            
            json_filename = f"{filename_with_batch_num}_{counter:05}_.json"
            json_data = prompt
            json_file_path = os.path.join(full_output_folder, json_filename)
            with open(json_file_path, 'w', encoding='utf-8') as json_file:
                json.dump(json_data, json_file, ensure_ascii=False, indent=4)
            
            # 调试信息0+
            print(f"保存的api格式json文件位置: {json_file_path}")
            counter += 1
           


        return { "ui": { "images": results } }
