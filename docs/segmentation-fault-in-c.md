# Debugging Segmentation Faults (SIGSEGV) in C

Root cause analysis, AddressSanitizer telemetry, and debugging workflows for memory access violations.

- **Canonical Troubleshooting Resource**: [Debugging Segmentation Faults in C](https://onlineccompiler.com/errors/segmentation-fault-in-c)
- **Cloud Sandbox**: [Online C Compiler](https://onlineccompiler.com/)

---

## 1. Common Causes of Segmentation Faults
- **NULL Dereferencing**: Attempting to read or write through a pointer that equals `NULL` (`0x0`).
- **Buffer Overflow**: Writing beyond stack or heap allocation bounds, corrupting frame pointers.
- **Modifying Read-Only Memory**: Writing into string literals residing in the `.rodata` section.
- **Dangling Pointers**: Accessing memory after calling `free()`.

## 2. Diagnostic Flags
Compile with `-g -fsanitize=address` on GCC/Clang to get instant stack trace telemetry.

Full debugging guide: **https://onlineccompiler.com/errors/segmentation-fault-in-c**
