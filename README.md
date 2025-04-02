# Healthcare-Access-Disparities
End-to-End Data Pipeline: Hospital Distance Analysis
Overview
This project analyzes hospital accessibility, with a focus on maternal hospitals, by examining travel distances and identifying potentially underserved areas.

Objectives
Assess hospital access across different regions.

Identify disparities in maternal healthcare availability.

Use OD Cost Matrix Analysis to measure travel times and distances.

Prioritize population-weighted centroids over geographic centroids for more accurate accessibility insights.

Pipeline Workflow
Data Collection: Gather hospital locations, population data, and road networks.

Data Cleaning & Transformation: Standardize datasets for spatial analysis.

Storage: Organize data efficiently for GIS processing.

OD Cost Matrix Analysis:

Compute travel times/distances from population-weighted centroids to hospitals.

Categorize hospitals by level (e.g., Level 0, Level 1, Level 2, Level 3).

Analysis & Insights: Identify underserved areas and generate visualizations.

Technologies Used
GIS Tools: ArcGIS Pro (OD Cost Matrix, Spatial Analysis)

Programming: Python (Arcpy, Pandas, Geopandas)

Data Sources: Census data, hospital locations, road networks

Next Steps
Integrate machine learning for predictive accessibility analysis.

Enhance data visualization using interactive maps.

Explore policy recommendations based on findings.
