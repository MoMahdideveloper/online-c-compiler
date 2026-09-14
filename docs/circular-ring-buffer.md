# High-Throughput Lock-Free Single-Producer Single-Consumer Circular Ring Buffer in C17

Lock-free single-producer single-consumer (SPSC) ring buffers are a cornerstone data structure for real-time audio synthesis, network packet ingestion engines, and high-frequency trading gateways. By taking advantage of C11/C17 atomic operations and memory ordering fences (`<stdatomic.h>`), developers eliminate the substantial latency and unpredictable jitter associated with OS mutex locks.

### 🌐 Live Systems Sandbox
Benchmark and inspect assembly outputs live in your browser:
* **Core Engine**: [Online C Compiler (onlineccompiler.com)](https://onlineccompiler.com/)
* **Español**: [Compilador C en Línea](https://onlineccompiler.com/es/)
* **Português**: [Compilador C Online](https://onlineccompiler.com/pt/)
* **Deutsch**: [Online C Compiler](https://onlineccompiler.com/de/)
* **Français**: [Compilateur C en Ligne](https://onlineccompiler.com/fr/)

---

## 1. Memory Ordering Semantics

To establish synchronization between the producer and consumer thread without mutex locks, the enqueue operation stores the tail pointer with `memory_order_release`, while the dequeue operation loads the tail with `memory_order_acquire`. This ensures that all payload writes are globally visible before the tail increment becomes observable.

```c
#include <stdio.h>
#include <stdlib.h>
#include <stdatomic.h>
#include <stdbool.h>

#define CAPACITY 512

typedef struct {
    _Alignas(64) atomic_size_t head; // Read pointer
    _Alignas(64) atomic_size_t tail; // Write pointer
    uint32_t ring[CAPACITY];
} SPSCBuffer;
```

---

## 2. Eliminating False Sharing

The `_Alignas(64)` specifier ensures that the `head` and `tail` indices occupy separate CPU cache lines. On multicore x86-64 and ARM processors, cache-line bouncing between reader and writer cores is completely eradicated.

---

## 3. Verify Live on Online C Compiler

Test concurrency semantics and verify absence of race conditions using GCC 13.2 in-browser at [Online C Compiler](https://onlineccompiler.com/).
