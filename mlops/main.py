
from fastapi import FastAPI, File, Form, UploadFile
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import torch
import torchvision.transforms as transforms
import os

# Initialize FastAPI app
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the model paths
MODEL_PATHS = {
    "Finetunex": r"models/model_full.pth",
    "Finetunex2": r"models/model_full2.pth",
    "Hugface1": r"models/model_full3.pth",
}

# Define image preprocessing
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])

@app.post("/predict/")
async def predict(file: UploadFile = File(...), model: str = Form(...)):
    try:
        # Validate the selected model
        model_path = MODEL_PATHS.get(model)
        print(File)
        print(model)
        if not model_path or not os.path.exists(model_path):
            return JSONResponse({"error": f"Model '{model}' not found."}, status_code=400)

        # Load the appropriate model
        device = torch.device("cpu")
        loaded_model = torch.load(model_path, map_location=device)
        loaded_model.eval()

        # Load the uploaded image
        image = Image.open(file.file).convert("RGB")

        # Preprocess the image
        input_tensor = transform(image).unsqueeze(0).to(device)

        # Perform inference
        with torch.no_grad():
            outputs = loaded_model(input_tensor)
            _, predicted_idx = torch.max(outputs, 1)
            predicted_idx = predicted_idx.item()

        # Map index to class label
        labels = {0: "Cat", 1: "Dog"}
        category = labels.get(predicted_idx, "unknown")

        # Confidence score
        confidence = torch.nn.functional.softmax(outputs, dim=1).max().item()

        return JSONResponse({
            "model": model,
            "category": category,
            "confidence": confidence
        })
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)
