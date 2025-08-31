import os
import subprocess

# ==================== 配置参数 ====================
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
os.environ["PYTHONPATH"] = "./3rdparty;./"  # 确保根目录在PYTHONPATH中

yaml_file = r"options\vfi-sr\1-TimeLens++\1-VFI-Only\3-Skip-Testing-In-1-Skip\1-TimeLems++-BS-ERGB-Skip-3-Train-Skip-1-Test.yaml"
log_dir = r".\log\vfi-sr\1-TimeLens++\1-VFI-Only\3-Skip-Testing-In-1-Skip\1-TimeLems++-BS-ERGB-Skip-3-Train-Skip-1-Test"
resume_path = r".\checkpoint.pth.tar"
# ==================== 运行程序 ====================
command = [
    "python",
    "egrsdb/main.py",
    f"--yaml_file={yaml_file}",
    f"--log_dir={log_dir}",
    "--alsologtostderr=True",
    f"--RESUME_PATH={resume_path}",
    "--VISUALIZE=True",
    "--TEST_ONLY=True"
]

try:
    # 运行命令并捕获 stdout 和 stderr
    result = subprocess.run(
        command, 
        check=True, 
        capture_output=True, 
        text=True,
        cwd=os.getcwd()  # 确保在项目根目录运行
    )
    print("程序输出：")
    print(result.stdout)
except subprocess.CalledProcessError as e:
    # 打印详细错误信息（关键！）
    print("="*50)
    print("命令运行失败！")
    print("错误代码：", e.returncode)
    print("标准错误输出：")
    print(e.stderr)  # 显示main.py的具体错误
    print("="*50)
    raise  # 抛出异常