import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
from scipy.stats import skewnorm
from scipy.optimize import differential_evolution
import scipy
from scipy import stats




def calculate_global_rates(hurricanes_df):
    """Calculate global hurricane occurrence rates and specific category combination rates."""
    total_years = max(hurricanes_df["Year"]) - min(hurricanes_df["Year"])
    categories = ['TS', 'H1', 'H2', 'H3', 'H4', 'H5']
    
    # Calculate rate for each category and overall
    rates = {cat: hurricanes_df[hurricanes_df["Max Category"] == cat].shape[0] / total_years for cat in categories}
    rates['global'] = hurricanes_df.shape[0] / total_years

    # Calculate combined category rates
    rates['global_h1ts'] = (rates['TS'] + rates['H1'])
    rates['global_h2h3'] = (rates['H2'] + rates['H3'])
    rates['global_h4h5'] = (rates['H4'] + rates['H5'])

    return rates


def fit_lognormal_distribution(data):
    """
    Fit a log-normal distribution to the given data and calculate parameters mu and sigma.
    
    Parameters:
    - data (array-like): The data to fit the log-normal distribution to.

    Returns:
    - mu (float): The mean of the log-normal distribution.
    - sigma (float): The standard deviation of the log-normal distribution.
    """
    shape, loc, scale = stats.lognorm.fit(data, floc=0)
    mu = np.log(scale)
    sigma = shape
    return mu, sigma

def plot_histogram(data, bins, title, xlabel, ylabel, file_name=None):
    """
    Plot a histogram of the given data.

    Parameters:
    - data (array-like): The data to plot.
    - bins (int): The number of bins for the histogram.
    - title (str): The title of the plot.
    - xlabel (str): The label for the x-axis.
    - ylabel (str): The label for the y-axis.
    - file_name (str, optional): If provided, the plot will be saved to this file.
    """
    plt.clf()
    plt.hist(data, bins=bins, color='black')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if file_name:
        plt.savefig(file_name, dpi=300)
    plt.show()

def calculate_annual_occurrences(hurricanes_df, start_year, end_year):
    """
    Calculate the number of hurricane occurrences per year.

    Parameters:
    - hurricanes_df (DataFrame): The DataFrame containing hurricane data.
    - start_year (int): The start year for the analysis.
    - end_year (int): The end year for the analysis.

    Returns:
    - occur (Series): A Pandas Series with the number of occurrences per year.
    """
    years = np.arange(start_year, end_year + 1)
    occur = [hurricanes_df[hurricanes_df['Year'] == year].shape[0] for year in years]
    return pd.Series(occur, index=years)


def poisson_process_interval(min_year, max_year, rate, mu, sigma, mu_change_ratio, rate_change_ratio):
    """
    Simulate occurrences of events based on a Poisson process with log-normally distributed intervals.

    Parameters:
    - min_year: Start year for the simulation.
    - max_year: End year for the simulation.
    - rate: Initial rate of occurrence per year.
    - mu, sigma: Parameters of the log-normal distribution for event magnitudes.
    - mu_change_ratio, rate_change_ratio: Multipliers to adjust mu and sigma over time.

    Returns:
    - DataFrame with columns 'year' and 'windSpeed' for each simulated event.
    """
    def adjust_mu_sigma(mean, std, mu_change_ratio):
        """Adjust mu and sigma based on the change ratio."""
        mean *= mu_change_ratio
        mu = np.log(mean**2 / np.sqrt(std**2 + mean**2))
        sigma = np.sqrt(np.log(std**2 / mean**2 + 1))
        return mu, sigma
    
    events = []  # List to store event data
    rate *= rate_change_ratio  # Adjust initial rate based on rate change ratio
    mean, std = np.exp(mu + sigma**2 / 2), np.sqrt((np.exp(sigma**2) - 1) * np.exp(2*mu + sigma**2))
    mu, sigma = adjust_mu_sigma(mean, std, mu_change_ratio)  # Adjust mu and sigma based on change ratio

    current_year = min_year
    while current_year < max_year:
        interval = np.random.exponential(1 / rate)  # Generate time until next event
        current_year += interval  # Update current year by adding the interval

        if current_year >= max_year:  # Stop if the current year exceeds the maximum year
            break

        windSpeed = np.random.lognormal(mu, sigma)  # Generate event magnitude
        events.append({'year': current_year, 'windSpeed': windSpeed})

    occurrences = pd.DataFrame(events)  # Create DataFrame from list of events
    return occurrences


def compute_damage(max_wind_speed, components, occ_no, failure_probs):
    """
    Compute the damage to components based on max wind speed.
    
    Parameters:
    - max_wind_speed: The maximum wind speed in the occurrence.
    - components: DataFrame containing information about the components.
    - occ_no: The occurrence number.
    - failure_probs: DataFrame to store the failure probabilities of components.

    Returns:
    - Updated failure_probs DataFrame, list of component failure probabilities, and list of damage states.
    """
    
    
    def get_failure_params(max_wind_speed, component_type):
        """
        Get the mean and standard deviation for the failure probability based on component type and max wind speed.
    
        Parameters:
        - max_wind_speed: The maximum wind speed in the occurrence.
        - component_type: The type of the component.
    
        Returns:
        - mean, std: Mean and standard deviation for the failure probability.
        """
        if component_type == 'Distribution Line':
            mean = 8 * 10**-12 * (max_wind_speed * 2.237)**5.1731
            # Source: https://woodpoles.org/portals/2/documents/UndergroundingAssessment_P3.pdf
        elif component_type == 'Tower':
            mean = stats.lognorm.cdf(max_wind_speed, s=0.224, scale=82.88, loc=0)
            # Source: Power System Resilience to Extreme Weather: Fragility Modeling, Probabilistic Impact Assessment, and Adaptation Measures
        elif component_type == 'Transmission Line':
            mean = 2 * 10**-7 * np.exp(max_wind_speed * 2.237 * 0.0834)
            # Source: Watson, E. Modeling Electrical Grid Resilience under Hurricane Wind Conditions with Increased Solar Photovoltaic and Wind Turbine Power Generation. (George Washington University, 2018).
        elif component_type == 'Substation':
            moderate_prob = stats.norm.cdf((np.log(max_wind_speed * 2.237) - 5.068) / 0.136)
            severe_prob = stats.norm.cdf((np.log(max_wind_speed * 2.237) - 5.204) / 0.147)
            comp_prob = stats.norm.cdf((np.log(max_wind_speed * 2.237) - 5.523) / 0.132)
            no_damage_prob = 1 - moderate_prob - severe_prob - comp_prob
            mean = no_damage_prob * 0 + moderate_prob * 0.05 + severe_prob * 0.4 + comp_prob * 0.7
            # Source: Watson, E. Modeling Electrical Grid Resilience under Hurricane Wind Conditions with Increased Solar Photovoltaic and Wind Turbine Power Generation. (George Washington University, 2018).
        elif component_type == 'Wind Generator':
            mean = ((max_wind_speed * 1.944 / 139.6)**18.6) / (1 + ((max_wind_speed * 1.944 / 139.6)**18.6))
            # Source: Quantifying the Hurricane Catastrophe Risk to Offshore Wind Power
        elif component_type == 'Solar Generator':
            mean = stats.lognorm.cdf(max_wind_speed * 2.237, s=0.14, scale=129.346, loc=0)
            # Source: PERFORMANCE MEASURES FOR RESIDENTIAL PV STRUCTURAL RESPONSE TO WIND EFFECTS
    
        std = 0.1 * mean  # Assuming a standard deviation as 10% of the mean as a generic approach
    
        return mean, std
  
    comp_fail_prob = []
    damage_states = []
   
    for _, component in components.iterrows():
        component_type = component['Type']
        mean, std = get_failure_params(max_wind_speed, component_type)

        # Compute the probability of failure and determine the damage state
        fail_prob = np.clip(np.random.normal(loc=mean, scale=std), 0, 1)
        comp_fail_prob.append(fail_prob)
        damage_state = int(np.random.uniform() < fail_prob)
        damage_states.append(damage_state)

    # Store the failure probabilities for this occurrence
    failure_probs[f"{occ_no}_fail_prob"] = comp_fail_prob

    return failure_probs, comp_fail_prob, damage_states



