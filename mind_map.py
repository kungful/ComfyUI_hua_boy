import os
from PIL import Image, ImageOps, ImageSequence
import numpy as np
import torch
# 导入 folder_paths 模块
import folder_paths # type: ignore
from .hua_icons import icons

class Go_to_image:
    _color_channels = 3  # 假设RGB颜色通道数为3
    @classmethod
    def INPUT_TYPES(s):  #定义输入类型
        input_dir = folder_paths.get_input_directory()  # 获取输入目录
        files = sorted(os.listdir(input_dir))  # 获取输入目录下的文件列表，并按字母排序
        return {
            "required": {  # 必需输入
                "image": (files, {"image_upload": True}),  # 图像文件名，允许上传
                "pos_text": ("STRING", {"multiline": True, "default": "positive text"}),  # 正面文本，默认为"positive text"

                "images": ("IMAGE", ), 
                
            }
        }
        
    
    

    RETURN_TYPES = ("IMAGE", "MASK", "CONDITIONING")   #返回类型，为3个输出口


    FUNCTION = "load_image" #函数名称

    CATEGORY = icons.get("hua_boy_one")  #传递一级类显示在树列表

    def load_image(self, image):
        image_path = folder_paths.get_annotated_filepath(image)
        img = Image.open(image_path)
        output_images = []
        output_masks = []
        for i in ImageSequence.Iterator(img):
            i = ImageOps.exif_transpose(i)
            if i.mode == 'I':
                i = i.point(lambda i: i * (1 / 255))
            image = i.convert("RGB")
            image = np.array(image).astype(np.float32) / 255.0
            image = torch.from_numpy(image)[None,]
            if 'A' in i.getbands():
                mask = np.array(i.getchannel('A')).astype(np.float32) / 255.0
                mask = 1. - torch.from_numpy(mask)
            else:
                mask = torch.zeros((64,64), dtype=torch.float32, device="cpu")
            output_images.append(image)
            output_masks.append(mask.unsqueeze(0))

        if len(output_images) > 1:
            output_image = torch.cat(output_images, dim=0)
            output_mask = torch.cat(output_masks, dim=0)
        else:
            output_image = output_images[0]
            output_mask = output_masks[0]

        return (output_image, output_mask)



NODE_CLASS_MAPPINGS = {   
    "brucelee": Go_to_image # 赋值类的名称
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {    #这是个字典，它将节点名称映射到人类容易读取的名字，可以通过 NODE_DISPLAY_NAME_MAPPINGS["Hua"] 访问到 "Demo Node" （第二级子目录）
    "brucelee": "思维导图"     # 相当于传递上面的："brucelee"= Go_to_image = "brucelee": "HUA_go_image"
}
