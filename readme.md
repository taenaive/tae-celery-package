# Celery Test Play package

This project shows you how to package celery worker and task
 
## python installation

```bash
  python3.11 -m venv .venv
  source .venv/bin/activate

  pip install celery redis ...etc
  #or just
  pip install -r requirements.txt
```

## distribution

```bash
pip install build
# source distribution.
python -m build -s -v
# binary build
python -m build --wheel -v

```