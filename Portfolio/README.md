# Hazel Mahajan - Interactive Resume

A professional, interactive resume built with Streamlit that showcases Hazel's experience, skills, and projects.

## Features

- **Professional Design**: Clean, modern layout with responsive design
- **Interactive Elements**: Clickable contact information and social links
- **QR Code Generation**: Automatically generates a QR code for easy sharing
- **Mobile Responsive**: Works perfectly on all devices
- **Downloadable QR Code**: Users can download the QR code for offline sharing

## Sections

1. **Summary**: Availability for full-time roles (Jan 2026) and co-op opportunities (Aug-Dec 2025)
2. **Professional Experience**: Detailed work history with achievements
3. **Education**: Academic background and coursework
4. **Technical Skills**: Programming languages and technologies
5. **Projects**: Portfolio of technical projects
6. **QR Code**: Shareable QR code for the resume

## Deployment to Streamlit Cloud

### Option 1: Deploy via Streamlit Cloud (Recommended)

1. **Push to GitHub**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Interactive resume"
   git branch -M main
   git remote add origin https://github.com/yourusername/your-repo-name.git
   git push -u origin main
   ```

2. **Deploy on Streamlit Cloud**:
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with your GitHub account
   - Click "New app"
   - Select your repository and set the path to `app.py`
   - Click "Deploy"

3. **Get Your Public URL**:
   - Your resume will be available at: `https://your-app-name-yourusername.streamlit.app`
   - The QR code will automatically link to this URL

### Option 2: Local Development

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run Locally**:
   ```bash
   streamlit run app.py
   ```

3. **Access Locally**:
   - Open your browser to `http://localhost:8501`

## Files Structure

```
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── resume.html        # Static HTML version (for reference)
└── README.md          # This file
```

## Customization

- **Colors**: Modify the CSS variables in the `app.py` file
- **Content**: Update the resume information directly in the Python code
- **Styling**: Adjust the CSS classes and styles as needed
- **QR Code**: The QR code automatically updates when deployed

## Benefits of Streamlit Hosting

- **Always Accessible**: Available 24/7 online
- **Professional URL**: Clean, shareable link
- **Automatic Updates**: Easy to modify and redeploy
- **Analytics**: Track visitor engagement
- **Mobile Friendly**: Optimized for all devices
- **No Server Management**: Fully managed by Streamlit

## Contact

For questions or modifications, contact: hazelmahajan8500@gmail.com

---

**Note**: After deployment, the QR code will automatically link to your Streamlit app URL, making it easy for anyone to scan and view your resume online! 