from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)

def generate_plot():
    # Replace 'your_file.csv' with the path to your CSV file
    csv_file_path = '../cleaning/dataset.csv'

    # Read the CSV file using pandas
    df = pd.read_csv(csv_file_path,encoding='utf-8')
    df['State Abbreviation'] = df['State/UT'].apply(lambda x: x[:4].upper())

    # Extracting data for each year
    crime_rates_2016 = df.loc[df['Category'] == 'State', ['State/UT', 'State Abbreviation', '2016']].nlargest(5, '2016')
    crime_rates_2017 = df.loc[df['Category'] == 'State', ['State/UT', 'State Abbreviation', '2017']].nlargest(5, '2017')
    crime_rates_2018 = df.loc[df['Category'] == 'State', ['State/UT', 'State Abbreviation', '2018']].nlargest(5, '2018')

    # Plotting bar graphs for each year
    plt.figure(figsize=(15, 5))

    # Bar chart for 2016
    plt.subplot(1, 3, 1)
    plt.bar(crime_rates_2016['State Abbreviation'], crime_rates_2016['2016'], color='blue')
    plt.xlabel('State')
    plt.ylabel('Rate of Total Cyber Crimes (2016)')
    plt.title('Cyber Crime Rates in 2016')
    plt.ylim(0, 7000)  # Set the y-axis limit

    # Bar chart for 2017
    plt.subplot(1, 3, 2)
    plt.bar(crime_rates_2017['State Abbreviation'], crime_rates_2017['2017'], color='green')
    plt.xlabel('State')
    plt.ylabel('Rate of Total Cyber Crimes (2017)')
    plt.title('Cyber Crime Rates in 2017')
    plt.ylim(0, 7000)  # Set the y-axis limit

    # Bar chart for 2018
    plt.subplot(1, 3, 3)
    plt.bar(crime_rates_2018['State Abbreviation'], crime_rates_2018['2018'], color='red')
    plt.xlabel('State')
    plt.ylabel('Rate of Total Cyber Crimes (2018)')
    plt.title('Cyber Crime Rates in 2018')
    plt.ylim(0, 7000)  # Set the y-axis limit

    # Adjust layout to prevent overlap
    plt.tight_layout()

    # Save the plot to a BytesIO object
    image_stream = BytesIO()
    plt.savefig(image_stream, format='png')
    image_stream.seek(0)
    encoded_image = base64.b64encode(image_stream.read()).decode('utf-8')

    plt.close()  # Close the plot to free up resources

    return encoded_image

@app.route('/crime_rate')
def crime_rate():
    plot_data = generate_plot()
    return render_template('crime_rate.html', plot_data=plot_data)

if __name__ == '__main__':
    app.run(debug=True)
