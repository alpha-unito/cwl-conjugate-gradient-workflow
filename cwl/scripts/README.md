# Application

The main application is `cj_toolkit.py`. It supplies the different functions necessary to calculate the conjugate gradient.

Execute the command to get the helper

```bash
python cj_toolkit.py  --help
```

# Requirement
Python>3.8  
numpy==2.0.0

```bash
pip install -r requirements.txt
```

# Monolithic run

The script `monolithic.py` executes the conjugate gradient without the workflow. It uses the same functions that can be called by the `cj_toolkit.py` application.