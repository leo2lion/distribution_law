import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import truncnorm

# Streamlit Configuration
st.set_page_config(page_title="Dynamic TVL Distribution Tool", layout="centered")

# === Title and Introduction ===
st.title("Dynamic TVL Distribution Tool")
st.write("This tool allows you to dynamically create and manage statistical distributions to simulate customized TVL (Total Value Locked).")

# === Sidebar for Parameters ===
st.sidebar.header("Configuration Parameters")

# Main distribution parameters
n_values = st.sidebar.number_input("Number of values (n)", min_value=100, max_value=100000, value=5000, step=100)
mean_deposit = st.sidebar.number_input("Mean deposit ($)", min_value=0, max_value=500000, value=75000, step=1000)
std_deviation = st.sidebar.number_input("Deposit standard deviation ($)", min_value=1000, max_value=100000, value=20000, step=1000)

# Distribution limits
min_value = st.sidebar.number_input("Minimum value ($)", min_value=0, max_value=mean_deposit, value=50, step=50)
max_value = st.sidebar.number_input("Maximum value ($)", min_value=mean_deposit, max_value=1000000, value=200000, step=5000)

# Parameters for "power users"
st.sidebar.subheader("Add 'Power Users'")
proportion_extra_low = st.sidebar.slider("Proportion (low values)", 0.0, 1.0, 0.1, step=0.01)
proportion_extra_high = st.sidebar.slider("Proportion (high values)", 0.0, 1.0, 0.5, step=0.01)
extra_low_range = st.sidebar.slider("Low value range ($)", min_value=0, max_value=100000, value=(2000, 50000), step=1000)
extra_high_range = st.sidebar.slider("High value range ($)", min_value=100000, max_value=1000000, value=(100000, 200000), step=5000)

# === Generate the Distribution ===
# Calculate parameters for the truncated normal distribution
a, b = (min_value - mean_deposit) / std_deviation, (max_value - mean_deposit) / std_deviation

# Generate the truncated normal distribution
tvl_distribution = truncnorm(a, b, loc=mean_deposit, scale=std_deviation).rvs(n_values)

# Add "power user" values
extra_low_values = np.random.uniform(extra_low_range[0], extra_low_range[1], int(proportion_extra_low * n_values))
extra_high_values = np.random.uniform(extra_high_range[0], extra_high_range[1], int(proportion_extra_high * n_values))
tvl_distribution = np.concatenate((tvl_distribution, extra_low_values, extra_high_values))

# === Visualization ===
st.subheader("Histogram of the Generated Distribution")
fig, ax = plt.subplots(figsize=(10, 6))
ax.hist(tvl_distribution, bins=100, color='blue', edgecolor='black', alpha=0.7)
ax.set_title('Normal Distribution of TVL Deposits per User')
ax.set_xlabel('Deposit Amount ($)')
ax.set_ylabel('Frequency')
ax.grid(False)

# Vertical lines to visualize ranges
ax.axvline(x=min_value, color='r', linestyle='--', label='Min Value')
ax.axvline(x=extra_low_range[0], color='g', linestyle='--', label='Low Range Start')
ax.axvline(x=extra_low_range[1], color='g', linestyle='--', label='Low Range End')
ax.axvline(x=extra_high_range[0], color='orange', linestyle='--', label='High Range Start')
ax.axvline(x=extra_high_range[1], color='orange', linestyle='--', label='High Range End')
ax.axvline(x=max_value, color='r', linestyle='--', label='Max Value')
ax.legend()
st.pyplot(fig)

# === Export Data ===
st.subheader("Export Generated Data")
if st.button("Download as CSV"):
    mock_tvl_df = pd.DataFrame(tvl_distribution, columns=['TVL'])
    csv = mock_tvl_df.to_csv(index=False).encode('utf-8')
    st.download_button(label="Download CSV File", data=csv, file_name='Mock_TVL_Distribution.csv', mime='text/csv')

# === Descriptive Statistics ===
st.subheader("Descriptive Statistics of the Distribution")
mock_tvl_df = pd.DataFrame(tvl_distribution, columns=['TVL'])
st.write(mock_tvl_df.describe())
