import pandas as pd


def read_output_fd(output_path, output_name):
    """
    Reads the output Excel file from a simulation and extracts capacity, activity, and emissions data.

    Parameters:
    - output_path: The directory path where the output file is located.
    - output_name: The name of the output Excel file.

    Returns:
    - A tuple containing dictionaries for Capacity and Activity data, and a total emissions value.
    """
    # Construct the full path to the Excel file
    file_path = f"{output_path}/{output_name}"
    
    # Use context manager for better resource management
    with pd.ExcelFile(file_path) as xls:
        # Define a function to read and process a sheet
        def read_sheet(sheet_name, index_col='Technology', year=2049):
            df = pd.read_excel(xls, sheet_name)
            df.set_index(index_col, drop=True, inplace=True)
            df.fillna(0, inplace=True)
            return df.loc[:, year] if year in df.columns else df

        # Read and process each sheet
        elc_cap = read_sheet('Capacity_electric')
        trnsprt_cap = read_sheet('Capacity_transport')
        elc_act = read_sheet('Activity_electric')
        trnsprt_act = read_sheet('Activity_transport')
        supply_act = read_sheet('Activity_supply')
        emissions = read_sheet('Emissions', index_col='Emissions')

    # Calculate total emissions if possible
    total_emissions = emissions.sum() if not emissions.empty else 0

    # Prepare Capacity and Activity dictionaries
    capacity = {tech: elc_cap.get(tech, 0) for tech in ['E_SOLPV', 'E_WIND', 'E_NGCC', 'E_BATT', 'E_NUCLEAR', 'E_HYDRO']}
    capacity.update({tech: trnsprt_cap.get(tech, 0) for tech in ['E_TRANS', 'E_COND', 'E_TWR', 'E_SUB']})

    activity = {tech: elc_act.get(tech, 0) for tech in ['E_SOLPV', 'E_WIND', 'E_NGCC', 'E_BATT', 'E_NUCLEAR', 'E_HYDRO']}
    activity.update({tech: trnsprt_act.get(tech, 0) for tech in ['E_TRANS', 'E_COND', 'E_TWR', 'E_SUB']})
    activity.update({tech: supply_act.get(tech, 0) for tech in ['S_IMPNG', 'S_IMPURN']})

    return capacity, activity, total_emissions


def read_output_bau(output_path, output_name):
    """
    Reads the output Excel file from a 'business as usual' simulation and extracts capacity, activity, and emissions data.

    Parameters:
    - output_path (str): The directory path where the output file is located.
    - output_name (str): The name of the output Excel file.

    Returns:
    - tuple: A tuple containing dictionaries for Capacity and Activity data, and total emissions.
    """
    file_path = f"{output_path}/{output_name}"

    with pd.ExcelFile(file_path) as xls:
        # Function to read and process each sheet
        def read_sheet(sheet_name, index_col='Technology', year=2049):
            df = pd.read_excel(xls, sheet_name)
            df.set_index(index_col, drop=True, inplace=True)
            df.fillna(0, inplace=True)
            return df.loc[:, year] if year in df.columns else df

        # Reading and processing each required sheet
        elc_cap = read_sheet('Capacity_electric')
        trnsprt_cap = read_sheet('Capacity_transport')
        elc_act = read_sheet('Activity_electric')
        trnsprt_act = read_sheet('Activity_transport')
        supply_act = read_sheet('Activity_supply')
        emissions = read_sheet('Emissions', index_col='Emissions')

    # Calculate total emissions
    total_emissions = emissions.sum() if not emissions.empty else 0

    # Constructing Capacity and Activity dictionaries
    capacity = {tech: elc_cap.get(tech, 0) for tech in ['E_SOLPV', 'E_WIND', 'E_NGCC', 'E_BATT', 'E_NUCLEAR', 'E_HYDRO', 'E_BIO', 'E_COAL', 'E_DSL', 'E_OIL']}
    capacity.update({tech: trnsprt_cap.get(tech, 0) for tech in ['E_TRANS', 'E_COND', 'E_TWR', 'E_SUB']})

    activity = {tech: elc_act.get(tech, 0) for tech in ['E_SOLPV', 'E_WIND', 'E_NGCC', 'E_BATT', 'E_NUCLEAR', 'E_HYDRO', 'E_BIO', 'E_COAL', 'E_DSL', 'E_OIL']}
    activity.update({tech: trnsprt_act.get(tech, 0) for tech in ['E_TRANS', 'E_COND', 'E_TWR', 'E_SUB']})
    activity.update({tech: supply_act.get(tech, 0) for tech in ['S_IMPNG', 'S_IMPURN', 'S_IMPCOAL', 'S_IMPDSL', 'S_IMPOIL', 'S_IMPBIO']})

    return capacity, activity, total_emissions


def read_output_fr(output_path, output_name):
    """
    Reads the output Excel file from a 'future scenario' simulation and extracts capacity, activity, and emissions data.

    Parameters:
    - output_path (str): The directory path where the output file is located.
    - output_name (str): The name of the output Excel file.

    Returns:
    - tuple: A tuple containing dictionaries for Capacity and Activity data, and total emissions.
    """
    file_path = f"{output_path}/{output_name}"

    with pd.ExcelFile(file_path) as xls:
        def read_sheet(sheet_name, index_col='Technology', year=2049):
            df = pd.read_excel(xls, sheet_name)
            df.set_index(index_col, drop=True, inplace=True)
            df.fillna(0, inplace=True)
            return df.loc[:, year] if year in df.columns else df

        elc_cap = read_sheet('Capacity_electric')
        trnsprt_cap = read_sheet('Capacity_transport')
        elc_act = read_sheet('Activity_electric')
        trnsprt_act = read_sheet('Activity_transport')
        supply_act = read_sheet('Activity_supply')
        emissions_data = read_sheet('Emissions', index_col='Emissions')

    total_emissions = emissions_data.sum() if not emissions_data.empty else 0

    capacity = {
        'Sol': elc_cap.get('E_SOLPV', 0), 'Wind': elc_cap.get('E_WIND', 0), 'NGCC': elc_cap.get('E_NGCC', 0),
        'Batt': elc_cap.get('E_BATT', 0), 'Nuc': elc_cap.get('E_NUCLEAR', 0), 'Hyd': elc_cap.get('E_HYDRO', 0),
        'Bio': elc_cap.get('E_BIO', 0), 'Trans': trnsprt_cap.get('E_TRANS', 0), 'Sub': trnsprt_cap.get('E_SUB', 0),
        'Cond': trnsprt_cap.get('E_COND', 0), 'Twr': trnsprt_cap.get('E_TWR', 0)
    }

    activity = {
        'Sol': elc_act.get('E_SOLPV', 0), 'Wind': elc_act.get('E_WIND', 0), 'NGCC': elc_act.get('E_NGCC', 0),
        'Batt': elc_act.get('E_BATT', 0), 'Nuc': elc_act.get('E_NUCLEAR', 0), 'Hyd': elc_act.get('E_HYDRO', 0),
        'Bio': elc_act.get('E_BIO', 0), 'Trans': trnsprt_act.get('E_TRANS', 0), 'Sub': trnsprt_act.get('E_SUB', 0),
        'Cond': trnsprt_act.get('E_COND', 0), 'Twr': trnsprt_act.get('E_TWR', 0), 'NG': supply_act.get('S_IMPNG', 0),
        'URN': supply_act.get('S_IMPURN', 0), 'Biofuel': supply_act.get('S_IMPBIO', 0)
    }

    return capacity, activity, total_emissions