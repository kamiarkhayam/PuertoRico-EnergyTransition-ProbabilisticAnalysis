import pandas as pd
import numpy as np
import os
import time
from utils import *
from input_file_write import *
from output_file_read import *
import warnings
warnings.filterwarnings('ignore')


np.random.seed(1234)

os.chdir('C:\\Users\\bmb2tn\\OneDrive - University of Virginia\\Ph.D. Projects\\Energy PR\\data')

hurricanes = pd.read_csv("puertoRicoHurricanes.csv")

# Calculate the global and specific category rates
rates = calculate_global_rates(hurricanes)
global_rate = rates['global']

# Load the 'PR Wind Speed' data
speed_data = hurricanes['PR Wind Speed'].values

# Fit a log-normal distribution to the 'PR Wind Speed' data and calculate 'mu' and 'sigma'
mu, sigma = fit_lognormal_distribution(speed_data)

# Plot the original wind speed distribution
plot_histogram(speed_data, bins=12, title="Occurrence Max Wind Speed Distribution", xlabel='Max Wind Speed (m/s)', ylabel='Frequency')

# Generate sample data from the fitted log-normal distribution and plot
test_data = np.random.lognormal(mean=mu, sigma=sigma, size=10000)
plot_histogram(test_data, bins=100, title="Histogram of Fitted Distribution to Max Wind Speed", xlabel='Max Wind Speed (m/s)', ylabel='Frequency')

# Calculate and plot the annual occurrences of hurricanes
annual_occurrences = calculate_annual_occurrences(hurricanes, 1851, 2022)
freq = annual_occurrences.value_counts()
number_occurrence_prob = freq / freq.sum()
plot_histogram(number_occurrence_prob.index, bins=4, title="Number of Occurrence per Year PMF", xlabel='Number of Occurrence', ylabel='Probability')

# Generate and plot data for the interval between occurrences
test_intervals = np.random.exponential(1 / 0.8, 10000)
plot_histogram(test_intervals, bins=100, title="Histogram of Fitted Distribution to Interval Between Two Occurrences", xlabel='Occurrence Interval', ylabel='Probability')

components = pd.read_csv('powerNetwork.csv')

# Load population projection data and set the year as the index
population_data = pd.read_csv('populationProj.csv')
population_data.set_index('Year', inplace=True)
# Fit a skewed normal distribution to the population data and save the parameters (commented out for potential future use)
# population_params = fit_skewed_norm_dist(population_data, 'population')
# np.save('populationParams', population_params)
# Load previously saved population distribution parameters
population_params = np.load('populationParams.npy')

# Repeat the process for other datasets
consumption_change_data = pd.read_csv('consumptionChangeProj.csv', index_col=0)
# Fit distribution and save parameters for per capita consumption change (commented out for future use)
# per_capita_params = fit_skewed_norm_dist(consumption_change_data, 'perCapita')
# np.save('perCapitaParams', per_capita_params)
per_capita_params = np.load('perCapitaParams.npy')

gas_price_data = pd.read_csv('ngPriceProj.csv', index_col=0)
# Fit distribution and save parameters for gas price (commented out for future use)
# gas_price_params = fit_skewed_norm_dist(gas_price_data, 'ngPrice')
# np.save('gasPriceParams', gas_price_params)
gas_price_params = np.load('gasPriceParams.npy')

urn_price_data = pd.read_csv('urnPriceProjNorm.csv', index_col=0)
# Fit distribution and save parameters for uranium price (commented out for future use)
# urn_price_params = fit_skewed_norm_dist(urn_price_data, 'urnPrice')
# np.save('urnPriceParams', urn_price_params)
urn_price_params = np.load('urnPriceParams.npy')


