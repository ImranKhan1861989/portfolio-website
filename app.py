#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st

# Set page configuration
st.set_page_config(page_title="Imran's Portfolio", page_icon=":briefcase:", layout="centered")

# Sidebar content
st.sidebar.title("Imran's Portfolio")
st.sidebar.image("PXL_20240331_162010550", use_column_width=True)  # Add your profile picture here
st.sidebar.markdown("""
Hi, I'm Imran! I'm a scientist specializing in immunology and molecular biology, with extensive experience in implant-induced autoimmune diseases, histochemistry, microscopy, and image acquisition. My career has been focused on achieving significant reductions in project timelines and enhancing diagnostic accuracy and patient outcomes.
In addition to my scientific expertise, I have a strong passion for integrating science with business and consulting. I have a proven track record in technical and grant writing, content strategy, and biomedical process optimization, where I have successfully reduced failure rates by 70% and ensured FDA compliance. My efforts have contributed to the launch of three error-free medical devices and a 35% growth in sales.
I have also worked extensively on CAR-T cell therapy clinical applications across diverse medical specialties, developing effective KOL relationships, and communicating complex medical concepts through impactful narratives. My experience includes roles as a Clinical Researcher, Senior Medical Writer, and Medical Science Communicator, where I have driven significant outcomes through strategic engagement and regulatory expertise.
Currently, I am exploring opportunities to further leverage my skills as a Scientits and also business consulting capacity, focusing on the intersection of science, technology, and business to drive innovation and improve healthcare outcomes.
""")
st.sidebar.markdown("### Connect with me")
st.sidebar.write("[LinkedIn](https://www.linkedin.com/in/your-linkedin-profile)")
st.sidebar.write("[GitHub](https://github.com/ImranKhan1861989)")
st.sidebar.write("[Email](mailto:emraan.9.4@gmail.com)")

# Main content
st.title("Step into a world where science meets innovation. Here, you'll discover my journey as a scientist specializing in immunology and molecular biology, driven by a passion for integrating groundbreaking research with strategic business insights. Explore my accomplishments, delve into my diverse projects, and witness how my expertise in biomedical process optimization and clinical research is shaping the future of healthcare. Let's embark on this exciting adventure together, where every discovery paves the way for transformative solutions.")
st.image("cover_photo.jpg", use_column_width=True)  # Add a cover photo here

# Introduction
st.header("About Me")
st.markdown("""
I am a dedicated scientist with a robust background in immunology and molecular biology. My experience spans across various research projects, focusing on implant-induced autoimmune diseases, histochemistry, microscopy, and image acquisition. I'm also skilled in technical writing, grant writing, business consulting, and process optimization.
""")

# Projects
st.header("Projects")

st.subheader("Project 1: Point-of-Care LFA for Breast Implant Illness (BII)")
st.markdown("""
**Description:** Developed a point-of-care lateral flow assay (LFA) to detect oxylipins as biomarkers for diseases associated with lipid metabolism, focusing on breast implant illness (BII).
**Role:** Lead Researcher
**Outcome:** Intended to establish a gold standard for future diagnostics in this area.
""")

st.subheader("Project 2: Adipose Tissue Metabolism in Implant-Related Illness")
st.markdown("""
**Description:** Investigated adipose tissue metabolism in the context of implant-related illnesses.
**Role:** Scientist
**Outcome:** Advanced understanding of metabolic implications and potential diagnostic pathways.
""")

st.subheader("Project 3: Immune Cell Response in Breast Implant Illness (BII)")
st.markdown("""
**Description:** Studied the role of T cells in the immune response associated with breast implant illness (BII).
**Role:** Lead Researcher
**Outcome:** Insights into immune mechanisms contributing to BII pathology.
""")

st.subheader("Project 4: Alcoholic Liver Disease Diagnostics")
st.markdown("""
**Description:** Collaborated on diagnostics for alcoholic liver disease.
**Role:** Scientist
**Outcome:** Significant advancements in diagnostic accuracy and patient outcomes.
""")

st.subheader("Project 5: Bioplastic Revolution")
st.markdown("""
**Description:** Collaborated globally on research initiatives aimed at developing bioplastics to combat plastic pollution.
**Role:** Scientist
**Outcome:** Innovations in bioplastic materials contributing to environmental sustainability.
""")

st.subheader("Project 6: AI Quality Control in Bioplastic Manufacturing")
st.markdown("""
**Description:** Led a global collaboration to develop AI-driven quality control systems for bioplastic manufacturing, integrating machine learning models to enhance material consistency and performance.
**Role:** Lead Data Scientist
**Skills:** Python, R, Streamlit, Joblib
**Outcome:** Implemented AI algorithms to optimize production processes, ensuring bioplastic quality meets stringent environmental standards. Published the project on [GitHub](https://github.com/ImranKhan1861989) for transparency and collaboration.
""")