def compute_restoration_period(components, comp_fail_prob, occ_no, all_repair_periods, actual_repair_periods, max_wind_speed,
                                wind_farm_no, solar_farm_no, substation_no, twr_no):

    def determine_repair_teams(wind_speed):
        """
        Determines the number of repair teams based on the wind speed.
        The number of teams is determined by predefined ranges of wind speeds.

        Parameters:
        - wind_speed: The maximum wind speed recorded during the occurrence.

        Returns:
        - A float representing the number of repair teams.
        """
        if wind_speed > 58:
            return np.random.uniform(300, 350)
        elif wind_speed > 43:
            return np.random.uniform(150, 300)
        elif wind_speed > 32:
            return np.random.uniform(100, 150)
        else:
            return np.random.uniform(50, 100)

    def calculate_repair_period(component_type, line_length, fail_prob):
        """
        Calculates the repair period for each component type based on its characteristics and failure probability.
        Different strategies are applied for different types of components, taking into account their unique attributes
        and the impact of the failure probability.

        Parameters:
        - component_type: The type of the component.
        - line_length: The length of the line for line-based components.
        - fail_prob: The failure probability of the component.

        Returns:
        - A float representing the repair period for the component.
        """
        if component_type == 'Distribution Line':
            # Calculations based on assumed pole distance and Biazar's Master Thesis for Distribution Line repair time estimation.
            no_poles = np.floor(line_length / np.random.uniform(50, 100))
            total_repair_period = (line_length / 1000) + no_poles * 0.125
            return max(np.random.normal(loc=total_repair_period, scale=0.2 * total_repair_period), 0) * fail_prob

        elif component_type == 'Tower':
            # Tower repair times based on 'Restoration and functionality assessment of a community subjected to tornado hazard'.
            return np.clip(np.random.normal(loc=2, scale=1), 1, 4) * twr_no * fail_prob

        elif component_type == 'Transmission Line':
            # Transmission Line repair times are considered twice that of Distribution Lines for simplicity, as per community restoration studies.
            total_repair_period = (line_length / 1000) * 2
            return max(np.random.normal(loc=total_repair_period, scale=0.2 * total_repair_period), 0) * fail_prob

        elif component_type == 'Substation':
            # Substation repair times interpolated from HAZUS for generation plants.
            repair_periods = [(1, 0.5), (3, 1.5), (7, 3.5), (30, 15)]
            for boundary, periods in zip([0.05, 0.11, 0.55, 1], repair_periods):
                if fail_prob <= boundary:
                    mean, std = periods
                    break
            return max(np.random.normal(loc=mean, scale=std), mean / 3) * substation_no

        elif component_type in ['Wind Generator', 'Solar Generator']:
            # Repair times for Wind and Solar Generators are based on hazard analysis for renewable energy sources.
            repair_periods = [(5, 0.1), (3.6, 3.6), (22, 21), (65, 30)]
            for boundary, periods in zip([0.05, 0.11, 0.55, 1], repair_periods):
                if fail_prob <= boundary:
                    mean, std = periods
                    break
            return max(np.random.normal(loc=mean, scale=std), mean / 3) * (wind_farm_no if component_type == 'Wind Generator' else solar_farm_no)

    # Initialize an array to store repair periods for all components for the current occurrence.
    occ_repair_periods = np.zeros((len(components)))
    # Determine the number of repair teams available based on the maximum wind speed for the occurrence.
    no_teams = determine_repair_teams(max_wind_speed)

    # Iterate over all components to compute individual repair periods.
    for i, component in components.iterrows():
        if comp_fail_prob[i] > 0:  # Only consider components with a non-zero failure probability.
            repair_period = calculate_repair_period(component['Type'], component['Line Length'], comp_fail_prob[i])
            occ_repair_periods[i] = repair_period

    # Update the dataframe with repair periods for the current occurrence.
    all_repair_periods[str(occ_no) + 'RepTime'] = occ_repair_periods
    # Calculate the total repair period for the occurrence and constrain it to a maximum of one year (365 days).
    occ_total_repair_period = sum(occ_repair_periods)
    occ_actual_repair_period = min(occ_total_repair_period / no_teams, 365)
    # Append the actual repair period for the occurrence to the list of periods.
    actual_repair_periods.append(occ_actual_repair_period)

    # Return the updated dataframes with all repair periods and actual repair periods for each occurrence.
    return all_repair_periods, actual_repair_periods



def compute_dmg_costs(components, failure_probs, occurrences, min_year, inflation_rate=1):
    """
    Computes the damage costs based on component replacement costs, failure probabilities, and occurrences.

    Parameters:
    - components: A DataFrame containing component information, including replacement costs.
    - failure_probs: A DataFrame containing the failure probabilities of components for each occurrence.
    - occurrences: A DataFrame containing information about each occurrence, including the year.
    - min_year: The minimum year from the occurrences to calculate inflation adjustments from.
    - inflation_rate: The annual inflation rate, defaulted to 1 (no inflation).

    Returns:
    - A 2D NumPy array containing the adjusted replacement costs for each component and occurrence.
    """

    if len(occurrences) > 0:
        rand_replacement_cost = np.zeros((len(components), len(occurrences)))

        # Generate random replacement costs based on a normal distribution around the listed replacement cost.
        for i in range(len(components)):
            for j in range(len(occurrences)):
                rand_replacement_cost[i, j] = np.random.normal(
                    loc=components['Replacement Cost'][i], scale=0.1 * components['Replacement Cost'][i])

        # Calculate the replacement costs by multiplying the random costs with the failure probabilities.
        replacement_costs = np.array(rand_replacement_cost) * np.array(failure_probs)

        # Adjust for inflation if the inflation rate is not 1 (no inflation).
        if inflation_rate != 1:
            for j, occurrence in occurrences.iterrows():
                year = occurrence['year']
                # Calculate the inflation coefficient based on the year of occurrence and the minimum year.
                coefficient = inflation_rate ** (year - min_year)
                # Apply the inflation adjustment to the replacement costs for the occurrence.
                replacement_costs[:, j] *= coefficient
    else:
        # If there are no occurrences, initialize the replacement costs to zero.
        replacement_costs = np.zeros((len(components), 1))

    return replacement_costs


def discount_dmg_costs(replacement_costs, occurrences, base_year, discount_rate=1.0):
    """
    Applies discounting to the replacement costs based on the year of occurrence, accounting for the time value of money.

    Parameters:
    - replacement_costs: A 2D NumPy array containing the adjusted replacement costs for each component and occurrence.
    - occurrences: A DataFrame containing information about each occurrence, including the year.
    - base_year: The base year for discounting calculations.
    - discount_rate: The annual discount rate, defaulted to 1.0 (no discount).

    Returns:
    - The total discounted replacement costs across all occurrences.
    """

    # Ensure the replacement costs are in a NumPy array format for element-wise operations.
    replacement_costs = np.array(replacement_costs)

    # Apply discounting to each column (occurrence) in the replacement costs array.
    for j in range(len(occurrences)):
        year = occurrences['year'][j]
        # Calculate the discount coefficient based on the difference between the occurrence year and the base year.
        coefficient = discount_rate ** (year - base_year)
        # Discount the replacement costs for the occurrence.
        replacement_costs[:, j] /= coefficient

    # Sum the discounted replacement costs across all occurrences to get the total costs.
    total_costs = np.sum(replacement_costs, axis=0)

    return total_costs


def compute_discounted_operational_costs(occurrences, repair_done_times, min_year, max_year, op_costs, base_year, disc_rate=1.0):
    """
    Computes the discounted operational costs considering the periods when components are operational post-repair.

    Parameters:
    - occurrences: A DataFrame containing information about each occurrence, including the year.
    - repair_done_times: A NumPy array indicating the year by which repairs are completed for each occurrence.
    - min_year: The minimum year from the occurrences for calculation.
    - max_year: The maximum year considered for operational costs calculation.
    - op_costs: A NumPy array of operational costs per component per year.
    - base_year: The base year for discounting calculations.
    - disc_rate: The discount rate for discounting future costs to present value.

    Returns:
    - disc_costs: The discounted operational costs for each period.
    - total_undamaged_periods: The total number of undamaged (operational) periods across all occurrences.
    """

    if len(occurrences) != 0:
        # Calculate the end times for operational periods, assuming each occurrence marks the start of a new period.
        end_times = np.array(occurrences['year'][1:])
        end_times = np.append(end_times, max_year)
        
        # Determine the undamaged (operational) periods by subtracting the repair done times from the end times.
        undamaged_periods = np.maximum(end_times - repair_done_times, np.zeros(end_times.shape))
    else:
        # If there are no occurrences, consider the entire period as undamaged.
        undamaged_periods = np.ones((1, ))

    # Calculate the undiscounted operational costs for each undamaged period.
    undisc_costs = undamaged_periods * np.random.normal(loc=np.sum(op_costs), scale=0.1 * np.sum(op_costs))

    # Determine the representative year for each undamaged period for discounting purposes.
    if len(occurrences) != 0:
        undamaged_periods_reps = repair_done_times + undamaged_periods * 0.5
    else:
        undamaged_periods_reps = 0.5 * (min_year + max_year)

    # Calculate the discount coefficients for each period based on the representative years.
    disc_coefs = disc_rate ** (undamaged_periods_reps - base_year)

    # Discount the operational costs to present value.
    disc_costs = undisc_costs / disc_coefs

    # Sum the undamaged periods to get the total operational time.
    total_undamaged_periods = np.sum(undamaged_periods)

    return disc_costs, total_undamaged_periods
    
    
    
