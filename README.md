# Python Development
## [1. Performance optimization](./docs/01_performance_optimization.md)
## [2.OOP](./docs/02_oop.md)
## [3.Network Programming](./docs/03_network_programming.md)
## [4.Linux](./docs/04_linux.md)
## [5.Pandas](./docs/05_pandas.md)
## [6.FastAPI](./docs/06_fastapi.md)
## [7.SQL](./docs/07_sql.md)
## [8.Git](./docs/08_git.md)
## [9.Tailwind CSS](./docs/09_tailwind_css.md)
## Important notice
### 1. Virtual Environment
```bash
# Create virtual environment
python -m venv venv
# Activate virtual environment
source venv/bin/activate
# Install dependencies
pip install -r requirements.txt
# Check dependencies
pip list
# Check the Python interpreter
python --version
which python  # Linux/macOS
where python  # Windows
```
### 2. React
```bash
mkdir web
cd web
```
```bash
# Create a React project (React 19 by default)
npx create-react-app frontend --use-npm --template cra-template
```
```bash
# Go into the frontend directory and uninstall React19, manually install React18
cd frontend
npm uninstall react react-dom
npm install react@18 react-dom@18

# Check Version
npm list react react-dom
# react@18.x.x
# react-dom@18.x.x
```
```bash
# Install web-vitals manually if get an error.
npm install web-vitals
```
```bash
# Start React
npm start
```
```bash
# Compiled successfully!
# You can now view frontend in the browser.
# Local: http://localhost:3000
```
### 3. Checking the shell type
```bash
echo $SHELL
```
If /bin/zsh is returned, using zsh and need to modify ~/.zshrc.

If /bin/bash is returned, using bash and need to modify ~/.bashrc or ~/.bash_profile.
### 4. Modify the Python version path
```bash
nano ~/.bash_profile
```
```bash
export PATH="/usr/local/bin:$PATH"
```
```bash
source ~/.bashrc
```
### 5. Anaconda and Jupyter book
#### 5.1 Check JupyterBook running Python
```python
import sys
print(sys.executable)

# /opt/anaconda3/envs/DataAnalysis/bin/python
```
#### 5.2 Check pip and python
```bash
which pip
which python

# /opt/anaconda3/envs/DataAnalysis/bin/python  ✅
# /opt/anaconda3/envs/DataAnalysis/bin/pip     ✅
```
#### 5.3 Get the Python3 kernel to use DataAnalysis
```bash
conda activate DataAnalysis

jupyter notebook

# Choose Python3 Kernel
```
