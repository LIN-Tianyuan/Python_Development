# Python Development
## [1. Performance optimization](./docs/01_performance_optimization.md)
## [2.OOP](./docs/02_oop.md)
## [3.Network Programming](./docs/03_network_programming.md)
## [4.Linux](./docs/04_linux.md)
## [5.Pandas](./docs/05_pandas.md)
## [6.FastAPI](./docs/06_fastapi.md)
## [7.SQL](./docs/07_sql.md)

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