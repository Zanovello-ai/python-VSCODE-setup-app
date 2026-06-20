import streamlit as st

st.set_page_config(page_title="Python + VS Code Setup Assistant", page_icon="🐍", layout="wide")

st.title("Python + VS Code Setup Assistant")
st.caption("Professional Education Course setup checklist for running a Jupyter Notebook in VS Code")

st.info("Follow the sections in order. Tick each box when completed. Copy the commands for your operating system.")

repo_url = st.text_input("Course GitHub repository URL", value="https://github.com/mit-fredfactory/FrED-PAL-Kit.git")

with st.sidebar:
    st.header("Progress")
    st.write("Use the checklist below to track completion.")
    st.markdown("---")
    st.link_button("Python downloads", "https://www.python.org/downloads/")
    st.link_button("VS Code downloads", "https://code.visualstudio.com/")
    st.link_button("Python VS Code extension", "https://marketplace.visualstudio.com/items?itemName=ms-python.python")
    st.link_button("Jupyter VS Code extension", "https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter")

sections = [
    "Install Python",
    "Install VS Code",
    "Install VS Code extensions",
    "Download course material",
    "Open project in VS Code",
    "Create virtual environment",
    "Install packages",
    "Select kernel",
    "Run test cell",
]

completed = []
for item in sections:
    completed.append(st.sidebar.checkbox(item, key=f"progress_{item}"))

progress = sum(completed) / len(completed)
st.sidebar.progress(progress)
st.sidebar.write(f"{sum(completed)} / {len(completed)} completed")

st.header("1. Install Python")
st.markdown("Download Python from the official website. Python 3.11 or 3.12 is recommended for most teaching notebooks.")
st.link_button("Download Python", "https://www.python.org/downloads/")
st.warning("Windows users: during installation, tick 'Add Python to PATH'.")

os_choice = st.radio("Choose your operating system", ["Windows", "macOS", "Linux"], horizontal=True)

if os_choice == "Windows":
    st.code("python --version\npip --version", language="bash")
    st.markdown("If `python` does not work, try:")
    st.code("py --version", language="bash")
elif os_choice == "macOS":
    st.code("python3 --version\npip3 --version", language="bash")
else:
    st.code("python3 --version\npip3 --version", language="bash")
    st.markdown("Ubuntu/Debian installation command:")
    st.code("sudo apt update\nsudo apt install python3 python3-pip python3-venv", language="bash")

st.header("2. Install Visual Studio Code")
st.markdown("Download and install Visual Studio Code using the default options.")
st.link_button("Download VS Code", "https://code.visualstudio.com/")

st.header("3. Install VS Code extensions")
st.markdown("Open VS Code, go to Extensions, and install these Microsoft extensions:")
st.markdown("- Python\n- Jupyter")
col1, col2 = st.columns(2)
with col1:
    st.link_button("Python extension", "https://marketplace.visualstudio.com/items?itemName=ms-python.python")
with col2:
    st.link_button("Jupyter extension", "https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter")

st.header("4. Download the course material")
st.markdown("Recommended option: download the GitHub repository as a ZIP file using Code -> Download ZIP.")
st.markdown("Advanced option: clone with Git.")
st.code(f"git clone {repo_url}\ncd <repository-folder>\ncode .", language="bash")

st.header("5. Open the project in VS Code")
st.markdown("In VS Code, select File -> Open Folder and choose the extracted repository folder. Then open the `.ipynb` notebook.")

st.header("6. Create and activate a virtual environment")
if os_choice == "Windows":
    st.code("python -m venv .venv\n.venv\\Scripts\\activate", language="bash")
elif os_choice == "macOS":
    st.code("python3 -m venv .venv\nsource .venv/bin/activate", language="bash")
else:
    st.code("python3 -m venv .venv\nsource .venv/bin/activate", language="bash")
st.markdown("When activated, the terminal prompt usually starts with `(.venv)`.")

st.header("7. Install required packages")
st.markdown("If the repository contains a `requirements.txt` file:")
st.code("pip install -r requirements.txt", language="bash")
st.markdown("Otherwise install the basic Jupyter support packages:")
st.code("pip install notebook jupyter ipykernel", language="bash")

st.header("8. Select the notebook kernel")
st.markdown("Open the notebook and select: Select Kernel -> Python Environments -> `.venv`.")

st.header("9. Test the setup")
st.markdown("Run this in a notebook cell:")
st.code('print("Setup completed successfully!")', language="python")

st.header("Troubleshooting")
with st.expander("Python command not found"):
    st.markdown("On Windows, try:")
    st.code("py --version\npy -m pip install notebook jupyter ipykernel", language="bash")
    st.markdown("If this works, Python is installed but the `python` command is not available in PATH.")

with st.expander("Cannot activate virtual environment on Windows"):
    st.markdown("Try using Command Prompt instead of PowerShell. If PowerShell blocks activation, run:")
    st.code("Set-ExecutionPolicy -Scope CurrentUser RemoteSigned", language="powershell")

with st.expander("VS Code does not detect Python"):
    st.markdown("Press Ctrl+Shift+P, search for 'Python: Select Interpreter', and select `.venv`.")

with st.expander("Notebook kernel missing"):
    st.code("pip install ipykernel jupyter", language="bash")
    st.markdown("Then restart VS Code and select the kernel again.")

st.header("Instructor backup checklist")
st.markdown("""
Prepare these files on a USB stick or shared drive:

- Python installer for Windows and macOS
- VS Code installer for Windows and macOS
- Repository ZIP file
- `requirements.txt`
- PDF or printed copy of the setup manual
""")

st.success("Setup complete when all checklist items are ticked and the test cell runs successfully.")
