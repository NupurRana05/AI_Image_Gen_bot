# AI_Image_Gen_bot
 
# 🎨 AI Image Generation Bot

An AI-powered image generation application built using **Stable Diffusion, PyTorch, FastAPI, and Streamlit**. Users can enter text prompts and generate AI images through an interactive chat-style interface.

## ✨ Features

* 🖼️ Generate images from text prompts.
 
* ✍️ Use positive prompts and negative prompts to guide image generation.
 
* 🤖 Generate images using the Stable Diffusion XL (SDXL) model.
 
* ⚡ Use GPU acceleration through Google Colab.
 
* 🔗 Connect the frontend and AI model using FastAPI.
 
* 🌐 Expose the API using ngrok.
 
* 💬 Interactive chat-style interface built with Streamlit.
  
* 📥 Download generated images.
  

## 🛠️ Technologies Used

* Python
  
* Stable Diffusion XL (SDXL)
  
* PyTorch
  
* Hugging Face Diffusers
  
* FastAPI
  
* Streamlit
  
* Google Colab
  
* ngrok
  
* Matplotlib
  
* Pillow
  
* Requests
  

## 🏗️ Project Architecture

```text
User Prompt
    ↓
Streamlit Frontend
    ↓
FastAPI Backend
    ↓
ngrok Public API
    ↓
Google Colab GPU
    ↓
Stable Diffusion XL
    ↓
Generated Image
```

## ⚙️ How It Works

1. The user enters a text prompt in the Streamlit application.
   
3. The application sends the prompt and generation settings to the FastAPI endpoint.
   
5. The API forwards the request to the Stable Diffusion XL pipeline running in Google Colab.
   
7. PyTorch performs model inference using GPU acceleration.
   
9. The generated image is returned to Streamlit and displayed to the user.
    
11. The user can download the generated image.


## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd AI_Image_Gen_bot
```

### 2. Create and activate a virtual environment

```bash
py -3.11 -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install streamlit requests pillow
```

### 4. Configure the API URL

Update the `COLAB_API` variable in `app.py` with your currently active FastAPI/ngrok URL.

### 5. Run the Streamlit application

```bash
streamlit run app.py
```

Open the local URL displayed in the terminal.

## 📌 Important Notes

* The Stable Diffusion model runs in Google Colab; it is not loaded directly by the Streamlit frontend.
  
* The Colab runtime and FastAPI/ngrok tunnel must be active for image generation to work.
  
* The ngrok URL may change when the tunnel restarts.
  
* GPU availability and inference speed depend on the Colab runtime.
  
* Never commit API authentication tokens, passwords, or other secrets to GitHub.
  

## 🎯 Learning Outcomes

* Understanding the Stable Diffusion image-generation workflow.
  
* Working with pretrained models and the DiffusionPipeline.
  
* Learning PyTorch tensors, model data types, and GPU inference.
  
* Testing prompts and negative prompts.
  
* Building REST APIs with FastAPI.
  
* Connecting a frontend to an AI backend.
  
* Visualizing generated images with Matplotlib.
  

## 👩‍💻 Project

**AI Image Generation Bot**

Built as a hands-on project to explore Generative AI and image generation.

**Technologies:** Python | Stable Diffusion | PyTorch | FastAPI | Streamlit






<img width="1297" height="894" alt="image" src="https://github.com/user-attachments/assets/a6648755-1f8c-473a-bada-8e40878881fc" />

















<img width="1333" height="912" alt="image" src="https://github.com/user-attachments/assets/86c3ac16-a541-466e-80c1-0c98bb064b8b" />




















