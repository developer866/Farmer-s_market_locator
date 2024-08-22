import streamlit as st

def home_page():
    st.title("Welcome to the Farmers Market Recommendation System")
    
    # Hero Section
    # st.image('farmer.jpeg', use_column_width=True)
    
    st.markdown("""
    <style>
    .hero {
        text-align: center;
        padding: 50px 20px;
    }
    .features {
        display: flex;
        flex-wrap: wrap;
        justify-content: space-around;
    }
    .feature {
        flex: 1;
        min-width: 200px;
        max-width: 300px;
        padding: 20px;
        text-align: center;
    }
    .feature img {
        width: 100px;
        height: 100px;
    }
    </style>
    <div class="hero">
        <h1>Discover Local Farmers Markets Near You</h1>
        <p>Find fresh produce, handmade goods, and more from local farmers and artisans.</p>
    </div>
    <div class="features">
        <div class="feature">
            <img src="https://cdn-icons-png.flaticon.com/512/1090/1090649.png" alt="Location">
            <h3>Find Markets</h3>
            <p>Locate farmers markets based on your location.</p>
        </div>
        <div class="feature">
            <img src="https://cdn-icons-png.flaticon.com/512/1150/1150751.png" alt="Preferences">
            <h3>Personalized Preferences</h3>
            <p>Get recommendations tailored to your preferences.</p>
        </div>
        <div class="feature">
            <img src="https://cdn-icons-png.flaticon.com/512/3198/3198208.png" alt="Fresh Produce">
            <h3>Fresh Produce</h3>
            <p>Find fresh, locally grown fruits and vegetables.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    ### How It Works
    1. **Register**: Sign up as a user or a farmer.
    2. **Login**: Access your personalized dashboard.
    3. **Get Recommendations**: Enter your location and preferences to get the best market recommendations.
    
    ### Why Choose Us?
    - **Freshness Guaranteed**: Connect directly with local farmers for the freshest produce.
    - **Support Local**: Help support local farmers and the community.
    - **Convenience**: Easily find markets that suit your schedule and preferences.
    
    ### Testimonials
    > "This app helped me find the best farmers market in my area. The produce is always fresh, and I love supporting local farmers." - Jane Doe
    
    > "As a farmer, this app has helped me reach more customers and grow my business." - John Smith
    """)

if __name__ == '__main__':
    home_page()