# Additional Information about AI Quality Control
st.header("AI Quality Control in Healthcare and Beyond")
st.markdown("""
In today's technology-driven world, AI plays a crucial role in ensuring quality and consistency across various industries, including healthcare and environmental sciences. AI-driven quality control systems leverage advanced algorithms to analyze large datasets, detect anomalies, and predict outcomes with high accuracy. In biomedical research, AI enhances diagnostic precision, accelerates drug discovery processes, and optimizes treatment protocols. For bioplastics, AI ensures material uniformity and performance reliability, contributing to sustainable solutions for global challenges like plastic pollution.
""")

st.header("Skills")

st.markdown("""
- **Immunology & Molecular Biology:** Proficient in studying immune responses at the molecular level, including cell signaling pathways, cytokine interactions, and genetic predispositions to immune-related diseases.

- **Histochemistry & Microscopy:** Skilled in using histochemical techniques to visualize cellular structures and interactions, combined with expertise in various microscopy methods for detailed examination and analysis.

- **Technical & Grant Writing:** Experienced in writing technical reports, research papers, and grant proposals that adhere to scientific standards and effectively communicate complex ideas to diverse audiences.

- **Business & Brand Consulting:** Knowledgeable in providing strategic advice to businesses and brands, focusing on market positioning, customer engagement, and growth strategies tailored to the healthcare and biomedical sectors.

- **Biomedical Process Optimization:** Specialized in optimizing biomedical processes to enhance efficiency, reduce costs, and ensure compliance with regulatory standards, thereby improving overall operational effectiveness.

- **Regulatory Compliance & Risk Management:** Skilled in navigating regulatory requirements and implementing risk management strategies in biomedical settings to ensure product safety, quality, and legal compliance.

- **Clinical Process Improvement:** Experienced in identifying inefficiencies in clinical workflows and implementing solutions that streamline processes, improve patient outcomes, and enhance overall clinical performance.

- **Medical Device Development:** Proficient in all stages of medical device development, from conceptualization and design to testing, regulatory approval, and market launch, with a focus on innovation and patient safety.
""")

st.header("Wet Lab Skills")

st.markdown("""
### Immunology and Cell Biology
- **Cell Culture Techniques:** Includes cell line maintenance, primary cell isolation, and culture.
- **Multi Color Flow Cytometry:** Analyzes and sorts cells based on surface markers.
- **Mass Cytometry:** Analyzes and sorts cells based on surface markers using CyTOF.
- **ELISA (Enzyme-Linked Immunosorbent Assay):** Quantifies proteins and antibodies in samples.
- **Western Blotting:** Detects specific proteins in complex mixtures.
- **Immunohistochemistry (IHC) and Immunofluorescence (IF):** Visualizes protein expression and localization in tissues or cells.
- **PCR (Polymerase Chain Reaction):** Amplifies DNA or RNA sequences for analysis.
- **Cellular Assays:** Includes proliferation assays, apoptosis assays, and cytokine release assays.

### Adipose Tissue Biology
- **Lipid Extraction:** Isolates lipids from adipose tissue for analysis.
- **Adipocyte Differentiation Assays:** Studies differentiation of precursor cells into adipocytes.
- **Metabolic Assays:** Measures metabolic activities in adipose tissue.

### Bioplastics
- **Biopolymer Synthesis:** Develops biopolymers from renewable sources.
- **Biodegradation Assays:** Evaluates degradation rates of bioplastics.
- **Material Characterization:** Analyzes physical and chemical properties of bioplastic materials.

### Genomics
- **DNA/RNA Extraction:** Isolates nucleic acids from cells or tissues.
- **Next-Generation Sequencing (NGS):** Conducts high-throughput sequencing for genomic analysis.
- **Genome Editing Techniques:** Includes CRISPR/Cas9 for modifying DNA sequences.

### Molecular Biology
- **Protein Expression and Purification:** Produces and isolates recombinant proteins.
- **Cloning Techniques:** Inserts DNA fragments into vectors for replication or expression.
- **Gene Expression Analysis:** Studies mRNA levels using techniques like qRT-PCR.
- **Biochemical Assays:** Measures enzymatic activities or protein interactions.
""")



# Contact Information
st.header("Contact Information")
st.markdown("""
Feel free to reach out to me through any of the following platforms:
- **Email:** emraan.9.4@gmail.com
- **LinkedIn:** [Your LinkedIn Profile](https://www.linkedin.com/in/your-linkedin-profile)
- **GitHub:** [Your GitHub Profile](https://github.com/ImranKhan1861989)
""")

# Footer
st.markdown("---")
st.markdown("© 2024 Imran Khan Mohammed")

