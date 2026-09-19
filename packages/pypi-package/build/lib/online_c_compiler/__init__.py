"""
Official Python SDK for onlineccompiler.com
Fast GCC C compilation, debugging, and memory visualization suite.
Website: https://onlineccompiler.com/
"""

import json
import urllib.request
from typing import Dict, Any, Optional

__version__ = "1.0.0"
__author__ = "Mahdi Hatefi"
__homepage__ = "https://onlineccompiler.com/"

API_URL = "https://onlineccompiler.com/api/compile"

def compile_c(code: str, stdin: str = "", optimization: str = "-O2") -> Dict[str, Any]:
    """
    Compile and run C code using the onlineccompiler.com cloud GCC engine.
    
    Args:
        code: C source code string
        stdin: Optional input for stdin
        optimization: GCC optimization flag ('-O0', '-O1', '-O2', '-O3')
        
    Returns:
        Dictionary containing execution result (success, stdout, stderr, executionTime, etc.)
    """
    payload = {
        "code": code,
        "input": stdin,
        "optimization": optimization
    }
    
    headers = {
        "Content-Type": "application/json",
        "Origin": "https://onlineccompiler.com",
        "Referer": "https://onlineccompiler.com/",
        "User-Agent": f"online-c-compiler-python/{__version__} (https://onlineccompiler.com)"
    }
    
    req = urllib.request.Request(
        API_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers=headers,
        method="POST"
    )
    
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.loads(resp.read().decode("utf-8"))

__all__ = ["compile_c", "API_URL", "__version__", "__homepage__"]
