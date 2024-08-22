import streamlit as st

def about_page():
    st.title("About the Farmers Market Recommendation System")

    st.image('images/about_us.svg', use_column_width=True)
    
    st.markdown("""
    ## Our Mission
    Our mission is to connect local farmers with consumers looking for fresh, locally grown produce. We believe in supporting local communities and promoting sustainable agriculture practices.

    ## What We Do
    The Farmers Market Recommendation System helps users find the best farmers markets based on their location and preferences. Whether you're looking for organic produce, handmade goods, or specific market times, our app provides personalized recommendations to meet your needs.

    ## Features
    - **Location-Based Search**: Find farmers markets near you.
    - **Personalized Recommendations**: Get suggestions based on your preferences for produce and other goods.
    - **Detailed Market Information**: View market locations, opening hours, available products, and more.
    - **Support Local Farmers**: Learn about the farmers in your area and what they offer.

    ## Our Team
    We are a passionate group of individuals dedicated to promoting local agriculture and making fresh, healthy food accessible to everyone. Our team consists of developers, designers, and local food enthusiasts working together to build this platform.

    ## Contact Us
    Have questions or feedback? We'd love to hear from you! Contact us at support@farmersmarketapp.com.

    Follow us on social media to stay updated:
    - [Facebook](https://facebook.com/farmersmarketapp)
    - [Twitter](https://twitter.com/farmersmarketapp)
    - [Instagram](https://instagram.com/farmersmarketapp)
    """)


if __name__ == '__main__':
    about_page()
