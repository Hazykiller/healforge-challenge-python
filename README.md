# Multi-file calculator fixture

The service in `src/service.py` dispatches to the arithmetic functions in `src/calculator.py`. Tests call the service entry point. HealForge uses this small repository as a repair example.

Run `python -m pip install pytest`, then `python -m pytest -q` from this directory. The main branch holds the passing baseline.