def weather_condition(min_year, max_year):
    """
    Generates simulated weather conditions based on historical climate data.

    Parameters:
    - min_year: The starting year for the simulation.
    - max_year: The ending year for the simulation.

    Returns:
    - A list containing the yearly ratios for different weather conditions.

    Source for historical climate data: 
    https://www.meteoblue.com/en/weather/historyclimate/climatemodelled/puerto-rico_puerto-rico_4566967
    """
    
    year_span = np.arange(min_year, max_year)
    
    # Initialize lists to hold yearly weather condition ratios
    sunny_ratio, partly_cloudy_ratio = [], []
    windy_ratio_7_12mph, windy_ratio_12_17mph, windy_ratio_17_24mph, windy_ratio_24_31mph, windy_ratio_31_38mph = [], [], [], [], []

    # Mean values for each weather condition based on historical data
    sunny_ratio_mean = 101.2
    partly_cloudy_ratio_mean = 214.9
    windy_ratio_7_12mph_mean = 110.7
    windy_ratio_12_17mph_mean = 197.3
    windy_ratio_17_24mph_mean = 30.1
    windy_ratio_24_31mph_mean = 0.7
    windy_ratio_31_38mph_mean = 0.1
    
    for y in year_span:
        # Generate yearly weather condition ratios based on normal distribution around historical means
        sunny_ratio.append(max(min(np.random.normal(loc=sunny_ratio_mean, scale=0.2 * sunny_ratio_mean), 365) / 365, 0))
        partly_cloudy_ratio.append(max(min(np.random.normal(loc=partly_cloudy_ratio_mean, scale=0.2 * partly_cloudy_ratio_mean), 365) / 365, 0))
        windy_ratio_7_12mph.append(max(min(np.random.normal(loc=windy_ratio_7_12mph_mean, scale=0.2 * windy_ratio_7_12mph_mean), 365) / 365, 0))
        windy_ratio_12_17mph.append(max(min(np.random.normal(loc=windy_ratio_12_17mph_mean, scale=0.2 * windy_ratio_12_17mph_mean), 365) / 365, 0))
        windy_ratio_17_24mph.append(max(min(np.random.normal(loc=windy_ratio_17_24mph_mean, scale=0.2 * windy_ratio_17_24mph_mean), 365) / 365, 0))
        windy_ratio_24_31mph.append(max(min(np.random.normal(loc=windy_ratio_24_31mph_mean, scale=0.2 * windy_ratio_24_31mph_mean), 365) / 365, 0))
        windy_ratio_31_38mph.append(max(min(np.random.normal(loc=windy_ratio_31_38mph_mean, scale=0.2 * windy_ratio_31_38mph_mean), 365) / 365, 0))
        
        # Ensure the sum of sunny and partly cloudy ratios does not exceed 1
        if sunny_ratio[-1] + partly_cloudy_ratio[-1] >= 1:
            coef = 0.9 / (sunny_ratio[-1] + partly_cloudy_ratio[-1])
            sunny_ratio[-1] *= coef
            partly_cloudy_ratio[-1] *= coef
            
        # Ensure the sum of all windy condition ratios does not exceed 1
        total_windy = sum([windy_ratio_7_12mph[-1], windy_ratio_12_17mph[-1], windy_ratio_17_24mph[-1], windy_ratio_24_31mph[-1], windy_ratio_31_38mph[-1]])
        if total_windy >= 1:
            coef = 0.95 / total_windy
            windy_ratio_7_12mph[-1] *= coef
            windy_ratio_12_17mph[-1] *= coef
            windy_ratio_17_24mph[-1] *= coef
            windy_ratio_24_31mph[-1] *= coef
            windy_ratio_31_38mph[-1] *= coef
    
    # Aggregate all weather condition ratios into a single list
    weather_conditions = [
        sunny_ratio, partly_cloudy_ratio, windy_ratio_7_12mph, windy_ratio_12_17mph,
        windy_ratio_17_24mph, windy_ratio_24_31mph, windy_ratio_31_38mph
    ]
    
    return weather_conditions



def weather_condition_mean(min_year, max_year):
    """
    Generates mean weather conditions based on historical climate data for a given range of years.

    Parameters:
    - min_year: The starting year for the simulation.
    - max_year: The ending year for the simulation.

    Returns:
    - A list containing the mean yearly ratios for different weather conditions.

    Source for historical climate data:
    https://www.meteoblue.com/en/weather/historyclimate/climatemodelled/puerto-rico_puerto-rico_4566967
    """
    
    year_span = np.arange(min_year, max_year)
    
    # Initialize lists to hold yearly weather condition ratios
    sunny_ratio, partly_cloudy_ratio = [], []
    windy_ratio_7_12mph, windy_ratio_12_17mph, windy_ratio_17_24mph, windy_ratio_24_31mph, windy_ratio_31_38mph = [], [], [], [], []

    # Mean values for each weather condition based on historical data
    sunny_ratio_mean = 101.2
    partly_cloudy_ratio_mean = 214.9
    windy_ratio_7_12mph_mean = 110.7
    windy_ratio_12_17mph_mean = 197.3
    windy_ratio_17_24mph_mean = 30.1
    windy_ratio_24_31mph_mean = 0.7
    windy_ratio_31_38mph_mean = 0.1
    
    for y in year_span:
        # Directly use mean values for each weather condition since scale is set to 0
        sunny_ratio.append(max(min(sunny_ratio_mean, 365) / 365, 0))
        partly_cloudy_ratio.append(max(min(partly_cloudy_ratio_mean, 365) / 365, 0))
        windy_ratio_7_12mph.append(max(min(windy_ratio_7_12mph_mean, 365) / 365, 0))
        windy_ratio_12_17mph.append(max(min(windy_ratio_12_17mph_mean, 365) / 365, 0))
        windy_ratio_17_24mph.append(max(min(windy_ratio_17_24mph_mean, 365) / 365, 0))
        windy_ratio_24_31mph.append(max(min(windy_ratio_24_31mph_mean, 365) / 365, 0))
        windy_ratio_31_38mph.append(max(min(windy_ratio_31_38mph_mean, 365) / 365, 0))
        
        # Adjust ratios if their sum exceeds 1
        if sunny_ratio[-1] + partly_cloudy_ratio[-1] >= 1:
            coef = 0.9 / (sunny_ratio[-1] + partly_cloudy_ratio[-1])
            sunny_ratio[-1] *= coef
            partly_cloudy_ratio[-1] *= coef
            
        total_windy = sum([windy_ratio_7_12mph[-1], windy_ratio_12_17mph[-1], windy_ratio_17_24mph[-1], windy_ratio_24_31mph[-1], windy_ratio_31_38mph[-1]])
        if total_windy >= 1:
            coef = 0.95 / total_windy
            windy_ratio_7_12mph[-1] *= coef
            windy_ratio_12_17mph[-1] *= coef
            windy_ratio_17_24mph[-1] *= coef
            windy_ratio_24_31mph[-1] *= coef
            windy_ratio_31_38mph[-1] *= coef
    
    # Aggregate all mean weather condition ratios into a single list
    weather_conditions = [
        sunny_ratio, partly_cloudy_ratio, windy_ratio_7_12mph, windy_ratio_12_17mph,
        windy_ratio_17_24mph, windy_ratio_24_31mph, windy_ratio_31_38mph
    ]
    
    return weather_conditions


def fit_skewnorm(p5, p50, p95, lower_bound=0, upper_bound=5000):
    
    def objective(params):
        xi, omega, alpha = params
        return (skewnorm.ppf(0.05, alpha, xi, omega) - p5)**2 + \
               (skewnorm.ppf(0.50, alpha, xi, omega) - p50)**2 + \
               (skewnorm.ppf(0.95, alpha, xi, omega) - p95)**2
    
    # Bounds for parameters, assuming you have some reasonable range in mind
    bounds = [(lower_bound, upper_bound), (0.01, 1000), (-100, 100)]
    
    result = differential_evolution(objective, bounds)
    
    return result.x

def skewnorm_inv_cdf(probability, xi, omega, alpha):
    
    return skewnorm.ppf(probability, alpha, xi, omega)


