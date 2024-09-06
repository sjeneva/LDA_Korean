import pandas as pd

# Load the uploaded Excel file containing duplicate articles
file_path = r'C:\Users\1234\OneDrive - 인하대학교\바탕 화면\ESGL_Korean\duplicates_esg_logistics_news.xlsx'
df = pd.read_excel(file_path)

# Print out the columns and the first few rows to check the data
print("Columns in the dataframe:", df.columns)
print(df.head())

# Define the keyword categories
keyword_categories = {
    "ESG": [
        "ESG Logistics",
        "ESG Reporting in Logistics",
        "ESG Metrics for Logistics",
        "ESG Transparency in Logistics",
        "ESG Strategies in Logistics",
        "ESG Impact on Logistics Performance",
        "ESG Policy Development in Logistics",
        "ESG Benchmarking in Logistics",
        "ESG Audits in Logistics",
        "ESG Compliance in Logistics"
    ],
    "ENVIRONMENT": [
        "Green Logistics",
        "Eco-friendly Transportation",
        "Carbon Footprint Reduction in Logistics",
        "Renewable Energy in Warehousing",
        "Waste Reduction Strategies",
        "Sustainable Packaging Solutions",
        "Green Warehousing",
        "Sustainable Freight Transportation",
        "Greenhouse Gas Emissions Tracking",
        "Eco-conscious Inventory Management"
    ],
    "SOCIAL": [
        "Worker Welfare in Supply Chains",
        "Diversity and Inclusion in Logistics",
        "Community Engagement in Logistics Projects",
        "Human Rights in Supply Chains",
        "Social Responsibility in Logistics",
        "Fair Labor Practices in Logistics",
        "Supply Chain Transparency",
        "Employee Health and Safety in Logistics",
        "Community Development in Logistics",
        "Labor Rights in Logistics Operations"
    ],
    "GOVERNANCE": [
        "Governance in Logistics Operations",
        "Ethical Compliance in Logistics",
        "Logistics Transparency",
        "Stakeholder Engagement in Logistics",
        "Logistics Risk Management",
        "Anti-corruption Measures in Supply Chains",
        "Regulatory Compliance in Logistics",
        "Corporate Governance in Supply Chain Management",
        "Third-party Audits in Logistics",
        "Supply Chain Ethics Policies"
    ],
    "SUSTAINABILITY": [
        "Sustainable Supply Chain Management",
        "Circular Economy in Logistics",
        "Climate-resilient Supply Chains",
        "Energy-efficient Fleet Management",
        "Long-term Environmental Impact Planning",
        "Sustainable Procurement Practices",
        "Life Cycle Assessment in Logistics",
        "Sustainable Logistics Innovations",
        "Sustainable Resource Management in Logistics",
        "Holistic Sustainability Strategies in Logistics"
    ]
}

# Function to categorize keywords
def categorize_keyword(keyword):
    for category, keywords in keyword_categories.items():
        if keyword in keywords:
            return category
    return None

# Check if 'keyword' column exists, if not, print an error message
if 'keyword' not in df.columns:
    print("Error: 'keyword' column not found in the dataframe")
else:
    # Apply categorization to the 'keyword' column
    df['keyword_2'] = df['keyword'].apply(categorize_keyword)

    # Save the updated dataframe to a new file
    updated_file_path = r'C:\Users\1234\Downloads\updated_duplicates_esg_logistics_news.xlsx'
    df.to_excel(updated_file_path, index=False)

    print("File saved successfully at:", updated_file_path)
