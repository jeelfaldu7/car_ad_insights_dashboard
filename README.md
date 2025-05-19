# 🚗 Car Sales Dashboard
A web application for exploring and visualizing car sales advertisement data using Streamlit, and Plotly. This project demonstrates basic data analysis and interactive dashboard development, and is deployed on Render for public access. 

## 📜 Table of Contents
  - Project Description
  - Features
  - Tech Stack
  - Steps to deploy the application to Render
  - Link to the application
  - Getting Started
  - Demo
  - Credits

## 🧾 Project Description
This project is a simple data dashboard built to explore used car advertisement listings. Users can interact with the data via filters, histograms, and scatterplots. The project is intended as a foundational excercise in combining data science and software engineering practices through full-cycle app deployment. 

## ✨ Features
- 📈 Interactive histograms and scatter plots using Plotly
- ✅ Checkbox filters that allow dynamic updates of visualizations
- 🔍 Basic exploratory data analysis included
- 🚀 Deployed on Render, publicly accessible
- 🧠 Built with Streamlit for real-time data interaction

## ⚙️ Tech Stack
  - Python
  - Streamlit
  - Plotly Express
  - Pandas
  - Scipy
  - Render for deployment 
  - GitHub for version control

## 🖼 Steps to deploy the application to Render:
- Create two new files: `requirements.txt` and `.streamlit/config.toml`.
- After creating those files in the project folder's root level, add the project's required packages.
  ```bash
  pandas==2.0.3
  scipy==1.11.1
  streamlit==1.25.0
  altair==5.0.1
  plotly==5.15.0
- Open your account on render.com and create a new web service as shown below:
  ![image](https://github.com/user-attachments/assets/b0f7dd85-f9b2-467f-90b5-92137a29f343)
- Create a new web service linked to your GitHyb repository as shown below:
  ![image](https://github.com/user-attachments/assets/8b058c44-9b98-48fa-9b0a-5a7e2eaa3e05)
- Configure the new Render web service. To the Build Command, add
  ```bash
  pip install streamlit & pip install -r requirements.txt
- To the Start Command, add: `streamlit run app.py` as shown below.
  ![image](https://github.com/user-attachments/assets/5f4112c0-6044-45ee-b7cf-a9e601b47ca3)
- Deploy to Render, wait for the build to succeed:
  ![image](https://github.com/user-attachments/assets/731dfe17-8d86-40d0-9f4d-7a7f3cc38680)

## 🌐 Link to the application:
Check out the live deployed version on Render here:
🔗 https://project-5-sda.onrender.com

## 🛠 Getting Started
Follow the steps below to run the project locally:
  1. Clone the repository
     ```bash
     git clone https://github.com/YOUR-USERNAME/car-sales-dashboard.git
     cd car-sales-dashboard
  2. Create and activate a virtual environment
     ```bash
     python -m venv venv
     source venv/bin/activate  # On Windows: venv\Scripts\activate
  3. Install required packages
     ```bash
     pip install -r requirements.txt
  4. Run the application
     ```bash
     streamlit run app.py

## 🚀 Demo
Check out the demo of the web application here provided by TripleTen Data Science Program: https://youtu.be/bna15Zj6jUI 

## 🤝 Credits
This project was created as part of the TripleTen Data Science program. Special thanks to:
TripleTen instructors and peers for ongoing support and feedback

## 🛡️ License
This project is licensed under the MIT License.




