import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO

st.set_page_config(
    page_title="Data Analysis Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Interactive Data Analysis Dashboard")
st.markdown("""
This tool helps you **explore, analyze, and visualize** your data in seconds!
- Upload CSV files
- Get instant statistical insights
- Create beautiful visualizations
- Identify patterns and correlations
- Clean and export your data
""")

st.header("📁 Step 1: Upload Your Data")

uploaded_file = st.file_uploader(
    "Choose a CSV file",
    type=['csv']
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.session_state.df = df
    st.success("✅ File uploaded successfully!")
    
    st.header("👀 Step 2: Data Overview")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Rows", len(df))
    with col2:
        st.metric("Total Columns", len(df.columns))
    with col3:
        st.metric("Missing Values", df.isnull().sum().sum())
    with col4:
        st.metric("Data Types", len(df.dtypes.unique()))
    
    st.subheader("First 5 Rows of Data")
    st.dataframe(df.head())
    
    st.header("📈 Step 3: Statistical Analysis")
    
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    
    st.subheader("Summary Statistics")
    st.dataframe(df.describe())
    
    st.subheader("Data Types")
    st.dataframe(pd.DataFrame({
        'Column': df.columns,
        'Data Type': df.dtypes.values,
        'Non-Null Count': df.count().values
    }))
    
    st.header("🔍 Step 4: Missing Values Detection")
    
    missing_data = pd.DataFrame({
        'Column': df.columns,
        'Missing Count': df.isnull().sum().values,
        'Missing %': (df.isnull().sum().values / len(df) * 100).round(2)
    })
    
    st.dataframe(missing_data)
    
    if missing_data['Missing Count'].sum() > 0:
        fig, ax = plt.subplots(figsize=(10, 5))
        missing_data_sorted = missing_data[missing_data['Missing Count'] > 0].sort_values('Missing Count', ascending=False)
        ax.barh(missing_data_sorted['Column'], missing_data_sorted['Missing %'], color='salmon')
        ax.set_xlabel('Missing Percentage (%)')
        ax.set_title('Missing Values Distribution')
        st.pyplot(fig)
    else:
        st.info("✅ No missing values found!")
    
    st.header("📊 Step 5: Distribution Analysis")
    
    if len(numeric_cols) > 0:
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Select a Column to Analyze")
            selected_col = st.selectbox("Choose numeric column:", numeric_cols)
        
        with col2:
            plot_type = st.radio("Choose plot type:", ["Histogram", "Box Plot", "Violin Plot"])
        
        fig, ax = plt.subplots(figsize=(10, 5))
        
        if plot_type == "Histogram":
            ax.hist(df[selected_col].dropna(), bins=30, color='skyblue', edgecolor='black')
            ax.set_xlabel(selected_col)
            ax.set_ylabel('Frequency')
            ax.set_title(f'Distribution of {selected_col}')
        
        elif plot_type == "Box Plot":
            ax.boxplot(df[selected_col].dropna())
            ax.set_ylabel(selected_col)
            ax.set_title(f'Box Plot of {selected_col}')
        
        else:
            parts = ax.violinplot(df[selected_col].dropna(), vert=True)
            ax.set_ylabel(selected_col)
            ax.set_title(f'Violin Plot of {selected_col}')
        
        st.pyplot(fig)
        
        st.subheader(f"Statistics for {selected_col}")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Mean", f"{df[selected_col].mean():.2f}")
        with col2:
            st.metric("Median", f"{df[selected_col].median():.2f}")
        with col3:
            st.metric("Std Dev", f"{df[selected_col].std():.2f}")
        with col4:
            st.metric("Range", f"{df[selected_col].max() - df[selected_col].min():.2f}")
    
    st.header("🔗 Step 6: Correlation Analysis")
    
    if len(numeric_cols) > 1:
        st.subheader("Correlation Heatmap")
        
        corr_matrix = df[numeric_cols].corr()
        
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(
            corr_matrix,
            annot=True,
            cmap='coolwarm',
            center=0,
            fmt='.2f',
            square=True,
            ax=ax,
            cbar_kws={'label': 'Correlation'}
        )
        ax.set_title('Correlation Matrix Heatmap')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        st.pyplot(fig)
        
        st.subheader("Strongest Correlations")
        
        # Find top correlations between variables
        corr_pairs = []
        for i in range(len(corr_matrix.columns)):
            for j in range(i+1, len(corr_matrix.columns)):
                corr_pairs.append({
                    'Variable 1': corr_matrix.columns[i],
                    'Variable 2': corr_matrix.columns[j],
                    'Correlation': corr_matrix.iloc[i, j]
                })
        
        corr_df = pd.DataFrame(corr_pairs)
        corr_df['Abs Correlation'] = corr_df['Correlation'].abs()
        corr_df = corr_df.sort_values('Abs Correlation', ascending=False).head(10)
        
        st.dataframe(corr_df[['Variable 1', 'Variable 2', 'Correlation']])
    
    st.header("⚠️ Step 7: Outlier Detection")
    
    if len(numeric_cols) > 0:
        selected_outlier_col = st.selectbox("Select column for outlier detection:", numeric_cols, key='outlier')
        
        # Using IQR method to identify outliers
        Q1 = df[selected_outlier_col].quantile(0.25)
        Q3 = df[selected_outlier_col].quantile(0.75)
        IQR = Q3 - Q1
        
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        outliers = df[(df[selected_outlier_col] < lower_bound) | (df[selected_outlier_col] > upper_bound)]
        
        st.write(f"**Outliers found:** {len(outliers)}")
        st.write(f"**Lower Bound:** {lower_bound:.2f}")
        st.write(f"**Upper Bound:** {upper_bound:.2f}")
        
        if len(outliers) > 0:
            st.warning(f"⚠️ {len(outliers)} outliers detected!")
            st.dataframe(outliers)
    
    st.header("🧹 Step 8: Data Cleaning & Export")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Data Cleaning Options")
        
        if st.button("Remove Missing Values"):
            df_cleaned = df.dropna()
            st.session_state.df = df_cleaned
            st.success(f"✅ Removed rows with missing values! Rows: {len(df)} → {len(df_cleaned)}")
        
        if st.button("Remove Duplicates"):
            df_cleaned = df.drop_duplicates()
            st.session_state.df = df_cleaned
            st.success(f"✅ Removed duplicates! Rows: {len(df)} → {len(df_cleaned)}")
    
    with col2:
        st.subheader("Export Options")
        
        csv_buffer = BytesIO()
        df.to_csv(csv_buffer, index=False)
        csv_buffer.seek(0)
        
        st.download_button(
            label="📥 Download as CSV",
            data=csv_buffer,
            file_name="cleaned_data.csv",
            mime="text/csv"
        )
        
        excel_buffer = BytesIO()
        with pd.ExcelWriter(excel_buffer, engine='openpyxl') as writer:
            df.to_excel(writer, index=False)
        excel_buffer.seek(0)
        
        st.download_button(
            label="📥 Download as Excel",
            data=excel_buffer,
            file_name="cleaned_data.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

else:
    st.info("👆 Please upload a CSV file to get started!")
    
    st.subheader("Example Data Format:")
    example_df = pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
        'Age': [25, 30, 22, 28],
        'Salary': [50000, 60000, 45000, 55000],
        'Experience': [2, 5, 1, 3]
    })
    st.dataframe(example_df)
