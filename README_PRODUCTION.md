# CropCare 360 - Production Setup Guide

**Developer Credit: S³V**

## 🚀 Quick Start

### 1. Install Dependencies
```bash
# Frontend dependencies
npm install

# Backend dependencies
cd backend
pip install -r requirements.txt
cd ..
```

### 2. Start the Application
```bash
# Start both frontend and backend
npm run start-full

# OR start separately:
# Terminal 1: Backend
npm run backend

# Terminal 2: Frontend  
npm start
```

### 3. Access the Application
- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs

## 📋 Features

✅ **Real-time plant disease detection**  
✅ **Camera capture & file upload**  
✅ **AI-powered diagnosis with confidence scores**  
✅ **Treatment solutions & prevention tips**  
✅ **History tracking with Supabase**  
✅ **CSV export functionality**  
✅ **Responsive green-themed UI**  
✅ **Optional user authentication**

## 🔧 Configuration

The `.env` file is pre-configured with working API keys. For production:

1. **Hugging Face API**: Get free key at https://huggingface.co/settings/tokens
2. **Supabase**: Create project at https://supabase.com
3. **Run the database migration** in Supabase SQL editor:
   ```sql
   -- Copy content from supabase/migrations/002_create_diagnosis_table.sql
   ```

## 🏗️ Architecture

```
CropCare 360/
├── backend/
│   ├── main.py              # FastAPI server
│   └── requirements.txt     # Python dependencies
├── src/
│   ├── pages/
│   │   └── Diagnostic.tsx   # Main diagnostic component
│   └── lib/
│       └── supabase.ts      # Database client
├── supabase/
│   └── migrations/          # Database schema
└── .env                     # Environment variables
```

## 🧪 Testing

1. **Upload a plant image** or use camera capture
2. **Click "Analyze Plant"** to get AI diagnosis
3. **View results** with disease name, confidence, and treatment
4. **Check History tab** for saved diagnoses
5. **Export data** as CSV

## 🌐 Production Deployment

### Frontend (Vercel/Netlify)
```bash
npm run build
# Deploy dist/ folder
```

### Backend (Railway/Render)
```bash
# Deploy backend/ folder
# Set environment variables
# Install Python dependencies
```

## 📊 API Endpoints

- `POST /diagnose` - Analyze plant image
- `GET /` - API status

## 🎨 UI Components

- **Green agricultural theme**
- **Responsive design**
- **Real-time analysis**
- **Loading states**
- **Error handling**

---

**Developed by S³V 🌱**