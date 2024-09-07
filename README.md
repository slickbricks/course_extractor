# XML File Combiner Streamlit App

## Features

- **Upload Compressed File**: Users can upload a compressed file (zip format, but does not require a `.zip` extension).
- **XML Data Extraction**: The app extracts text data from all XML files within the compressed file.
- **Combine Data**: Combines data from all XML files into a single text file.
- **Downloadable Output**: Allows users to download the combined XML data in a single `.txt` file.

## Prerequisites

- Python 3.x
- Streamlit

## Installation

1. Clone the repository or download the script.
2. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv myenv
    ```

    Activate the virtual environment:

    - **Windows**: 
      ```bash
      myenv\Scripts\activate
      ```
    - **Mac/Linux**: 
      ```bash
      source myenv/bin/activate
      ```

3. Install the required packages:

    ```bash
    pip install streamlit
    ```

## Usage

1. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

2. Open the URL provided in the terminal (usually `http://localhost:8501`).
3. Upload a compressed file containing XML files.
4. Click the **Combine XML Files** button to process the files.
5. Download the combined data by clicking the **Download Combined Output** button.

## File Structure

```plaintext
.
├── app.py           # Main Streamlit app script
├── README.md        # This README file
└── combined_output.txt  # The combined output (generated after running the app)
