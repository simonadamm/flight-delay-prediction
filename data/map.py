import pandas as pd
import plotly.graph_objects as go

# Load datasets
try:
    flights_df = pd.read_csv('data/flights.csv')
    airports_df = pd.read_csv('data/airports.csv')
except FileNotFoundError:
    print("Make sure 'flights.csv' and 'airports.csv' are in the 'data/' directory.")
    exit()

# Create the IS_DELAYED feature
flights_df['IS_DELAYED'] = (flights_df['ARRIVAL_DELAY'] >= 15).astype(int)

# Filter for delayed flights and count them by origin airport
delayed_flights = flights_df[flights_df['IS_DELAYED'] == 1]
delay_counts = delayed_flights['ORIGIN_AIRPORT'].value_counts().reset_index()
delay_counts.columns = ['IATA_CODE', 'delay_count']

# Merge with airport data to get coordinates
airport_delays = pd.merge(delay_counts, airports_df, on='IATA_CODE')

# Create the map
fig = go.Figure(data=go.Scattergeo(
    lon=airport_delays['LONGITUDE'],
    lat=airport_delays['LATITUDE'],
    text=airport_delays.apply(lambda row: f"{row['AIRPORT']}<br>Delayed Flights: {row['delay_count']}", axis=1),
    mode='markers',
    marker=dict(
        color='red',
        size=airport_delays['delay_count'],
        sizemin=4,
        sizemode='area',
        sizeref=2.*max(airport_delays['delay_count'])/(40.**2), # Scale marker size
        opacity=0.7
    )
))

fig.update_layout(
    title_text='Number of Delayed Flights by Origin Airport in the US',
    geo=dict(
        scope='usa',
        projection_type='albers usa',
        showland=True,
        landcolor='rgb(217, 217, 217)',
        subunitcolor="rgb(255, 255, 255)",
    ),
)

# Save to an HTML file
fig.write_html("flight_delays_map.html")

print("Map has been generated and saved as 'flight_delays_map.html'")