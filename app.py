import streamlit as st
import requests

# Page config
st.set_page_config(
    page_title="RFP Upload",
    page_icon="📄",
    layout="centered"
)

# Define the webhook URL
WEBHOOK_URL = "https://infinite-wasp-terminally.ngrok-free.app/webhook/e7120083-e23a-46a9-a92d-5d200eeeace2"

def send_file_to_webhook(file):
    try:
        # Prepare the file for sending
        files = {
            'file': (file.name, file.getvalue(), 'application/pdf')
        }
        
        # Send POST request
        response = requests.post(WEBHOOK_URL, files=files)
        
        # Check response
        if response.status_code == 200:
            return True, "Document processed successfully!"
        else:
            return False, f"Error: Server returned status code {response.status_code}"
    except Exception as e:
        return False, f"Error: {str(e)}"

# Custom CSS
st.markdown("""
    <style>
        .main {
            padding: 2rem;
        }
        .stTitle {
            color: #1E88E5;
            font-size: 3rem !important;
            padding-bottom: 2rem;
        }
        .upload-section {
            background-color: #f8f9fa;
            padding: 2rem;
            border-radius: 10px;
            border: 2px dashed #1E88E5;
            margin: 2rem 0;
            transition: all 0.3s ease;
            cursor: pointer;
            position: relative;
            min-height: 150px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }
        .upload-section:hover {
            border-color: #1565C0;
            background-color: #E3F2FD;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }
        .upload-section::before {
            content: '📄 Drag and drop your PDF here';
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            font-size: 1.2rem;
            color: #666;
            pointer-events: none;
            transition: all 0.3s ease;
            text-align: center;
            width: 100%;
        }
        .upload-section:hover::before {
            color: #1565C0;
            transform: translate(-50%, -60%);
        }
        .upload-section::after {
            content: 'or click to browse files';
            position: absolute;
            top: 60%;
            left: 50%;
            transform: translate(-50%, 0);
            font-size: 0.9rem;
            color: #888;
            pointer-events: none;
            opacity: 0.8;
        }
        .file-info {
            background-color: #e3f2fd;
            padding: 1.5rem;
            border-radius: 5px;
            margin-top: 1rem;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
        }
        .info-text {
            color: #666;
            font-size: 0.9rem;
            background-color: #fff;
            padding: 1rem;
            border-radius: 5px;
            border-left: 4px solid #1E88E5;
            margin: 1rem 0;
        }
        /* Hide the default streamlit upload text */
        .upload-section .st-emotion-cache-1erivf3 {
            visibility: hidden;
        }
        .stButton>button {
            background-color: #1E88E5;
            color: white;
            border-radius: 25px;
            padding: 0.5rem 2rem;
            transition: all 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #1565C0;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            transform: translateY(-2px);
        }
    </style>
""", unsafe_allow_html=True)

# Header section
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.title("RFP Document Upload")

# Info section
st.markdown("""
    <div class='info-text'>
        <h4>📋 Instructions:</h4>
        <ul>
            <li>Upload your RFP document in PDF format</li>
            <li>Maximum file size: 200MB</li>
            <li>Supported format: PDF only</li>
        </ul>
    </div>
""", unsafe_allow_html=True)

# Upload section
st.markdown("<div class='upload-section'>", unsafe_allow_html=True)
uploaded_file = st.file_uploader(
    " ",  # Empty label since we're using CSS for the text
    type=['pdf'],
    help="Upload a PDF file containing your RFP document"
)
st.markdown("</div>", unsafe_allow_html=True)

# Display file information if uploaded
if uploaded_file is not None:
    st.markdown("<div class='file-info'>", unsafe_allow_html=True)
    
    # Create two columns for file info
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("##### 📄 File Details")
        st.write(f"**Name:** {uploaded_file.name}")
        st.write(f"**Size:** {uploaded_file.size / 1024:.2f} KB")
    
    with col2:
        st.markdown("##### 🔍 Status")
        st.success("✅ File uploaded successfully")
        
        # Add a process button
        if st.button("Process Document 🚀", key="process_btn"):
            with st.spinner("Processing document..."):
                # Send file to webhook
                success, message = send_file_to_webhook(uploaded_file)
                if success:
                    st.success(message)
                else:
                    st.error(message)
    
    st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("""
    <div style='position: fixed; bottom: 0; width: 100%; text-align: center; padding: 1rem; background-color: #f8f9fa;'>
        <p style='color: #666; font-size: 0.8rem;'>
            Upload your RFP documents securely • Supported format: PDF
        </p>
    </div>
""", unsafe_allow_html=True) 