# Load data for battery and hydro projects without fitting distributions (as the commented-out fitting process is omitted)
batt_cf_data = pd.read_csv('battCfProj.csv', index_col=0)
batt_fix_data = pd.read_csv('battFixProj.csv', index_col=0)
batt_inv_data = pd.read_csv('battInvProj.csv', index_col=0)
#batt_fix_params = fitSkewedNormDist(batt_fix_data, 'battFix')
#batt_inv_params = fitSkewedNormDist(batt_inv_data, 'battInv')
# np.save('battFixParams', batt_fix_params)
# np.save('urnPriceParams', batt_inv_params)
batt_fix_params = np.load('battFixParams.npy')
batt_inv_params = np.load('battInvParams.npy')

hyd_cf_data = pd.read_csv('hydCfProj.csv', index_col=0)
hyd_fix_data = pd.read_csv('hydFixProj.csv', index_col=0)
hyd_inv_data = pd.read_csv('hydInvProj.csv', index_col=0)
#hyd_fix_params = fitSkewedNormDist(hyd_fix_data, 'hydFix')
#hyd_inv_params = fitSkewedNormDist(hyd_inv_data, 'hydInv')
#np.save('hydFixParams', hyd_fix_params)
#np.save('hydInvParams', hyd_inv_params)
hyd_fix_params = np.load('hydFixParams.npy')
hyd_inv_params = np.load('hydInvParams.npy')


sol_cf_data = pd.read_csv('solCfProj.csv', index_col=0)
sol_fix_data = pd.read_csv('solFixProj.csv', index_col=0)
sol_inv_data = pd.read_csv('solInvProj.csv', index_col=0)
#sol_cf_params = fitSkewedNormDist(sol_cf_data, 'solCF')
#sol_fix_params = fitSkewedNormDist(sol_fix_data, 'solFix')
#sol_inv_params = fitSkewedNormDist(sol_inv_data, 'solInv')
#np.save('solCfParams', sol_cf_params)
#np.save('solFixParams', sol_fix_params)
#np.save('solInvParams', sol_inv_params)
sol_cf_params = np.load('solCfParams.npy')
sol_fix_params = np.load('solFixParams.npy')
sol_inv_params = np.load('solInvParams.npy')

wind_cf_change_data = pd.read_csv('windCfChangeProj.csv', index_col=0)
wind_fix_data = pd.read_csv('windFixProj.csv', index_col=0)
wind_inv_data = pd.read_csv('windInvProj.csv', index_col=0)
#wind_cf_change_params = fitSkewedNormDist(wind_cf_change_data, 'windCF')
#wind_fix_params = fitSkewedNormDist(wind_fix_data, 'windFix')
#wind_inv_params = fitSkewedNormDist(wind_inv_data, 'windInv')
#np.save('windCfChangeParams', wind_cf_change_params)
#np.save('windInvParams', wind_inv_params)
#np.save('windFixParams', wind_fix_params)
wind_cf_change_params = np.load('windCfChangeParams.npy')
wind_inv_params = np.load('windInvParams.npy')
wind_fix_params = np.load('windFixParams.npy')

# Load data for natural gas and nuclear energy projects without fitting distributions
ng_var_data = pd.read_csv('ngVarProj.csv', index_col=0)
ng_fix_data = pd.read_csv('ngFixProj.csv', index_col=0)
ng_inv_data = pd.read_csv('ngInvProj.csv', index_col=0)

nuc_var_data = pd.read_csv('nucVarProj.csv', index_col=0)
nuc_fix_data = pd.read_csv('nucFixProj.csv', index_col=0)
nuc_inv_data = pd.read_csv('nucInvProj.csv', index_col=0)
nuc_cf_data = pd.read_csv('nucCfProj.csv', index_col=0)

# Load data for electricity price change projections
price_change_data = pd.read_csv('changeInElectrcitiyPriceProj.csv', index_col=0)
# Fit distribution and save parameters for electricity price change (commented out for future use)
# price_change_params = fit_skewed_norm_dist(price_change_data, 'priceChange')
# np.save('priceChangeParams', price_change_params)
price_change_params = np.load('priceChangeParams.npy')

