# Water Quality Data Dashboard

This project provides an interactive dashboard for visualizing water quality data from Biscayne Bay using data collected by aquatic robots. The dashboard is built using [Streamlit](https://streamlit.io/) for the web UI and [Plotly](https://plotly.com/python/) for advanced data visualizations.

## Features

- **Upload Your Own Data:** Easily upload a CSV file with water quality measurements.
- **Default Dataset:** If no file is uploaded, a sample dataset (`biscayne_bay_dataset_oct_2021-1.csv`) will be loaded automatically.
- **Correlation Analysis:** Visualize relationships between water parameters with dynamic scatter plots.
- **Line Charts:** Plot temporal changes of water quality parameters and customize colors.
- **Interactive Maps:** View sample locations and water parameter values on an interactive map.
- **3D Visualization:** Explore data in three dimensions (latitude, longitude, water depth).
- **Data Tables:** Inspect raw data and descriptive statistics.

## Quick Start

### Prerequisites

- Python 3.7 or higher
- [pip](https://pip.pypa.io/en/stable/)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/gregorymurad/internshipReady.git
   cd internshipReady
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   If you don't have a `requirements.txt`, install directly:
   ```bash
   pip install streamlit plotly pandas
   ```

3. **Run the app:**
   ```bash
   streamlit run main.py
   ```

4. **Open your browser:**  
   Streamlit will display a local URL (e.g., `http://localhost:8501`)—open it to use the dashboard.

## File Format

Your CSV file should have the following columns (header names must match exactly):

- `Salinity (ppt)`
- `Temperature (C)`
- `ODO (mg/L)`
- `latitude`
- `longitude`
- `pH`
- `Total Water Column (m)`

## Example

You can use the provided `biscayne_bay_dataset_oct_2021-1.csv` as a template for your own data.

## Screenshots

*Add screenshots here by dropping images into this README or linking to hosted images.*

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions, suggestions, or contributions, open an issue or contact [@gregorymurad](https://github.com/gregorymurad).

---
*Visualization Tool for Biscayne Bay Water Quality using Aquatic Robots*
