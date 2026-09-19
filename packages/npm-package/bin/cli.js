#!/usr/bin/env node

const fs = require('fs');
const path = require('path');
const { exec } = require('child_process');
const { compileC, WEBSITE_URL } = require('../index');

const args = process.argv.slice(2);

function printBanner() {
  console.log('\x1b[36m========================================================\x1b[0m');
  console.log('\x1b[1m\x1b[32m⚡ online-c-compiler CLI (onlineccompiler.com)\x1b[0m');
  console.log('\x1b[90mCloud GCC 13.2 C Compiler & Memory Diagnostics Suite\x1b[0m');
  console.log('\x1b[36mWeb IDE:\x1b[0m \x1b[4mhttps://onlineccompiler.com/\x1b[0m');
  console.log('\x1b[36m========================================================\x1b[0m\n');
}

function printHelp() {
  printBanner();
  console.log('Usage:');
  console.log('  occ <file.c>              Compile and execute a local C file');
  console.log('  occ run -c "<code>"       Execute inline C code string');
  console.log('  occ open                  Open the online compiler in your browser');
  console.log('  occ --help                Show this help information\n');
  console.log('Website: https://onlineccompiler.com/');
  console.log('International Portals:');
  console.log('  Español:    https://onlineccompiler.com/es/');
  console.log('  Português:  https://onlineccompiler.com/pt/');
  console.log('  Deutsch:    https://onlineccompiler.com/de/');
  console.log('  Français:   https://onlineccompiler.com/fr/\n');
}

async function main() {
  if (args.length === 0 || args.includes('--help') || args.includes('-h')) {
    printHelp();
    process.exit(0);
  }

  if (args.includes('open')) {
    printBanner();
    console.log('🌐 Opening https://onlineccompiler.com/ in your default browser...');
    const startCmd = process.platform === 'win32' ? 'start' : process.platform === 'darwin' ? 'open' : 'xdg-open';
    exec(`${startCmd} ${WEBSITE_URL}`);
    process.exit(0);
  }

  let code = '';
  const inlineIdx = args.indexOf('-c');
  if (inlineIdx !== -1 && args[inlineIdx + 1]) {
    code = args[inlineIdx + 1];
  } else {
    const filePath = path.resolve(process.cwd(), args[0]);
    if (!fs.existsSync(filePath)) {
      console.error(`\x1b[31mError: File not found: ${filePath}\x1b[0m`);
      process.exit(1);
    }
    code = fs.readFileSync(filePath, 'utf-8');
  }

  printBanner();
  console.log(`🚀 Compiling via GCC cloud engine on onlineccompiler.com...`);
  const startTime = Date.now();

  try {
    const result = await compileC(code);
    const duration = Date.now() - startTime;

    if (result.success) {
      console.log(`\x1b[32m✔ Execution Succeeded (${duration}ms | Engine: ${result.engine || 'GCC'})\x1b[0m\n`);
      console.log('--- Standard Output ---');
      console.log(result.stdout || '(no output)');
      if (result.stderr) {
        console.log('\n--- Compiler Diagnostics / Warnings ---');
        console.log(`\x1b[33m${result.stderr}\x1b[0m`);
      }
    } else {
      console.log(`\x1b[31m✖ Compilation/Execution Failed\x1b[0m\n`);
      if (result.stderr) {
        console.log('--- Compiler Errors ---');
        console.log(`\x1b[31m${result.stderr}\x1b[0m`);
      }
      if (result.stdout) {
        console.log('--- Output ---');
        console.log(result.stdout);
      }
    }
    console.log('\n\x1b[90mInspect memory visuals & AST at: https://onlineccompiler.com/\x1b[0m');
  } catch (err) {
    console.error(`\x1b[31mNetwork/API Error: ${err.message}\x1b[0m`);
    process.exit(1);
  }
}

main();
