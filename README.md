# AI Study

Hands-on notes and examples while working through the Hugging Face
Transformers course.

## Repository structure
- `huggingface_ch1.py` – quick sentiment-analysis pipeline example that
  downloads a ready-made model and classifies sample sentences.
- `huggingface_ch1_p1.py` – lower-level walkthrough that tokenizes text,
  runs it through a pretrained model, and inspects the outputs.
- `course/en/chapter1/section3.ipynb` – Jupyter notebook companion for
  Chapter 1, Section 3 of the course.

## Getting started
1. Ensure Python 3.9+ is available.
2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install transformers torch --upgrade
   ```
   The first run will download pretrained model weights from Hugging Face
   and cache them locally.

## Usage
- Run the sentiment pipeline sample:
  ```bash
  python huggingface_ch1.py
  ```
- Inspect tokenization and model outputs step by step:
  ```bash
  python huggingface_ch1_p1.py
  ```
- Explore the notebook in Jupyter:
  ```bash
  pip install notebook
  jupyter notebook course/en/chapter1/section3.ipynb
  ```

## Rotating 3D Earth demo
- Start a local server and open the browser-friendly globe:
  ```bash
  python serve_rotating_earth.py
  # then visit http://localhost:8000/rotating_earth_web.html
  ```

## Helpful links
- Hugging Face course: https://huggingface.co/learn
- Transformers docs: https://huggingface.co/docs/transformers
