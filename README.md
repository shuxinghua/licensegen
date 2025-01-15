# C++

## 一、概述

C++ 是一种静态类型的、编译式的、通用的、大小写敏感的、不规则的编程语言，支持过程化编程、面向对象编程和泛型编程。它是 C 的一个超集，事实上，任何合法的 C 程序都是合法的 C++ 程序。

该模板包含了一个简单的C++程序，内置了的 `g++` 编译器 、`gdb` 调试工具以及`.clang-tidy` 代码检查工具。

## 二、快速开始

使用如下编译命令，快速运行一个简单的 C++ 程序：

```
g++ main.cpp -o main && ./main
```

- **`g++ main.cpp -o main`**：
  - `g++` 是 GNU 编译器集合（GCC）中的 C++ 编译器，用于将 C++ 源代码文件编译成可执行文件。
  - `main.cpp` 待编译的 C++ 源文件的文件名。
  - `-o main` 用来指定输出文件的名称，不指定名称默认生成 a.out。
- **`&&./main`**：
  - `&&` 逻辑与运算符，它让前后两条命令产生关联。
  - `./main` 执行编译后的可执行文件。 

**关于构建工具**

本环境默认安装了 GNU 编译器集合（GCC），可以满足基础的 C++ 代码编译需求。但如果您想要使用其他的构建工具，例如 CMake，由于它并未预装，您需要额外自行安装。

### 三.  文件结构

```
clang-quickstart/
├── .vscode 
│   ├── launch.json   // gdb 配置文件
│   ├── preview.yml   // Cloud Studio 配置文件（运行、预览等）
│   ├── setting.json  // vscode 配置文件（外观，代码编辑等）
│   └── tasks.json    // 在vscode 中用来定义和配置任务的
├── main.cpp          // 主源文件
├── .clang-tidy       // Clang-Tidy 代码检查工具的配置文件
├── README.md         // 项目说明文档
├── img               // 图片目录
    └── ...                
```

### 2.  C++官方文档与资源

[https://gcc.gnu.org/](https://gcc.gnu.org/)

[cplusplus]([https://www.cplusplus.com/](https://www.cplusplus.com/))

[C++ 教程 | 菜鸟教程](https://www.runoob.com/cplusplus/cpp-tutorial.html)

[clang-tidy 文档](https://clang.llvm.org/extra/clang-tidy/)

## 三、  常见问题

[Cloud Studio（云端 IDE） | Cloud Studio](https://ide.cloud.tencent.com/docs/)

[Cloud Studio 帮助文档](https://docs.qq.com/aio/DRUFZcHVvZlJuY3l2?p=1QOiTiIR9g0KMJneBDyfgM)

[Cloud Studio（云端 IDE） 常见问题-文档中心-腾讯云](https://cloud.tencent.com/document/product/1039/33505)

## 帮助和支持

##### 欢迎加入Cloud Studio用户反馈群

当您遇到问题需要处理时，您可以直接通过到扫码进入Cloud Studio用户群进行提问.

- 腾讯云工程师实时群内答疑

- 扫码入群可先享受产品上新功能

- 更多精彩活动群内优享

<img title="" src="img/qr-code.png" alt="qr-code.png" width="270">
