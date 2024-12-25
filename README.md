# MLOps-1 by R. Ananda Swaroop

**Department:** CSE-B  
**Roll No:** 106123102

---

## Task 1: MLOps Databyte

### Description:
Welcome to the Cat-Dog Classifier Project!  
The site is live at: [Cat-Dog Classifier](https://ananda-swaroop.github.io/cat-dog/)  
Please check it out!

---

## Features
1. **Multi-Model ML Prediction**: Identifies whether the input is a Cat (🙀) or Dog (🐶) using models:
   - finetunex
   - finetunex2
   - Hugface1
2. **Drag and Drop Feature**: Direct image browsing support.
3. **Live Camera Image Capturing**: Capture images directly from your camera.
4. **Fast Response**: Under 15 seconds powered by FastAPI backend (Uvicorn server).

---

## CNN-Based Cat-Dog Image Classifier

### Instructions to Run the Model Locally:

1. **Clone the Repository**:
   Clone this repository into your favorite text editor.

2. **Verify Model Files**:
   Ensure the following model files are available in your `backend` folder:
   - `model_full.pth`
   - `model_full2.pth`
   - `model_full3.pth`

   If these files are missing, download them from this [Google Drive Link](https://drive.google.com/drive/folders/1V-9RSp-hMDXC-vZeqdUIT2oiM9ji32gj?usp=drive_link).  
   The dataset used to train and test the models is also available in the same drive.

3. **Setup Tailwind Configuration**:
   Create an empty `tailwind.config.js` file in the root directory to enable Tailwind IntelliSense.

4. **Frontend Preview**:
   Use website viewers like Live Server to preview the frontend.

5. **Check Model Paths**:
   Before starting the server, ensure the `MODEL_PATHS` in the backend point to the correct locations of the downloaded models (if using the Google Drive link).

### Requirements
To run this project, you need the following dependencies:

- Python 3.8+
- FastAPI
- Uvicorn
- Pillow
- PyTorch
- Torchvision
- python-multipart

Dependencies are listed in the `requirements.txt` file.

### Setting Up:

1. **Create a Virtual Environment (if needed):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On non-Windows machines
   ```
   On Windows:
   ```bash
   venv\Scripts\activate
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r backend/requirements.txt
   ```

3. **Start the Application:**
   ```bash
   uvicorn backend.main:app --reload
   ```

4. **Access the Application:**
   Visit [http://127.0.0.1:8000](http://127.0.0.1:8000).

### Note:
- If running locally, ensure that the frontend (e.g., line no. 241 in the code) correctly points to your FastAPI backend.
- Update the backend hosted API endpoint to:
  ```
  http://127.0.0.1:8000/predict/
  ```
  This should match the local backend server address.

---

Enjoy using the Cat-Dog Classifier! 🐾

