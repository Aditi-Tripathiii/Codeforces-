# Codeforces Auto-Push Setup Guide

This project listens for Codeforces submissions through the Competitive Companion browser extension and automatically commits + pushes the accepted code to this GitHub repository.

## Requirements

- Python 3.8+
- Git installed and configured
- Competitive Companion extension installed in Chrome/Firefox/Edge
- GitHub repo access configured locally

## Install Competitive Companion

- Chrome: https://chrome.google.com/webstore/detail/competitive-companion/
- Firefox: https://addons.mozilla.org/firefox/addon/competitive-companion/
- Edge: https://microsoftedge.microsoft.com/addons/detail/competitive-companion/

## Run the listener

```bash
python3 listen.py
```

The script listens on `http://localhost:10042`.

## How it works

1. Solve a problem on Codeforces.
2. Use the Competitive Companion extension.
3. It sends the code to the local listener.
4. The script saves the file into a contest/problem folder.
5. Git automatically adds, commits, and pushes the file.

## Example folder structure

```text
1234/
  A/
    A.py
  B/
    B.cpp
```

## Troubleshooting

- Make sure `listen.py` keeps running.
- Confirm `git remote -v` points to your GitHub repo.
- Run `git status` to see uncommitted files.
- If push fails, set your GitHub credentials or SSH key.

## Optional background run

```bash
nohup python3 listen.py > codeforces.log 2>&1 &
```