def fit_skewed_norm_dist(data, data_type):
    
    params = []
    if data_type == 'population':
        for i in range(len(data)):
            p95 = data['95% Upper Bound'].iloc[i] + 0.1
            p5 = data['95% Lower Bound'].iloc[i] - 0.1
            p50 = data['Median'].iloc[i] - 0.1
            
            xi_est, omega_est, alpha_est = fit_skewnorm(p5, p50, p95, 2500, 3500)

            params.append([xi_est, omega_est, alpha_est])
            
    elif data_type == 'perCapita':
        for i in range(len(data)):
            p95 = data['High'].iloc[i] + 0.01
            p5 = data['Low'].iloc[i] - 0.01
            p50 = data['Median'].iloc[i]
            
            xi_est, omega_est, alpha_est = fit_skewnorm(p5, p50, p95, 0.9, 2)
            
            params.append([xi_est, omega_est, alpha_est])
    
    elif data_type == 'ngPrice':
        for i in range(len(data)):
            p95 = data['max'].iloc[i] + 0.1
            p5 = data['min'].iloc[i] - 0.1
            p50 = data['median'].iloc[i]
            
            xi_est, omega_est, alpha_est = fit_skewnorm(p5, p50, p95, 0, 10)
            
            params.append([xi_est, omega_est, alpha_est])
            
    elif data_type == 'urnPrice':
        for i in range(len(data)):
            p95 = data['90p'].iloc[i] + 0.1
            p5 = data['10p'].iloc[i] - 0.1
            p50 = data['Mean'].iloc[i]
            
            xi_est, omega_est, alpha_est = fit_skewnorm(p5, p50, p95, 0, 2)
            
            params.append([xi_est, omega_est, alpha_est])
            
    elif data_type == 'hydInv':
        for i in range(len(data)):
            p95 = data['Inv Max'].iloc[i] + 1
            p5 = data['Inv Min'].iloc[i] - 1
            p50 = data['Inv Median'].iloc[i]
            
            xi_est, omega_est, alpha_est = fit_skewnorm(p5, p50, p95, 2200, 2600)
            
            params.append([xi_est, omega_est, alpha_est])
            
    elif data_type == 'hydFix':
        for i in range(len(data)):
            p95 = data['Fix Max'].iloc[i] + 0.1
            p5 = data['Fix Min'].iloc[i] - 0.1
            p50 = data['Fix Median'].iloc[i]
            
            xi_est, omega_est, alpha_est = fit_skewnorm(p5, p50, p95, 55, 65)
            
            params.append([xi_est, omega_est, alpha_est])
    
    elif data_type == 'solInv':
        for i in range(len(data)):
            p95 = data['Inv Max'].iloc[i] + 1
            p5 = data['Inv Min'].iloc[i] - 1
            p50 = data['Inv Median'].iloc[i]
            
            xi_est, omega_est, alpha_est = fit_skewnorm(p5, p50, p95, 400, 1200)
            
            params.append([xi_est, omega_est, alpha_est])
            
    elif data_type == 'solFix':
        for i in range(len(data)):
            p95 = data['Fix Max'].iloc[i] + 0.1
            p5 = data['Fix Min'].iloc[i] - 0.1
            p50 = data['Fix Median'].iloc[i]
            
            xi_est, omega_est, alpha_est = fit_skewnorm(p5, p50, p95, 10, 25)
            
            params.append([xi_est, omega_est, alpha_est])
            
    elif data_type == 'solCF':
        for i in range(len(data)):
            p95 = data['CF Max'].iloc[i]+ 0.01
            p5 = data['CF Min'].iloc[i] - 0.01
            p50 = data['CF Median'].iloc[i]
            
            xi_est, omega_est, alpha_est = fit_skewnorm(p5, p50, p95, 0.2, 0.5)
            
            params.append([xi_est, omega_est, alpha_est])
            
    elif data_type == 'windInv':
        for i in range(len(data)):
            p95 = data['Inv Max'].iloc[i] + 1 
            p5 = data['Inv Min'].iloc[i] - 1
            p50 = data['Inv Median'].iloc[i]
            
            xi_est, omega_est, alpha_est = fit_skewnorm(p5, p50, p95, 500, 1500)
            
            params.append([xi_est, omega_est, alpha_est])
            
    elif data_type == 'windFix':
        for i in range(len(data)):
            p95 = data['Fix Max'].iloc[i] + 0.1
            p5 = data['Fix Min'].iloc[i] - 0.1
            p50 = data['Fix Median'].iloc[i]
            
            xi_est, omega_est, alpha_est = fit_skewnorm(p5, p50, p95, 25, 50)
            
            params.append([xi_est, omega_est, alpha_est])
    
    elif data_type == 'windCF':
        for i in range(len(data)):
            p95 = data['CF Max'].iloc[i] + 0.01
            p5 = data['CF Min'].iloc[i] - 0.01
            p50 = data['CF Median'].iloc[i]
            
            xi_est, omega_est, alpha_est = fit_skewnorm(p5, p50, p95, 0.9, 1.2)
            
            params.append([xi_est, omega_est, alpha_est])
            
    elif data_type == 'battInv':
        for i in range(len(data)):
            p95 = data['Inv Max'].iloc[i] + 1
            p5 = data['Inv Min'].iloc[i] - 1
            p50 = data['Inv Median'].iloc[i]
            
            xi_est, omega_est, alpha_est = fit_skewnorm(p5, p50, p95, 900, 3500)
            
            params.append([xi_est, omega_est, alpha_est])
            
    elif data_type == 'battFix':
        for i in range(len(data)):
            p95 = data['Fix Max'].iloc[i] + 0.1
            p5 = data['Fix Min'].iloc[i] - 0.1
            p50 = data['Fix Median'].iloc[i]
            
            xi_est, omega_est, alpha_est = fit_skewnorm(p5, p50, p95, 20, 85)
            
            params.append([xi_est, omega_est, alpha_est])
    
    elif data_type == 'coalPrice':
        for i in range(len(data)):
            p95 = data['High'].iloc[i] + 0.1
            p5 = data['Low'].iloc[i] - 0.1
            p50 = data['Median'].iloc[i]
            
            xi_est, omega_est, alpha_est = fit_skewnorm(p5, p50, p95, 3, 4)
            
            params.append([xi_est, omega_est, alpha_est])
            
    elif data_type == 'oilPrice':
        for i in range(len(data)):
            p95 = data['High'].iloc[i] + 0.1
            p5 = data['Low'].iloc[i] - 0.1
            p50 = data['Median'].iloc[i]
            
            xi_est, omega_est, alpha_est = fit_skewnorm(p5, p50, p95, 10, 16)
            
            params.append([xi_est, omega_est, alpha_est])
            
    elif data_type == 'dslPrice':
        for i in range(len(data)):
            p95 = data['High'].iloc[i] + 0.1
            p5 = data['Low'].iloc[i] - 0.1
            p50 = data['Median'].iloc[i]
            
            xi_est, omega_est, alpha_est = fit_skewnorm(p5, p50, p95, 17, 22)
            
            params.append([xi_est, omega_est, alpha_est])
            
    elif data_type == 'coalInv':
        for i in range(len(data)):
            p95 = data['High'].iloc[i] + 1
            p5 = data['Low'].iloc[i] - 1
            p50 = data['Median'].iloc[i]
            
            xi_est, omega_est, alpha_est = fit_skewnorm(p5, p50, p95, 2200, 3500)
            
            params.append([xi_est, omega_est, alpha_est])
            
    elif data_type == 'coalFix':
        for i in range(len(data)):
            p95 = data['High'].iloc[i] + 0.1
            p5 = data['Low'].iloc[i] - 0.1
            p50 = data['Median'].iloc[i]
            
            xi_est, omega_est, alpha_est = fit_skewnorm(p5, p50, p95, 60, 75)
            
            params.append([xi_est, omega_est, alpha_est])
        
    elif data_type == 'coalVar':
        for i in range(len(data)):
            p95 = data['High'].iloc[i] + 0.01
            p5 = data['Low'].iloc[i] - 0.01
            p50 = data['Median'].iloc[i]
            
            xi_est, omega_est, alpha_est = fit_skewnorm(p5, p50, p95, 1.5, 2.5)
            
            params.append([xi_est, omega_est, alpha_est])
            
            
    elif data_type == 'priceChange':
        for i in range(len(data)):
            p95 = data['Max'].iloc[i] + 0.01
            p5 = data['Min'].iloc[i] - 0.01
            p50 = data['Median'].iloc[i]
            
            xi_est, omega_est, alpha_est = fit_skewnorm(p5, p50, p95, 0.8, 1.2)
            
            params.append([xi_est, omega_est, alpha_est])    
    
    else:
        print('wrong input')
        return -1
    
    
    return np.array(params)


def predict_population(min_year, max_year, interval, data, params):
    """
    Predicts population sizes based on skewed normal distribution parameters for specified years.

    Parameters:
    - min_year: The starting year for predictions.
    - max_year: The ending year for predictions.
    - interval: The interval between prediction years.
    - data: A dictionary containing median population data for each year.
    - params: A NumPy array containing the parameters (location, scale, shape) for the skew normal distribution.

    Returns:
    - A tuple containing two dictionaries with predicted populations and median populations, and the percentile used for predictions.
    """
    percentile = np.random.uniform(0, 1)  # Random percentile for population size prediction
    predicted_population = {}
    median_population = {}
    param_index = 0

    for year in range(min_year, max_year + interval, interval):
        year_str = str(year)
        median = data['Median'][year]  # Median population for the year

        # Predict population size using the inverse CDF of the skew normal distribution
        predicted_pop = skewnorm_inv_cdf(percentile, *params[param_index]) * 1000

        predicted_population[year_str] = predicted_pop
        median_population[year_str] = median * 1000  # Convert to absolute population size

        param_index += 5  # Assuming parameters are spaced 5 years apart

    return predicted_population, median_population, percentile



def predict_per_capita_consumption(min_year, max_year, interval, data, params):
    """
    Predicts per capita energy consumption based on skewed normal distribution parameters for specified years.

    Parameters:
    - min_year: The starting year for predictions.
    - max_year: The ending year for predictions.
    - interval: The interval between prediction years.
    - data: A DataFrame containing median energy consumption data for each year.
    - params: A NumPy array containing the parameters (location, scale, shape) for the skew normal distribution.

    Returns:
    - A tuple containing two dictionaries with predicted and median per capita energy consumption, and the percentile used for predictions.

    Source for data:
    https://www.eia.gov/outlooks/aeo/data/browser/#/?id=8-AEO2022&region=0-0&cases=ref2022~highmacro~lowmacro&start=2020&end=2050&f=A&linechart=~~~ref2022-d011222a.13-8-AEO2022~highmacro-d011622a.13-8-AEO2022~lowmacro-d011222a.13-8-AEO2022&ctype=linechart&chartindexed=0&sourcekey=0
    Unit: kWh
    """
    percentile = np.random.uniform(0, 1)
    predicted_consumption = {}
    median_consumption = {}
    param_index = 0

    for year in range(min_year, max_year + interval, interval):
        year_str = str(year)
        median = data.loc[year]['Median']

        # Coefficient relative to Puerto Rico 2021 electricity production (5602 kWh)
        coef = skewnorm_inv_cdf(percentile, *params[param_index])

        predicted_consumption[year_str] = 5602 * coef  # kWh
        median_consumption[year_str] = 5602 * median  # kWh

        param_index += 5  # Assuming parameters are spaced 5 years apart

    return predicted_consumption, median_consumption, percentile



