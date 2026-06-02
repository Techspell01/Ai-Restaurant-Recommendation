import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


st.set_page_config(page_title="Restaurant Recommender", page_icon="🍔", layout="wide")


st.title("🍔 Restaurant Recommendation System")
st.markdown("""
Welcome to the Content-Based Recommendation Engine! 
Tell us what you want to eat and your budget, and the AI will find the best restaurants tailored specifically to your tastes. 
""")

st.sidebar.header("1. Upload Dataset")
uploaded_file = st.sidebar.file_uploader("Upload your 'Dataset.csv' file", type=["csv"])

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)
    
    with st.spinner("Processing data..."):
    
        df['Cuisines'] = df['Cuisines'].fillna('Unknown')
        df['Aggregate rating'] = df['Aggregate rating'].fillna(0)
        df['Price range'] = df['Price range'].fillna(1)

        all_cuisines = set()
        for cuisine_list in df['Cuisines'].str.split(','):
            for cuisine in cuisine_list:
                all_cuisines.add(cuisine.strip())
        all_cuisines = sorted(list(all_cuisines))
        

        df['Content_Tags'] = df['Cuisines'] + " PriceLevel" + df['Price range'].astype(str)


    st.write("### 🎯 What are you craving today?")
    
    col1, col2 = st.columns(2)
    with col1:
        preferred_cuisine = st.selectbox("Select your preferred Cuisine:", all_cuisines)
    with col2:
        preferred_price = st.selectbox("Select your Price Range (1 = Cheap, 4 = Expensive):", [1, 2, 3, 4])
        
    if st.button("🔍 Find My Restaurants", type="primary"):

        user_profile = f"{preferred_cuisine} PriceLevel{preferred_price}"

        content_list = df['Content_Tags'].tolist()
        content_list.append(user_profile)

        tfidf = TfidfVectorizer(stop_words='english')
        tfidf_matrix = tfidf.fit_transform(content_list)
        
        cosine_sim = linear_kernel(tfidf_matrix[-1], tfidf_matrix[:-1]).flatten()
    
        df['Similarity_Score'] = cosine_sim
        
        recommended_df = df[df['Similarity_Score'] > 0].sort_values(
            by=['Similarity_Score', 'Aggregate rating'], 
            ascending=[False, False]
        )
        st.write("---")
        if not recommended_df.empty:
            st.success(f" We found {len(recommended_df)} restaurants matching your criteria! Here are the best ones:")
            
            display_columns = ['Restaurant Name', 'Cuisines', 'Price range', 'Aggregate rating', 'City', 'Average Cost for two']

            st.dataframe(recommended_df[display_columns].head(10), use_container_width=True)
            
            st.write("*(Note: Restaurants are ranked mathematically based on how closely they match your preferred cuisine and price, broken by their aggregate rating!)*")
        else:
            st.warning("😕 We couldn't find any restaurants that perfectly match both that cuisine and price range. Try adjusting your preferences!")

else:
    st.info("👈 Please upload your 'Dataset.csv' file in the sidebar to begin.")

    st.write("### Waiting for data...")
    st.write("Once uploaded, you will be able to filter restaurants by **Cuisine** and **Price Range** using advanced Machine Learning text-similarity algorithms.")