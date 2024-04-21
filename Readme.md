# Install Python 3.9 Version

- conda create -n py39 python=3.9
- conda activate py39

# VS Code

- Open command palette Ctrl + Shift + P
- Select python interpreter
- Choose py39

# Local Development

- pip install -r requirements.txt
- uvicorn main:app --reload

# Production

- docker build -t python-app .
- docker run -p 8000:8000 python-app
