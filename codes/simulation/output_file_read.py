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
#        emissions = read_sheet('Emissions', index_col='Emissions')

    # Calculate total emissions if possible
#    total_emissions = emissions.sum() if not emissions.empty else 0

    # Prepare Capacity and Activity dictionaries
    capacity = {tech: elc_cap.get(tech, 0) for tech in ['E_SOLPV', 'E_WIND', 'E_NGCC', 'E_BATT', 'E_NUCLEAR', 'E_HYDRO']}
    capacity.update({tech: trnsprt_cap.get(tech, 0) for tech in ['E_TRANS', 'E_COND', 'E_TWR', 'E_SUB']})

    activity = {tech: elc_act.get(tech, 0) for tech in ['E_SOLPV', 'E_WIND', 'E_NGCC', 'E_BATT', 'E_NUCLEAR', 'E_HYDRO']}
    activity.update({tech: trnsprt_act.get(tech, 0) for tech in ['E_TRANS', 'E_COND', 'E_TWR', 'E_SUB']})
    activity.update({tech: supply_act.get(tech, 0) for tech in ['S_IMPNG', 'S_IMPURN']})

    return capacity, activity#, total_emissions


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
        #emissions = read_sheet('Emissions', index_col='Emissions')

    # Calculate total emissions
    #total_emissions = emissions.sum() if not emissions.empty else 0

    # Constructing Capacity and Activity dictionaries
    capacity = {tech: elc_cap.get(tech, 0) for tech in ['E_SOLPV', 'E_WIND', 'E_NGCC', 'E_BATT', 'E_NUCLEAR', 'E_HYDRO', 'E_BIO', 'E_COAL', 'E_DSL', 'E_OIL']}
    capacity.update({tech: trnsprt_cap.get(tech, 0) for tech in ['E_TRANS', 'E_COND', 'E_TWR', 'E_SUB']})

    activity = {tech: elc_act.get(tech, 0) for tech in ['E_SOLPV', 'E_WIND', 'E_NGCC', 'E_BATT', 'E_NUCLEAR', 'E_HYDRO', 'E_BIO', 'E_COAL', 'E_DSL', 'E_OIL']}
    activity.update({tech: trnsprt_act.get(tech, 0) for tech in ['E_TRANS', 'E_COND', 'E_TWR', 'E_SUB']})
    activity.update({tech: supply_act.get(tech, 0) for tech in ['S_IMPNG', 'S_IMPURN', 'S_IMPCOAL', 'S_IMPDSL', 'S_IMPOIL', 'S_IMPBIO']})

    return capacity, activity#, total_emissions


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
        # Function to read and process each sheet
        def read_sheet(sheet_name, index_col='Technology', year=2049):
            df = pd.read_excel(xls, sheet_name)
            df.set_index(index_col, drop=True, inplace=True)
            df.fillna(0, inplace=True)
            return df.loc[:, year] if year in df.columns else df

        # Reading and processing each required sheet
        elc_cap = read_sheet('Capacity_electric').to_dict()
        trnsprt_cap = read_sheet('Capacity_transport').to_dict()
        elc_act = read_sheet('Activity_electric').to_dict()
        trnsprt_act = read_sheet('Activity_transport').to_dict()
        supply_act = read_sheet('Activity_supply').to_dict()
        # emissions_data = read_sheet('Emissions', index_col='Emissions').to_dict()

    #total_emissions = sum(emissions_data.values()) if emissions_data else 0

    # Constructing Capacity and Activity dictionaries with adapted keys
    capacity = {tech: elc_cap.get(tech, 0)for tech in ['E_SOLPV', 'E_WIND', 'E_NGCC', 'E_BATT', 'E_NUCLEAR', 'E_HYDRO', 'E_BIO']}
    capacity.update({tech: trnsprt_cap.get(tech, 0) for tech in ['E_TRANS', 'E_COND', 'E_TWR', 'E_SUB']})

    activity = {tech: elc_act.get(tech, 0) for tech in ['E_SOLPV', 'E_WIND', 'E_NGCC', 'E_BATT', 'E_NUCLEAR', 'E_HYDRO', 'E_BIO']}
    activity.update({tech: trnsprt_act.get(tech, 0) for tech in ['E_TRANS', 'E_COND', 'E_TWR', 'E_SUB']})
    activity.update({tech: supply_act.get(tech, 0) for tech in ['S_IMPNG', 'S_IMPURN', 'S_IMPBIO']})

    return capacity, activity  #, total_emissions