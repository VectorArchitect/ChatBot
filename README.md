# WhatsApp Chat Text Copier

This repository currently contains a small desktop-automation script, not an AI chatbot or an auto-reply system.

## What the script does

Running `main.py` uses PyAutoGUI to:

1. Wait three seconds before interacting with the desktop.
2. Click fixed screen coordinates intended for WhatsApp and its full-screen control.
3. Open a specific chat, select a screen region, and copy the selected text.
4. Print the clipboard contents and the number of copied characters.

The script only copies the selected text. It does not call an AI API, analyze messages, or send replies.

## Requirements

- Python
- A desktop session with WhatsApp open and positioned as expected by the script
- The Python packages listed in `requirements.txt`

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Run

```bash
python main.py
```

The script waits three seconds before the first click. PyAutoGUI's fail-safe is enabled: move the mouse to the top-left corner of the primary screen to abort automation.

## Important limitations and safety

- The click and drag coordinates in `main.py` are hard-coded for one screen layout. Adjust them for your display resolution, scaling, window position, and WhatsApp layout before running.
- The script uses `Ctrl+C`; macOS users may need to change this to `Command+C`.
- Keep the intended WhatsApp chat visible and verify the selected region before relying on the copied output.
- Clipboard contents may include private conversations. Review and handle the output appropriately.
- This is a UI automation experiment, not a robust WhatsApp integration.