def compute_gas_proj(min_year, max_year, interval, data, params):
    """
    Computes projected gas prices based on skewed normal distribution parameters for specified years.

    Parameters:
    - min_year: The starting year for projections.
    - max_year: The ending year for projections.
    - interval: The interval between projection years.
    - data: A DataFrame containing median gas price data for each year.
    - params: A NumPy array containing the parameters (location, scale, shape) for the skew normal distribution.

    Returns:
    - A tuple containing two dictionaries with projected and median gas prices, and the percentile used for projections.

    Source for data:
    https://www.eia.gov/outlooks/aeo/data/browser/#/?id=3-AEO2022&region=1-5&cases=ref2022~highogs~lowogs&start=2020&end=2050&f=A&linechart=~~~ref2022-d011222a.38-3-AEO2022.1-5~highogs-d011222a.38-3-AEO2022.1-5~lowogs-d011222a.38-3-AEO2022.1-5&map=highogs-d011222a.3-3-AEO2022.1-5&sourcekey=0
    Unit: $/MMBTu converted to M$/PJ
    """
    percentile = np.random.uniform(0, 1)
    projected_prices = {}
    median_prices = {}
    param_index = 0

    for year in range(min_year, max_year + interval, interval):
        year_str = str(year)
        median = data.loc[year]['median']

        gas_price = skewnorm_inv_cdf(percentile, *params[param_index])
        gas_price *= 0.9487  # Convert $/MMBTu to M$/PJ

        projected_prices[year_str] = gas_price
        median_prices[year_str] = median

        param_index += 5  # Assuming parameters are spaced 5 years apart

    return projected_prices, median_prices, percentile


def compute_coal_proj(min_year, max_year, interval, data, params):
    """
    Computes projected coal prices based on skewed normal distribution parameters for specified years.

    Parameters:
    - min_year (int): The starting year for projections.
    - max_year (int): The ending year for projections.
    - interval (int): The interval between projection years.
    - data (pd.DataFrame): DataFrame containing median coal price data for each year.
    - params (np.array): Numpy array containing the parameters (location, scale, shape) for the skew normal distribution.

    Returns:
    - Tuple[Dict, Dict, float]: A tuple containing two dictionaries with projected and median coal prices, and the percentile used for projections.

    Note:
    - Data source: https://www.eia.gov/outlooks/aeo/data/browser
    - Unit: $/MMBTu converted to M$/PJ by multiplying with 0.9478
    """
    percentile = np.random.uniform(0, 1)
    projected_prices = {}
    median_prices = {}
    param_index = 0

    for year in range(min_year, max_year + interval, interval):
        median = data.loc[year, 'Median']
        
        # Considering normal distribution
        coal_price = skewnorm_inv_cdf(percentile, *params[param_index])
        coal_price *= 0.9478  # Convert $/MMBTu to M$/PJ

        projected_prices[str(year)] = coal_price
        median_prices[str(year)] = median

        param_index += 5  # Assuming parameters are spaced 5 years apart

    return projected_prices, median_prices, percentile


def compute_dsl_proj(min_year, max_year, interval, data, params):
    """
    Computes projected diesel prices based on skewed normal distribution parameters for specified years.

    Parameters:
    - min_year (int): The starting year for projections.
    - max_year (int): The ending year for projections.
    - interval (int): The interval between projection years.
    - data (pd.DataFrame): DataFrame containing median diesel price data for each year.
    - params (np.array): Numpy array containing the parameters (location, scale, shape) for the skew normal distribution.

    Returns:
    - Tuple[Dict, Dict, float]: A tuple containing two dictionaries with projected and median diesel prices, and the percentile used for projections.

    Note:
    - Data source: https://www.eia.gov/outlooks/aeo/data/browser
    - Unit: $/MMBTu converted to M$/PJ by multiplying with 0.9487
    """
    percentile = np.random.uniform(0, 1)
    projected_prices = {}
    median_prices = {}
    param_index = 0

    for year in range(min_year, max_year + interval, interval):
        median = data.loc[year, 'Median']
        
        # Considering normal distribution
        diesel_price = skewnorm_inv_cdf(percentile, *params[param_index])
        diesel_price *= 0.9487  # Convert $/MMBTu to M$/PJ

        projected_prices[str(year)] = diesel_price
        median_prices[str(year)] = median

        param_index += 5  # Assuming parameters are spaced 5 years apart

    return projected_prices, median_prices, percentile


def compute_oil_proj(min_year, max_year, interval, data, params):
    """
    Computes projected oil prices based on skewed normal distribution parameters for specified years.

    Parameters:
    - min_year (int): The starting year for projections.
    - max_year (int): The ending year for projections.
    - interval (int): The interval between projection years.
    - data (pd.DataFrame): DataFrame containing median oil price data for each year.
    - params (np.array): Numpy array containing the parameters (location, scale, shape) for the skew normal distribution.

    Returns:
    - Tuple[Dict, Dict, float]: A tuple containing two dictionaries with projected and median oil prices, and the percentile used for projections.

    Note:
    - Data source: [EIA Outlooks](https://www.eia.gov/outlooks/aeo/data/browser)
    - Unit: $/MMBTu converted to M$/PJ by multiplying with 0.9487
    """
    percentile = np.random.uniform(0, 1)
    projected_prices = {}
    median_prices = {}
    param_index = 0

    for year in range(min_year, max_year + interval, interval):
        median = data.loc[year, 'Median']
        oil_price = skewnorm_inv_cdf(percentile, *params[param_index])
        oil_price *= 0.9487  # Convert $/MMBTu to M$/PJ
        projected_prices[str(year)] = oil_price
        median_prices[str(year)] = median
        param_index += 5  # Assuming parameters are spaced 5 years apart

    return projected_prices, median_prices, percentile


def compute_uranium_proj(min_year, max_year, interval, data, params):
    """
    Computes projected uranium prices based on skewed normal distribution parameters for specified years.

    Parameters:
    - min_year: The starting year for projections.
    - max_year: The ending year for projections.
    - interval: The interval between projection years.
    - data: A DataFrame containing median uranium price data for each year.
    - params: A NumPy array containing the parameters (location, scale, shape) for the skew normal distribution.

    Returns:
    - A tuple containing two dictionaries with projected and median uranium prices, and the percentile used for projections.

    Notes:
    - The price conversion factor was originally set to 4.23e-3 ($/kg to M$/PJ) based on the energy content of uranium.
      This has been replaced with a generic conversion factor of 0.9487 for consistency with the gas projections.
    """
    percentile = np.random.uniform(0, 1)
    projected_prices = {}
    median_prices = {}
    param_index = 0

    for year in range(min_year, max_year + interval, interval):
        year_str = str(year)
        median = data.loc[year]['Median']

        uranium_price = skewnorm_inv_cdf(percentile, *params[param_index])
        uranium_price *= 0.9487  # Convert $/MMBTu to M$/PJ

        projected_prices[year_str] = uranium_price
        median_prices[year_str] = median

        param_index += 5  # Assuming parameters are spaced 5 years apart

    return projected_prices, median_prices, percentile


def compute_battery_proj(min_year, max_year, interval, inv_data, fix_data, cf_data, inv_params, fix_params):
    """
    Computes projected battery storage costs and capacity factors for specified years based on skewed normal distribution parameters.

    Parameters:
    - min_year: The starting year for projections.
    - max_year: The ending year for projections.
    - interval: The interval between projection years.
    - inv_data: A DataFrame containing median investment cost data for each year.
    - fix_data: A DataFrame containing median fixed cost data for each year.
    - cf_data: A DataFrame containing capacity factor data for each year.
    - inv_params: A NumPy array containing the parameters (location, scale, shape) for the investment cost distribution.
    - fix_params: A NumPy array containing the parameters (location, scale, shape) for the fixed cost distribution.

    Returns:
    - Tuple containing dictionaries of projected and median investment costs, fixed costs, and capacity factors, along with the percentiles used for investment and fixed cost projections.

    Source for data methodology:
    NREL
    """
    percentile_inv = np.random.uniform(0, 1)
    percentile_fix = np.random.uniform(0, 1)

    inv_costs, fix_costs = {}, {}
    md_inv_costs, md_fix_costs = {}, {}
    cfs = {}

    param_index = 0
    for year in range(min_year, max_year + interval, interval):
        year_str = str(year)

        # Investment costs
        median_inv = inv_data.loc[year]['Inv Median']
        inv_price = skewnorm_inv_cdf(percentile_inv, *inv_params[param_index])
        inv_costs[year_str] = inv_price
        md_inv_costs[year_str] = median_inv

        # Fixed costs
        median_fix = fix_data.loc[year]['Fix Median']
        fix_price = skewnorm_inv_cdf(percentile_fix, *fix_params[param_index])
        fix_costs[year_str] = fix_price
        md_fix_costs[year_str] = median_fix

        # Capacity factors
        cf = cf_data.loc[year]['CF']
        cfs[year_str] = cf

        param_index += 1

    return inv_costs, md_inv_costs, fix_costs, md_fix_costs, cfs, percentile_inv, percentile_fix


