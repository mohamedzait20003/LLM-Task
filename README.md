# LLM Chat Generator

This script generates chat-like responses from a young man's perspective on various topics using Meta's Llama 3.1 8B model.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the script:
```bash
python main.py
```

3. Enter a topic when prompted (e.g., "soccer", "gambling", "AI")

## Features

- Generates 10-40 word casual responses
- Uses Llama 3.1 8B Instruct model (quantized Q4_K_M)
- Models are automatically downloaded to the `models/` directory
- GPU acceleration enabled (if available)

## Note

The first run will download the model (~5GB) to the `models/` directory. Subsequent runs will use the cached model.
