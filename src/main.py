import matplotlib.pyplot as plt
import pandas as pd

def main():
    print("This is the main function of the script.")

    with open('assets/example.txt', 'r') as file:
        content = file.read()
        print("Content of example.txt:")
        print(content)

    # Additional functionality can be added here

    # Load the example data
    df = pd.read_csv("./example.csv")
    print("DataFrame created from example.csv:")
    print(df.head())
    
    # Convert timestamp to datetime
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    
    # Create multiple plots
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    fig.suptitle('Time Series Analysis Dashboard', fontsize=16)
    
    # Plot 1: Value and Moving Average over time
    axes[0, 0].plot(df['timestamp'], df['value'], label='Value', color='blue')
    axes[0, 0].plot(df['timestamp'], df['moving_average'], label='Moving Average', color='red')
    axes[0, 0].set_title('Value and Moving Average Over Time')
    axes[0, 0].set_xlabel('Time')
    axes[0, 0].set_ylabel('Value')
    axes[0, 0].legend()
    axes[0, 0].tick_params(axis='x', rotation=45)
    
    # Plot 2: Rate of Change
    axes[0, 1].plot(df['timestamp'], df['rate_of_change'], color='green', marker='o', markersize=3)
    axes[0, 1].set_title('Rate of Change Over Time')
    axes[0, 1].set_xlabel('Time')
    axes[0, 1].set_ylabel('Rate of Change')
    axes[0, 1].tick_params(axis='x', rotation=45)
    axes[0, 1].axhline(y=0, color='black', linestyle='--', alpha=0.3)
    
    # Plot 3: Cumulative Sum
    axes[1, 0].plot(df['timestamp'], df['cumulative_sum'], color='purple')
    axes[1, 0].set_title('Cumulative Sum Over Time')
    axes[1, 0].set_xlabel('Time')
    axes[1, 0].set_ylabel('Cumulative Sum')
    axes[1, 0].tick_params(axis='x', rotation=45)
    
    # Plot 4: Day/Night Distribution
    day_data = df[df['day_night'] == 'day']['value']
    night_data = df[df['day_night'] == 'night']['value']
    
    axes[1, 1].hist([day_data, night_data], bins=10, alpha=0.7, label=['Day', 'Night'], color=['orange', 'navy'])
    axes[1, 1].set_title('Value Distribution: Day vs Night')
    axes[1, 1].set_xlabel('Value')
    axes[1, 1].set_ylabel('Frequency')
    axes[1, 1].legend()
    
    plt.tight_layout()
    plt.savefig("output/time_series_analysis.png", dpi=300, bbox_inches='tight')
    print("Plot saved as 'output/time_series_analysis.png'")
    
    # Perform some analysis on the DataFrame
    print("\nSummary statistics:")
    print(df.describe())
    
    print("\nData insights:")
    print(f"- Total data points: {len(df)}")
    print(f"- Date range: {df['timestamp'].min()} to {df['timestamp'].max()}")
    print(f"- Average value: {df['value'].mean():.2f}")
    print(f"- Day/Night distribution: {df['day_night'].value_counts().to_dict()}")
    print(f"- Anomalies detected: {df['anomaly'].sum()}")

    

if __name__ == "__main__":
    main()