# MMCVs App

The **CV Creator** app allows users to easily create, edit, compare and customize their curriculum vitae (CV). It offers a user-friendly interface, making the process of building a professional CV quick and simple.

## Features

- **User-friendly Interface**: Easy-to-use platform for creating and customizing CVs.
- **Pre-designed Templates**: Choose from a range of templates that suit your professional needs.
- **Customization Options**: Add sections for personal information, work experience, skills, education, certifications, and more.
- **Downloadable PDF**: Generate and download your CV in PDF format.
- **Save Progress**: Save and load drafts to complete your CV at your convenience.
- **Mobile Responsive**: View and edit CV on mobile devices.

## Tech Stack
- **Backend**: Python 3.13+ (FastAPI)

## Installation

### Backend Setup

1. Clone the repository:
   ```bash command (terminal)
   git clone https://github.com/maratNeSlaiv/mmcvs_back.git
   cd mmcvs_back

2. Create a virtual environment:
    ```bash command (terminal)
    python3.13 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. Install dependencies:
    ```bash command (terminal)
    pip install -r requirements.txt

4. Run the backend server:
    ```bash command (terminal)
    uvicorn src.main:app --reload