template_path = 'C:\\Users\\bmb2tn\\OneDrive - University of Virginia\\Ph.D. Projects\\Energy PR\\codes\\TEMOA\\Temoa\\data_files\\PuertoRico\\PuertoRicoTempFD.txt'
new_file_path = 'C:\\Users\\bmb2tn\\OneDrive - University of Virginia\\Ph.D. Projects\\Energy PR\\codes\\TEMOA\\Temoa\\data_files\\PuertoRico'
new_file_name = 'PR_FD.sql'

temoa_path = 'C:\\Users\\bmb2tn\\OneDrive - University of Virginia\\Ph.D. Projects\\Energy PR\\codes\\TEMOA\\Temoa'
sql_path = new_file_path
sql_name = 'PR_FD'
config_path = new_file_path
config_name = 'config_FD'

output_path = 'C:\\Users\\bmb2tn\\OneDrive - University of Virginia\\Ph.D. Projects\Energy PR\\codes\TEMOA\\Temoa\\data_files\\PuertoRico\\PR_FD_test_run_model'
output_name = 'test_run.xlsx'

input_output_dir = "C:\\Users\\bmb2tn\\OneDrive - University of Virginia\\Ph.D. Projects\\Energy PR\\codes\\simulation\\input_output_pairs"

min_year = 2049
max_year = 2050
 

external_loops = 200
internal_loops = 1000
inputs = []
outputs = []

time_in = time.time()

# Projected costs and capacities for gas and uranium
gas_price, gas_md_price, gas_price_percentile = compute_gas_proj(2020, 2050, 5, gas_price_data, gas_price_params)
urn_price, urn_md_price, urn_price_percentile = compute_uranium_proj(2020, 2050, 5, urn_price_data, urn_price_params)

# Battery energy projections
batt_inv_costs, batt_md_inv_costs, batt_fix_costs, batt_md_fix_costs, _, batt_percentile_inv, batt_percentile_fix = compute_battery_proj(2020, 2050, 5, batt_inv_data, batt_fix_data, batt_cf_data, batt_inv_params, batt_fix_params)

# Hydro energy projections
hyd_inv_costs, hyd_md_inv_costs, hyd_fix_costs, hyd_md_fix_costs, _, hyd_percentile_inv, hyd_percentile_fix = compute_hydro_proj(2020, 2050, 5, hyd_inv_data, hyd_fix_data, hyd_cf_data, hyd_inv_params, hyd_fix_params)

# Solar energy projections
sol_inv_costs, sol_md_inv_costs, sol_fix_costs, sol_md_fix_costs, sol_cfs, sol_md_cfs, sol_percentile_inv, sol_percentile_fix, sol_percentile_cf = compute_solar_proj(2020, 2050, 5, sol_inv_data, sol_fix_data, sol_cf_data, sol_inv_params, sol_fix_params, sol_cf_params)

# Wind energy projections
wind_inv_costs, wind_md_inv_costs, wind_fix_costs, wind_md_fix_costs, wind_cf_changes, wind_md_cf_changes, wind_percentile_inv, wind_percentile_fix, wind_percentile_cf_change = compute_wind_proj(2020, 2050, 5, wind_inv_data, wind_fix_data, wind_cf_change_data, wind_inv_params, wind_fix_params, wind_cf_change_params)

# NGCC energy projections
ng_inv_costs, ng_fix_costs, ng_var_costs = compute_ngcc_proj(2020, 2050, 5, ng_inv_data, ng_fix_data, ng_var_data)

# Nuclear energy projections
nuc_inv_costs, nuc_fix_costs, nuc_var_costs = compute_nuclear_proj(2020, 2050, 5, nuc_inv_data, nuc_fix_data, nuc_var_data)

# Population and Per Capita Consumption projections
population, md_population, pop_percentile = predict_population(2020, 2050, 5, population_data, population_params)
per_capita, md_per_capita, per_capita_percentile = predict_per_capita_consumption(2020, 2050, 5, consumption_change_data, per_capita_params)

