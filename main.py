import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Set the app title and layout
st.set_page_config(page_title="Data Visualization", layout="wide")
st.title("Data Visualization Dashboard")
st.write("Upload your dataset to explore and visualize it interactively.")


# Data upload and preview
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file:
    data = pd.read_csv(uploaded_file)

    st.markdown("***")  # Add a separator

    st.write("## Data Preview")
    st.write(data.head())

    st.markdown("***")  # Add a separator

    st.write(f"## Data Shape")
    st.write(f"##### Rows: {data.shape[0]}, Columns: {data.shape[1]}")

    st.markdown("***")  # Add a separator

    st.write("## Data Summary")
    st.write(data.describe())

    st.markdown("***")  # Add a separator
else:
    st.write("Awaiting file upload...")


# Plots and visualizations
if uploaded_file:
    st.sidebar.header("Visualization Settings")
    plot_type = st.sidebar.selectbox("Select Plot Type", ["Scatter Plot", "Bar Chart", "Line Chart", "Area Chart", "Histogram", "Box Plot", "Pie Chart"], index=1)
    x_axis = st.sidebar.selectbox("X-axis", data.columns, index=1)
    y_axis = st.sidebar.selectbox("Y-axis", data.columns, index=2)

    st.write("## Data Visualization")
    st.write(f"### Plotting {plot_type} of {y_axis} by {x_axis}")

    # Generate the plot based on the selected plot type
    fig, ax = plt.subplots(figsize=(15, 8))
    

    if plot_type == "Scatter Plot":
        plt.scatter(data[x_axis], data[y_axis], color='skyblue', edgecolor='k', alpha=0.7, s=100)
        plt.title("Scatter Plot", pad=20, fontsize=18, fontweight='bold')
        plt.xlabel(x_axis, labelpad=20)
        plt.ylabel(y_axis, labelpad=20)
        st.pyplot(plt)  # Display the plot

    elif plot_type == "Bar Chart":
        st.bar_chart(data[[x_axis, y_axis]].set_index(x_axis))

    elif plot_type == "Line Chart":
        st.line_chart(data[[x_axis, y_axis]].set_index(x_axis))

    elif plot_type == "Area Chart":
        st.area_chart(data[[x_axis, y_axis]].set_index(x_axis))

    elif plot_type == "Histogram":
        plt.hist(data[x_axis], bins=20, color='purple', edgecolor='k')
        plt.title("Histogram", pad=20, fontsize=18, fontweight='bold')
        plt.xlabel(x_axis, labelpad=20)
        plt.ylabel("Frequency", labelpad=20)
        st.pyplot(plt)

    elif plot_type == "Box Plot":
        sns.boxplot(data=data, x=x_axis, y=y_axis, ax=ax, palette="Set2")
        ax.set_title(f"Box Plot of {y_axis} by {x_axis}")
        st.pyplot(fig)

    elif plot_type == "Pie Chart":
        pie_data = data[x_axis].value_counts()  # Aggregating data for the pie chart
        ax.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette("Set3"))
        ax.set_title(f"Pie Chart of {x_axis}")
        st.pyplot(fig)


    # Data Filtering
    st.sidebar.header("Data Filtering Settings")
    columns = data.columns.tolist()
    selected_column = st.sidebar.selectbox("Select column to filter by", columns)
    unique_values = data[selected_column].unique()
    selected_value = st.sidebar.selectbox("Select value", unique_values)

    st.markdown("***")  # Add a separator

    st.write("## Data Filtering")
    filtered_data = data[data[selected_column] == selected_value]
    st.write(filtered_data)

else:
    st.write("Please upload a CSV file to start exploring your data.")


# Footer: Made with ❤️ by Mohamed Gamal © 2024
st.markdown("***")
st.write(f"Made with ❤️ by [Mohamed Gama](https://www.linkedin.com/in/mohamed-gamal-74192b1a7/) &copy; {pd.Timestamp.now().year}")
