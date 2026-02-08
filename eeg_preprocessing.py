# EEG Motor Imagery Classification for BCI

This repository contains code for classifying motor imagery (hand open/close and wrist rotation) from EEG signals using MNE-Python and CSP.

## Project Overview
- Dataset: MOVING EEG dataset
- Features: CSP + band power (alpha/beta)
- Classifier: SVM / LDA
- Goal: High-accuracy BCI for transradial prosthetic control
- Status: Work in progress – submitted/accepted to MICCAI 2026 (pending confirmation)

## Key Files
- preprocessing.py: Raw EEG loading, filtering, artifact removal
- feature_extraction.ipynb: CSP and band power computation
- classification.py: Model training and evaluation

## Results (so far)
- Cross-validation accuracy: XX% (update after CSP)
- Strong ERD in alpha band during motor imagery

## Technologies
Python, MNE, scikit-learn, NumPy, Matplotlib

## Contact
Nour Aldeen Fahsa  
Email: abdulqadiradla@gmail.com  
LinkedIn: www.linkedin.com/in/abdulqadir-adla-b898033a4
