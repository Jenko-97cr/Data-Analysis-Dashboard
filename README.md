# 📊 Interactive Data Analysis Dashboard

A powerful, user-friendly web application for exploring and analyzing CSV data without writing code. Built with Streamlit and Python, this dashboard transforms raw data into actionable insights through interactive visualizations and statistical analysis.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.28+-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## ✨ Features

- **📁 Easy File Upload** - Drag and drop CSV files for instant analysis
- **📈 Statistical Summary** - Automatic calculation of mean, median, standard deviation, and more
- **🔍 Missing Data Detection** - Identify and visualize missing values with interactive charts
- **📊 Multiple Visualizations**
  - Histograms for distribution analysis
  - Box plots for outlier detection
  - Violin plots for detailed distribution shapes
- **🔗 Correlation Analysis** - Interactive heatmaps showing relationships between variables
- **⚠️ Outlier Detection** - IQR-based method to identify anomalies in your data
- **🧹 Data Cleaning** - Remove missing values and duplicates with one click
- **📥 Export Options** - Download cleaned data as CSV or Excel files

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. Clone the repository:
```bash
git clone https://github.com/saimtec/Data-Analysis-Dashboard.git
cd Data-Analysis-Dashboard
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run app.py
```

4. Open your browser and navigate to `http://localhost:8501`

## 📦 Dependencies

- **streamlit** - Web application framework
- **pandas** - Data manipulation and analysis
- **numpy** - Numerical computing
- **matplotlib** - Data visualization
- **seaborn** - Statistical data visualization
- **openpyxl** - Excel file support

## 💡 Usage

### Upload Your Data
1. Click "Browse files" or drag and drop your CSV file
2. The dashboard automatically loads and displays your data

### Explore Statistics
- View summary statistics including count, mean, std, min, max
- Check data types and non-null counts for each column
- Identify missing values with percentage breakdown

### Visualize Distributions
- Select any numeric column from the dropdown
- Choose between Histogram, Box Plot, or Violin Plot
- View key statistics: mean, median, standard deviation, and range

### Analyze Correlations
- Interactive heatmap shows relationships between all numeric variables
- Color-coded from red (negative) to blue (positive) correlation
- Table displays the strongest correlations

### Detect Outliers
- Select a column for outlier detection
- Uses IQR (Interquartile Range) method
- Shows outlier count with upper and lower bounds

### Clean & Export
- Remove rows with missing values
- Eliminate duplicate records
- Download cleaned data as CSV or Excel

## 📊 Sample Data

The repository includes a sample dataset (`Heart_Disease_Prediction.csv`) with:
- Patient demographics and health metrics
- Missing values for testing data cleaning features
- Multiple numeric and categorical variables
- Perfect for exploring all dashboard capabilities

## 🎯 Use Cases

- **Data Scientists** - Quick exploratory data analysis before modeling
- **Business Analysts** - Generate insights from sales, customer, or operational data
- **Students** - Learn data analysis concepts through interactive visualization
- **Researchers** - Analyze survey results and experimental data
- **Anyone** - Explore CSV data without programming knowledge

## 🛠️ Project Structure

```
Data-Analysis-Dashboard/
│
├── app.py                              # Main Streamlit application
├── requirements.txt                    # Python dependencies
├── Heart_Disease_Prediction.csv        # Sample dataset
└── README.md                           # Project documentation
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Visualization powered by [Matplotlib](https://matplotlib.org/) and [Seaborn](https://seaborn.pydata.org/)
- Data handling with [Pandas](https://pandas.pydata.org/)

## 📧 Contact

Have questions or suggestions? Feel free to open an issue or reach out!

---

⭐ Star this repository if you found it helpful!
