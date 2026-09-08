import streamlit as st
import gspread
from google.oauth2.service_account import Credentials


# =========================
# GOOGLE SHEETS CONNECTION
# =========================

credentials = Credentials.from_service_account_info(
    st.secrets["google"],
    scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]
)

client = gspread.authorize(credentials)

sheet = client.open_by_key(
    "11D0ExcTCbSqYyk_WxrAHJHyFftrdZ_DrgWBIY04WMUM"
).sheet1


# =========================
# CBT TITLE
# =========================

st.title("GNS 101 CBT")

Name = st.text_input("Enter your name")


# =========================
# QUESTIONS
# =========================

Questions = [
    {
        "question": "Who is the President of Nigeria?",
        "options": [
            "a) Muhammadu Buhari",
            "b) Bola Tinubu",
            "c) Goodluck Jonathan",
            "d) Olusegun Obasanjo"
        ],
        "answer": "b"
    },

    {
        "question": "What is the capital of Nigeria?",
        "options": [
            "a) Lagos",
            "b) Ibadan",
            "c) Abuja",
            "d) Kano"
        ],
        "answer": "c"
    },

    {
        "question": "How many states are there in Nigeria?",
        "options": [
            "a) 30",
            "b) 36",
            "c) 37",
            "d) 40"
        ],
        "answer": "b"
    },

    {
        "question": "Which planet is known as the Red Planet?",
        "options": [
            "a) Earth",
            "b) Venus",
            "c) Mars",
            "d) Jupiter"
        ],
        "answer": "c"
    },

    {
        "question": "What is 10 + 15?",
        "options": [
            "a) 20",
            "b) 25",
            "c) 30",
            "d) 35"
        ],
        "answer": "b"
    },

    {
        "question": "Which of these is a programming language?",
        "options": [
            "a) Python",
            "b) Google",
            "c) Windows",
            "d) Facebook"
        ],
        "answer": "a"
    },

    {
        "question": "What does CPU stand for?",
        "options": [
            "a) Central Processing Unit",
            "b) Computer Personal Unit",
            "c) Central Program Utility",
            "d) Computer Processing User"
        ],
        "answer": "a"
    },

    {
        "question": "Which device is used for typing on a computer?",
        "options": [
            "a) Monitor",
            "b) Keyboard",
            "c) Printer",
            "d) Speaker"
        ],
        "answer": "b"
    },

    {
        "question": "How many days are there in a normal year?",
        "options": [
            "a) 300",
            "b) 365",
            "c) 366",
            "d) 400"
        ],
        "answer": "b"
    },

    {
        "question": "Which continent is Nigeria located in?",
        "options": [
            "a) Asia",
            "b) Europe",
            "c) Africa",
            "d) America"
        ],
        "answer": "c"
    },

    {
        "question": "What is 100 divided by 4?",
        "options": [
            "a) 20",
            "b) 25",
            "c) 30",
            "d) 40"
        ],
        "answer": "b"
    },

    {
        "question": "Which of these is an operating system?",
        "options": [
            "a) Windows",
            "b) Google",
            "c) YouTube",
            "d) Facebook"
        ],
        "answer": "a"
    },

    {
        "question": "What is the opposite of hot?",
        "options": [
            "a) Warm",
            "b) Cold",
            "c) Heat",
            "d) Fire"
        ],
        "answer": "b"
    },

    {
        "question": "Which animal is known as the king of the jungle?",
        "options": [
            "a) Tiger",
            "b) Lion",
            "c) Elephant",
            "d) Leopard"
        ],
        "answer": "b"
    },

    {
        "question": "What does RAM stand for?",
        "options": [
            "a) Random Access Memory",
            "b) Read Access Machine",
            "c) Rapid Application Memory",
            "d) Random Application Manager"
        ],
        "answer": "a"
    }
]


# =========================
# START TEST
# =========================

if Name:

    st.write(f"Welcome {Name}!")
    st.write("You are about to begin your GNS 101 test.")
    st.write("Kindly Answer all Questions using the options")
    st.write("GOOD LUCK!")

    student_answers = []

    for number, item in enumerate(Questions, 1):

        st.write(f"### {number}. {item['question']}")

        answer = st.radio(
            "Choose your answer:",
            item["options"],
            key=f"question_{number}"
        )

        student_answers.append(answer[0])


    # =========================
    # SUBMIT TEST
    # =========================

    if st.button("Submit Test"):

        score = 0

        for user_answer, item in zip(student_answers, Questions):

            if user_answer == item["answer"]:
                score += 1

        percentage = (score / len(Questions)) * 100

        if percentage >= 50:
            result = "PASSED"
        else:
            result = "FAILED"


        # =========================
        # SAVE RESULT TO GOOGLE SHEETS
        # =========================

        sheet.append_row([
            Name,
            f"{score}/{len(Questions)}",
            f"{percentage:.0f}%",
            result
        ])


        # =========================
        # DISPLAY RESULT
        # =========================

        st.write("## FINAL RESULT")

        st.write(f"Student: {Name}")
        st.write(f"Total: {score}/{len(Questions)}")
        st.write(f"Percentage: {percentage:.0f}%")

        if result == "PASSED":
            st.success("PASSED 🎉")
        else:
            st.error("FAILED ❌")

        st.success("Your result has been recorded successfully! ✅")