# Mean weather condition ratios
md_weather = weather_condition_mean(2020, 2050)  # Assuming min_year and max_year are 2020 and 2050 respectively

# Extracting specific ratios from the mean weather conditions
md_sunny_ratios = np.array([md_weather[0][0], md_weather[1][0], 1 - (md_weather[0][0] + md_weather[1][0])])
md_windy_ratios = np.array([md_weather[2][0], md_weather[3][0], md_weather[4][0], md_weather[5][0], md_weather[6][0], 
                            1 - sum(md_weather[2:7][0])])

# Specific Capacity Factors
sol_cf = sol_cfs['2050']
hyd_cf = 0.49  # Hardcoded value for Hydro CF

# Wind Capacity Factor function coefficients
md_wind_cf_change = wind_cf_changes['2050']
cut_in, rated = 3 * 3.6, 13 * 3.6  # Wind turbine cut-in and rated speeds in m/s
wind_cf1, wind_cf2, wind_cf3, wind_cf4 = compute_wind_cf_func(cut_in, rated, md_wind_cf_change)

demand_mean = write_temoa_input_file_fd(
    template_path, new_file_path, new_file_name,
    md_sunny_ratios, md_windy_ratios, md_population, md_per_capita,
    gas_md_price, urn_md_price,
    ng_var_costs, ng_fix_costs, ng_inv_costs,
    nuc_var_costs, nuc_fix_costs, nuc_inv_costs,
    sol_md_inv_costs, wind_md_inv_costs, hyd_md_inv_costs, batt_md_inv_costs,
    sol_md_fix_costs, wind_md_fix_costs, hyd_md_fix_costs, batt_md_fix_costs,
    hyd_cf, sol_cf, wind_cf1, wind_cf2, wind_cf3, wind_cf4
)

# Uncomment the next line to run the Temoa model with the specified configurations
# run_temoa(temoa_path, sql_path, sql_name, config_path, config_name)

# Reading Temoa model output and adjusting capacities
caps, acts = read_output_fd(output_path, output_name)
caps = {key: value * 1.2 for key, value in caps.items()}  # Adjusting capacities by 20%
nuc_max_act = caps['E_NUCLEAR'] * 365 * 24 / 277.78 * 0.94  # Calculating maximum nuclear activity


