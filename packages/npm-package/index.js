/**
 * Official Node.js SDK for onlineccompiler.com
 * https://onlineccompiler.com/
 */

const https = require('https');

const COMPILER_API_URL = 'https://onlineccompiler.com/api/compile';

/**
 * Compile and run C code using the onlineccompiler.com cloud GCC engine.
 * @param {string} code - C source code
 * @param {Object} [options]
 * @param {string} [options.input=''] - Standard input (stdin)
 * @param {string} [options.optimization='-O2'] - Optimization flag (-O0, -O1, -O2, -O3)
 * @returns {Promise<Object>} Execution result object
 */
function compileC(code, options = {}) {
  return new Promise((resolve, reject) => {
    const payload = JSON.stringify({
      code: code,
      input: options.input || '',
      optimization: options.optimization || '-O2'
    });

    const url = new URL(COMPILER_API_URL);
    const reqOptions = {
      hostname: url.hostname,
      port: 443,
      path: url.pathname,
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Content-Length': Buffer.byteLength(payload),
        'Origin': 'https://onlineccompiler.com',
        'Referer': 'https://onlineccompiler.com/',
        'User-Agent': 'online-c-compiler-cli/1.0.0 (https://onlineccompiler.com)'
      }
    };

    const req = https.request(reqOptions, (res) => {
      let data = '';
      res.on('data', (chunk) => { data += chunk; });
      res.on('end', () => {
        try {
          const parsed = JSON.parse(data);
          resolve(parsed);
        } catch (e) {
          reject(new Error(`Failed to parse response from onlineccompiler.com: ${data}`));
        }
      });
    });

    req.on('error', (err) => {
      reject(err);
    });

    req.write(payload);
    req.end();
  });
}

module.exports = {
  compileC,
  WEBSITE_URL: 'https://onlineccompiler.com/',
  REGIONAL_PORTALS: {
    es: 'https://onlineccompiler.com/es/',
    pt: 'https://onlineccompiler.com/pt/',
    de: 'https://onlineccompiler.com/de/',
    fr: 'https://onlineccompiler.com/fr/'
  }
};
