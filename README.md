# tt

`tt` is a Linux daily schedule manager with Pomodoro reminders, desktop
notifications, and status bar output.

This branch contains the Linux version. The old macOS menu bar Pomodoro app is
preserved on the `macos` branch.

## Features

- Shows the current schedule block and remaining time.
- Runs a background daemon for block transition reminders.
- Starts Pomodoro cycles automatically during deep work blocks.
- Sends desktop notifications through `notify-send`.
- Provides one-line and JSON output for Waybar, Polybar, and similar bars.
- Can install itself as a systemd user service.

## Schedule

See [timetable.md](./timetable.md) for the current daily schedule.

Deep work blocks currently use 25-minute focus sessions and 5-minute breaks.

## Requirements

- Linux
- Python 3.10+
- `uv` for development checks
- Optional: `notify-send`, `systemctl --user`, `pw-play`/`paplay`/`aplay`

## Install

Clone the repository and put `tt` somewhere on your `PATH`:

```bash
chmod +x tt
mkdir -p ~/.local/bin
ln -sf "$PWD/tt" ~/.local/bin/tt
```

Start the daemon manually:

```bash
tt start
```

Or install it as a systemd user service:

```bash
tt install
```

## Usage

```bash
tt             # current schedule and Pomodoro status
tt start       # start background daemon
tt stop        # stop background daemon
tt restart     # restart daemon
tt watch       # live terminal view
tt pom         # one-line Pomodoro status
tt bar         # JSON status for Waybar custom modules
tt log [N]     # show recent daemon logs
tt help        # show command help
```

Data is stored in `~/.local/share/tt/`.

## Waybar Example

```json
{
  "custom/tt": {
    "exec": "tt bar",
    "return-type": "json",
    "interval": 30
  }
}
```

## Development

Run the syntax check with `uv`:

```bash
env UV_CACHE_DIR=/tmp/uv-cache uv run python -m py_compile tt
```

## License

MIT
