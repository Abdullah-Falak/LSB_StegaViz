# LSB-StegaViz: Image-in-Image Steganography

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Kali](https://img.shields.io/badge/Kali_Linux-557C94?style=for-the-badge&logo=kali-linux&logoColor=white)
![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white)

**LSB-StegaViz** is an Information Security tool built in Python. It demonstrates the concept of data hiding by mathematically embedding a secret image inside a standard cover image using the **Least Significant Bit (LSB) substitution** method.

**Course:** Information Security  
**Environment:** Kali Linux / Python 3  
**Group Members:** Abdullah Falak, Usman Satti, Mubashir Mazhar, Taha Satti  

---

## 📖 How It Works (The Core Logic)
This tool leverages OpenCV and NumPy to treat digital images as large matrices of 8-bit binary numbers. 
* It takes the top 4 **Most Significant Bits (MSBs)** of a secret image (the important visual data).
* It hides them inside the bottom 4 **Least Significant Bits (LSBs)** of a cover image (the minor color details).
* The resulting Stego-Image looks exactly like the original cover image to the human eye, but mathematically contains a completely hidden second image.

---

## 📂 Project Structure
To maintain a clean MVC architecture, the project is divided into two main files:
```text
├── stego_logic.py        # The backend core logic handling OpenCV bitwise math
├── stega_gui.py          # The frontend Tkinter Graphical User Interface
└── README.md             # Project documentation

```
## ⚙️ Prerequisites
This project requires Python 3 and the following external libraries: opencv-python, numpy, and pillow.
If you are running this on Kali Linux or Ubuntu, install the dependencies via the terminal:
```bash
sudo apt update
sudo apt install python3-opencv python3-numpy python3-pil python3-tk -y

```
## 🚀 How to Run the Tool
**1. Clone the Repository**
```bash
git clone [https://github.com/yourusername/lsb-stegaviz.git](https://github.com/yourusername/lsb-stegaviz.git)
cd lsb-stegaviz

```
**2. Launch the Application**
Because the GUI imports the logic automatically, you only need to run the interface file:
```bash
python3 stega_gui.py

```
**3. Usage Instructions**
 * **To Hide:** Click the "Hide Data" button, select your Cover Image and Secret Image, and save the output. *(Note: Always save outputs as .png or .bmp to prevent compression from destroying the hidden bits).*
 * **To Extract:** Click the "Extract Data" button, select your Stego-Image, and save the extracted hidden file.
```

```