def compute_ecoal_proj(min_year, max_year, interval, inv_data, fix_data, var_data, inv_params, fix_params, var_params):
    """
    Computes projected costs for eCoal (electricity from coal) based on investment, fixed, and variable costs.

    Parameters:
    - min_year (int): Starting year of the projections.
    - max_year (int): Ending year of the projections.
    - interval (int): Year interval between projections.
    - inv_data (pd.DataFrame): Investment cost data per year.
    - fix_data (pd.DataFrame): Fixed cost data per year.
    - var_data (pd.DataFrame): Variable cost data per year.
    - inv_params (np.array): Parameters for the skewed normal distribution of investment costs.
    - fix_params (np.array): Parameters for the skewed normal distribution of fixed costs.
    - var_params (np.array): Parameters for the skewed normal distribution of variable costs.

    Returns:
    - A tuple containing dictionaries for investment, fixed, and variable costs, their corresponding median costs, 
      and the percentiles used for investment, fixed, and variable cost projections.

    Notes:
    - Assumes costs are projected using a skewed normal distribution.
    - The 'Median' column is expected in each of the data inputs (inv_data, fix_data, var_data).
    """
    percentile_inv = np.random.uniform(0, 1)
    percentile_fix = np.random.uniform(0, 1)
    percentile_var = np.random.uniform(0, 1)

    inv_costs = {}
    fix_costs = {}
    var_costs = {}
    md_inv_costs = {}
    md_fix_costs = {}
    md_var_costs = {}
    param_index = 0

    for year in range(min_year, max_year + interval, interval):
        year_str = str(year)

        # Investment Costs
        median_inv = inv_data.loc[year, 'Median']
        inv_cost = skewnorm_inv_cdf(percentile_inv, *inv_params[param_index])
        inv_costs[year_str] = inv_cost
        md_inv_costs[year_str] = median_inv

        # Fixed Costs
        median_fix = fix_data.loc[year, 'Median']
        fix_cost = skewnorm_inv_cdf(percentile_fix, *fix_params[param_index])
        fix_costs[year_str] = fix_cost
        md_fix_costs[year_str] = median_fix

        # Variable Costs
        median_var = var_data.loc[year, 'Median']
        var_cost = skewnorm_inv_cdf(percentile_var, *var_params[param_index])
        var_costs[year_str] = var_cost
        md_var_costs[year_str] = median_var

        param_index += 1

    return inv_costs, md_inv_costs, fix_costs, md_fix_costs, var_costs, md_var_costs, percentile_inv, percentile_fix, percentile_var



def compute_solar_proj(min_year, max_year, interval, inv_data, fix_data, cf_data, inv_params, fix_params, cf_params):
    """
    Computes projected solar energy investment and fixed costs, along with capacity factors for specified years.

    Parameters:
    - min_year: The starting year for projections.
    - max_year: The ending year for projections.
    - interval: The interval between projection years.
    - inv_data: A DataFrame containing median investment cost data for each year.
    - fix_data: A DataFrame containing median fixed cost data for each year.
    - cf_data: A DataFrame containing median capacity factor data for each year.
    - inv_params: A NumPy array containing the parameters (location, scale, shape) for the investment cost distribution.
    - fix_params: A NumPy array containing the parameters (location, scale, shape) for the fixed cost distribution.
    - cf_params: A NumPy array containing the parameters (location, scale, shape) for the capacity factor distribution.

    Returns:
    - Tuple containing dictionaries of projected and median investment costs, fixed costs, and capacity factors, along with the percentiles used for each projection.

    Notes:
    - Based on NREL ATB 2022 projections.
    """
    percentile_inv = np.random.uniform(0, 1)
    percentile_fix = np.random.uniform(0, 1)
    percentile_cf = np.random.uniform(0, 1)

    inv_costs, fix_costs, cfs = {}, {}, {}
    md_inv_costs, md_fix_costs, md_cfs = {}, {}, {}

    param_index = 0
    for year in range(min_year, max_year + interval, interval):
        year_str = str(year)

        # Investment costs
        median_inv = inv_data.loc[year]['Inv Median']
        inv_price = skewnorm_inv_cdf(percentile_inv, *inv_params[param_index])
        inv_costs[year_str] = inv_price
        md_inv_costs[year_str] = median_inv

        # Fixed costs
        median_fix = fix_data.loc[year]['Fix Median']
        fix_price = skewnorm_inv_cdf(percentile_fix, *fix_params[param_index])
        fix_costs[year_str] = fix_price
        md_fix_costs[year_str] = median_fix

        # Capacity factors
        median_cf = cf_data.loc[year]['CF Median']
        cf = skewnorm_inv_cdf(percentile_cf, *cf_params[param_index])
        cfs[year_str] = cf
        md_cfs[year_str] = median_cf

        param_index += 1

    return inv_costs, md_inv_costs, fix_costs, md_fix_costs, cfs, md_cfs, percentile_inv, percentile_fix, percentile_cf


def compute_wind_proj(min_year, max_year, interval, inv_data, fix_data, cf_data, inv_params, fix_params, cf_params):
    """
    Computes projected wind energy investment and fixed costs, along with changes in capacity factors, for specified years.

    Parameters:
    - min_year: The starting year for projections.
    - max_year: The ending year for projections.
    - interval: The interval between projection years.
    - inv_data: A DataFrame containing median investment cost data for each year.
    - fix_data: A DataFrame containing median fixed cost data for each year.
    - cf_data: A DataFrame containing median capacity factor change data for each year.
    - inv_params: A NumPy array containing the parameters (location, scale, shape) for the investment cost distribution.
    - fix_params: A NumPy array containing the parameters (location, scale, shape) for the fixed cost distribution.
    - cf_params: A NumPy array containing the parameters (location, scale, shape) for the capacity factor change distribution.

    Returns:
    - Tuple containing dictionaries of projected and median investment costs, fixed costs, and capacity factor changes, along with the percentiles used for each projection.

    Notes:
    - Based on NREL ATB 2022 projections.
    """
    percentile_inv = np.random.uniform(0, 1)
    percentile_fix = np.random.uniform(0, 1)
    percentile_cf = np.random.uniform(0, 1)

    inv_costs, fix_costs, cf_changes = {}, {}, {}
    md_inv_costs, md_fix_costs, md_cf_changes = {}, {}, {}

    param_index = 0
    for year in range(min_year, max_year + interval, interval):
        year_str = str(year)

        # Investment costs
        median_inv = inv_data.loc[year]['Inv Median']
        inv_price = skewnorm_inv_cdf(percentile_inv, *inv_params[param_index])
        inv_costs[year_str] = inv_price
        md_inv_costs[year_str] = median_inv

        # Fixed costs
        median_fix = fix_data.loc[year]['Fix Median']
        fix_price = skewnorm_inv_cdf(percentile_fix, *fix_params[param_index])
        fix_costs[year_str] = fix_price
        md_fix_costs[year_str] = median_fix

        # Capacity factor changes
        median_cf_change = cf_data.loc[year]['CF Median']
        cf_change = skewnorm_inv_cdf(percentile_cf, *cf_params[param_index])
        cf_changes[year_str] = cf_change
        md_cf_changes[year_str] = median_cf_change

        param_index += 1

    return inv_costs, md_inv_costs, fix_costs, md_fix_costs, cf_changes, md_cf_changes, percentile_inv, percentile_fix, percentile_cf


def compute_hydro_proj(min_year, max_year, interval, inv_data, fix_data, cf_data, inv_params, fix_params):
    """
    Computes projected hydroelectric energy investment and fixed costs for specified years based on skewed normal distribution parameters.
    It also includes the capacity factor data directly without projection.

    Parameters:
    - min_year: The starting year for projections.
    - max_year: The ending year for projections.
    - interval: The interval between projection years.
    - inv_data: A DataFrame containing median investment cost data for each year.
    - fix_data: A DataFrame containing median fixed cost data for each year.
    - cf_data: A DataFrame containing capacity factor data for each year.
    - inv_params: A NumPy array containing the parameters (location, scale, shape) for the investment cost distribution.
    - fix_params: A NumPy array containing the parameters (location, scale, shape) for the fixed cost distribution.

    Returns:
    - Tuple containing dictionaries of projected and median investment costs, fixed costs, and capacity factors, along with the percentiles used for investment and fixed cost projections.

    Notes:
    - Based on NREL ATB 2022 projections.
    """
    percentile_inv = np.random.uniform(0, 1)
    percentile_fix = np.random.uniform(0, 1)

    inv_costs, fix_costs = {}, {}
    cf_values = {}
    md_inv_costs, md_fix_costs = {}, {}

    param_index = 0
    for year in range(min_year, max_year + interval, interval):
        year_str = str(year)

        # Investment costs
        median_inv = inv_data.loc[year]['Inv Median']
        inv_price = skewnorm_inv_cdf(percentile_inv, *inv_params[param_index])
        inv_costs[year_str] = inv_price
        md_inv_costs[year_str] = median_inv

        # Fixed costs
        median_fix = fix_data.loc[year]['Fix Median']
        fix_price = skewnorm_inv_cdf(percentile_fix, *fix_params[param_index])
        fix_costs[year_str] = fix_price
        md_fix_costs[year_str] = median_fix

        # Capacity factors - directly using provided data
        cf = cf_data.loc[year]['CF']
        cf_values[year_str] = cf

        param_index += 1

    return inv_costs, md_inv_costs, fix_costs, md_fix_costs, cf_values, percentile_inv, percentile_fix


