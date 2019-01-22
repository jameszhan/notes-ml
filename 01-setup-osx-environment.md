# 打造 OS X 开发环境

版本号 | 修订日期 | 修订概述 | 修订人 | 备注
----- | ------ | ------- | ----- | -----
v0.0.1 | 2019-01-13 | Setup a new Mac | James Zhan |
v0.0.2 | 2019-01-20 | Merge notes-history/HOMEBREW.md | James Zhan |
v0.0.3 | 2019-01-22 | Add 画图工具 | James Zhan |


## 准备工作

### 安装必要软件

#### 安装 Xcode

从 App Store 上搜索 Xcode 并安装到本地。

#### 安装 Homebrew

官方地址： [Homebrew](https://brew.sh/)

一键安装

```bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

测试是否安装成功

```bash
brew --version
brew --help
```

**用法**

```bash
# 查找依赖
brew deps nginx

# 查找依赖，以树形结构显示，包含 build 和 optional 依赖。
brew deps nginx --include-build --include-optional --tree
```

```bash
# 查找当前包被谁引用了
brew uses openssl

# 查找当前包被谁引用了，只查找本地安装的
brew uses openssl --installed

# 查找当前包被谁引用了，只查找本地安装的，包含间接依赖
brew uses openssl --installed --recursive

# 查找当前包被谁引用了，包含 build 依赖，只查找本地安装的，包含间接依赖
brew uses makedepend --installed --recursive --include-build
```

**安装软件**

```bash
brew install wget
```

## 通过 Homebrew 安装软件

### 安装 App

#### Google Chrome

```bash
brew cask info google-chrome
brew cask install google-chrome
```

#### 搜狗输入法

```bash
brew cask info sogouinput
brew cask install sogouinput
open /usr/local/Caskroom/sogouinput/<VERSION>/sogou_mac_<NUM>.app
```

#### Alfred

```bash
brew cask info alfred
brew cask install alfred
```

#### iTerm2

```bash
brew cask info iterm2
brew cask install iterm2
```

#### Docker

```bash
brew cask info docker
brew cask install docker
```

#### Visual Studio Code

```bash
brew cask info visual-studio-code
brew cask install visual-studio-code
alias vscode="open -b com.microsoft.VSCode"
```

#### Sublime Text 3

```bash
brew cask info sublime-text
brew cask install sublime-text
```

#### Typora

```bash
brew cask info typora
brew cask install typora
alias typora="open -a typora"
```

#### kdiff3

```bash
brew cask info kdiff3
brew cask install kdiff3
```

## 配置开发环境

### 开发环境准备

#### 配置工作目录

```bash
sudo mkdir /james
sudo chown -R james:staff /james
cd /james
mkidr workdir
cd workdir
```

#### 配置 Git

安装最新版本的 git

```bash
brew install git
brew install git-lfs
```

配置你的 git 项目

```bash
git config user.name "James Zhan"
git config user.email "zhiqiangzhan@gmail.com"
git commit --amend --reset-author
```
git 全局配置

```
git config --global core.editor subl
git config --global user.name "James Zhan"
git config --global user.email "zhiqiangzhan@gmail.com"
```

配置 Git LFS

```bash
git lfs install

git lfs track "*.csv"
git lfs track "*.zip"
git lfs track "*.tar.gz"
git lfs track "*.dat"
git lfs track "*.mat"

git lfs track

git lfs ls-files
```

#### 配置 GitHub 访问权限

```bash
ssh-keygen -t rsa -b 4096 -C "zhiqiangzhan@gmail.com"
ls -la ~/.ssh

eval "$(ssh-agent -s)"
ssh-add -K ~/.ssh/id_rsa

pbcopy < ~/.ssh/id_rsa.pub
```

添加这个 key 到 `GitHub Settings` / `SSH and GPG keys` / `New SSH key`

```
ssh -T git@github.com
```

#### 配置 ZSH

```bash
git clone https://github.com/jameszhan/oh-my-zsh.git ~/.oh-my-zsh

cd ~/.oh-my-zsh
git remote add upstream https://github.com/robbyrussell/oh-my-zsh.git
git fetch upstream
git checkout master

cp ~/.zshrc ~/.zshrc.orig
cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc
chsh -s /bin/zsh
```

编辑 ~/.zshrc 个性化你的配置

```bash
ZSH_THEME="jameszhan"
plugins=(git svn mvn brew gem go lein npm node rails ruby rvm)
```

## 配置主流开发环境

### 准备 Ruby 开发环境

#### 安装 GPG

```bash
brew info gpg
brew install gpg

gpg --gen-key
gpg --list-secret-keys --keyid-format LONG
# gpg: checking the trustdb
# gpg: marginals needed: 3  completes needed: 1  trust model: pgp
# gpg: depth: 0  valid:   1  signed:   0  trust: 0-, 0q, 0n, 0m, 0f, 1u
# gpg: next trustdb check due at 2021-01-13
# /Users/james/.gnupg/pubring.kbx
# -------------------------------
# sec   rsa2048/AAAAAAAAAAAAAAA 2019-01-14 [SC] [expires: 2021-01-13]
#       AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
# uid                 [ultimate] James Zhan <zhiqiangzhan@gmail.com>
# ssb   rsa2048/AAAAAAAAAAAAAAA 2019-01-14 [E] [expires: 2021-01-13]
git config --global user.signingkey AAAAAAAAAAAAAAA
```

#### 安装 RVM

```bash
# gpg --keyserver hkp://pool.sks-keyservers.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3 7D2BAF1CF37B13E2069D6956105BD0E739499BDB
gpg --keyserver pgp.ocf.berkeley.edu --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3 7D2BAF1CF37B13E2069D6956105BD0E739499BDB
\curl -sSL https://get.rvm.io | sudo bash -s stable

sudo chown -R james:rvm /usr/local/rvm
rvm reload
```

#### 安装 Ruby

```bash
rvm list known
rvm install 2.6

rvm use 2.6 --default

ruby --version

gem sources --add https://gems.ruby-china.com/ --remove https://rubygems.org/
gem sources -l

gem update --verbose
gem install bundler pry jekyll
```

#### 更新 RVM

```bash
rvmsudo rvm get stable
sudo chown -R james:rvm /usr/local/rvm
rvm reload
```

### 准备 Python 开发环境

#### 安装 Anaconda

```bash
wget https://repo.continuum.io/archive/Anaconda3-2018.12-MacOSX-x86_64.sh
bash ./Anaconda3-2018.12-MacOSX-x86_64.sh
```

#### 更新和配置 conda

```bash
conda update -n base conda
conda update -n base anaconda
conda update -n base --all

conda config --set show_channel_urls yes
```

#### 安装不同版本的 Python

```bash
conda create -n py2 python=2
source activate py2
conda list
python -c 'import sys; print sys.version'
source deactivate py2
```

### 准备 Java 开发环境

#### 安装 Java

从 [Oracle 官网](https://www.oracle.com/technetwork/java/javase/downloads/index.html)上下载 JDK 安装包，并安装到本地。

如果有安装多个版本，可以通过如下命令来切换版本。

```bash
# export JAVA_HOME=$(/usr/libexec/java_home -version 1.6)
# export JAVA_HOME=$(/usr/libexec/java_home -version 1.7)
export JAVA_HOME=$(/usr/libexec/java_home -version 1.8)
```

#### 安装 IntelliJ IDEA

可以从 [JetBrains 官网下载](https://www.jetbrains.com/idea/download/#section=mac)下载。

#### 安装 JVM 其他语言

**Kotlin**

```bash
brew install kotlin
```

**Clojure**

Leiningen: Build tool for Clojure
- https://github.com/technomancy/leiningen

```bash
brew install leiningen
```

**Scala**                                                                                                                                                                   
- scala: JVM-based programming language
    - https://www.scala-lang.org/
- typesafe-activator: Tools for working with Lightbend Reactive Platform
    - https://www.lightbend.com/community/core-tools/activator-and-sbt

```bash
brew install scala
brew install typesafe-activator
```

**Groovy**                                                                                                                                                                   
Java-based scripting language
- http://www.groovy-lang.org

```bash
brew install groovy
```

#### Build Tool

**Gradle**

Open-source build automation tool based on the Groovy and Kotlin DSL
- https://www.gradle.org/

```bash
brew install gradle
```

**Maven**

Java-based project management
- https://maven.apache.org/

```bash
brew install maven
```

#### 其他工具集

```bash
brew install zookeeper
brew install elasticsearch
```

## 编程语言相关

### 玩转编程语言

#### llvm

Next-gen compiler infrastructure
- https://llvm.org/

```bash
brew install llvm
```

#### gcc

GNU compiler collection
- https://gcc.gnu.org/

```bash
brew install gcc
```

#### Bison                                                                                                                                                                       
Parser generator, 
Bison is upward compatible with Yacc: all properly-written Yacc grammars ought to work with Bison with no change. 
Anyone familiar with Yacc should be able to use Bison with little trouble. 
You need to be fluent in C or C++ programming in order to use Bison. Java is also supported as an experimental feature.
- https://www.gnu.org/software/bison/

```bash
brew install bison
```

#### yasm

Modular BSD reimplementation of NASM
- https://yasm.tortall.net/

```bash
brew info yasm
brew install yasm
```

#### NASM

Netwide Assembler (NASM) is an 80x86 assembler
- https://www.nasm.us/

```bash
brew info nasm
brew install nasm
```

#### Common Lisp

GNU CLISP, a Common Lisp implementation
- https://clisp.sourceforge.io/

```bash
brew info clisp
brew install clisp
```

#### NewLISP

Lisp-like, general-purpose scripting language
- http://www.newlisp.org/

```bash
brew info newlisp
brew install newlisp
```

#### Scheme

MIT/GNU Scheme development tools and runtime library
- https://www.gnu.org/software/mit-scheme/

```bash
brew info mit-scheme
brew install mit-scheme
```

#### Racket                                                                                                                                               

Modern programming language in the Lisp/Scheme family
- https://racket-lang.org/

```bash
brew info racket
brew info minimal-racket
brew install racket
brew install minimal-racket
```

#### Go 语言

Open source programming language to build simple/reliable/efficient software
- https://golang.org

```bash
brew info go
brew install go
```

#### Prolog                                                                                                                                                                  
Prolog compiler with constraint solving
- http://www.gprolog.org/

```bash
brew info swi-prolog
brew install swi-prolog --with-jpl --with-xpce

brew info gnu-prolog
brew install gun-prolog
```

#### Io 语言

Small prototype-based programming language
- http://iolanguage.com/

```bash
brew info io
brew install io
```

#### Lua

Powerful, lightweight programming language
- https://www.lua.org/

```bash
brew info lua
brew install lua
```

#### Node

- node: Platform built on V8 to build network applications
    - https://nodejs.org/
- yarn: JavaScript package manager
    - https://yarnpkg.com/

```bash
brew install node --enable-debug
brew install yarn
```

#### Smalltalk

```bash
brew info gnu-smalltalk
brew install gnu-smalltalk --tcltk
```

#### Erlang

```bash
brew info erlang
brew install erlang
```

#### R 语言

Software environment for statistical computing
- https://www.r-project.org/

```bash
brew info r
brew install r
```

#### ghostscript

Interpreter for PostScript and PDF
- https://www.ghostscript.com/

```bash
brew info ghostscript
brew install ghostscript
```

### 代码库

#### boost

Collection of portable C++ source libraries
- https://www.boost.org/

#### gobject-introspection

Generate introspection data for GObject libraries
- https://wiki.gnome.org/Projects/GObjectIntrospection

#### gnuplot

Command-driven, interactive function plotting
- http://www.gnuplot.info/

#### protobuf

Protocol buffers (Google's data interchange format)
- https://github.com/protocolbuffers/protobuf/

#### sqlmap

Penetration testing for SQL injection and database servers
- http://sqlmap.org

#### pcre

Perl compatible regular expressions library
- https://www.pcre.org/

#### pcre2

Perl compatible regular expressions library with a new API
- https://www.pcre.org/

#### gmp

GNU multiple precision arithmetic library
- https://gmplib.org/

## 安装系统服务

### 数据库软件

#### PostgreSQL

```bash
brew info postgresql
brew install postgresql
```

#### MySQL

```bash
brew info mysql
brew install mysql
```

#### MongoDB

```bash
brew info mongodb
brew install mongodb
```

#### Redis

```bash
brew info redis
brew install redis
```

#### SQLite

```bash
brew info sqlite
brew install sqlite
```

#### Neo4j

```bash
brew info neo4j
brew install neo4j
```

### 安装系统软件

#### nginx

HTTP(S) server and reverse proxy, and IMAP/POP3 proxy server
- https://nginx.org/

#### passenger
Server for Ruby, Python, and Node.js apps via Apache/NGINX
- https://www.phusionpassenger.com/

#### zeromq

- zeromq: High-performance, asynchronous messaging library
    - http://www.zeromq.org/
- czmq: High-level C binding for ZeroMQ
    - http://czmq.zeromq.org/


## 其他工具

### 玩转机器学习

#### octave

High-level interpreted language for numerical computing
- https://www.gnu.org/software/octave/index.html

#### sundials

Nonlinear and differential/algebraic equations solver
- https://computation.llnl.gov/casc/sundials/main.html

#### open-mpi

High performance message passing library
- https://www.open-mpi.org/

#### opencc

Simplified-traditional Chinese conversion tool
- https://github.com/BYVoid/OpenCC

#### 安装 TensorFlow

```bash
conda create -n tf -y python=3.6
conda install -n tf -c conda-forge tensorflow
source activate tf
conda list
python -c "import tensorflow as tf; print(tf.__version__)"
```

### 经典编辑器

#### Vim

```bash
brew cask install macvim
```

#### Emacs

```bash
brew cask install emacs
```

### 多媒体软件

#### graphviz

`graphviz`是贝尔实验室开发的一个开源的工具包，它使用 特有的 DSL 作为脚本语言，然后使用布局引擎来解析此脚本，并完成自动布局。`graphviz`提供丰富的导出格式。

graphviz中包含了众多的布局器：

- dot - filter for drawing directed graphs（有向图）
- neato - filter for drawing undirected graphs（基于 force-based 算法）
- twopi - filter for radial layouts of graphs（径向布局）
- circo - filter for circular layout of graphs（圆环布局）
- fdp - filter for drawing undirected graphs（无向图）
- sfdp - filter for drawing large undirected graphs
- patchwork - filter for squarified tree maps
- osage - filter for array-based layouts

Graph visualization software from AT&T and Bell Labs
- https://www.graphviz.org/

```bash
brew install graphviz --with-app --with-librsvg
```

#### PlantUML

```bash
brew install plantuml
```

#### ffmpeg

在Windows下，我们有很多视频格式转换的工具，尽管良莠不齐，但是只要有耐心，总是可以达到转换的要求，在OS X下，App Store上也可以找到一些转码工具，但是一般都价格不菲。事实上，绝大部分视频转码工具底层都用到了FFmpeg，而FFmpeg是完全开源和免费的，既然如此，我们为何不直接使用ffmpeg来进行视音频的转码处理呢。

Play, record, convert, and stream audio and video
- https://ffmpeg.org/

```bash
# 查看ffmpeg的安装选项，可以按照你自己的要求选装
brew info ffmpeg

# 安装FFmpeg
brew install ffmpeg --with-fdk-aac --without-faac

#列出支持的编解码器
ffmpeg -codecs

#列出支持的滤镜
ffmpeg -filters
 
#列出支持的格式
ffmpeg -formats
```

> 注：FFmpeg是一个开源免费跨平台的视频和音频流方案，属于自由软件，采用LGPL或GPL许可证（依据你选择的组件）。它提供了录制、转换以及流化音视频的完整解决方案。

#### VLC

OS X 下免费又好用的视频播放器当属 VLC，可以支持几乎所有常用的视频格式。

```bash
brew cask info vlc
brew cask install vlc
```

#### flac

Free lossless audio codec
- https://xiph.org/flac/

#### x265

H.265/HEVC encoder
- http://x265.org

#### x264

H.264/AVC encoder
- https://www.videolan.org/developers/x264.html

#### lame

High quality MPEG Audio Layer III (MP3) encoder
- https://lame.sourceforge.io/


### 虚拟软件

#### QEMU

QEMU是一套由Fabrice Bellard所编写的以GPL许可证分发源码的模拟处理器，在GNU/Linux平台上使用广泛。

Open source IA-32 (x86) PC emulator written in C++
- https://bochs.sourceforge.io/

```bash
brew info qemu
brew install qemu --with-libssh2 --with-sdl --with-vde
```

#### Bochs

Bochs 是一个基于LGPL的开源x86 虚拟机软件（类似于QEMU）。Bochs 的 CPU 指令是完全自己模拟出来的，这种方式的缺点是速度比较慢；优点是具有无以伦比的可移植性：有 gcc 的地方就可以有 Bochs。甚至已经有了跑在 PocketPC 上的 Bochs。

x86 and PowerPC Emulator
- https://www.qemu.org/

```bash
brew info bochs
brew install bochs
```

### 网络工具

#### telnet

User interface to the TELNET protocol (built from macOS Sierra sources)
- https://opensource.apple.com/

#### wireshark

Graphical network analyzer and capture tool
- https://www.wireshark.org

##### nmap
Port scanning utility for large networks
- https://nmap.org/

### 其他工具

#### epstool

Edit preview images and fix bounding boxes in EPS files
- http://www.ghostgum.com.au/software/epstool.htm

#### gnupg

GNU Pretty Good Privacy (PGP) package
- https://gnupg.org/

#### pstree

Show ps output as a tree
- http://www.thp.uni-duisburg.de/pstree/

#### rename

Perl-powered file rename script with many helpful built-ins
- http://plasmasturm.org/code/rename

#### gawk

GNU awk utility
- https://www.gnu.org/software/gawk/

#### tree

Display directories as trees (with optional color/HTML output)
- http://mama.indstate.edu/users/ice/tree/

#### gnu-sed

GNU implementation of the famous stream editor
- https://www.gnu.org/software/sed/

#### gnu-getopt

Command-line option parsing library
- http://frodo.looijaard.name/project/getopt

#### readline

Library for command-line editing
- https://tiswww.case.edu/php/chet/readline/rltop.html

#### re2

Alternative to backtracking PCRE-style regular expression engines
- https://github.com/google/re2

#### imagemagick

Tools and libraries to manipulate images in many formats
- https://www.imagemagick.org/

#### qt

Cross-platform application and UI framework
- https://www.qt.io/

#### memtester

Utility for testing the memory subsystem
- http://pyropus.ca/software/memtester/