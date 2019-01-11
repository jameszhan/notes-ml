# Python 环境准备

## Anaconda

### 安装 Anaconda

#### OS X 环境安装

```bash
wget https://repo.continuum.io/archive/Anaconda3-2018.12-MacOSX-x86_64.sh
bash ./Anaconda3-2018.12-MacOSX-x86_64.sh
```

#### Linux 环境安装

```bash
wget https://repo.continuum.io/archive/Anaconda3-2018.12-Linux-x86_64.sh
bash ./Anaconda3-2018.12-Linux-x86_64.sh
```

### 配置 Anaconda 环境

```bash
conda update conda
conda update anaconda

conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --set show_channel_urls yes

conda env list
```

### 切换 Python 版本

```bash
conda create -n py2 python=2
source activate py2
conda list
python -c 'import sys; print sys.version'
source deactivate py2
```