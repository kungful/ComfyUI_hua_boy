# ComfyUI_hua_boy

## 概述
<span style="color:blue;">**示例工作流在**</span> Sample_preview 文件夹里面
<span style="color:blue;">**`ComfyUI_hua_boy` 是一个为 ComfyUI工作流变成webui的项目**</span>

## 计划的功能
- **自动保存api json流**: 已编写完成
- **gradio前端动态显示图像输入口**：已编写完成
- **模型选择**：开发中.......
- **分辨率选择**：开发中......
- **种子管理**：已编写完成
- **生成的批次** 开发中.....
  <span style="color:purple;">随机种已经完成</span>
- **增强的界面**：更美观、用户友好的界面。

## 安装

### 导航到custom_nodes
1. **克隆仓库**：
   ```bash
   git clone https://github.com/yourusername/ComfyUI_hua_boy.git
   cd ComfyUI_hua_boy
   ..\..\..\python_embeded\python.exe -m pip install -r requirements.txt
## 使用方法
你的comfyui搭建好工作流后不需要手动保存api格式json文件，只需要运行一遍跑通后就可以了，在输出端接入"☀️gradio前端传入图像这个节点就行

### 已经完成自动保存api工作流功能，工作流位置在output
1. **api工作流自动保存位置**
   ```bash
   D:\
     └── comfyUI\
       ├── ComfyUI\
       │   ├── output
       │   └── ...
     

### gradio前端效果
后续会开发更多功能
![预览image](https://github.com/kungful/ComfyUI_hua_boy/blob/470abc9bc95fc410815eb61deb43d0590abf92d3/Sample_preview/%E5%89%8D%E7%AB%AF.png)
### 搭建需要封装的工作流
需要使用本插件的节点才可以与gradio前端交互。随机种输入输出等
![预览image](https://github.com/kungful/ComfyUI_hua_boy/blob/c4176cc896378e4745925c1d528cb910f6f6fa11/Sample_preview/484b25201870c5e8105a6ee08e6370d.png)
### 思维导图节点
不可推理
![预览image](https://github.com/kungful/ComfyUI_hua_boy/blob/c4176cc896378e4745925c1d528cb910f6f6fa11/Sample_preview/6b8564af2dbb2b75185f0bcc7cf5cd5.png)

### 这是检索多提示词字符串判断图片是否传递哪个模型和图片的布尔节点，为的是跳过puilid的报错
![预览image](https://github.com/kungful/ComfyUI_hua_boy/blob/a58958bcd59ec3c44130a8f72ea061b08d6a555a/Sample_preview/image.png)
![预览model](https://github.com/kungful/ComfyUI_hua_boy/blob/e662eb157599db53d5efca70d481a1ad59ea53bb/Sample_preview/model.png)
