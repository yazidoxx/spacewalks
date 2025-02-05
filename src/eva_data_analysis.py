import matplotlib.pyplot as plt
import pandas as pd


def read_json_to_dataframe(input_file):
    """
    Read the data from a JSON file into a Pandas dataframe.
    Clean the data by removing any incomplete rows and sort by date.

    Args:
        input_file (str): The path to the JSON file.

    Returns:
        pd.DataFrame: The cleaned and sorted data as a dataframe structure.
    """
    print(f'Reading JSON file {input_file}')
    # Read the data from a JSON file into a Pandas dataframe
    df = pd.read_json(input_file, convert_dates=['date'])
    df['eva'] = df['eva'].astype(float)  # Ensure 'eva' column is of float type
    # Clean the data by removing any incomplete rows and sort by date
    df.dropna(axis=0, inplace=True)  # Remove rows with missing values
    df.sort_values('date', inplace=True)  # Sort the dataframe by date
    return df


def write_dataframe_to_csv(df, output_file):
    """
    Write the dataframe to a CSV file.

    Args:
        df (pd.DataFrame): The input dataframe.
        output_file (str): The path to the output CSV file.

    Returns:
        None
    """
    print(f'Saving to CSV file {output_file}')
    # Save dataframe to CSV file for later analysis
    df.to_csv(output_file, index=False)  # Do not include row indices in the CSV


if __name__ == "__main__":
    # Main code execution starts here

    print("--START--")

    # Define input and output file paths
    input_file_path = './data/eva_data.json'
    output_file_path = './processed_data/eva_data.csv'
    graph_file_path = './results/cumulative_eva_graph.png'

    # Read the data from JSON file
    eva_data = read_json_to_dataframe(input_file_path)

    # Convert and export data to CSV file
    write_dataframe_to_csv(eva_data, output_file_path)

    print(f'Plotting cumulative spacewalk duration and saving to {graph_file_path}')
    # Plot cumulative time spent in space over years
    eva_data['duration_hours'] = eva_data['duration'].str.split(":").apply(
        lambda x: int(x[0]) + int(x[1]) / 60)  # Convert duration to hours
    eva_data['cumulative_time'] = eva_data['duration_hours'].cumsum()  # Calculate cumulative time
    plt.plot(eva_data['date'], eva_data['cumulative_time'], 'ko-')  # Plot the data
    plt.xlabel('Year')  # Label for x-axis
    plt.ylabel('Total time spent in space to date (hours)')  # Label for y-axis
    plt.tight_layout()  # Adjust layout to prevent clipping of labels
    plt.savefig(graph_file_path)  # Save the plot as a PNG file
    plt.show()  # Display the plot

    print("--END--")