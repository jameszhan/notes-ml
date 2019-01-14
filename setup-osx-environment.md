# 打造 OS X 开发环境

版本号 | 修订日期 | 修订概述 | 修订人 | 备注
----- | ------ | ------- | ----- | -----
v0.0.1 | 2019-01-13 | Setup a new Mac | James Zhan |

## 准备工作

### 安装必要软件

#### 安装 Xcode

从 App Store 上搜索 Xcode 并安装到本地。

#### 安装 Java

从 [Oracle 官网](https://www.oracle.com/technetwork/java/javase/downloads/index.html)上下载 JDK 安装包，并安装到本地。

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

试着安装软件

```bash
brew install wget
```

## 通过 Homebrew 安装软件

### 安装 App

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

#### Visual Studio Code

```bash
brew cask info visual-studio-code
brew cask install visual-studio-code
alias vscode="open -b com.microsoft.VSCode"
```

#### Google Chrome

```bash
brew cask info google-chrome
brew cask install google-chrome
```

#### Docker

```bash
brew cask info docker
brew cask install docker
```

#### Sublime Text 3

```bash
brew cask info sublime-text
brew cask install sublime-text
```

#### 搜狗输入法

```bash
brew cask info sogouinput
brew cask install sogouinput
open /usr/local/Caskroom/sogouinput/<VERSION>/sogou_mac_<NUM>.app
```

#### kdiff3

```bash
brew cask info kdiff3
brew cask install kdiff3
```

#### Typora

```bash
brew cask info typora
brew cask install typora
alias typora="open -a typora"
```

#### VLC

```bash
brew cask info vlc
brew cask install vlc
```

### 安装数据库服务

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

### 玩转编程语言

#### Go 语言

```bash
brew info go
brew install go
```

#### Common Lisp

```bash
brew info clisp
brew install clisp
```

#### Scheme

```bash
brew info mit-scheme
brew install mit-scheme
```

#### NewLISP

```bash
brew info newlisp
brew install newlisp
```

#### Lua

```bash
brew info lua
brew install lua
```

#### Smalltalk

```bash
brew info gnu-smalltalk
brew install gnu-smalltalk --tcltk
```

#### Io 语言

```bash
brew info io
brew install io
```

#### Erlang

```bash
brew info erlang
brew install erlang
```

#### Prolog

```bash
brew info swi-prolog
brew install swi-prolog --with-jpl --with-xpce
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

#### 安装 GPG

```bash
brew info gpg
brew install gpg
```

#### 配置 GitHub 访问权限





