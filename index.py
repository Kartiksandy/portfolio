import streamlit as st

# Set up the page configuration
st.set_page_config(page_title="Kartik Chopra Portfolio", page_icon="👨‍💻", layout="centered")

# Sidebar navigation
st.sidebar.title("Navigate")
menu = st.sidebar.radio(
    "Sections",
    ["Home", "Work Experience", "Projects & Accomplishments", "Education & Certifications", "Volunteering & Leadership"]
)

# Home Section
if menu == "Home":
    st.image("pic.jpg", width=150)
    st.title("Kartik Chopra")
    st.markdown(
        """
        **Go-Getter, People Person, Co-founder of Vibin, Data Enthusiast, Driving to become a product manager**

        👉 [kartik.chopra8@gmail.com](mailto:kartik.chopra8@gmail.com) · Barrie, Ontario · +1 437-333-0409
        """
    )
    st.subheader("Social Links")
    st.markdown(
        """
        - [Twitter](https://twitter.com/kartikchopra8)
        - [LinkedIn](https://www.linkedin.com/in/kartik-chopra-a26ab6165/)
        - [GitHub](https://github.com/kartikchopra1)
        - [Download Resume](https://drive.google.com/file/d/1x42n8cGxC3UOJ-yvHvqEkUERZK86UXe6/view?usp=sharing)
        """
    )

# Work Experience Section
elif menu == "Work Experience":
    st.title("Work Experience")
    st.subheader("🚧 Night Auditor | Monte Carlo INN")
    st.write("01/2024 – Present")
    st.markdown(
        """
        - Directed front desk operations for a 100-room hotel, enhancing guest satisfaction, reducing discrepancies, and boosting annual profits by 15% through strategic promotions.
        - Performed end-of-day accounting and bookkeeping tasks handling $25,000+ daily transactions.
        """
    )
    st.subheader("🚧 Product Owner | Shor in City Pvt. Ltd. (Vibin)")
    st.write("07/2023 – Present")
    st.markdown(
        """
        - Developed a music sharing app with a team of 7, recognized by the Indian government's DPITT.
        - Reduced development time by 50% through innovative product design and development strategies.
        - Generated a viral social media campaign with 1 million views and organized 4 major college events.
        """
    )
    st.subheader("🚧 Associate Product Specialist | Edifecs Pvt. Ltd.")
    st.write("12/2022 - 02/2023")
    st.markdown(
        """
        - Executed US Healthcare EDI transactions, improving compliance and efficiency while managing over 1,000,000 records daily.
        - Resolved 100+ monthly tickets and managed 7 customer distributed environments.
        - Reengineered an outdated product for 100,000+ users, achieving 90% efficiency and earning awards.
        """
    )

# Projects & Accomplishments Section
elif menu == "Projects & Accomplishments":
    st.title("Projects & Accomplishments")
    st.subheader("🏆 Built my first startup | [Vibin](https://www.vibin.in)")
    st.subheader("🏆 Capstone Project | [Professional Data Analytics Certification](https://www.kaggle.com/code/kartikchopra01/capstone-project-cyclist-case-study)")
    st.subheader("🏆 Real-Time Vehicle Monitoring via Data Pipeline")
    st.markdown(
        """
        - Created a real-time data pipeline for IoT devices, providing insights and alerts using AWS, Kafka, Spark, and Docker.
        """
    )
    st.subheader("🏆 Cost-Effective Data Lakehouse")
    st.markdown(
        """
        - Built a Data Lakehouse with Kafka, MinIO, and Spark, leveraging AWS services to build a cost-effective data lakehouse.
        """
    )
    st.subheader("🏆 AI-Powered JetBot Utilizing OpenCV")
    st.markdown(
        """
        - Assembled Jetson Nano with OpenCV, trained neural networks, and performed real-time object detection and movement.
        """
    )
    st.subheader("🏆 Awarded Star and Spot Award of the Year")
    st.subheader("🏆 Freelancing: Supreme Records' EDM Fest")
    st.markdown(
        """
        - Contributed to event organization and promotional activities, making the event a success.
        """
    )
    st.subheader("🏆 Marketing Head: Technical & Cultural Fest")
    st.markdown(
        """
        - Secured $10,000 in sponsorships, engaging 20 new colleges and enhancing the event's reach.
        """
    )

# Education & Certifications Section
elif menu == "Education & Certifications":
    st.title("Education & Certifications")
    st.subheader("Post-Secondary Diploma in AI | Georgian College")
    st.write("01/2024 – 12/2024")
    st.markdown("Courses: AI Infrastructure and Architecture, ML Programming, Neural Networks")

    st.subheader("Post-Secondary Diploma in Big Data Analytics | Georgian College")
    st.write("05/2023 – 12/2023")
    st.markdown("Courses: Data System Architecture, Mathematics for Data Analytics, Data Visualization, Cloud Data Engineering")

    st.subheader("B.E. Computer Science Engineering | Chitkara University")
    st.write("01/2020 - 11/2022")
    st.markdown("Coursework: Computer Networking, Client-Side Technologies, Database Management System, Operating System, Software Engineering, Full Stack Development")

    st.subheader("Taiwan Summer School: Intro to AI | Providence University")
    st.write("06/2019 - 06/2019")

# Volunteering & Leadership Section
elif menu == "Volunteering & Leadership":
    st.title("Volunteering & Leadership")
    st.subheader("Student Ambassador | Georgian College")
    st.write("05/2024 - 06/2024")
    st.markdown(
        """
        - Guided 20+ students daily for smooth registration and ONECard distribution, resolving 95% of inquiries on first contact.
        """
    )
    st.subheader("Volunteer | Aashman Foundation")
    st.markdown(
        """
        - Organized fundraising activities, installed donation boxes, and recruited interns, leading to a significant increase in funds raised.
        - Developed investor pitch decks and business plans, securing project funding.
        """
    )
