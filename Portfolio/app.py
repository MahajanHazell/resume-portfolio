import streamlit as st
import qrcode
from PIL import Image
import io
import base64

# Page configuration
st.set_page_config(
    page_title="Hazel Mahajan - Resume",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2rem;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .main-header h1 {
        font-size: 3rem;
        margin-bottom: 1rem;
        font-weight: 300;
        color: white !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .contact-info {
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        gap: 1rem;
        margin-top: 1rem;
    }
    
    .contact-item {
        background: rgba(255, 255, 255, 0.1);
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-size: 0.9rem;
    }
    
    .section {
        margin-bottom: 2rem;
        padding: 1.5rem;
        background: white;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }
    
    .section h2 {
        color: #667eea;
        border-bottom: 2px solid #667eea;
        padding-bottom: 0.5rem;
        margin-bottom: 1rem;
        font-size: 1.8rem;
        font-weight: 600;
    }
    
    .experience-item, .education-item, .project-item, .summary-item {
        margin-bottom: 1.5rem;
        padding: 1.5rem;
        border-left: 4px solid #667eea;
        background-color: #f8f9fa;
        border-radius: 0 8px 8px 0;
    }
    
    .company, .school, .project-name {
        font-weight: bold;
        color: #667eea;
        font-size: 1.2rem;
        margin-bottom: 0.5rem;
    }
    
    .role, .degree {
        font-weight: 600;
        color: #333;
        font-size: 1.1rem;
        margin-bottom: 0.5rem;
    }
    
    .dates, .location {
        color: #666;
        font-size: 0.95rem;
        font-weight: 500;
    }
    
    .responsibilities ul {
        margin-top: 1rem;
        padding-left: 1.5rem;
    }
    
    .responsibilities li {
        margin-bottom: 0.8rem;
        color: #333;
        line-height: 1.6;
        font-size: 1rem;
    }
    
    .skill-tag {
        background-color: #667eea;
        color: white;
        padding: 0.4rem 0.9rem;
        border-radius: 15px;
        font-size: 0.85rem;
        margin: 0.3rem;
        display: inline-block;
        font-weight: 500;
    }
    
    .summary-content {
        color: #333;
        line-height: 1.8;
        font-size: 1.1rem;
    }
    
    .summary-content strong {
        color: #667eea;
        font-weight: 600;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.5rem 2rem;
        font-weight: 600;
    }
    
    /* Ensure all text is visible */
    .stMarkdown, .stMarkdown p, .stMarkdown li, .stMarkdown strong {
        color: #333 !important;
    }
    
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        color: #667eea !important;
    }
    
    /* Override for header name specifically */
    .main-header h1, .main-header .stMarkdown h1 {
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-header">
    <h1>HAZEL MAHAJAN</h1>
    <div class="contact-info">
        <div class="contact-item">📍 San Francisco, CA 94111</div>
        <div class="contact-item">📧 hazelmahajan8500@gmail.com</div>
        <div class="contact-item">📱 +1-(716)-259-6124</div>
        <div class="contact-item">🔗 GitHub</div>
        <div class="contact-item">💼 LinkedIn</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Summary Section
with st.container():
    st.markdown("## SUMMARY")
    st.markdown("""
    <div class="summary-item">
        <div class="summary-content">
            <p><strong>Open to:</strong> Full-time Software Engineering roles starting January 2026</p>
            <p><strong>Available for:</strong> Co-op/Internship opportunities from August - December 2025</p>
            <p><strong>Location:</strong> Open to relocation within the United States</p>
            <br>
            <p><strong>Key Experience Highlights:</strong></p>
            <ul style="margin-top: 0.5rem; padding-left: 1.5rem;">
                <li>2+ years of experience building scalable microservices and distributed systems</li>
                <li>Expertise in Golang, Python, Node.js, and cloud technologies (AWS, GCP, Azure)</li>
                <li>Proven track record of improving system performance by 25-40%</li>
                <li>Experience handling high-volume data processing (10M+ daily requests)</li>
                <li>Strong background in machine learning, AI, and data analytics</li>
                <li>Led successful client onboarding and expanded portfolio by 15%</li>
                <li>Maintained 99.9% service uptime in production environments</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Professional Experience
with st.container():
    st.markdown("## PROFESSIONAL EXPERIENCE")
    
    # KYM Advisors
    st.markdown("""
    <div class="experience-item">
        <div class="company">KYM Advisors Inc.</div>
        <div class="role">Software Engineer Intern</div>
        <div style="display: flex; justify-content: space-between; align-items: center; margin: 1rem 0;">
            <div class="dates">June 2025 - August 2025</div>
            <div class="location">Washington, DC</div>
        </div>
        <div class="responsibilities">
            <ul>
                <li>Developed RESTful APIs in Django (Python) for a document declassification platform, integrating with a React frontend via well-defined contracts (JSON, pagination, error codes) enabling fast, reliable processing of high-volume documents.</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Research Foundation for SUNY
    st.markdown("""
    <div class="experience-item">
        <div class="company">The Research Foundation for SUNY</div>
        <div class="role">Software Engineer (Research Assistant)</div>
        <div style="display: flex; justify-content: space-between; align-items: center; margin: 1rem 0;">
            <div class="dates">January 2025 - May 2025</div>
            <div class="location">Buffalo, NY</div>
        </div>
        <div class="responsibilities">
            <ul>
                <li>Engineered real-time data synchronization and enhanced backend performance using Node.js and AWS, while optimizing React based learning modules to increase frontend load speed by 25%.</li>
                <li>Improved user engagement in agile research projects by refining UI responsiveness and backend API efficiency for interactive learning experiences.</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Delhivery Software Engineer
    st.markdown("""
    <div class="experience-item">
        <div class="company">Delhivery Pvt. Ltd</div>
        <div class="role">Software Engineer</div>
        <div style="display: flex; justify-content: space-between; align-items: center; margin: 1rem 0;">
            <div class="dates">July 2022 - July 2024</div>
            <div class="location">Gurugram, India</div>
        </div>
        <div class="responsibilities">
            <ul>
                <li>Built a microservice orchestrator in Golang, Kafka, and DynamoDB to map service hierarchies and data flows, improving deployment visibility and reducing release coordination time by 25%.</li>
                <li>Engineered "Waybill as a Service", scaling bulk AWB generation with AWS Lambda, Kinesis, and Kafka to handle 10M+ daily requests with high availability.</li>
                <li>Redesigned the async package manifestation pipeline to an event-driven model, cutting processing time by 30% and increasing throughput during peak loads.</li>
                <li>Developed Python reconciliation scripts to align client facility and user data during migration, reducing mismatches by 40% and ensuring smooth onboarding.</li>
                <li>Led Product OS1 core service enhancements, successful onboarding of BIRA and Meesho India, expanding client portfolio by 15%.</li>
                <li>Implemented optimized RESTful APIs for real-time logistics tracking, reducing average API latency by 35%.</li>
                <li>Provided L3 production support, resolving high-priority incidents within SLA and maintaining 99.9% service uptime.</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Delhivery Intern
    st.markdown("""
    <div class="experience-item">
        <div class="company">Delhivery Pvt. Ltd</div>
        <div class="role">Software Engineer Intern</div>
        <div style="display: flex; justify-content: space-between; align-items: center; margin: 1rem 0;">
            <div class="dates">Feb 2022 - June 2022</div>
            <div class="location">Gurugram, India</div>
        </div>
        <div class="responsibilities">
            <ul>
                <li>Worked on containerizing services with Docker, contributing to a 40% improvement in platform reliability and a 25% reduction in code evaluation time.</li>
                <li>Assisted in developing a real-time data streaming pipeline using Firebase and Socket.io, integrating TypeScript, EC2, and Elasticsearch to enable low-latency processing of high-volume event data.</li>
                <li>Supported automation of shipment lifecycle workflows through Python scripting, streamlining the custom CI platform and reducing manual intervention by 30%.</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Yamaha
    st.markdown("""
    <div class="experience-item">
        <div class="company">Yamaha Motor Solutions Co Pvt. Ltd.</div>
        <div class="role">Software Engineer Intern</div>
        <div style="display: flex; justify-content: space-between; align-items: center; margin: 1rem 0;">
            <div class="dates">May 2021 - July 2021</div>
            <div class="location">Greater Noida, India</div>
        </div>
        <div class="responsibilities">
            <ul>
                <li>Automated PostgreSQL maintenance by developing optimized SQL scripts for index reorganization, table partitioning, and performance diagnostics, improving query execution times and database health monitoring.</li>
                <li>Practiced Agile development workflows while implementing secure web practices (CORS, CSP) and leveraging Git, Bash scripting, and advanced PostgreSQL tuning for scalable, high-performance database systems.</li>
                <li>Engineered Python-based statistical analysis tools to evaluate fragmentation levels, monitor row count growth, and analyse data distribution patterns across large-scale datasets, enabling proactive optimization and capacity planning.</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Education
with st.container():
    st.markdown("## EDUCATION")
    
    # University at Buffalo
    st.markdown("""
    <div class="education-item">
        <div class="school">University at Buffalo, The State University of New York</div>
        <div class="degree">Master of Science: Computer Science and Engineering</div>
        <div style="display: flex; justify-content: space-between; align-items: center; margin: 1rem 0;">
            <div class="dates">Aug 2024 - Dec 2025</div>
            <div class="location">Buffalo, NY</div>
        </div>
        <p style="margin-top: 1rem; color: #333;"><strong>GPA:</strong> 3.56/4</p>
        <p style="color: #333;"><strong>Coursework:</strong> Algorithm Analysis, Data Model and Query Languages, Machine Learning, Operating Systems, Deep Learning.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Jaypee Institute
    st.markdown("""
    <div class="education-item">
        <div class="school">Jaypee Institute of Information Technology</div>
        <div class="degree">Bachelor of Technology: Electronics and Communication Engineering</div>
        <div style="display: flex; justify-content: space-between; align-items: center; margin: 1rem 0;">
            <div class="dates">July 2018 - July 2022</div>
            <div class="location">Noida, India</div>
        </div>
        <p style="margin-top: 1rem; color: #333;"><strong>Coursework:</strong> Data Structures, Software Development, Telecommunication Networks, Database Management, Computer Networks.</p>
    </div>
    """, unsafe_allow_html=True)

# Technical Skills
with st.container():
    st.markdown("## TECHNICAL SKILLS")
    skills = [
        "Golang", "Python", "C++", "TypeScript", "JavaScript", "Java", "Node.js", "GraphQL", 
        "Angular", "Flask", "Django", "MongoDB", "ScyllaDB", "AWS", "GCP", "Azure", 
        "Kubernetes", "Docker", "Git", "Redis", "Elasticsearch", "Kibana", "Postman", 
        "Bitbucket", "Devtron", "Spinnaker", "Coralogix", "Grafana", "Jenkins", "DynamoDB"
    ]
    
    skill_html = ""
    for skill in skills:
        skill_html += f'<span class="skill-tag">{skill}</span>'
    
    st.markdown(f'<div style="margin-top: 1rem;">{skill_html}</div>', unsafe_allow_html=True)

# Projects
with st.container():
    st.markdown("## PROJECTS")
    
    # Collab Note
    st.markdown("""
    <div class="project-item">
        <div class="project-name">Collab Note</div>
        <p style="margin-top: 1rem; color: #333;"><strong>Technologies:</strong> Python, FastAPI, Express.js, Hugging Face Transformers, BART, Docker, AWS/GCP/Azure, REST APIs, WebSockets</p>
        <p style="color: #333;"><strong>Description:</strong> Developed a production-ready collaborative content platform by implementing real-time AI features with the Hugging Face BART model, improving content processing speed by 60%. Built a scalable microservice architecture using FastAPI and Express.js, achieving sub-3-second AI response times, and deployed intelligent content analysis, sentiment detection, and topic extraction services.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sound Scape
    st.markdown("""
    <div class="project-item">
        <div class="project-name">Sound Scape</div>
        <p style="margin-top: 1rem; color: #333;"><strong>Technologies:</strong> Python, PySpark, MLlib, Scikit-learn, Librosa, AWS EMR, S3, Docker</p>
        <p style="color: #333;"><strong>Description:</strong> Designed and deployed a PySpark-based machine learning pipeline for large-scale music analytics, applying supervised and unsupervised models for trend detection and genre classification with 92% accuracy. Optimized distributed feature extraction and model training pipelines to process 10M+ audio tracks (20+ TB) three times faster than the baseline, enabling rapid insights from massive datasets.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # MediSearch
    st.markdown("""
    <div class="project-item">
        <div class="project-name">MediSearch</div>
        <p style="margin-top: 1rem; color: #333;"><strong>Technologies:</strong> Python, Streamlit, FAISS, LangChain, Hugging Face, Transformers</p>
        <p style="color: #333;"><strong>Description:</strong> Built an AI-driven RAG assistant to extract and summarize insights from medical research papers and clinical guidelines using LangChain and FAISS for vector retrieval. Integrated biomedical Hugging Face embeddings and a fine-tuned transformer to deliver context-aware, domain-specific responses in real time via Streamlit, supporting evidence-based medical decision-making.</p>
    </div>
    """, unsafe_allow_html=True)

# QR Code Section
with st.container():
    st.markdown("---")
    st.markdown("## 📱 Scan to Share This Resume")
    
    # Get the current Streamlit URL
    current_url = st.experimental_get_query_params()
    
    # Create QR code
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(st.experimental_get_query_params().get('url', [''])[0] or "https://your-streamlit-app-url.streamlit.app")
    qr.make(fit=True)
    
    # Create QR code image
    qr_image = qr.make_image(fill_color="#667eea", back_color="white")
    
    # Convert to bytes for display
    img_buffer = io.BytesIO()
    qr_image.save(img_buffer, format='PNG')
    img_buffer.seek(0)
    
    # Display QR code
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(img_buffer, width=300, caption="Scan this QR code to share the resume")
        
        # Download button for QR code
        st.download_button(
            label="📥 Download QR Code",
            data=img_buffer.getvalue(),
            file_name="hazel_mahajan_resume_qr.png",
            mime="image/png"
        )

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 1rem;">
    <p>© 2025 Hazel Mahajan - Software Engineer</p>
    <p>Built with ❤️ using Streamlit</p>
</div>
""", unsafe_allow_html=True) 