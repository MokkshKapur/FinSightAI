import streamlit as st

def main():

    st.title("💼 AI Financial Advisor")
    st.write("Fill in your profile to get personalized investment advice.")

    # User Input Form
    with st.form("advisor_form"):
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        age = st.slider("Age", 18, 100, 30)
        avenues = st.multiselect(
            "Investment Avenues Interested In",
            ["Mutual Funds", "Equity Market", "Debentures", "Government Bonds", "Fixed Deposits", "PPF", "Gold"]
        )
        objective = st.text_input("Investment Objectives")
        purpose = st.text_input("Investment Purpose")
        duration = st.selectbox("Investment Duration", ["<1 year", "1-3 years", "3-5 years", "5+ years"])
        expect = st.text_input("Expected Returns (%)")
        savings_goal = st.text_input("Savings Objectives")
        source = st.selectbox("How did you hear about investing?", ["Friends", "Online", "Advisor", "Other"])

        submitted = st.form_submit_button("Get Advice")

    if submitted:
        profile = f"""
        Gender: {gender}
        Age: {age}
        Interested In: {', '.join(avenues)}
        Objective: {objective}
        Purpose: {purpose}
        Duration: {duration}
        Expected Return: {expect}%
        Savings Goal: {savings_goal}
        Source: {source}
        """

        st.subheader("🧠 Suggested Strategy")
        # placeholder response (replace with model later)
        st.success(f"Based on your inputs, consider diversifying across: {', '.join(avenues)}.\n\n""A long-term goal might suit equity or mutual funds. For shorter horizons, fixed deposits or gold may help.")