# External loop
for k in range(external_loops):
    st_out = time.time()
    
    print(f'Sample no.: {k + 1}')
    
    # Projected gas prices and capacities
    gas_price, gas_md_price, gas_price_percentile = compute_gas_proj(2020, 2050, 5, gas_price_data, gas_price_params)
    urn_price, urn_md_price, urn_price_percentile = compute_uranium_proj(2020, 2050, 5, urn_price_data, urn_price_params)
    
    batt_inv_costs, batt_md_inv_costs, batt_fix_costs, batt_md_fix_costs, _, batt_percentile_inv, batt_percentile_fix = compute_battery_proj(2020, 2050, 5, batt_inv_data, batt_fix_data, batt_cf_data, batt_inv_params, batt_fix_params)
    hyd_inv_costs, hyd_md_inv_costs, hyd_fix_costs, hyd_md_fix_costs, _, hyd_percentile_inv, hyd_percentile_fix = compute_hydro_proj(2020, 2050, 5, hyd_inv_data, hyd_fix_data, hyd_cf_data, hyd_inv_params, hyd_fix_params)
    sol_inv_costs, sol_md_inv_costs, sol_fix_costs, sol_md_fix_costs, sol_cfs, sol_md_cfs, sol_percentile_inv, sol_percentile_fix, sol_percentile_cf = compute_solar_proj(2020, 2050, 5, sol_inv_data, sol_fix_data, sol_cf_data, sol_inv_params, sol_fix_params, sol_cf_params)
    wind_inv_costs, wind_md_inv_costs, wind_fix_costs, wind_md_fix_costs, wind_cf_changes, wind_md_cf_changes, wind_percentile_inv, wind_percentile_fix, wind_percentile_cf_change = compute_wind_proj(2020, 2050, 5, wind_inv_data, wind_fix_data, wind_cf_change_data, wind_inv_params, wind_fix_params, wind_cf_change_params)
    ng_inv_costs, ng_fix_costs, ng_var_costs = compute_ngcc_proj(2020, 2050, 5, ng_inv_data, ng_fix_data, ng_var_data)
    nuc_inv_costs, nuc_fix_costs, nuc_var_costs = compute_nuclear_proj(2020, 2050, 5, nuc_inv_data, nuc_fix_data, nuc_var_data)
    
    # Population and Per Capita Consumption projections
    population, md_population, pop_percentile = predict_population(2020, 2050, 5, population_data, population_params)
    per_capita, md_per_capita, per_capita_percentile = predict_per_capita_consumption(2020, 2050, 5, consumption_change_data, per_capita_params)

    # Demand projection for 2050
    demand_2050 = population['2050'] * per_capita['2050'] / (277.78 * 10**6)

    # Intensity and frequency changes for weather events
    intensity_change = (np.random.lognormal(1.6564, 0.5396) - 2.5) / 100 + 1
    frequency_change = (np.random.lognormal(3.9344, 0.4347) - 65) / 100 + 1

    # Electricity price change projections
    elc_price_change, elc_md_price_change, elc_price_change_percentile = compute_elc_price_proj(2025, 2050, 5, price_change_data, price_change_params, per_capita_percentile)
    
    # Mean weather conditions
    weather = weather_condition_mean(2020, 2050)

    # Sunny and windy ratios based on weather conditions
    sunny_ratios = np.array([weather[0][0], weather[1][0], 1 - (weather[0][0] + weather[1][0])])
    windy_ratios = np.array([weather[2][0], weather[3][0], weather[4][0], weather[5][0], weather[6][0], 1 - sum(weather[2:7][0])])

    # Emission cost rate
    #emission_cost_rate = np.random.lognormal(-3.5, 1.21)

    # Corruption factor for adjustments
    corruption_factor = np.random.uniform(1, 4)
    
    inputs.append([
        urn_price_percentile,  # Uranium price percentile
        batt_percentile_inv,  # Battery investment percentile
        batt_percentile_fix,  # Battery fixed cost percentile
        hyd_percentile_inv,  # Hydro investment percentile
        hyd_percentile_fix,  # Hydro fixed cost percentile
        sol_percentile_inv,  # Solar investment percentile
        sol_percentile_fix,  # Solar fixed cost percentile
        wind_percentile_inv,  # Wind investment percentile
        wind_percentile_fix,  # Wind fixed cost percentile
        pop_percentile,  # Population percentile
        per_capita_percentile,  # Per Capita Consumption percentile
        intensity_change,  # Intensity change for weather events
        frequency_change,  # Frequency change for weather events
        elc_price_change_percentile,  # Electricity price change percentile
        corruption_factor  # Corruption factor
        ])
        
    
    # Fixed and variable costs for 2050
    sol_fix_50 = sol_fix_costs['2050']
    wind_fix_50 = wind_fix_costs['2050']
    batt_fix_50 = batt_fix_costs['2050']
    hyd_fix_50 = hyd_fix_costs['2050']
    ngcc_fix_50 = ng_fix_costs['2050']
    nuc_fix_50 = nuc_fix_costs['2050']

    ngcc_var_50 = ng_var_costs['2050']
    ng_var_50 = gas_price['2050']
    nuc_var_50 = nuc_var_costs['2050']
    urn_var_50 = urn_price['2050']

    trans_var_50 = 0.86  # Assumed value for transmission variable costs
    cond_var_50 = 1.15  # Assumed value for distribution variable costs
    
    wind_farm_no = max(np.floor(caps['E_WIND'] / (np.random.uniform(40, 150) / 1000)), 1) #Assuming each wind farm can have 40-150 MW
    solar_farm_no = max(np.floor(caps['E_SOLPV'] / (np.random.uniform(20, 100) / 1000)), 1) #Assuming each solar farm can have 20-100 MW
    # Since the initial number of substation in data file is 340
    substation_no = np.floor(340 * caps['E_SUB'] / 3.08 / 23.67)
    twr_no = np.floor(4284511 / np.random.uniform(150, 600)) #Considering the transmission line length and the distance between two towers in considered U(150, 600m)
    

    # Store internal results for further analysis
    internal_results = []
    total_costs = []
    mean_of_total_costs = []
    
    for j in range(internal_loops):
        # Modifying Acts based on Weather
        added_cost_ratio = 1
        weather_in = weather_condition(min_year, max_year)
        
        sunny_ratios_in = np.array([weather_in[0][0], weather_in[1][0], 1 - (weather_in[0][0] + weather_in[1][0])])
        windy_ratios_in = np.array([weather_in[2][0], weather_in[3][0], weather_in[4][0], weather_in[5][0], weather_in[6][0], 1 - (weather_in[2][0] + weather_in[3][0] + weather_in[4][0] + weather_in[5][0] + weather_in[6][0])])
        
        const_acts = acts['E_WIND'] + acts['E_SOLPV'] + acts['E_NUCLEAR']
        
        change_in_sol_act = (sunny_ratios_in[0] + 0.5 * sunny_ratios_in[1]) / (sunny_ratios[0] + 0.5 * sunny_ratios[1])
        
        in_avg_wind = (windy_ratios_in[0] * 9.5 + windy_ratios_in[1] * 14.5 + windy_ratios_in[2] * 20.5 + windy_ratios_in[3] * 27.5 + windy_ratios_in[4] * 34.5)
        out_avg_wind = (windy_ratios[0] * 9.5 + windy_ratios[1] * 14.5 + windy_ratios[2] * 20.5 + windy_ratios[3] * 27.5 + windy_ratios[4] * 34.5)
        
        change_in_wind_act = (wind_cf1 * (in_avg_wind * 1.609)**3 + wind_cf2 * (in_avg_wind * 1.609)**2 + wind_cf3 * (in_avg_wind * 1.609) + wind_cf4) / \
                             (wind_cf1 * (out_avg_wind * 1.609)**3 + wind_cf2 * (out_avg_wind * 1.609)**2 + wind_cf3 * (out_avg_wind * 1.609) + wind_cf4)
        change_in_wind_act = min(change_in_wind_act, 1.5)
        
        change_in_sol_act = min(change_in_sol_act, 1.5)
            
        acts_in = acts.copy()
        caps_in = caps.copy()
        #emissions_in = emissions
        
        acts_in['E_SOLPV'] *= change_in_sol_act
        acts_in['E_WIND'] *= change_in_wind_act
        
        acts_in['E_NUCLEAR'] = max(demand_2050 - acts_in['E_SOLPV'] - acts_in['E_WIND'], 0)
        
        if acts_in['E_NUCLEAR'] > nuc_max_act:
            added_cost_ratio = ((acts_in['E_NUCLEAR'] - nuc_max_act) / acts_in['E_NUCLEAR']) * 1.2 + (nuc_max_act / acts_in['E_NUCLEAR'])
    
        acts_in['URN'] = 2.91 * acts_in['E_NUCLEAR']
        
        
        acts_in['E_TRANS'] *= demand_2050 / demand_mean
        acts_in['E_SUB'] *= demand_2050 / demand_mean
        acts_in['E_COND'] *= demand_2050 / demand_mean
        acts_in['E_TWR'] *= demand_2050 / demand_mean
        
        op_cost_undamaged, sol_cost, wind_cost, batt_cost, hyd_cost, nuc_cost, ngcc_cost, trans_cost, cond_cost = compute_normal_op_costs_fd(caps_in, acts_in, sol_fix_50, wind_fix_50, batt_fix_50, ngcc_fix_50, nuc_fix_50, hyd_fix_50, ngcc_var_50, nuc_var_50, trans_var_50, cond_var_50, ng_var_50, urn_var_50, added_cost_ratio)
        
        # Calculate operational cost ratios
        sol_op_ratio = sol_cost * 10**6 / op_cost_undamaged
        wind_op_ratio = wind_cost * 10**6 / op_cost_undamaged
        batt_op_ratio = batt_cost * 10**6 / op_cost_undamaged
        hyd_op_ratio = hyd_cost * 10**6 / op_cost_undamaged
        nuc_op_ratio = nuc_cost * 10**6 / op_cost_undamaged
        ngcc_op_ratio = ngcc_cost * 10**6 / op_cost_undamaged
        trans_op_ratio = trans_cost * 10**6 / op_cost_undamaged
        cond_op_ratio = cond_cost * 10**6 / op_cost_undamaged
        #emission_cost = emission_cost_rate * emissions_in * 10**6

        
        # Unit costs for transmission, distribution, substation, and towers
        trans_unit_cost, cond_unit_cost, sub_unit_cost, twr_unit_cost = 2251.804e6, 1057.159e6, 500.163e6, 634.296e6
        
        # Write grid data based on current capacities and unit costs
        components = write_grid_data(caps, sol_inv_costs, wind_inv_costs, trans_unit_cost, cond_unit_cost, sub_unit_cost, twr_unit_cost)
        
        # Generate occurrences based on a Poisson process with adjusted intensity and frequency
        occurrences = poisson_process_interval(min_year, max_year, global_rate, mu, sigma, frequency_change, intensity_change)
        
        # Initialize data structures for failure probabilities, repair periods, and occurrence costs
        failure_probs = pd.DataFrame()
        all_repair_periods = pd.DataFrame()
        actual_repair_periods = []
        all_occurrence_costs = np.zeros((len(components), len(occurrences)))
        
        
        # Process each occurrence to compute damage and restoration
        for i in range(len(occurrences)):
            occ_no = i + 1
            failure_probs, comp_fail_prob, damage_states = compute_damage(occurrences.iloc[i]['windSpeed'], components, occ_no, failure_probs)
            all_repair_periods, actual_repair_periods = compute_restoration_period(components, comp_fail_prob, occ_no, all_repair_periods, actual_repair_periods, occurrences.iloc[i]['windSpeed'], wind_farm_no, solar_farm_no, substation_no, twr_no)

        # Initialize power outage cost and operational ratios
        power_outage_cost, op_ratio, unop_ratio = 0, 1.0, 0
        lost_load_res, lost_load_com, lost_load_ind = 0, 0, 0

        # Compute power outage impacts and costs if failures are present
        if not failure_probs.empty:
            unop_occ = 1 - np.prod(1 - failure_probs.loc[[0, 1]], axis=0)
            unop_ratio = min(np.sum(unop_occ * np.array(actual_repair_periods)) * corruption_factor, (2050 - occurrences.iloc[0]['year']) * 365) / 365
            op_ratio = 1 - unop_ratio
            
            lost_load = unop_ratio * population['2050'] * per_capita['2050'] / 2 # /2 is because we assumed a linear recovery of system, and the lost load is the area under the triangular recovery function, which is half the rectangular one
            
            lost_load_res = 0.43 * lost_load #ratios from https://www.eia.gov/state/print.php?sid=RQ#:~:text=The%20commercial%20sector%20consumes%20about,of%20the%2050%20U.S.%20states.
            lost_load_com = 0.45 * lost_load
            lost_load_ind = 0.11 * lost_load
            
            lost_load_res = 0.735 * lost_load # Adjusting for solar rooftop

            price_res = elc_price_change['2050'] * 15.64 #cents from https://www.eia.gov/state/print.php?sid=RQ
            price_ind = elc_price_change['2050'] * 12.5
            price_com = elc_price_change['2050'] * 8.5
            
            # Power outage cost based on PREDICTION OF DOMESTIC, INDUSTRIAL AND COMMERCIAL, INTERRUPTION COSTS BY RELATIONAL APPROACH (1997), changing the units from HK$ to $ since the conversion rate has not changed. Also, the values obtained match the 5000$/MWh estimated value of Ercot
            # Compute Value of Lost Load (VoLL) for each sector
            voll_res = (-1.0058 + 0.58 * price_res) * lost_load_res #USD
            voll_com = (-4.585 + 0.991 * price_com) * lost_load_com
            voll_ind = (-1.859 + 0.49 * price_ind) * lost_load_ind
            power_outage_cost = (voll_res + voll_com + voll_ind) / 1.81
            
        # Calculate operational cost taking into account undamaged operational cost and unoperational ratios
        op_cost = op_cost_undamaged * (op_ratio + unop_ratio / 2)   
        
        # Compute undiscounted damage costs
        undisc_dmg_costs = compute_dmg_costs(components, failure_probs, occurrences, min_year)

        total_dmg_cost = sum(sum(undisc_dmg_costs))
        if total_dmg_cost != 0:
            # Calculating the repair ratios for each type of component
            rep_trans_ratio = np.sum(undisc_dmg_costs, axis=1)[0]
            rep_dist_ratio = np.sum(undisc_dmg_costs, axis=1)[1]
            rep_twr_ratio = np.sum(undisc_dmg_costs, axis=1)[2]
            rep_sub_ratio = np.sum(undisc_dmg_costs, axis=1)[3]
            rep_sol_ratio = np.sum(undisc_dmg_costs, axis=1)[4]
            rep_wind_ratio = np.sum(undisc_dmg_costs, axis=1)[5]
        else:
            # Setting repair ratios to 0 if there are no damage costs
            rep_trans_ratio = 0
            rep_dist_ratio = 0
            rep_twr_ratio = 0
            rep_sub_ratio = 0
            rep_sol_ratio = 0
            rep_wind_ratio = 0
        
        # Applying corruption factor to the total damage cost
        total_dmg_cost *= corruption_factor
        
        # Calculating the total cost including operational, damage, and power outage costs
        total_cost = total_dmg_cost + op_cost + power_outage_cost
        
        # Normalization coefficient for total cost to convert PJ to MWh
        coef = 277777.778
        
        # Appending results for this iteration to the internal results list
        internal_results.append([
            float(total_cost) / demand_2050 / coef,  # Normalized total cost
            float(total_dmg_cost) / demand_2050 / coef,  # Normalized damage cost
            op_cost / demand_2050 / coef,  # Normalized operational cost
            power_outage_cost / demand_2050 / coef,  # Normalized power outage cost
            demand_2050,  # Demand for 2050
            voll_res,  # Residential lost load
            voll_com,  # Commercial lost load
            voll_ind,  # Industrial lost load
            np.sum(np.array(actual_repair_periods)),  # Total repair periods
            # Repair ratios normalized by demand
            rep_trans_ratio / demand_2050,
            rep_dist_ratio / demand_2050,
            rep_twr_ratio / demand_2050,
            rep_sub_ratio / demand_2050,
            rep_sol_ratio / demand_2050,
            rep_wind_ratio / demand_2050,
            # Operational cost ratios
            sol_op_ratio,
            wind_op_ratio,
            batt_op_ratio,
            hyd_op_ratio,
            ngcc_op_ratio,
            nuc_op_ratio,
            trans_op_ratio,
            cond_op_ratio,
        ]) 
        
        # Appending the total cost for this iteration to the total costs list
        total_costs.append(float(total_cost))
        
        # Calculating and appending the mean of total costs so far to the list
        mean_of_total_costs.append(np.mean(np.array(total_costs)))

    outputs.append(np.mean(np.array(internal_results), axis=0))

    np.savetxt(os.path.join(input_output_dir, 'outputFD.txt'), np.array(outputs))
    np.savetxt(os.path.join(input_output_dir,'inputFD.txt'), np.array(inputs))
    
    et_out = time.time()
    t_out = et_out - st_out
    print('external loop time = ', t_out)
    
print('Time Elapsed: ', time.time() - time_in)   