def compute_nuclear_proj(min_year, max_year, interval, inv_data, fix_data, var_data):
    """
    Computes projected nuclear energy costs, including investment, fixed, and variable costs for specified years.

    Parameters:
    - min_year: The starting year for projections.
    - max_year: The ending year for projections.
    - interval: The interval between projection years.
    - inv_data: A DataFrame containing investment cost data (Capex) for each year.
    - fix_data: A DataFrame containing fixed cost data for each year.
    - var_data: A DataFrame containing variable cost data for each year.

    Returns:
    - A tuple containing dictionaries of projected investment costs, fixed costs, and variable costs.

    Notes:
    - Projections are based on the NREL ATB 2022 data.
    """
    inv_costs = {}
    fix_costs = {}
    var_costs = {}

    for year in range(min_year, max_year + interval, interval):
        year_str = str(year)

        # Investment costs
        inv_costs[year_str] = inv_data.loc[year]['Capex']

        # Fixed costs
        fix_costs[year_str] = fix_data.loc[year]['Fix']

        # Variable costs
        var_costs[year_str] = var_data.loc[year]['Var']

    return inv_costs, fix_costs, var_costs



def compute_ngcc_proj(min_year, max_year, interval, inv_data, fix_data, var_data):
    """
    Computes projected costs for Natural Gas Combined Cycle (NGCC) power plants, including investment, fixed,
    and variable costs for specified years.

    Parameters:
    - min_year: The starting year for projections.
    - max_year: The ending year for projections.
    - interval: The interval between projection years.
    - inv_data: A DataFrame containing investment cost data (Capex) for each year.
    - fix_data: A DataFrame containing fixed cost data for each year.
    - var_data: A DataFrame containing variable cost data for each year.

    Returns:
    - A tuple containing dictionaries of projected investment costs, fixed costs, and variable costs.

    Notes:
    - Projections are based on data, such as the NREL ATB 2022, or other relevant datasets.
    """
    inv_costs = {}
    fix_costs = {}
    var_costs = {}

    for year in range(min_year, max_year + interval, interval):
        year_str = str(year)

        # Investment costs
        inv_costs[year_str] = inv_data.loc[year]['Capex']

        # Fixed costs
        fix_costs[year_str] = fix_data.loc[year]['Fix']

        # Variable costs
        var_costs[year_str] = var_data.loc[year]['Var']

    return inv_costs, fix_costs, var_costs



def compute_bio_proj(min_year, max_year, interval, inv_data, fix_data, var_data):
    """
    Computes projected costs for biomass energy projects, including investment, fixed, and variable costs for specified years.

    Parameters:
    - min_year: The starting year for the cost projections.
    - max_year: The ending year for the cost projections.
    - interval: The interval between years for which projections are made.
    - inv_data: A DataFrame containing investment cost data (Capex) for each year.
    - fix_data: A DataFrame containing fixed cost data for each year.
    - var_data: A DataFrame containing variable cost data for each year.

    Returns:
    - A tuple containing dictionaries of projected investment costs, fixed costs, and variable costs for each year in the specified range.

    Notes:
    - The costs are obtained directly from the provided data, assuming they are deterministic for the given years.
    """
    inv_costs = {}
    fix_costs = {}
    var_costs = {}

    for year in range(min_year, max_year + interval, interval):
        year_str = str(year)

        # Investment costs
        inv_costs[year_str] = inv_data.loc[year]['Capex']

        # Fixed costs
        fix_costs[year_str] = fix_data.loc[year]['Fix']

        # Variable costs
        var_costs[year_str] = var_data.loc[year]['Var']

    return inv_costs, fix_costs, var_costs




def generate_dependant_uniform(first_uniform, correlation):
    
    # Convert the first uniform variable to a standard normal variable
    first_normal = scipy.stats.norm.ppf(first_uniform)

    # Generate an independent standard normal variable
    independent_normal = np.random.normal(0, 1)

    # Apply the correlation using the formula for conditional expectation in a bivariate normal distribution
    second_normal = correlation * first_normal + np.sqrt(1 - correlation**2) * independent_normal

    # Convert the second normal variable back to uniform
    second_uniform = scipy.stats.norm.cdf(second_normal)

    return second_uniform


def compute_elc_price_proj(min_year, max_year, interval, price_change_data, params, per_capita_percentile):
    """
    Computes projected electricity prices based on skewed normal distribution parameters for specified years.

    Parameters:
    - min_year: The starting year for projections.
    - max_year: The ending year for projections.
    - interval: The interval between projection years.
    - price_change_data: A DataFrame containing median price change data for each year.
    - params: A NumPy array containing the parameters (location, scale, shape) for the price change distribution.
    - per_capita_percentile: The percentile used as a base for generating the dependent electricity price percentile.

    Returns:
    - Tuple containing dictionaries of projected electricity prices, median prices, and the electricity price percentile.
    """
    percentile_elc = generate_dependant_uniform(per_capita_percentile, 0.573)

    elc_prices = {}
    median_prices = {}
    param_index = 4  # Assuming starting index is 4 for some reason, could be clarified

    for year in range(min_year, max_year + interval, interval):
        year_str = str(year)
        median = price_change_data.loc[year]['Median']

        # Projected electricity price
        elc_price = skewnorm_inv_cdf(percentile_elc, *params[param_index])
        elc_prices[year_str] = elc_price
        median_prices[year_str] = median

        param_index += 5  # Assuming parameters are spaced 5 years apart

    return elc_prices, median_prices, percentile_elc
    
   

    
import numpy as np

def compute_wind_cf_func(cut_in, rated, wind_cf_change):
    """
    Calculates the coefficients of a cubic function modeling the wind turbine's capacity factor as a function of wind speed.

    Parameters:
    - cut_in: The cut-in wind speed of the turbine, below which the turbine does not generate power.
    - rated: The rated wind speed of the turbine, at which the turbine generates its maximum power.
    - wind_cf_change: A factor to adjust the capacity factor of the turbine.

    Returns:
    - A tuple of coefficients (a, b, c, d) for the cubic function a*x^3 + b*x^2 + c*x + d.

    Notes:
    - The function assumes a capacity factor of 0 at cut-in speed and 1 (100%) at rated speed.
    - The derivative at both cut-in and rated speeds is assumed to be 0, reflecting a flat response at these transition points.
    - The wind_cf_change factor scales the function to reflect changes in capacity factor.
    """
    # Coefficient matrix for the cubic equation system
    A = np.array([
        [cut_in**3, cut_in**2, cut_in, 1],
        [rated**3, rated**2, rated, 1],
        [3 * cut_in**2, 2 * cut_in, 1, 0],
        [3 * rated**2, 2 * rated, 1, 0]
    ])

    # Result vector for the equation system
    b = np.array([0, 1, 0, 0])

    # Solve the system of equations for the coefficients, and apply the wind_cf_change factor
    X = np.linalg.solve(A, b) * wind_cf_change

    return X[0], X[1], X[2], X[3]



def run_temoa(temoa_path, sql_path, sql_name, config_path, config_name):
    cmdString = ''
    cmdString += 'cd ' + config_path + ';'
    cmdString += 'rm ' + sql_name + '.sqlite;'
    cmdString += 'sqlite3 ' + sql_name + '.sqlite < ' + sql_name + '.sql;'
    cmdString += 'cd ' + temoa_path + ';'
    cmdString += 'python temoa_model/ --config=' + config_path + '/' + config_name
    
    os.system(cmdString)



def compute_normal_op_costs_fd(caps, acts, sol_fix_50, wind_fix_50, batt_fix_50, ngcc_fix_50, nuc_fix_50, hyd_fix_50, 
                            ngcc_var_50, nuc_var_50, trans_var_50, cond_var_50, ng_var_50, urn_var_50, added_cost_ratio):
    """
    Computes the normal operational costs for various energy technologies based on their capacities and activities.

    Parameters:
    - caps: Dictionary containing capacities for various energy sources.
    - acts: Dictionary containing activities for various energy sources.
    - sol_fix_50, wind_fix_50, batt_fix_50, ngcc_fix_50, nuc_fix_50, hyd_fix_50: Fixed costs for solar, wind, battery, NGCC, nuclear, and hydro respectively.
    - ngcc_var_50, nuc_var_50, trans_var_50, cond_var_50, ng_var_50, urn_var_50: Variable costs for NGCC, nuclear, transmission, conduction, natural gas, and uranium respectively.
    - added_cost_ratio: Additional cost ratio applied specifically to nuclear operations.

    Returns:
    - Total operational cost in million units, and individual operational costs for solar, wind, battery, hydro, nuclear (including uranium), NGCC (including natural gas), transmission, and conduction.
    """
    sol_cost = sol_fix_50 * caps['E_SOLPV']
    wind_cost = wind_fix_50 * caps['E_WIND']
    batt_cost = batt_fix_50 * caps['E_BATT']
    nuc_cost = (nuc_fix_50 * caps['E_NUCLEAR'] + nuc_var_50 * acts['E_NUCLEAR']) * added_cost_ratio
    hyd_cost = hyd_fix_50 * caps['E_HYDRO']
    ngcc_cost = ngcc_fix_50 * caps['E_NGCC'] + ngcc_var_50 * acts['E_NGCC']
    trans_cost = trans_var_50 * acts['E_TRANS']
    cond_cost = cond_var_50 * acts['E_COND']
    ng_cost = ng_var_50 * acts['S_IMPNG']
    urn_cost = urn_var_50 * acts['S_IMPURN']

    # Total operational cost
    op_cost = sum([sol_cost, wind_cost, batt_cost, hyd_cost, nuc_cost, ngcc_cost, trans_cost, cond_cost, ng_cost, urn_cost])

    # Multiply by 10^6 to convert to million units
    return op_cost * 10**6, sol_cost, wind_cost, batt_cost, hyd_cost, nuc_cost, ngcc_cost + ng_cost, trans_cost, cond_cost

    
