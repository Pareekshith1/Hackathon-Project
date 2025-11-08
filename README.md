# Hackathon Projects Portfolio

This repository contains three innovative hackathon projects, each addressing unique challenges with cutting-edge solutions. Below you'll find comprehensive documentation for each project including setup instructions, features, and usage guidelines.

---

## Table of Contents

- [Project 1: CreativeStudio - AI Image Generation & Editing Platform](#project-1-creativestudio---ai-image-generation--editing-platform)
- [Project 2: FinTech Credit Card Security System](#project-2-fintech-credit-card-security-system)
- [Project 3: Smart Parking Management System](#project-3-smart-parking-management-system)
- [Contributors](#contributors)
- [License](#license)

---

## Project 1: CreativeStudio - AI Image Generation & Editing Platform

### 📋 Overview
CreativeStudio is a comprehensive image processing and AI-powered image generation platform built with Streamlit. It combines traditional image filters with state-of-the-art AI image generation using Stability AI's SDXL model through Replicate API.

### 🎯 Features
- **AI Text-to-Image Generation**: Generate stunning images from text prompts using SDXL
- **Image Filters**: Apply various filters including Grayscale, Sepia, Blur, Contour, and Sketch
- **Image Corrections**: Enhance images with brightness, contrast, and sharpness adjustments
- **Background Removal**: Advanced background removal functionality
- **Gallery Management**: View and manage generated images
- **User-Friendly Interface**: Modern, intuitive UI with wide layout support

### 🛠️ Technology Stack
- **Framework**: Streamlit
- **AI/ML**: Replicate API (Stability AI SDXL)
- **Image Processing**: OpenCV, PIL (Pillow)
- **Additional Libraries**: NumPy, requests, streamlit-image-select

### 📦 Installation

1. **Navigate to the project directory**:
   ```bash
   cd combined-application
   ```

2. **Install Python dependencies**:
   ```bash
   pip install streamlit
   pip install opencv-python
   pip install pillow
   pip install numpy
   pip install replicate
   pip install requests
   pip install streamlit-image-select
   ```

   Alternatively, if you're using the provided wheel files:
   ```bash
   pip install numpy-1.23.0-cp310-cp310-win_amd64.whl  # For Python 3.10
   # or
   pip install numpy-1.23.0-cp39-cp39-win_amd64.whl   # For Python 3.9
   ```

3. **Configure Streamlit Secrets**:
   Create a `.streamlit/secrets.toml` file with your API credentials:
   ```toml
   REPLICATE_API_TOKEN = "your_replicate_api_token"
   REPLICATE_MODEL_ENDPOINTSTABILITY = "stability-ai/sdxl"
   ```

### 🚀 Running the Application

**Main Application (AI Image Generator)**:
```bash
streamlit run streamlit_app.py
```

**Alternative Entry Points**:
```bash
streamlit run app.py        # Creative Studio interface
streamlit run main.py       # Filter Selector
```

### 📁 Project Structure
```
combined-application/
├── app.py                  # Main CreativeStudio interface
├── streamlit_app.py        # AI Image Generation interface
├── main.py                 # Filter Selector application
├── bg_remove.py            # Background removal functionality
├── utils/                  # Utility modules
│   ├── icon.py            # Icon utilities
│   └── __init__.py
├── .streamlit/            # Streamlit configuration
├── gallery/               # Generated images gallery
├── Images/                # Static images
└── Support_Notebook.ipynb # Development notebook
```

### 💡 Usage Examples

**Generate AI Images**:
1. Run the Streamlit app
2. Enter your text prompt in the sidebar
3. Adjust parameters (width, height, guidance scale, etc.)
4. Click "Submit" to generate images

**Apply Filters**:
1. Upload an image
2. Select desired filter from the sidebar
3. View and download the processed image

---

## Project 2: FinTech Credit Card Security System

### 📋 Overview
A comprehensive credit card fraud detection and prevention system built with Flask. This system includes multiple layers of security including fraud detection, trust score calculation, double verification, and transaction monitoring.

### 🎯 Features
- **Fraud Detection**: Machine Learning-based fraud detection using Random Forest Classifier
- **Trust Score System**: Real-time trust score calculation based on transaction patterns
- **Double Verification**: Aadhar-based verification system for secure transactions
- **Transaction Monitoring**: Track and analyze suspicious transactions
- **User Activity Dashboard**: Monitor user activities and transaction history
- **Complaint Management**: Built-in complaint submission and tracking system
- **Admin Portal**: Comprehensive admin dashboard for system management
- **Location-Based Analysis**: Geographic visualization of transactions using Indian map

### 🛠️ Technology Stack
- **Backend**: Flask (Python)
- **Machine Learning**: scikit-learn (Random Forest Classifier)
- **Data Processing**: Pandas, NumPy
- **Frontend**: HTML, CSS, JavaScript
- **Payment Integration**: Razor Pay
- **Data Visualization**: Jupyter Notebook integration

### 📦 Installation

1. **Navigate to the project directory**:
   ```bash
   cd fin-tech-creditcard-Kochi-hackathon
   ```

2. **Install Python dependencies**:
   ```bash
   pip install flask
   pip install pandas
   pip install numpy
   pip install scikit-learn
   pip install jupyter
   ```

3. **Verify required datasets**:
   - `fraud_dataset_example.csv` - Fraud detection training data
   - `trustScore.csv` - Trust score calculation data
   - `dataset.csv` - General transaction data

### 🚀 Running the Application

**Main Application**:
```bash
python main.py
```

**Individual Modules**:
```bash
python flask-backend.py    # Double verification system
python trustscore.py       # Trust score calculation
python activity.py         # Activity monitoring
python transactions.py     # Transaction management
python login.py           # Authentication system
python mistral-ai.py      # AI integration features
```

### 📁 Project Structure
```
fin-tech-creditcard-Kochi-hackathon/
├── main.py                        # Main Flask application
├── flask-backend.py               # Double verification backend
├── trustscore.py                  # Trust score calculation
├── activity.py                    # Activity monitoring
├── transactions.py                # Transaction processing
├── login.py                       # Authentication system
├── mistral-ai.py                  # AI features
├── templates/                     # HTML templates
│   ├── index.html
│   ├── login.html
│   ├── trustscore.html
│   ├── suspicioustransaction.html
│   ├── activity.html
│   ├── admin.html
│   ├── double_verification_index.html
│   └── ... (other templates)
├── static/                        # Static files
│   ├── style.css
│   ├── loginstyle.css
│   ├── admin_styles.css
│   ├── app.js
│   └── images/
├── dataset.csv                    # Transaction dataset
├── fraud_dataset_example.csv      # Fraud detection dataset
├── trustScore.csv                 # Trust score dataset
└── MAP_india.ipynb               # Geographic analysis notebook
```

### 💡 Usage Examples

**Fraud Detection**:
1. Access the fraud detection portal
2. Input transaction details (amount, balance changes)
3. System analyzes and provides fraud probability

**Trust Score Calculation**:
1. Navigate to `/` endpoint
2. Enter mobile number
3. View calculated trust score and fraud alert status

**Double Verification**:
1. Access verification portal
2. Enter verification and receiver mobile numbers
3. System validates Aadhar match

### 🔐 Security Features
- Multi-factor authentication
- Aadhar-based verification
- Real-time fraud detection
- Transaction pattern analysis
- Suspicious location detection
- Business hours validation

---

## Project 3: Smart Parking Management System

### 📋 Overview
A futuristic smart parking management system built with Tkinter that enables users to book parking slots, generate QR code tickets, and visualize real-time parking availability with an interactive simulation.

### 🎯 Features
- **Slot Booking System**: Real-time parking slot booking
- **QR Code Generation**: Automatic QR code ticket generation for bookings
- **Visual Simulation**: Interactive canvas showing parking lot status
- **Real-time Updates**: Live parking slot availability tracking
- **Timer Management**: Automated booking timer system
- **Multi-slot Support**: Manages 6 parking slots simultaneously
- **User-Friendly GUI**: Modern, intuitive interface with hover effects

### 🛠️ Technology Stack
- **GUI Framework**: Tkinter
- **QR Code Generation**: qrcode, PIL (Pillow)
- **Audio/Media**: Pygame
- **Image Processing**: PIL (Pillow)

### 📦 Installation

1. **Navigate to the project directory**:
   ```bash
   cd uyir-hackathon
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   Or install manually:
   ```bash
   pip install tkinter
   pip install Pillow
   pip install qrcode
   pip install pygame
   ```

   **Note**: Tkinter usually comes pre-installed with Python. If not available, install it via your system package manager.

### 🚀 Running the Application

**Main Application**:
```bash
python main.py
```

**Simulation Mode**:
```bash
python simulation.py
```

**Test Cases**:
```bash
python case-2.py    # Test case 2
python case-3.py    # Test case 3
```

### 📁 Project Structure
```
uyir-hackathon/
├── main.py                    # Main parking system interface
├── simulation.py              # Parking simulation with test cases
├── case-2.py                  # Additional test case
├── case-3.py                  # Additional test case
├── requirements.txt           # Python dependencies
├── qr_ticket.png             # Sample QR ticket
├── ticket.png                # Ticket template
├── test 1_parking_qr.png     # Test QR code
└── pyvenv.cfg                # Virtual environment config
```

### 💡 Usage Guide

**Booking a Parking Slot**:
1. Launch the application
2. Click "🅿️ Book a Slot"
3. Select an available parking slot
4. Enter vehicle details
5. Confirm booking
6. QR code ticket is automatically generated

**Simulation Features**:
1. Visual representation of 6 parking slots
2. Color-coded status indicators:
   - **Available**: Open slots
   - **Booked**: Reserved slots with timer
3. Real-time timer countdown
4. Interactive slot selection

### 🎮 GUI Features
- Modern dark theme (#0A0A0A background)
- Hover effects on buttons
- Color transitions for better UX
- Responsive layout (800x500 default)
- Unicode emoji support for better visual appeal

### 🔧 Configuration
The system manages 6 parking slots (numbered 1-6) with the following default positions:
- Slots 1-3: Top row (positions: 100, 250, 400 x 100)
- Slots 4-6: Bottom row (positions: 100, 250, 400 x 300)

---

## 🔄 Common Requirements Across Projects

### System Requirements
- **Python**: 3.9 or higher
- **Operating System**: Windows, macOS, or Linux
- **RAM**: Minimum 4GB (8GB recommended for AI features)
- **Storage**: At least 500MB free space

### Development Tools
- Python 3.9+
- pip (Python package manager)
- Virtual environment (recommended)
- Git (for version control)

### Setting Up Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Install project dependencies
cd <project-directory>
pip install -r requirements.txt  # If requirements.txt exists
```

---

## 🚀 Quick Start Guide

### For All Projects:

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd Hackathon-Project
   ```

2. **Choose your project**:
   - CreativeStudio: `cd combined-application`
   - FinTech Security: `cd fin-tech-creditcard-Kochi-hackathon`
   - Smart Parking: `cd uyir-hackathon`

3. **Install dependencies** (see individual project sections)

4. **Run the application** (see individual project sections)

---

## 📝 Project-Specific Notes

### CreativeStudio
- Requires active internet connection for AI image generation
- API tokens must be configured in `.streamlit/secrets.toml`
- Generated images are stored in the `gallery/` directory

### FinTech Credit Card Security System
- Ensure all CSV datasets are present before running
- Default port is 5000 (Flask default)
- Dummy user data is pre-configured for testing
- Admin portal accessible after authentication

### Smart Parking Management System
- No internet connection required
- QR codes are saved locally
- Supports up to 6 concurrent parking slots
- Timer-based booking management

---

## 🐛 Troubleshooting

### Common Issues:

**Import Errors**:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**Port Already in Use (Flask)**:
```bash
# Change port in the Python file
app.run(debug=True, port=5001)  # Use different port
```

**Tkinter Not Found**:
```bash
# Ubuntu/Debian
sudo apt-get install python3-tk
# macOS
brew install python-tk
```

**Streamlit Secrets Not Found**:
- Create `.streamlit` directory
- Add `secrets.toml` file with required API keys

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📧 Support

For questions, issues, or suggestions regarding any of the projects:
- Open an issue in the repository
- Contact the project maintainers

---

## 📄 License

This repository contains multiple projects developed for hackathon purposes. Please refer to individual project directories for specific license information.

---

## 🏆 Acknowledgments

These projects were developed as part of various hackathon competitions, showcasing innovative solutions in:
- AI/ML and Image Processing
- Financial Technology and Security
- Smart City Infrastructure

Special thanks to all contributors, mentors, and hackathon organizers who made these projects possible.

---

## 📊 Project Statistics

| Project | Technology | Complexity | Use Case |
|---------|-----------|------------|----------|
| CreativeStudio | Streamlit + AI | High | Content Creation |
| FinTech Security | Flask + ML | High | Financial Security |
| Smart Parking | Tkinter | Medium | Urban Infrastructure |

---

**Last Updated**: 2025-11-08

**Repository Structure**:
```
Hackathon-Project/
├── combined-application/          # Project 1: CreativeStudio
├── fin-tech-creditcard-Kochi-hackathon/  # Project 2: FinTech Security
├── uyir-hackathon/               # Project 3: Smart Parking
└── README.md                     # This file
```

---

*Developed with ❤️ for Hackathons*
