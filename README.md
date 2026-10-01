# Codeforces Solutions

> 🚀 Automatic Codeforces problem submission to GitHub using Competitive Companion

A Python-based automation tool that listens for Codeforces problem submissions and automatically commits & pushes them to this GitHub repository.

## Features

- Real-time sync from Competitive Companion
- Auto-organized directory structure by contest ID and problem index
- Automatic git commit and push
- Supports Python, C++, Java, JavaScript, and others

## Quick Start

### 1. Install Competitive Companion

- Chrome: https://chrome.google.com/webstore/detail/competitive-companion/
- Firefox: https://addons.mozilla.org/firefox/addon/competitive-companion/
- Edge: https://microsoftedge.microsoft.com/addons/detail/competitive-companion/

### 2. Run the listener

```bash
python3 listen.py
```

### 3. Solve a problem on Codeforces

After you submit or copy a solution, use the Competitive Companion browser extension to send the code to `http://localhost:10042`.

The script automatically saves the file in a folder structure like:

```text
1234/
  A/
    A.py
  B/
    B.cpp
```

and then commits and pushes it to GitHub.

## Notes

- This repo is set up for local automation.
- Keep the Python listener running while solving on Codeforces.
- The files are saved using contest/problem metadata.

## Setup details

See `SETUP.md` for full instructions, troubleshooting, and system startup options.
