# Python 环境准备

## Anaconda

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
conda create -n python2 python=2 scikit-learn
conda install numpy scipy sympy matplotlib -n python2

source activate python2
conda list
python -c 'import sys; print(sys.version)'
source deactivate python2
```