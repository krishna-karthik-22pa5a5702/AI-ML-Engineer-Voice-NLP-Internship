# MemoTag: Voice-Based Cognitive Decline Detection

This repository contains a proof-of-concept machine learning pipeline designed to detect early signs of cognitive decline using voice patterns.

---

## 🌐 Overview
Using audio samples and transcriptions, this project extracts linguistic and acoustic features that may correlate with early cognitive impairment. It applies unsupervised learning techniques to identify anomalous speech behaviors.

---

## 🔬 Features Extracted
- **Pauses per sentence**
- **Hesitation markers** (e.g., "um", "uh")
- **Hesitation ratio** (pauses/words)
- **Speech rate** (words per sentence)

---

## 🔧 Getting Started

### Installation
```bash
pip install -r requirements.txt
```

### Folder Structure
```
memotag-cognitive-ml/
├── data/
│   ├── audio_samples/           # Voice recordings (simulated)
│   └── transcriptions/          # Corresponding transcriptions
├── notebooks/
│   └── cognitive_detection.ipynb
├── src/
│   └── risk_score_api.py        # API-style function to score risk
├── visuals/
│   └── feature_trends.png       # Visualized clustering
├── report/
│   └── summary_report.pdf       # Written overview
```

### Running the Notebook
```bash
jupyter notebook notebooks/cognitive_detection.ipynb
```

---

## 🎯 API Risk Score (Example)
The file `src/risk_score_api.py` contains a function:
```python
calculate_risk_score(hesitation_ratio, pauses_per_sentence, speech_rate)
```
This returns a numerical score representing cognitive risk.

---

## 📊 Results
- Anomaly detection highlighted samples with high hesitation + pause frequency
- Visual trends show clustering patterns

---

## 🧠 Future Enhancements
- Use real clinical datasets
- Incorporate acoustic features (MFCCs, pitch jitter)
- Supervised learning with clinician-labeled data
- Real-time voice capture + scoring API

---

**Author:** AI/ML Intern — MemoTag
**Date:** April 2025
