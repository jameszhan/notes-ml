# notes-ml

机器学习手札

## Git LFS

```bash
git lfs install

git lfs track "*.csv"
git lfs track "*.zip"
git lfs track "*.tar.gz"
git lfs track "*.mat"

git lfs track

git lfs ls-files
```

## Anaconda

```bash
conda update conda
conda update anaconda

conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --set show_channel_urls yes

conda env list
```

```bash
conda create -n python2 python=2 scikit-learn
conda install numpy scipy sympy matplotlib -n python2

source activate python2
conda list
python -c 'import sys; print(sys.version)'
source deactivate python2
```

```bash
# conda install -c conda-forge jupyter_contrib_nbextensions

conda install nb_conda
conda remove nb_conda
```

## How to Run Python3 File In VS Code

### Select Workspace Interpreter

* CMD + SHIFT + P: Select Workspace Interpreter
* RIGNT CLICK: Run Python File In Ternimal




