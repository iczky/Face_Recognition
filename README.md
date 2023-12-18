# Face Recognition Project

This project uses Python and OpenCV for face recognition using the DeepFace library. It captures a reference image and then continuously compares it with the live video feed for face matching.

## Prerequisites

- Python 3.x installed
- Virtual environment (venv) for managing dependencies

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/iczky/Face_Recognition.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Face_Recognition
   ```

3. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate      # On Linux/Mac
   .\venv\Scripts\activate      # On Windows
   ```

4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the main script:

   ```bash
   python main.py
   ```

2. Follow the on-screen instructions to enter the user name.

3. The program will capture a reference image after a 5-second countdown.

4. Once the reference image is captured, the program will continuously compare it with the live video feed for face matching.

5. Press 'q' to exit the program.
