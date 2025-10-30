# CROPCARE 360 - Real-Time Plant Disease Diagnostic Setup

## Overview
CROPCARE 360 is an intelligent agricultural platform with real-time plant disease detection using AI. This guide will help you set up the complete diagnostic system locally.

## Features
- 📸 **Real-time image capture** or file upload
- 🤖 **AI-powered disease detection** using Hugging Face models
- 📊 **Instant results** with confidence scores
- 💾 **History tracking** with Supabase integration
- 📤 **CSV export** functionality
- 🔐 **Optional authentication** for data sync
- 🎨 **Modern green-themed UI** with Tailwind CSS

## Prerequisites
- Node.js (v16 or higher)
- Python (v3.8 or higher)
- Git

## Quick Setup

### 1. Clone and Install Dependencies

```bash
# Clone the repository
git clone <your-repo-url>
cd cropcare-360-agri-smart-main

# Install Node.js dependencies
npm install

# Install Python dependencies
pip install -r requirements.txt
```

### 2. Environment Configuration

Copy the `.env` file and update with your API keys:

```bash
# The .env file is already configured with example keys
# For production, get your own keys:

# Hugging Face API Key (Free)
# 1. Go to https://huggingface.co/settings/tokens
# 2. Create a new token
# 3. Replace HUGGINGFACE_API_KEY in .env

# Supabase (Optional - for user auth and data sync)
# 1. Go to https://supabase.com
# 2. Create a new project
# 3. Replace VITE_SUPABASE_* values in .env
```

### 3. Database Setup (Optional)

If using Supabase for user authentication and data storage:

```bash
# Run the migration to create the diagnoses table
# Copy the SQL from supabase/migrations/001_create_diagnoses_table.sql
# and run it in your Supabase SQL editor
```

### 4. Start the Application

**Option A: Using Node.js backend (existing)**
```bash
npm start
```

**Option B: Using Flask backend (recommended for AI features)**
```bash
npm run start-flask
```

The application will be available at:
- Frontend: http://localhost:5173
- Node.js Backend: http://localhost:5000
- Flask Backend: http://localhost:5001

## Usage Guide

### 1. Plant Disease Diagnosis

1. **Upload Image**: Click "Upload" or use "Camera" to capture a live photo
2. **Analyze**: Click "Analyze Plant" to get AI-powered diagnosis
3. **View Results**: See disease name, confidence score, causes, and treatment
4. **Try Again**: Use "Try Again" button for new diagnosis

### 2. Features

- **Real-time Analysis**: Instant results without page reloads
- **Confidence Scoring**: Color-coded confidence levels (Green: >80%, Yellow: >60%, Red: <60%)
- **Treatment Recommendations**: Detailed step-by-step treatment plans
- **History Tracking**: View past diagnoses with thumbnails
- **CSV Export**: Download diagnosis history as spreadsheet
- **Optional Login**: Sync data across devices with Supabase Auth

### 3. Supported Plant Diseases

The AI model can detect:
- Healthy plants
- Bacterial spot
- Early blight
- Late blight
- Leaf mold
- Septoria leaf spot
- Spider mites
- Target spot
- Mosaic virus
- Yellow leaf curl virus

## API Endpoints

### Flask Backend (Port 5001)
- `GET /api/health` - Health check and model status
- `POST /api/diagnose` - Plant disease diagnosis
- `GET /api/models` - List available AI models

### Node.js Backend (Port 5000)
- `GET /api/health` - Health check
- `GET /api/weather` - Weather data
- `POST /api/diagnose` - Basic diagnosis (fallback)

## File Structure

```
cropcare-360-agri-smart-main/
├── src/
│   ├── pages/
│   │   └── Diagnostic.tsx          # Main diagnostic component
│   ├── components/
│   │   └── Auth.tsx                # Authentication component
│   └── integrations/
│       └── supabase/               # Supabase integration
├── server/
│   ├── index.js                    # Node.js backend
│   └── app.py                      # Flask backend (AI features)
├── supabase/
│   └── migrations/                 # Database schema
├── requirements.txt                # Python dependencies
├── .env                           # Environment variables
└── package.json                   # Node.js dependencies
```

## Troubleshooting

### Common Issues

1. **AI Model Loading Error**
   - Wait 30-60 seconds for the model to load on first request
   - Check Hugging Face API key in .env file

2. **Camera Not Working**
   - Ensure HTTPS or localhost (required for camera access)
   - Grant camera permissions in browser

3. **Supabase Connection Issues**
   - Verify Supabase URL and keys in .env
   - Check if RLS policies are properly set

4. **Python Dependencies**
   ```bash
   # If pip install fails, try:
   pip install --upgrade pip
   pip install -r requirements.txt --force-reinstall
   ```

### Development Tips

- Use `npm run dev` for frontend-only development
- Use `npm run flask-server` to run only the Flask backend
- Check browser console for detailed error messages
- Monitor server logs for API issues

## Production Deployment

### Frontend (Vercel/Netlify)
```bash
npm run build
# Deploy the dist/ folder
```

### Backend Options

**Option 1: Heroku (Flask)**
```bash
# Add Procfile: web: gunicorn server.app:app
git push heroku main
```

**Option 2: Railway/Render**
- Deploy the Flask app (server/app.py)
- Set environment variables
- Install Python dependencies

## Environment Variables Reference

```env
# Server Configuration
PORT=5000                          # Node.js server port
FLASK_PORT=5001                    # Flask server port

# AI Configuration
HUGGINGFACE_API_KEY=hf_xxx         # Required for AI diagnosis
HF_MODEL=linkanjarad/mobilenet_v2_1.0_224-plant-disease-identification

# Supabase (Optional)
VITE_SUPABASE_URL=https://xxx.supabase.co
VITE_SUPABASE_PUBLISHABLE_KEY=eyJxxx

# Weather API (Optional)
OPENWEATHER_API_KEY=xxx
```

## Credits

**Developed by S³V**
- Real-time AI plant disease detection
- Modern React + TypeScript frontend
- Flask + Hugging Face AI backend
- Supabase integration for data persistence

## License

This project is part of CROPCARE 360 agricultural platform.

---

For support or questions, please check the troubleshooting section or create an issue in the repository.