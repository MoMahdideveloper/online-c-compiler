# ⚡ online-c-compiler

> Official CLI tool and Node.js SDK for **[onlineccompiler.com](https://onlineccompiler.com/)** — Fast, in-browser GCC C compiler, debugger, and memory visualization suite.

[![npm version](https://img.shields.io/badge/npm-1.0.0-cb3837.svg?style=for-the-badge&logo=npm)](https://www.npmjs.com/)
[![Web IDE](https://img.shields.io/badge/Online%20IDE-onlineccompiler.com-blue?style=for-the-badge&logo=c)](https://onlineccompiler.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![GCC Version](https://img.shields.io/badge/GCC-14.2%20%7C%20Clang-19.1-green?style=for-the-badge&logo=gnu)](https://onlineccompiler.com/)

Compile, execute, and analyze C programs directly from your terminal or Node.js applications without installing local GCC, Clang, or build tools.

👉 **Launch Online Compiler & Memory Visualizer**: [https://onlineccompiler.com/](https://onlineccompiler.com/)

---

## 🌐 Regional Language Editions

* 🇪🇸 **Español**: [Compilador de C Online](https://onlineccompiler.com/es/)
* 🇧🇷 **Português**: [Compilador C Online](https://onlineccompiler.com/pt/)
* 🇩🇪 **Deutsch**: [Online C Compiler](https://onlineccompiler.com/de/)
* 🇫🇷 **Français**: [Compilateur C en Ligne](https://onlineccompiler.com/fr/)

---

## 🚀 Installation

### Run directly with `npx` (No Install Needed)

```bash
npx online-c-compiler main.c
```

### Install Globally via npm

```bash
npm install -g online-c-compiler
```

---

## 💻 CLI Usage

Once installed, use either `online-c-compiler` or the short alias `occ`:

### 1. Compile a Local C File
```bash
occ main.c
```

### 2. Execute Inline C Code
```bash
occ run -c "#include <stdio.h>\nint main(){ printf(\"Hello, World!\\n\"); return 0; }"
```

### 3. Open the Cloud Web IDE
```bash
occ open
```
*Directly opens [https://onlineccompiler.com/](https://onlineccompiler.com/) in your default browser with live memory inspector, variable tracking, and AST diagnostics.*

---

## 📦 Node.js API

You can also import `online-c-compiler` as a library in your Node.js scripts:

```javascript
const { compileC } = require('online-c-compiler');

async function run() {
  const code = `
    #include <stdio.h>
    int main() {
        int arr[5] = {10, 20, 30, 40, 50};
        for(int i = 0; i < 5; i++) {
            printf("Index %d = %d\\n", i, arr[i]);
        }
        return 0;
    }
  `;

  const result = await compileC(code, {
    optimization: '-O2'
  });

  console.log('Compiler Output:', result.stdout);
  console.log('Execution Time:', result.executionTime, 'ms');
}

run();
```

---

## 🛠️ Key Features of onlineccompiler.com

* **Zero Toolchain Setup**: No need to install MinGW, WSL, or GCC locally.
* **Modern Standards**: Full support for C89, C99, C11, C17, and experimental C23.
* **Memory Visualizer**: Visual representation of stack frames, heap allocations (`malloc`/`free`), and pointer dereferences.
* **Sub-200ms Execution**: Ultra-low latency sandboxed execution powered by high-speed cloud infrastructure.

---

## 🔗 Official Links & Resources

* **Website**: [https://onlineccompiler.com/](https://onlineccompiler.com/)
* **GitHub Suite**: [MoMahdideveloper/online-c-compiler-suite](https://github.com/MoMahdideveloper/online-c-compiler-suite)
* **Memory Visualizer**: [https://onlineccompiler.com/learn/c-memory-architecture](https://onlineccompiler.com/)
* **Issues & Bug Reports**: [GitHub Issues](https://github.com/MoMahdideveloper/online-c-compiler-suite/issues)

---

## 📄 License

MIT License © 2026 Mahdi Hatefi ([onlineccompiler.com](https://onlineccompiler.com/))
