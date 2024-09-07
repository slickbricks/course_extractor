import os
import xml.etree.ElementTree as ET
import streamlit as st
import zipfile
import io

# Function to extract data from a single XML file
def extract_xml_data(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        extracted_data = ""
        for elem in root.iter():
            if elem.text:
                extracted_data += elem.text.strip() + "\n"
        return extracted_data
    except ET.ParseError as e:
        return f"Error parsing {file_path}: {e}\n"

# Function to combine all XML files in a folder and return as text
def combine_xml_files(zip_file):
    combined_data = ""
    with zipfile.ZipFile(zip_file) as z:
        for filename in z.namelist():
            if filename.endswith(".xml"):
                with z.open(filename) as xml_file:
                    xml_data = extract_xml_data(io.BytesIO(xml_file.read()))
                    combined_data += f"\n--- Data from {filename} ---\n"
                    combined_data += xml_data
    return combined_data

# Streamlit UI
st.title("XML File Combiner")

# File uploader for zip or other archive file
uploaded_file = st.file_uploader("Upload a zipped file containing XML files", type=None)

if uploaded_file is not None:
    # Button to process the uploaded file
    if st.button("Combine XML Files"):
        try:
            # Combine XML data from the uploaded archive
            combined_data = combine_xml_files(uploaded_file)

            if combined_data:
                # Save the combined data to a text file
                output_file = "combined_output.txt"
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(combined_data)

                # Allow the user to download the file
                with open(output_file, 'rb') as f:
                    st.download_button(
                        label="Download Combined Output",
                        data=f,
                        file_name=output_file,
                        mime="text/plain"
                    )
                st.success("XML files combined successfully!")
            else:
                st.error("No XML files found in the uploaded archive.")
        except zipfile.BadZipFile:
            st.error("The uploaded file is not a valid zip file.")
