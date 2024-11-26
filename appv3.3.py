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
    
    # Display the image
    st.image(image_url, caption="Air Quality Monitoring", use_column_width=True)

    # New section for detailed explanation about the data
    st.write(
        """
        ### Data Descriptions:
        
        **# Days with AQI**  
        Number of days in the year having an Air Quality Index value. This is the number of days on which measurements from any monitoring site in the county or MSA were reported to the AQS database.

        **# Days Good**  
        Number of days in the year having an AQI value 0 through 50.

        **# Days Moderate**  
        Number of days in the year having an AQI value 51 through 100.

        **# Days Unhealthy for Sensitive Groups**  
        Number of days in the year having an AQI value 101 through 150.

        **# Days Unhealthy**  
        Number of days in the year having an AQI value 151 through 200.

        **# Days Very Unhealthy**  
        Number of days in the year having an AQI value 201 through 300.

        **# Days Hazardous**  
        Number of days in the year having an AQI value 301 or higher.

        **AQI Max**  
        The highest daily AQI value in the year.

        **AQI 90th %ile**  
        90 percent of daily AQI values during the year were less than or equal to the 90th percentile value.

        **AQI Median**  
        Half of daily AQI values during the year were less than or equal to the median value, and half equaled or exceeded it.

        **# Days CO**  
        The number of days in the year when CO was the main pollutant.

        **# Days NO2**  
        The number of days in the year when NO2 was the main pollutant.

        **# Days O3**  
        The number of days in the year when O3 was the main pollutant.

        **# Days PM2.5**  
        The number of days in the year when PM2.5 was the main pollutant.

        **# Days PM10**  
        The number of days in the year when PM10 was the main pollutant.
        
        A daily index value is calculated for each air pollutant measured. The highest of those index values is the AQI value, and the pollutant responsible for the highest index value is the "Main Pollutant." These columns give the number of days each pollutant measured was the main pollutant. A blank column indicates a pollutant not measured in the county or CBSA.
        """
    )


