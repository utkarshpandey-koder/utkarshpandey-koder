# EV Population and Trend Analysis Dashboard (Power BI)

## Objective
This project aims to create a comprehensive, insightful, and visually appealing dashboard using the EV population dataset. The dashboard assesses key performance indicators (KPIs) and presents meaningful insights on electric vehicle adoption, regional trends, and customer demographics in a clear, actionable format.

---

## Analysis Conducted (Questions)
1. Display the total EV population, total EV sales, and year-over-year growth percentage.
2. Compare year-wise EV sales trends.
3. Determine the most popular EV models and manufacturers.
4. Identify the regions with the highest EV adoption rates.
5. Analyze the EV population by vehicle type (e.g., SUVs, sedans, hatchbacks).
6. Show the distribution of EVs by battery capacity.
7. Analyze the percentage of EVs by fuel type (Battery Electric Vehicle (BEV), Plug-in Hybrid Electric Vehicle (PHEV), etc.).
8. Determine sales trends by customer demographic (age group and gender).
9. Analyze sales by charging infrastructure density.
10. Identify regions with the highest growth in EV adoption over time.

---

## Solution

### Data Cleaning
1. Removed duplicate entries from the EV population dataset.
2. Standardized the naming conventions for EV models and manufacturers.
3. Filled missing data for vehicle type and battery capacity using relevant imputation techniques.
4. Dropped irrelevant columns, such as registration ID, that did not contribute to the analysis.
5. Removed data entries with invalid or incomplete demographic information.

### Data Modeling
1. Created a relationship between the EV sales data and demographic data using the Customer ID column.
2. Built a Date table for time-based analysis, connecting it to the EV sales table using the date columns.
3. Created a Measure table to store KPIs such as Total EV Sales, Total EV Population, and Year-over-Year Growth Percentage.
4. Established a relationship between the EV sales table and the charging infrastructure table using location identifiers.

---

## Visualizations
1. **KPIs (Cards):** Displayed Total EV Population, Total BEVs, and PHEVs.
2. **Year-wise Sales Trend (Line Chart):** Showed sales trends over time, highlighting key performance years.
3. **Popular EV Models (Bar Chart):** Showed the most and least popular EV models.
4. **EV Adoption by Region (Map Chart):** Highlighted regions with high and low EV adoption.
5. **EVs by Vehicle CAFV Eligibility (Donut Chart):** Displayed the distribution of EVs by vehicle CAFV Eligibility.

---

## Filters (Slicers)
Interactive slicers were created to filter by:
- City
- Make
- Electric Vehicle type

---

## Sample Screenshots
![image](https://github.com/user-attachments/assets/04e90159-baa9-431f-bf24-238bcb119694)

---

## Conclusion
The **EV Population and Trend Analysis Dashboard** The dashboard shows that the electric vehicle (EV) market is growing quickly. Most EVs are fully electric (78%), and Tesla is the top manufacturer. On average, EVs can travel 67.83 km on a single charge, showing current battery performance. Popular models like the Model Y and Model 3 are driving this growth, especially after 2020, when the market expanded rapidly due to better technology and more interest from buyers.
