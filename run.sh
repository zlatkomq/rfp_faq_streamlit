#!/bin/bash

# Activate virtual environment if it exists
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Set environment variables
export STREAMLIT_SERVER_ADDRESS=127.0.0.1
export STREAMLIT_SERVER_PORT=8501
export STREAMLIT_BROWSER_GATHER_USAGE_STATS=false
export STREAMLIT_THEME_BASE="light"

# Run the app
streamlit run app.py --server.fileWatcherType none 