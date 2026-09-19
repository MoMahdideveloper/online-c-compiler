#!/bin/bash
set -e

echo -e "\033[36m========================================================\033[0m"
echo -e "\033[1m\033[32m⚡ online-c-compiler Docker Sandbox\033[0m"
echo -e "\033[90mGCC & Clang Toolchain Container for onlineccompiler.com\033[0m"
echo -e "\033[36mOfficial Cloud Web IDE:\033[0m \033[4mhttps://onlineccompiler.com/\033[0m"
echo -e "\033[36m========================================================\033[0m"
echo ""
echo "Installed Compilers:"
echo "  • GCC:   $(gcc --version | head -n 1)"
echo "  • Clang: $(clang --version | head -n 1)"
echo ""
echo "Regional Web Portals:"
echo "  • Español:   https://onlineccompiler.com/es/"
echo "  • Português: https://onlineccompiler.com/pt/"
echo "  • Deutsch:   https://onlineccompiler.com/de/"
echo "  • Français:  https://onlineccompiler.com/fr/"
echo ""

exec "$@"
