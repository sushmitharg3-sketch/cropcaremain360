# CROPCARE 360 - Smart Farming Assistant

A comprehensive, AI-powered smart farming web application built with React, TypeScript, and Tailwind CSS.

## 🌾 Features

### 1. Dashboard (Home Page)
- Beautiful hero section with farm imagery
- Weather overview card with real-time data
- Farm statistics (plant health, orders, revenue, community)
- Animated savings jar widget
- Fully responsive design

### 2. Plant Disease Diagnostic
- Image upload for plant leaves
- AI-powered disease detection (ready for TensorFlow.js integration)
- Detailed diagnosis with causes and treatment recommendations
- Diagnosis history saved locally
- Mock analysis included (production-ready for ML model integration)

### 3. Marketplace
- Product categories: Seeds, Fertilizers, Pesticides, Tools
- Product cards with images, prices, descriptions
- Shopping cart functionality
- Wishlist feature
- Filter by category
- Price tracking (ready for Recharts integration)

### 4. Weather Station
- Current weather display (temperature, humidity, wind speed, rainfall)
- Location-based weather (mock data included)
- Search for different locations
- Farming recommendations based on weather
- Ready for OpenWeatherMap API integration

### 5. Savings Tracker
- Income/expense management
- Transaction history
- Visual charts using Recharts
- Balance tracking
- LocalStorage persistence
- Add/view transactions

### 6. About Page
- Mission statement
- Feature highlights
- Statistics display
- Professional layout

### 7. Contact Page
- Contact form
- Contact information cards
- Form validation
- Toast notifications

## 🎨 Design System

The app uses a professional agricultural theme with:
- **Primary Color**: Farm Green (HSL: 120, 60%, 35%)
- **Secondary Color**: Earth Brown (HSL: 30, 40%, 45%)
- **Accent Color**: Golden Harvest (HSL: 45, 95%, 55%)
- Custom gradients and shadows
- Smooth transitions and animations
- Fully responsive grid layouts

## 🚀 Getting Started

### Prerequisites
- Node.js (v16 or higher)
- npm or yarn

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd cropcare360
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

4. Open your browser and navigate to:
```
http://localhost:8080
```

## 📦 Project Structure

```
src/
├── components/
│   ├── ui/              # shadcn/ui components
│   ├── Hero.tsx         # Landing hero section
│   ├── Navbar.tsx       # Navigation bar
│   ├── StatsCard.tsx    # Statistics display card
│   ├── WeatherCard.tsx  # Weather information card
│   └── SavingsJar.tsx   # Savings widget
├── pages/
│   ├── Dashboard.tsx    # Home page
│   ├── Diagnostic.tsx   # Plant disease detection
│   ├── Marketplace.tsx  # Product marketplace
│   ├── Weather.tsx      # Weather station
│   ├── Savings.tsx      # Finance tracker
│   ├── About.tsx        # About page
│   ├── Contact.tsx      # Contact form
│   └── NotFound.tsx     # 404 page
├── assets/              # Images and static files
├── lib/                 # Utility functions
├── App.tsx             # Main app component
├── index.css           # Global styles & design system
└── main.tsx            # Entry point
```

## 🔌 API Integration Guide

### For Backend Integration (Node.js + Express + MongoDB):

1. **Create Backend Structure**:
```bash
mkdir backend
cd backend
npm init -y
npm install express mongoose dotenv cors jsonwebtoken bcryptjs
```

2. **Environment Variables (.env)**:
```env
MONGODB_URI=your_mongodb_connection_string
JWT_SECRET=your_jwt_secret
OPENWEATHER_API_KEY=your_openweather_api_key
PORT=5000
```

3. **Backend API Endpoints to Implement**:
- `POST /api/auth/signup` - User registration
- `POST /api/auth/login` - User login
- `GET /api/products` - Get marketplace products
- `POST /api/diagnosis` - Save diagnosis results
- `GET /api/diagnosis/history` - Get diagnosis history
- `GET /api/weather/:location` - Weather proxy endpoint
- `POST /api/transactions` - Save transaction
- `GET /api/transactions` - Get transaction history

4. **Update Frontend API Calls**:
Replace localStorage calls with fetch/axios calls to your backend:

```typescript
// Example: Savings transactions
const saveTransaction = async (transaction) => {
  const response = await fetch('http://localhost:5000/api/transactions', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${token}`
    },
    body: JSON.stringify(transaction)
  });
  return response.json();
};
```

### For OpenWeatherMap Integration:

1. Get API key from: https://openweathermap.org/api
2. Create backend proxy endpoint to keep API key secure
3. Update Weather.tsx to call your backend endpoint

### For TensorFlow.js Plant Disease Detection:

1. Install TensorFlow.js:
```bash
npm install @tensorflow/tfjs @tensorflow-models/mobilenet
```

2. Integrate in Diagnostic.tsx:
```typescript
import * as tf from '@tensorflow/tfjs';
import * as mobilenet from '@tensorflow-models/mobilenet';

const model = await mobilenet.load();
const predictions = await model.classify(imageElement);
```

## 🌐 Features Ready for Enhancement

1. **Authentication System**
   - JWT-based login/signup
   - Protected routes
   - User profiles

2. **Real AI Disease Detection**
   - TensorFlow.js model integration
   - Custom trained plant disease model
   - Image preprocessing

3. **Live Weather Data**
   - OpenWeatherMap API integration
   - Geolocation
   - Weather alerts

4. **Database Integration**
   - MongoDB for data persistence
   - User data management
   - Transaction history

5. **Payment Integration**
   - Stripe/Razorpay for marketplace checkout
   - COD option implementation

6. **Advanced Features**
   - Push notifications
   - Multilingual support
   - Dark mode toggle
   - Community forum
   - AI chatbot

## 🛠️ Technologies Used

- **Frontend**: React 18, TypeScript
- **Styling**: Tailwind CSS, shadcn/ui
- **Routing**: React Router v6
- **Charts**: Recharts
- **Icons**: Lucide React
- **State Management**: React Hooks
- **Build Tool**: Vite
- **Notifications**: Sonner

## 📱 Responsive Design

The application is fully responsive and works seamlessly on:
- Desktop (1920px+)
- Laptop (1024px - 1919px)
- Tablet (768px - 1023px)
- Mobile (320px - 767px)

## 🎯 Current Status

✅ Complete frontend implementation
✅ Responsive design
✅ Navigation and routing
✅ Mock data for all features
✅ LocalStorage persistence
✅ Beautiful UI with animations
✅ Form validation
✅ Toast notifications

⏳ Ready for backend integration
⏳ Ready for ML model integration
⏳ Ready for API integrations

## 📝 Notes

- All data is currently stored in browser localStorage
- Disease detection uses mock data (ready for TensorFlow.js model)
- Weather data is simulated (ready for OpenWeatherMap API)
- Payment system is mock (ready for Stripe/Razorpay)

## 🤝 Contributing

This is a fully functional frontend application ready for backend integration. Follow the API Integration Guide above to connect your backend services.

## 📄 License

MIT License - feel free to use this project for learning and development.

---

**Built with ❤️ for farmers everywhere**
