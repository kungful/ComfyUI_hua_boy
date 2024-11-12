# ComfyUI_hua_boy

## 概述
_ **示例工作流在** Sample_preview 文件夹里面
`ComfyUI_hua_boy` 是一个为 ComfyUI工作流变成webui的项目


## 未完成的功能。
- **Gradio 集成**：根据数字键检索自动开启 gradio 前端图像输入框。
- **模型选择**：轻松选择项目所需的模型。
- **分辨率选择**：选择所需的输出分辨率。
- **种子管理**：随机种。
- **增强的界面**：更美观、用户友好的界面。

## 安装

### 导航到custom_nodes
1. **克隆仓库**：
   ```bash
   git clone https://github.com/yourusername/ComfyUI_hua_boy.git
   cd ComfyUI_hua_boy
   ..\..\..\python_embeded\python.exe -m pip install -r requirements.txt
## 使用方法
你的comfyui搭建好工作流后开启comfyui设置里的开发者模式，保存api格式工作流放入下面的路径替换即可

### 把api格式工作流文件放到comfyui根目录###
1. **示例**
   ```bash
   D:\
     └── comfyUI\
       ├── ComfyUI\
       │   ├── run1.json
       │   └── ...
       └── custom_nodes\
              └── ComfyUI_hua_boy

### gradio前端效果
后续会开发更多功能
![预览image](https://github.com/kungful/ComfyUI_hua_boy/blob/c4176cc896378e4745925c1d528cb910f6f6fa11/Sample_preview/c1e59d869b7f79c33f686b94c1db368.png)
### 搭建需要封装的工作流
需要使用本插件的节点才可以与gradio前端交互。随机种输入输出等
![预览image](https://github.com/kungful/ComfyUI_hua_boy/blob/c4176cc896378e4745925c1d528cb910f6f6fa11/Sample_preview/484b25201870c5e8105a6ee08e6370d.png)
### 思维导图节点
不可推理
![预览image](https://github.com/kungful/ComfyUI_hua_boy/blob/c4176cc896378e4745925c1d528cb910f6f6fa11/Sample_preview/6b8564af2dbb2b75185f0bcc7cf5cd5.png)

### 这是检索多提示词字符串判断图片是否传递哪个模型和图片的布尔节点，为的是跳过puilid的报错
![预览image](https://github.com/kungful/ComfyUI_hua_boy/blob/a58958bcd59ec3c44130a8f72ea061b08d6a555a/Sample_preview/image.png)
![预览model](https://github.com/kungful/ComfyUI_hua_boy/blob/e662eb157599db53d5efca70d481a1ad59ea53bb/Sample_preview/model.png)
