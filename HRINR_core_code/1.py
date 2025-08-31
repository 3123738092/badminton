import os
import shutil

def find_and_copy_out_png(source_dir, dest_dir, recursive=True):
    """
    查找指定目录中所有后缀为out.png的文件，并复制到目标文件夹
    
    参数:
        source_dir: 源目录路径（要搜索的文件夹）
        dest_dir: 目标目录路径（保存复制文件的新文件夹）
        recursive: 是否递归查找子文件夹，默认为True
        
    返回:
        成功复制的文件数量
    """
    # 确保目标文件夹存在，如果不存在则创建
    os.makedirs(dest_dir, exist_ok=True)
    
    # 检查源目录是否有效
    if not os.path.isdir(source_dir):
        print(f"错误: 源目录 '{source_dir}' 不存在或不是一个有效的目录")
        return 0
    
    copied_count = 0
    
    # 遍历源目录
    for item in os.listdir(source_dir):
        item_path = os.path.join(source_dir, item)
        
        # 如果是目录且需要递归查找，则递归处理
        if os.path.isdir(item_path) and recursive:
            copied_count += find_and_copy_out_png(item_path, dest_dir, recursive)
        # 如果是文件且以out.png结尾
        elif os.path.isfile(item_path) and item.endswith('out.png'):
            # 构建目标文件路径
            dest_path = os.path.join(dest_dir, item)
            
            # 处理同名文件的情况
            counter = 1
            while os.path.exists(dest_path):
                # 如果文件已存在，添加编号区分
                name, ext = os.path.splitext(item)
                dest_path = os.path.join(dest_dir, f"{name}_{counter}{ext}")
                counter += 1
            
            # 复制文件
            shutil.copy2(item_path, dest_path)  # copy2会保留文件元数据
            copied_count += 1
            print(f"已复制: {item_path} -> {dest_path}")
    
    return copied_count

if __name__ == "__main__":
    # 源文件夹路径（要搜索的文件夹）
    source_directory = "./log/vfi-sr/1-TimeLens++"  # Linux/Mac示例
    # source_directory = "C:\\path\\to\\source\\folder"  # Windows示例
    
    # 目标文件夹路径（新文件夹，用于保存筛选出的文件）
    destination_directory = "./output"  # Linux/Mac示例
    # destination_directory = "C:\\path\\to\\destination\\folder"  # Windows示例
    
    # 执行查找和复制操作（recursive=False可关闭递归查找）
    total_copied = find_and_copy_out_png(source_directory, destination_directory, recursive=True)
    
    # 输出结果
    if total_copied > 0:
        print(f"\n操作完成，共复制了 {total_copied} 个out.png文件到 {destination_directory}")
    else:
        print("未找到任何out.png文件或复制过程出错")
    