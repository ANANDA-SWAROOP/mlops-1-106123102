# mlops-1 by R.Ananda Swaroop
Dept:CSE-B
Rollno:106123102
task1 mlops databyte



# description:
welcome to the cat dog classifier project
the site is live at https://ananda-swaroop.github.io/cat-dog/
pls check it out

# Features
1.Multi model ML prediction( Cat 🙀 or Dog 🐶 ) - {finetunex,finetunex2,Hugface1}
2.Drag and drop feature, direct image browsing
3.live camera image capturing
4.under 15sec responce powered by fastapi backend (uvicorn server)

# CNN based Cat-dog-Image Classifier
Please follow the give instructions to run the model locally:

1.clone the repo into your favorite text editor
2. verify if the models(model_full.pth,model_full2.pth,model_full3.pth) are cloned in your backend folder
if the models are not cloned pls go ahead and download them from https://drive.google.com/drive/folders/1V-9RSp-hMDXC-vZeqdUIT2oiM9ji32gj?usp=drive_link
this drive link also has the dataset which was used to train the models and testing
  
3.once created pls create an empty tailwind.config.js file to use tailwind intellisense

4.use website viewers like live server to preview the frontend

5.before starting the server pls ensure if the MODEL_PATHS are correctly pointing to the downloaded location (if downloading via google drive)

Requirements
To run this project, you need the following dependencies:

Python 3.8+
FastAPI
Uvicorn
Pillow
PyTorch
Torchvision
python-multipart
These dependencies are listed in the requirements.txt file.

6.Create a virtual environment(if needed):

python -m venv venv
source venv/bin/activate (on non-windows machines)

On Windows: venv\Scripts\activate

Install dependencies:

pip install -r backend/requirements.txt


Start the application:
uvicorn backend.main:app --reload
Access the application at http://127.0.0.1:8000.

note:if running locally ensure that the frontend (line no 241) correctly points to your fastapi backend
i.e 
change the backend hosted api endpoint to http://127.0.0.1:8000/predict/ (which is running locally on your machine)



