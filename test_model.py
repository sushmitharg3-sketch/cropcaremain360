#!/usr/bin/env python3
"""
Test script for Hugging Face plant disease detection model
Run this to verify your API key and model access
"""

import os
import requests
import base64
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

HUGGINGFACE_API_KEY = os.getenv('HUGGINGFACE_API_KEY')
HF_MODEL = os.getenv('HF_MODEL', 'linkanjarad/mobilenet_v2_1.0_224-plant-disease-identification')

def test_model_access():
    """Test if we can access the Hugging Face model"""
    
    if not HUGGINGFACE_API_KEY:
        print("❌ HUGGINGFACE_API_KEY not found in .env file")
        print("Please add your Hugging Face API key to the .env file")
        print("Get one free at: https://huggingface.co/settings/tokens")
        return False
    
    print(f"✅ API Key found: {HUGGINGFACE_API_KEY[:10]}...")
    print(f"🤖 Testing model: {HF_MODEL}")
    
    # Test API endpoint
    url = f"https://api-inference.huggingface.co/models/{HF_MODEL}"
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}
    
    # Create a simple test payload (1x1 pixel image)
    test_image = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x02\x00\x00\x00\x90wS\xde\x00\x00\x00\tpHYs\x00\x00\x0b\x13\x00\x00\x0b\x13\x01\x00\x9a\x9c\x18\x00\x00\x00\nIDATx\x9cc```\x00\x00\x00\x04\x00\x01\xdd\x8d\xb4\x1c\x00\x00\x00\x00IEND\xaeB`\x82'
    
    try:
        print("🔄 Sending test request...")
        response = requests.post(url, headers=headers, data=test_image, timeout=30)
        
        if response.status_code == 200:
            result = response.json()
            print("✅ Model is accessible and working!")
            print(f"📊 Response: {result}")
            return True
        elif response.status_code == 503:
            error_data = response.json()
            if 'loading' in error_data.get('error', '').lower():
                print("⏳ Model is loading... This is normal for the first request.")
                print("💡 Try again in 30-60 seconds.")
                return True
            else:
                print(f"❌ Service error: {error_data}")
                return False
        else:
            print(f"❌ HTTP Error {response.status_code}: {response.text}")
            return False
            
    except requests.exceptions.Timeout:
        print("⏳ Request timed out - model might be loading")
        print("💡 This is normal for the first request. Try again in a minute.")
        return True
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

def test_alternative_models():
    """Test alternative plant disease detection models"""
    
    alternative_models = [
        "microsoft/resnet-50",
        "google/vit-base-patch16-224",
        "facebook/deit-base-distilled-patch16-224"
    ]
    
    print("\n🔍 Testing alternative models...")
    
    for model in alternative_models:
        print(f"\n📋 Testing: {model}")
        url = f"https://api-inference.huggingface.co/models/{model}"
        headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}
        
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                print(f"✅ {model} is accessible")
            else:
                print(f"❌ {model} returned {response.status_code}")
        except Exception as e:
            print(f"❌ {model} error: {str(e)}")

if __name__ == "__main__":
    print("🌱 CROPCARE 360 - Model Test Script")
    print("=" * 50)
    
    success = test_model_access()
    
    if success:
        print("\n🎉 Setup looks good! You can now run the diagnostic system.")
        print("\nNext steps:")
        print("1. Start the Flask server: python server/app.py")
        print("2. Start the frontend: npm run dev")
        print("3. Visit http://localhost:5173 to test the diagnostic feature")
    else:
        print("\n🔧 Please fix the issues above before running the diagnostic system.")
        test_alternative_models()
    
    print("\n" + "=" * 50)
    print("Developed by S³V • CROPCARE 360")