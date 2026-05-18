# Fake News Detection using RoBERTa and FastAI

## Overview
This project is a deep learning based fake news detection system developed for the MH20 Hackathon. The system uses transformer-based NLP models such as RoBERTa along with FastAI to classify news statements into multiple truthfulness categories.

The project focuses on improving classification accuracy using transfer learning, transformer fine-tuning, and ensemble blending techniques.

---

## Problem Statement
Fake news and misleading information spread rapidly on digital platforms. Manual verification is difficult and time-consuming. This project aims to automate fake news classification using Natural Language Processing (NLP) and transformer models.

---

## Technologies Used
- Python
- PyTorch
- FastAI
- HuggingFace Transformers
- RoBERTa
- NumPy
- Pandas
- Scikit-learn

---

## Models Used
The project experiments with multiple transformer architectures:

- RoBERTa-base
- FastAI Transformer Pipeline
- Ensemble Blending Models

Final predictions are generated using blended outputs from multiple trained models.

---

## Dataset
Dataset used:
MH20 Fake News Dataset

Dataset contains:
- News text
- Text tags/categories
- Multi-class labels

- 🔗 Live Demo: https://j9esrjoeo4uurjdy5jsc9f.streamlit.app/

- 

---

## Project Structure

```text
FakeNews-Hackathon-Project/

├── mh20-basline-v1.ipynb
├── mh20-fastai-v1.ipynb
├── mh20-fastai-v2.ipynb
├── Blend_v1f.ipynb
├── Blend_v4d.ipynb
├── README.md
├── requirements.tx


