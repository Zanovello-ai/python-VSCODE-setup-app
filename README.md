# Python + VS Code Setup Assistant

A small Streamlit app for guiding Professional Education Course participants through Python, VS Code, Jupyter, and notebook setup.

## Run locally

1. Install Python 3.11 or 3.12.
2. Open a terminal in this folder.
3. Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

4. Install requirements:

```bash
pip install -r requirements.txt
```

5. Start the app:

```bash
streamlit run app.py
```

## Files

- `app.py`: the Streamlit setup assistant
- `requirements.txt`: packages needed to run the app
