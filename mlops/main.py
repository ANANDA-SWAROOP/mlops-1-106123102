from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import torch
import torchvision.transforms as transforms

# Initialize FastAPI app
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to restrict origins if needed
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)
# Load the custom-trained model
MODEL_PATH = r"C:\Users\anand\OneDrive\Desktop\testing102\model_full.pth"  # Path to your saved model
device = torch.device("cpu")
model = torch.load(MODEL_PATH, map_location=device)
model.eval()  # Set the model to evaluation mode

# Define image preprocessing
transform = transforms.Compose([
    transforms.Resize((224, 224)),  # Resize to match model input size
    transforms.ToTensor(),         # Convert image to PyTorch tensor
    transforms.Normalize(          # Normalize using ImageNet statistics
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    try:
        # Load the uploaded image
        image = Image.open(file.file).convert("RGB")

        # Preprocess the image
        input_tensor = transform(image).unsqueeze(0).to(device)

        # Perform inference
        with torch.no_grad():
            outputs = model(input_tensor)
            _, predicted_idx = torch.max(outputs, 1)
            predicted_idx = predicted_idx.item()

        # Map index to class label
        labels = {0: "cat", 1: "dog"}  # Adjust according to your training labels
        category = labels.get(predicted_idx, "unknown")

        # Confidence score
        confidence = torch.nn.functional.softmax(outputs, dim=1).max().item()

        return JSONResponse({
            "category": category,
            "confidence": confidence
        })
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)
    