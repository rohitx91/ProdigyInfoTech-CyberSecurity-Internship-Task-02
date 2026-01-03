# ProdigyInfoTech-CyberSecurity-Internship-Task-02
Task 02: Image Encryption using Pixel Manipulation 

This project is part of the **Prodigy InfoTech Cyber Security Internship**.  
The task focuses on implementing **image encryption and decryption** using
**pixel-level manipulation** in Python.

---

## 📌 Task Objective
To develop a Python program that encrypts and decrypts images by modifying
their RGB pixel values using a **secret key**.

---

## 🧠 Concept Used
An image consists of pixels, and each pixel has three values:
- Red (R)
- Green (G)
- Blue (B)

During encryption:
- A secret key is added to each RGB value of every pixel.

During decryption:
- The same key is subtracted to retrieve the original image.

This demonstrates a basic concept of **image-based cryptography**.

---

## 🛠️ Technologies Used
- Python 3
- Pillow (PIL) library

---

## ⚙️ Features
- Encrypts any image using pixel manipulation  
- Decrypts the encrypted image using the same key  
- Supports dynamic image file names  
- Handles large key values using modulo operation  
- Simple command-line interface  

---

## ▶️ How to Run the Program

1. Install required library:
```bash
pip install pillow
