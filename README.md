## README.md

# Dynamic TVL Distribution Tool

This Streamlit app allows users to simulate and analyze Total Value Locked (TVL) distributions using customizable statistical models. It includes options to introduce 'power users' and export generated data for further analysis.

## Features

- **Statistical Distribution Simulation**: Create TVL distributions using truncated normal distributions.
- **Custom Parameters**: Configure mean, standard deviation, min/max values, and adjust the influence of 'power users'.
- **Interactive Visualization**: View histograms with key range indicators.
- **Data Export**: Download generated data as a CSV file.
- **Descriptive Statistics**: Analyze summary statistics of the generated distribution.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Configuration

- **Distribution Parameters**: Adjust the number of values, mean, and standard deviation.
- **Range Limits**: Set minimum and maximum values for the distribution.
- **Power Users**: Customize the proportion and value ranges for low and high deposit users.

## Visualization

- **Histogram**: Displays the generated TVL distribution with visual markers for configured ranges.
- **Descriptive Statistics**: Provides summary statistics (mean, standard deviation, min, max, etc.).

## Export

- Download the generated dataset as a CSV file for external analysis.

## License

Creative Commons Legal Code License
