# EVA Data Analysis

## Overview

The `eva_analysis.py` script processes EVA (Extravehicular Activity) data from NASA. It reads data from a JSON file, converts it into a CSV format, and generates a plot showing the total time spent in space over the years.

## Requirements

- Python 3.x
- Libraries:
  - `json`
  - `csv`
  - `datetime`
  - `matplotlib`
  - `pandas`

## Setting Up a Virtual Environment

1. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

2. **Activate the virtual environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. **Install the required libraries**:
   ```bash
   pip install matplotlib pandas
   ```

## Data Sources

The script uses the EVA data from the following source:
- [NASA EVA Data](https://data.nasa.gov/resource/eva.json)

Make sure to download the data and save it as `eva_data.json` in the same directory as the script.

## Usage

1. Place the `eva_data.json` file in the same directory as `eva_analysis.py`.
2. Run the script:

```bash
python eva_analysis.py
```

3. The script will generate a CSV file named `eva_data.csv` and a plot saved as `myplot.png`.

## Output

- `eva_data.csv`: A CSV file containing the processed EVA data.
- `myplot.png`: A plot showing the total time spent in space over the years.

## Notes

- The script currently processes a fixed number of lines (374) from the JSON file. Adjust this number if necessary based on the actual data size.
- The script prints the processed data to the console for verification.


