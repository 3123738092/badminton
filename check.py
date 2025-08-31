import torch

checkpoint = torch.load("D:\桌面\checkpoint.pth.tar", map_location='cpu')
print(checkpoint.keys())  # 查看包含哪些主键

# 查看模型参数结构
for k in checkpoint['state_dict'].keys():
    print(k)