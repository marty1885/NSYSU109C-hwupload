# NSYSU109C-hwupload

## 這是什麼
讓你可以快速上傳C語言程式作業的小程式

## 準備使用工具
### 如果你是用Windows
  1. 去下載Python3 : [點此](https://www.python.org/ftp/python/3.5.2/python-3.5.2.exe)
  2. 安裝它

### 如果你用Linux
   * 請先確認自己使用的發行版

#### **你用Ubuntu的話：**
   * ```sudo apt-get install python3```

#### **你用Arch Linux/Manjaro的話**
   * ```sudo pacman -S python3```

#### 你是用Fedora的話
   * ```dnf install python3```

### 如果你用Mac OS X
  1. 去下載Python3 : [點此](https://www.python.org/ftp/python/3.5.2/python-3.5.2-macosx10.6.pkg)
  2. 安裝它

## 使用工具
反正基本上就是開一個CMD(那個黑黑的視窗)，切換到這小程式的所在目錄。
```
cd <Path/to/the/NSYSU109C-hwupload/project/directory>
```
之後輸入
```
python3 ./uploadhw.py <功課名稱> <學號> <檔案位置>
```

像是如此
```
cd /home/marty/Documents/hwupload
python3 ./uploadhw.py HW1 B053040051 ~/文件/homework/hw1.c
```
就會把你的功課上傳上去HW1了~~

## 安裝這隻程式
或是你可以把這隻程式安裝到系統裡面，這樣以後使用就可以直接呼叫。請**以系統管理員權限**開起CMD、切換到這個專案的目錄之後輸入
```
python3 ./install.py
```

如果你用的是Mac OS X或是Linux，你也可以用`sudo`指令來去得系統權限來安裝
```
sudo python3 ./install.py
```

## 開發
歡迎大家來協助發這隻程式，讓它更完整。
有任何意見/建議請發issue到[這專案的GutHub issue](https://github.com/marty1885/NSYSU109C-hwupload/issues)。<br>
也當然歡迎各位把專案給fork出去，然後發pull request給我~<br>
(或是你可以Fork走之後就不回來了)
### 程式碼風格
 * Line Ending
  * LF LF LF(很重要所以說三遍)
 * Tab
  * Hard Tab(不要用Space)

剩下的應該很好理解，請自行閱讀程式碼


## 程式碼授權
當然是GPLv3拉~~~<br>
請見LICSENCE檔案
