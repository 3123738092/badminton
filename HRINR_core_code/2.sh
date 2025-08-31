#!/bin/bash

#SBATCH -N 1                  # 使用1个节点
#SBATCH -p i64m1tga800u       # 指定分区（可选：i64m1tga40u, i64m1tga800u）
#SBATCH --gres=gpu:1          # 申请1块GPU
#SBATCH --time=7-00:00:00     # 最长运行时间7天
#SBATCH --job-name=rstt-TL-vfi-d1020-4-7-256-pretrained-large-v4  # 作业名称
#SBATCH --output=./hpc-ii-11/%j-job.out  # 输出日志（%j为作业ID）
#SBATCH --error=./hpc-ii-11/%j-error.err  # 错误日志
#SBATCH --cpus-per-task=8     # 每个任务分配8个CPU核心

# 确保日志目录存在
mkdir -p ./hpc-ii-11
mkdir -p ./log/vfi-sr/1-TimeLens++/1-VFI-Only/3-Skip-Testing-In-1-Skip/1-TimeLems++-BS-ERGB-Skip-3-Train-Skip-1-Test/

source /hpc2hdd/home/ychen590/miniconda3/etc/profile.d/conda.sh
conda activate HRINR

# 设置环境变量（根据实际情况调整）
export CUDA_VISIBLE_DEVICES="0"  # Slurm已分配1块GPU，建议使用0而非3
export PYTHONPATH="./3rdparty/:./:$PYTHONPATH"  # 合并路径设置

# 打印作业信息（便于调试）
echo "============================================="
echo "Job started at: $(date "+%Y-%m-%d %H:%M:%S")"
echo "Job ID: $SLURM_JOB_ID"
echo "Node: $(hostname)"
echo "Partition: $SLURM_JOB_PARTITION"
echo "GPU(s) allocated: $SLURM_GPUS_ON_NODE"
echo "CPU cores allocated: $SLURM_CPUS_PER_TASK"
echo "============================================="
echo "Python version: $(python --version 2>&1)"
echo "Python path: $(which python)"
echo "CUDA version: $(nvcc --version | grep release | cut -d ' ' -f 5 | cut -d ',' -f 1)"
nvidia-smi
echo "============================================="

# 执行任务
python 2.py


# 记录作业结束时间
echo "============================================="
echo "Job finished at: $(date "+%Y-%m-%d %H:%M:%S")"
echo "============================================="
