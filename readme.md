# Celery Test Play package

This project shows you how to package celery worker and task
 
 ## python installation

 ```bash
  python3.11 -m venv .venv
  pip install celery redis
  ```

## distribution

```bash
pip install build
# source distribution.
python -m build -s -v
# binary build
python -m build --wheel -v
#
```