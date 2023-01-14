import streamlit as st
import pandas as pd
import numpy as np

# Load the dataframe
df = pd.read_csv("properties_cleaned.csv")

conditions = {}
n_cols = 3

# Create a function to filter the DataFrame
def init_filters(df):
    st_cols = st.columns(n_cols)
    # Create empty dictionary to store filtering conditions
    index = 0
    for col in df.columns:
        # Determine the data type of the column
        if df[col].dtype in ['int', 'float']:
            # Ask for min and max values if the column is numeric
            all_min_val, all_max_val = df[col].min(), df[col].max()
            if isinstance(all_min_val, np.int64):
                step = 1
            else:
                step = 1.0
            min_val = st_cols[index].number_input(f"Min {col}", value=all_min_val, min_value=all_min_val, max_value=all_max_val, step=step)
            max_val = st_cols[index].number_input(f"Max {col}", value=all_max_val, min_value=all_min_val, max_value=all_max_val, step=step)
            conditions[col] = (min_val, max_val)
        elif df[col].dtype in ['bool']:
            # Ask for a checkbox if the column is boolean
            conditions[col] = st_cols[index].checkbox(f"Has {col}")
        elif df[col].dtype == 'object':
            if len(df[col].value_counts()) < 10:
                # Ask for a select box if the column is categorical
                conditions[col] = st_cols[index].multiselect(f'Select {col}',df[col].unique())
            else:
                conditions[col] = st_cols[index].text_input(f'Enter {col}')
        index = (index + 1) % n_cols
    return df

# Create a function to filter the DataFrame
def filter_dataframe(df):
    # Apply filtering conditions to the DataFrame
    for col, value in conditions.items():
        if df[col].dtype in ['int', 'float']:
            min_val, max_val = value
            df = df[(df[col].isna()) | ((df[col] >= min_val) & (df[col] <= max_val))]
        elif df[col].dtype in ['bool']:
            if value:
                df = df[df[col] == value]
        elif df[col].dtype == 'object':
            if len(df[col].value_counts()) < 10:
                cond = pd.Series([False] * len(df))
                if value:
                    for v in value:
                        cond |= (df[col] == v)
                    df = df[cond]
            else:
                df = df[(df[col].isna()) | df[col].str.lower().str.contains(value.lower())]
    return df

# Create the search bar
st.title("Mali search real estate")

search_button = st.button("Search")
init_filters(df)
# Show the filtered DataFrame
if search_button:
    searchable_columns = [
        'source',
        'title',
        'status',
        'price',
        'description',
        'location_adress',
        'location_country',
        'location_city',
        'location_district',
        'location_neighborhood',
        'info_reference',
        'info_ad_type',
        'info_ad_status',
        'info_rooms',
        'info_bedrooms',
        'info_bathrooms',
        'info_garages',
        'info_living_rooms',
        'info_annex_bedrooms',
        'agent_name',
        'agent_type',
        'agent_mobile',
        'agent_email',
        'ratings_average',
        'ratings_count',
        'ratings_5',
        'ratings_4',
        'ratings_3',
        'ratings_2',
        'ratings_1',
        'property_date',
        'info_postal_code',
        'info_building_year',
        'info_surface',
        'info_land_surface',
        'info_tag',
        'info_dining_room',
        'info_kitchen',
        'info_balcony',
        'info_internet',
        'info_wardrobe',
        'info_kettle',
        'info_chairs',
        'info_water_heater',
        'info_air_conditioner',
        'info_dressers',
        'info_prepaid_electricity',
        'info_iron',
        'info_microwave',
        'info_generator',
        'info_adult_bed',
        'info_fridge',
        'info_tables',
        'info_tv',
        'info_fan',
        'info_washing_machine',
        'info_security',
        'info_box',
        'info_dependencies',
        'info_electricity',
        'info_garden',
        'info_library',
        'info_buffets',
        'info_digital_tv_channels',
        'info_dressing_table',
        'info_fully_equipped_kitchen',
        'info_fully_furnished',
        'info_swimming_pool',
        'currency'
    ]
    filtered_df = filter_dataframe(df)
    st.dataframe(filtered_df)
    st.write(conditions["price"])