def compute_normal_op_costs_bau(caps, acts, sol_fix_50, wind_fix_50, batt_fix_50, ngcc_fix_50, coal_fix_50, dsl_fix_50, oil_fix_50, nuc_fix_50, hyd_fix_50, bio_fix_50, biofuel_50,
                                ngcc_var_50, ecoal_var_50, edsl_var_50, eoil_var_50, nuc_var_50, bio_var_50, trans_var_50, cond_var_50, ng_var_50, coal_var_50, dsl_var_50, oil_var_50, urn_var_50, added_cost_ratio):
    """
    Computes the operational costs for various energy technologies based on their capacities and activities in a business-as-usual scenario.

    Parameters:
    - caps (dict): Capacities for various energy sources.
    - acts (dict): Activities for various energy sources.
    - Fixed and variable costs for solar, wind, battery, NGCC, coal, diesel, oil, nuclear, hydro, and biofuel technologies.
    - added_cost_ratio (float): Additional cost ratio applied to specific operations, influencing the total operational cost.

    Returns:
    - Total operational cost (in million units) and individual operational costs for each energy technology.
    """
    # Operational costs for renewable and non-renewable sources
    sol_cost = sol_fix_50 * caps['E_SOLPV']
    wind_cost = wind_fix_50 * caps['E_WIND']
    batt_cost = batt_fix_50 * caps['E_BATT']
    hyd_cost = hyd_fix_50 * caps['E_HYDRO']
    bio_cost = (bio_fix_50 * caps['E_BIO'] + bio_var_50 * acts['E_BIO']) + biofuel_50 * acts['S_IMPBIO']

    # Operational costs for nuclear energy, considering additional cost ratio
    nuc_cost = (nuc_fix_50 * caps['E_NUCLEAR'] + nuc_var_50 * acts['E_NUCLEAR']) 
    
    # Operational costs for fossil fuel technologies
    ngcc_cost = (ngcc_fix_50 * caps['E_NGCC'] + ngcc_var_50 * acts['E_NGCC']) * added_cost_ratio
    ecoal_cost = coal_fix_50 * caps['E_COAL'] + ecoal_var_50 * acts['E_COAL']
    edsl_cost = dsl_fix_50 * caps['E_DSL'] + edsl_var_50 * acts['E_DSL']
    eoil_cost = oil_fix_50 * caps['E_OIL'] + eoil_var_50 * acts['E_OIL']
    
    # Operational costs for transmission and conduction
    trans_cost = trans_var_50 * acts['E_TRANS']
    cond_cost = cond_var_50 * acts['E_COND']
    
    # Costs associated with raw materials and fuels
    ng_cost = ng_var_50 * acts['S_IMPNG']
    coal_cost = coal_var_50 * acts['S_IMPCOAL']
    dsl_cost = dsl_var_50 * acts['S_IMPDSL']
    oil_cost = oil_var_50 * acts['S_IMPOIL']
    urn_cost = urn_var_50 * acts['S_IMPURN']
    
    # Total operational cost in million units
    op_cost = sum([sol_cost, wind_cost, batt_cost, hyd_cost, bio_cost, nuc_cost, ngcc_cost, ecoal_cost, edsl_cost, eoil_cost, trans_cost, cond_cost, ng_cost, coal_cost, dsl_cost, oil_cost, urn_cost]) * 10**6

    return op_cost, sol_cost, wind_cost, batt_cost, hyd_cost, bio_cost, nuc_cost, ngcc_cost, ecoal_cost, edsl_cost, eoil_cost, trans_cost, cond_cost

def compute_normal_op_costs_fr(caps, acts, sol_fix_50, wind_fix_50, batt_fix_50, ngcc_fix_50, nuc_fix_50, hyd_fix_50, bio_fix_50,
                               ngcc_var_50, nuc_var_50, bio_var_50, biofuel_50, trans_var_50, cond_var_50, ng_var_50, urn_var_50, added_cost_ratio):
    """
    Computes normal operational costs for various energy technologies based on their capacities and activities in a future scenario.

    Parameters:
    - caps: Dictionary containing capacities for various energy sources.
    - acts: Dictionary containing activities for various energy sources.
    - sol_fix_50, wind_fix_50, batt_fix_50, ngcc_fix_50, nuc_fix_50, hyd_fix_50, bio_fix_50: Fixed costs for solar, wind, battery, NGCC, nuclear, hydro, and bio respectively.
    - ngcc_var_50, nuc_var_50, bio_var_50, trans_var_50, cond_var_50, ng_var_50, urn_var_50: Variable costs for NGCC, nuclear, bio, transmission, conduction, natural gas, and uranium respectively.
    - biofuel_50: Fixed cost for biofuel.
    - added_cost_ratio: Additional cost ratio applied specifically to certain operations.

    Returns:
    - Total operational cost in million units, and individual operational costs for solar, wind, battery, hydro, bio, NGCC, nuclear, transmission, and conduction.
    """
    sol_cost = sol_fix_50 * caps['E_SOLPV']
    wind_cost = wind_fix_50 * caps['E_WIND']
    batt_cost = batt_fix_50 * caps['E_BATT']
    nuc_cost = nuc_fix_50 * caps['E_NUCLEAR'] + nuc_var_50 * acts['E_NUCLEAR']
    hyd_cost = hyd_fix_50 * caps['E_HYDRO']
    bio_cost = (bio_fix_50 * caps['E_BIO'] + bio_var_50 * acts['E_BIO']) * added_cost_ratio
    ngcc_cost = ngcc_fix_50 * caps['E_NGCC'] + ngcc_var_50 * acts['E_NGCC']

    trans_cost = trans_var_50 * acts['E_TRANS']
    cond_cost = cond_var_50 * acts['E_COND']
    ng_cost = ng_var_50 * acts['S_IMPNG']
    urn_cost = urn_var_50 * acts['S_IMPURN']
    biofuel_cost = biofuel_50 * acts['S_IMPBIO']

    op_cost = sum([sol_cost, wind_cost, batt_cost, hyd_cost, bio_cost, ngcc_cost, trans_cost, cond_cost, ng_cost, urn_cost, biofuel_cost]) * 10**6

    return op_cost, sol_cost, wind_cost, batt_cost, hyd_cost, bio_cost, ngcc_cost, nuc_cost, trans_cost, cond_cost


def write_grid_data(caps, sol_inv_costs, wind_inv_costs, trans_inv_cost, cond_inv_cost, sub_inv_cost, twr_inv_cost):
    """
    Creates a DataFrame with grid components, their replacement costs, and other attributes.

    Parameters:
    - caps: Dictionary of capacities for different components.
    - sol_inv_costs: Dictionary of investment costs for solar components.
    - wind_inv_costs: Dictionary of investment costs for wind components.
    - trans_inv_cost: Investment cost per unit for transmission lines.
    - cond_inv_cost: Investment cost per unit for distribution lines.
    - sub_inv_cost: Investment cost per unit for substations.
    - twr_inv_cost: Investment cost per unit for towers.

    Returns:
    - A DataFrame with grid components and their attributes.
    """

    components = [
        {'Type': 'Transmission Line', 'Replacement Cost': caps['E_TRANS'] * trans_inv_cost, 'Line Length': 4284511},
        {'Type': 'Distribution Line', 'Replacement Cost': caps['E_COND'] * cond_inv_cost, 'Line Length': 26742880},
        {'Type': 'Tower', 'Replacement Cost': caps['E_TWR'] * twr_inv_cost, 'Line Length': None},
        {'Type': 'Substation', 'Replacement Cost': caps['E_SUB'] * sub_inv_cost, 'Line Length': None},
        {'Type': 'Solar Generator', 'Replacement Cost': caps['E_SOLPV'] * sol_inv_costs['2050'] * 10**6, 'Line Length': None},
        {'Type': 'Wind Generator', 'Replacement Cost': caps['E_WIND'] * wind_inv_costs['2050'] * 10**6, 'Line Length': None}
    ]

    # Convert the list of dictionaries to a DataFrame
    comp = pd.DataFrame(components)

    return comp