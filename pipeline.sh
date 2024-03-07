#!/bin/bash
VENV_DIR="venv"

if [ ! -d "$VENV_DIR" ]; then
    python3 -m venv "$VENV_DIR"
    source "$VENV_DIR/bin/activate"
    pip install -r requirements.txt
else
    source "$VENV_DIR/bin/activate"
fi

python3 data_creation.py
python3 model_preprocessing.py
python3 model_preparation.py
python3 model_testing.py
