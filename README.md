# 🏥 Clinical Dosage Recommendation Environment (CDRE)

## 📌 Overview
This project simulates a real-world healthcare task where an AI agent recommends drug dosage based on patient data.

---

## 🎯 Objective
The agent must:
- Analyze patient information
- Recommend correct dosage
- Avoid unsafe decisions

---

## 🧠 Observation Space
- Age
- Weight
- Condition
- Creatinine level
- Allergies
- Current medications

---

## ⚡ Action Space
- Drug name
- Dosage (mg)
- Frequency

---

## 🏆 Reward
- Correct → +1.0  
- Slight error → +0.5  
- Wrong → -1.0  
- Unsafe → penalty  

---

## 🧪 Tasks
- Easy
- Medium
- Hard

---

## ▶️ Run
