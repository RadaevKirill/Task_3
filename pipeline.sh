#!/bin/bash
VENV_DIR="venv"

if [ ! -d "$VENV_DIR" ]; then
    python3 -m venv "$VENV_DIR"
    source "$VENV_DIR/bin/activate"
    py -m pip install -r requirements.txt
else
    source "$VENV_DIR/bin/activate"
fi

py data_creation.py
py model_preprocessing.py
py model_preparation.py
py model_testing.py
