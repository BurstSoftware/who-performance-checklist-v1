import streamlit as st

def main():
    st.title("WHO Performance Evaluation Checklist")
    st.markdown("""
    ### Evaluate the World Health Organization's (WHO) performance
    Use this checklist to grade the WHO's role in vaccine/medicine effectiveness and outbreak management based on epidemic kinetics.
    """)

    st.sidebar.header("Evaluation Criteria")
    st.sidebar.markdown("""
    - **Power-law behavior**: Consider whether outbreak models reflected transitions from exponential growth to power-law behavior.
    - **Mixed-kinetics model**: Evaluate if the WHO incorporated non-first-order kinetics in their analysis.
    - **Reaction order**: Assess flexibility in modeling transmission dynamics using reaction orders (e.g., \([S][I]^p\)).
    - **Stages of spread**: Review their identification and response to different outbreak stages.
    - **Network effects**: Grade how well the WHO accounted for disease propagation through networks.
    - **Transmission rate constant**: Analyze their estimation of transmission rates and heterogeneity.
    """)

    st.subheader("Key Evaluation Criteria")
    power_law = st.slider("Power-law Behavior: How effectively did the WHO model power-law transitions?", 0, 10, 5)
    mixed_kinetics = st.slider("Mixed-Kinetics Model: How well were non-first-order kinetics incorporated?", 0, 10, 5)
    reaction_order = st.slider("Reaction Order: How effectively did WHO use flexible reaction order models?", 0, 10, 5)
    stages_spread = st.slider("Stages of Spread: How well did WHO respond to outbreak stages?", 0, 10, 5)
    network_effects = st.slider("Network Effects: How effectively did WHO account for network dynamics?", 0, 10, 5)
    transmission_rate = st.slider("Transmission Rate Constant: How accurately did WHO estimate transmission rates?", 0, 10, 5)

    st.subheader("Factors Influencing Outbreak Kinetics")
    social_heterogeneity = st.slider("Social Heterogeneity: How well did WHO integrate social dynamics?", 0, 10, 5)
    spatial_heterogeneity = st.slider("Spatial Heterogeneity: How effectively did WHO address varying susceptibilities?", 0, 10, 5)

    st.subheader("Overall Assessment")
    overall_score = (power_law + mixed_kinetics + reaction_order + stages_spread + \
                     network_effects + transmission_rate + social_heterogeneity + spatial_heterogeneity) / 8

    st.metric(label="Overall WHO Performance Score", value=f"{overall_score:.1f}/10")

    st.text_area("Additional Comments", "")

    if st.button("Submit Evaluation"):
        st.success("Thank you for your evaluation! Your feedback has been recorded.")

if __name__ == "__main__":
    main()
