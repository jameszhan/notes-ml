# TensorFlow

## 安装 TensorFlow

### 通过 conda 安装

#### 更新 conda

```bash
conda update -n base conda
conda update -n base anaconda
conda update -n base --all
```

#### 通过 conda-forge 安装

```bash
conda create -n tf -y python=3.6
conda install -n tf -c conda-forge tensorflow

source activate tf

conda list
python -c "import tensorflow as tf; print(tf.__version__)"
```

#### 删除 Tensorflow

```bash
conda remove tensorflow
source deactivate
conda env remove -y -n tf
```

### 通过 pip 安装

#### 更新 pip

```bash
conda create -n tf -y python=3.6
source activate tf

pip install --upgrade pip
```

#### 安装指定版本

```bash
# 列出 pypi 上所有可用的版本
../../../06-programing-languages/01-pythons/03-just-for-fun/01-systems/pypi_versions tensorflow

pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -U tensorflow==1.8.0
pip check
conda list

python -c "import tensorflow as tf; print(tf.__version__)"
```

#### 删除指定版本

```bash
pip uninstall -y tensorflow==1.8.0
source deactivate
conda env remove -y -n tf
```