# 🍅 macOS Pomodoro Timer

A simple Pomodoro timer that lives in your macOS menu bar.

## Features

- 25-minute focus timer.
- Runs in the menu bar (no Dock icon).
- Start/Pause control.
- System notification when time is up.

## Requirements

- macOS
- Python 3
- `rumps`, `py2app`

## Setup

1.  Install dependencies:
    ```bash
    pip install rumps py2app
    ```
2.  Package the app:
    ```bash
    python setup.py py2app -A
    ```
3.  Find the `.app` file in the `dist/` folder and run it.

## Usage

Click the 🍅 icon in the menu bar and select `Start`.

## License

MIT
