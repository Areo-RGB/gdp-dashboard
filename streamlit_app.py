import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def main():
    # Set page title
    st.title("Random Bar Chart Generator")
    
    # Add description
    st.write("This app displays a bar chart with 10 random values.")
    
    # Sidebar controls
    st.sidebar.header("Chart Controls")
    seed = st.sidebar.number_input("Random Seed", min_value=1, max_value=1000, value=42)
    min_value = st.sidebar.number_input("Minimum Value", min_value=1, max_value=50, value=1)
    max_value = st.sidebar.number_input("Maximum Value", min_value=51, max_value=200, value=100)
    
    # Color selection
    color_options = ['skyblue', 'salmon', 'lightgreen', 'violet', 'gold']
    selected_color = st.sidebar.selectbox("Bar Color", color_options)
    
    # Generate button
    if st.sidebar.button("Generate New Chart"):
        # This will trigger a rerun with the current settings
        st.experimental_rerun()
    
    # Set random seed for reproducibility
    np.random.seed(seed)
    
    # Generate 10 random values
    values = np.random.randint(min_value, max_value, 10)
    
    # Create categories
    categories = [f'Item {i+1}' for i in range(10)]
    
    # Create DataFrame for the data
    df = pd.DataFrame({
        'Category': categories,
        'Value': values
    })
    
    # Display the raw data as a table
    if st.checkbox("Show Raw Data"):
        st.write(df)
    
    # Create the bar chart with matplotlib
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(categories, values, color=selected_color)
    
    # Add title and labels
    ax.set_title('Bar Chart with 10 Random Entries', fontsize=16)
    ax.set_xlabel('Categories', fontsize=12)
    ax.set_ylabel('Values', fontsize=12)
    
    # Add the values on top of each bar
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 1,
                f'{height}', ha='center', va='bottom')
    
    # Add grid lines for better readability
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)
    
    # Adjust layout
    plt.tight_layout()
    
    # Display the plot in Streamlit
    st.pyplot(fig)
    
    # Add download option for CSV
    csv = df.to_csv(index=False)
    st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name="random_bar_data.csv",
        mime="text/csv"
    )
    
    # GitHub info
    st.markdown("---")
    st.write("Code available on [GitHub](https://github.com/yourusername/streamlit-random-bar-chart)")

if __name__ == "__main__":
    main()
