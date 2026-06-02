# Restaurant Recommendation System Dashboard

This project is an intelligent recommendation engine built with **Streamlit**. It leverages your dataset to provide personalized dining suggestions based on user preferences, such as preferred cuisines, price range, and minimum rating requirements.

---

## 🚀 Key Features

* **Smart Filtering:** Narrow down thousands of restaurants instantly using criteria like cuisine type, budget (price range), and service quality (rating).
* **Top-Rated Suggestions:** Easily identify the highest-rated restaurants in your chosen category.
* **Interactive UI:** A clean, sidebar-driven interface that allows for quick adjustments to your search preferences.
* **Dynamic Results:** View a curated list of restaurant recommendations that meet all your specified constraints.

---

## 🛠️ Prerequisites

To run this system, ensure you have the required libraries installed:

```bash
pip install streamlit pandas

```

---

## 📋 Data Requirements

The recommendation engine performs best with a `Dataset.csv` containing these columns:

* `Restaurant Name`
* `Cuisines`: (Supports comma-separated values)
* `Aggregate rating`: (0.0 to 5.0)
* `Price range`: (1 to 4)
* `City`

---

## 🏃‍♂️ How to Run

1. **Save** your script (e.g., `recommend.py`).
2. **Open** your terminal/command prompt.
3. **Execute** the application:

```bash
streamlit run recommend.py

```

4. **Explore:** Upload your dataset and use the sidebar sliders and dropdowns to generate your personalized list of restaurant recommendations.

---

## 💡 How It Works

The recommendation system follows a **Content-Based Filtering** approach:

1. **Input Parsing:** The system cleans and normalizes the `Cuisines` column to ensure multi-cuisine restaurants are searchable by any of their specific tags.
2. **User Constraints:** It applies real-time Boolean indexing on the DataFrame based on the thresholds you set in the sidebar.
3. **Ranking:** Results are automatically sorted by `Aggregate rating` in descending order, ensuring the "best" options appear first.
4. **Feedback Loop:** If no restaurants meet all your criteria, the system provides helpful feedback to adjust your filters.

