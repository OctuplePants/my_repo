import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np  # For standard deviation calculation
from PIL import Image  # Import the Python Imaging Library (PIL) to handle images

# Set up the background image for the top section
def add_partial_background_image(image_url):
    partial_background_css = f"""
    <style>
    .top-section {{
        height: 25vh; /* Set height to 1/4 of the viewport */
        background: url("{image_url}");
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center;
    }}
    </style>
    <div class="top-section"></div>
    """
    st.markdown(partial_background_css, unsafe_allow_html=True)

# Add your image URL here (can also be a local file served as a URL)
image_url = "https://globalprograms.unm.edu/assets/img/peng-logo-wide.png"  # Provided image URL
add_partial_background_image(image_url)

# Title directly under the image
st.markdown("""
    <h1 style='text-align: center;'>ENG-220 Group 7<br>Air Quality<br>Visualization Dashboard</h1>
""", unsafe_allow_html=True)

# Create a tab navigation bar
tab_selection = st.radio("Select Tab", ["Home", "About the Data"])

# Content for "Home" tab
if tab_selection == "Home":
    st.write("### Upload and Visualize Data")
    
    # File uploader for CSV
    uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

    if uploaded_file is not None:
        # Read the CSV file
        data = pd.read_csv(uploaded_file)
        st.write("### Data Preview")
        st.dataframe(data)

        # Get total number of rows and columns
        total_rows, total_columns = data.shape

        # Inputs for start and end rows
        st.write("### Select Row Range for Analysis")
        start_row = st.number_input(
            "Start Row (0-indexed)", min_value=0, max_value=total_rows - 1, value=0, step=1
        )
        end_row = st.number_input(
            "End Row (0-indexed, inclusive)", min_value=start_row, max_value=total_rows - 1, value=total_rows - 1, step=1
        )

        # Filter the data for the selected row range
        filtered_data = data.iloc[start_row : end_row + 1]
        st.write("### Filtered Data Preview (Rows)")
        st.dataframe(filtered_data)

        # Multiselect for column filtering
        st.write("### Select Columns for Analysis")
        selected_columns = st.multiselect(
            "Select Columns",
            options=data.columns.tolist(),
            default=data.columns.tolist()  # Default to all columns
        )

        # Filter the data for selected columns
        filtered_data = filtered_data[selected_columns]
        st.write("### Filtered Data Preview (Rows & Columns)")
        st.dataframe(filtered_data)

        # Standard Deviation Calculator
        st.write("### Standard Deviation Calculator")
        std_column = st.selectbox("Select Column for Standard Deviation", selected_columns)
        if st.button("Calculate Standard Deviation"):
            try:
                std_values = filtered_data[std_column].astype(float)
                std_result = np.std(std_values, ddof=1)  # Using sample standard deviation
                st.success(f"The standard deviation of '{std_column}' is: {std_result}")
            except ValueError:
                st.error(f"Selected column '{std_column}' contains non-numeric data. Please select a numeric column.")

        # Dropdown for selecting columns for plotting
        x_column = st.selectbox("Select X-axis column", selected_columns)
        y_column = st.selectbox("Select Y-axis column", selected_columns)

        # Dropdown for graph type
        graph_type = st.selectbox(
            "Select Graph Type",
            ["Line", "Scatter", "Bar", "Pie"]
        )

        # Plot button
        if st.button("Plot Graph"):
            fig, ax = plt.subplots()

            if graph_type == "Line":
                ax.plot(filtered_data[x_column], filtered_data[y_column], marker='o')
                ax.set_title(f"{y_column} vs {x_column} (Line Plot)")

            elif graph_type == "Scatter":
                ax.scatter(filtered_data[x_column], filtered_data[y_column])
                ax.set_title(f"{y_column} vs {x_column} (Scatter Plot)")

            elif graph_type == "Bar":
                ax.bar(filtered_data[x_column], filtered_data[y_column])
                ax.set_title(f"{y_column} vs {x_column} (Bar Chart)")

            elif graph_type == "Pie":
                # Pie chart only makes sense for single-column data
                if len(filtered_data[x_column].unique()) <= 10:  # Limit to 10 unique categories for readability
                    plt.pie(
                        filtered_data[y_column],
                        labels=filtered_data[x_column],
                        autopct='%1.1f%%',
                        startangle=90,
                    )
                    plt.title(f"{y_column} (Pie Chart)")
                else:
                    st.error("Pie chart requires fewer unique categories in the X-axis.")

            if graph_type != "Pie":
                ax.set_xlabel(x_column)
                ax.set_ylabel(y_column)
                st.pyplot(fig)
            else:
                st.pyplot(plt)

        st.write("Tip: Ensure the selected columns are numeric for meaningful plots.")
    else:
        st.info("Please upload a CSV file to get started.")

# Content for "About the Data" tab
elif tab_selection == "About the Data":
    st.write("### About the Data")
    st.write(
        """
        This dataset contains air quality data collected from various monitoring stations.
        The data includes measurements of pollutants such as PM2.5, PM10, CO, and other 
        air quality indicators across different regions and times. 
        """
    )

    # Reference the image stored in your GitHub repository (use raw URL)
    image_url = "https://raw.githubusercontent.com/OctuplePants/my_repo/main/DATA.jpg"
    
    # Display the image 1.3 times bigger than the default size (adjust width)
    st.image(image_url, caption="Air Quality Monitoring", width=1300)  # Set width to 1300 pixels (about 1.3 times larger)

    st.write(
        """
        The dataset can be used for various analyses including time series, pollution trends, 
        and regional comparisons. It is ideal for exploring the impact of air quality on health and 
        environment.
        """
    )



