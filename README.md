
# Energy Transition in Puerto Rico: Probabilistic Cost and Sensitivity Analysis

This repository contains the source code and data used in the research paper titled "Changes in the frequency of hurricanes and organizational dysfunction are the key uncertainties impacting energy transition cost: a Puerto Rico case study". The study presents a comprehensive framework that leverages surrogate-based sensitivity analysis to identify key sources driving the uncertainty in the cost of different energy transition scenarios in Puerto Rico.

## Repository Structure

- `simulation/`: Contains main code snippets for running the probabilistic cost analysis for three transition scenarios in Puerto Rico. It includes:
  - `scenario_*.py`: Scripts for each transition scenario.
  - `utils.py`: Utility functions required by the main scripts.
  - `temoa_input_writer.py`: Script for generating TEMOA input files for all scenarios.
  - `temoa_output_reader.py`: Script for reading and processing TEMOA output files.

- `surrogates/`: Includes surrogate models (Deep Neural Networks) for total and operational costs, aimed at reducing computational time for sensitivity analysis.
  - `total_cost_surrogate.py`: Surrogate model for total cost analysis.
  - `op_cost_surrogate.py`: Surrogate model for operational cost analysis.

- `TEMOA/`: A submodule link to the [TEMOA project repository](https://github.com/TemoaProject/temoa). Includes the `data_files/PuertoRico/` directory with necessary files for running simulation codes.

- `UQLab/`: Contains the UQLab toolbox for MATLAB, focusing on uncertainty quantification. A `project_codes/` folder is added for ease of use, containing scripts for conducting global sensitivity analysis using Sobol Indices.

## Getting Started

To replicate the analyses or use the framework for your study, follow these steps:

1. Ensure you have Python installed for running the simulation and surrogate models. MATLAB is required for UQLab scripts.
2. Clone this repository and initialize submodules with `git clone --recurse-submodules <repository-url>`.
3. Navigate to the `simulation/` directory to run cost analyses for different scenarios. Modify input data as needed for custom analyses.
4. For surrogate modeling, go to the `surrogates/` directory. Train the DNN models using your data or use the provided models for quick analysis.
5. Use UQLab in MATLAB for sensitivity analysis. Scripts in `UQLab/project_codes/` are prepared for analyzing the influence of various uncertainties.

## Requirements

- Python 3.x
- MATLAB (for UQLab)
- Relevant Python packages as listed in `requirements.txt`
- UQLab installation in MATLAB (follow instructions on the [UQLab website](https://www.uqlab.com/download))

## License

This project is open-sourced under the MIT License. See the LICENSE file for more details.

## Citation

If you use this code or the framework in your research, please cite our paper:

```
Khayambashi, K., Clarens, A.F., Shobe, W.M., Alemazkoor, N. (Year). Title. Journal, Volume(Issue), pages. DOI
```
