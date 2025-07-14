# Stellar Atlas: Simulating and Visualizing Stellar Evolution

## Project Overview

The **Stellar Atlas** is an independent research project focused on simulating and visualizing the evolution of stars across a wide range of masses and metallicities. Developed by Aniket Mishra, a BS-MS student at IISER Kolkata, this project leverages advanced computational tools to explore the intricate life cycles of stars, from their birth on the main sequence through various evolutionary stages, including hydrogen and helium exhaustion.

The primary goal of the Stellar Atlas is to provide an accessible and interactive platform for understanding stellar behavior. It aims to visualize key evolutionary indicators such as Hertzsprung-Russell (HR) diagrams, core temperature vs. density profiles, and luminosity vs. central hydrogen fraction over time. These visualizations, combined with detailed analysis, offer insights into the internal structure, fusion processes, and life cycles of stars.

## Features

The Streamlit web application provides the following key features:

*   **Interactive Stellar Simulations**: Explore stellar evolution models based on varying stellar mass and metallicity.
*   **Customizable Stopping Conditions**: Analyze stellar evolution up to different phases, including Hydrogen Exhaustion and Helium Exhaustion (simulations for Helium Exhaustion are currently running and will be updated).
*   **Hertzsprung-Russell (HR) Diagrams**: Visualize stellar tracks on HR diagrams, highlighting the main sequence and post-main sequence evolution.
*   **Detailed Data Exploration**: Dive into specific stellar parameters like luminosity, effective temperature, radius, and internal structure.
*   **Project Report Access**: Directly download the comprehensive project report in PDF format from within the application.
*   **About Project Section**: Learn more about the project methodology, tools used, and contact information for the author.
*   **User-Friendly Interface**: Intuitive navigation and dropdown menus for easy data selection and visualization.

## Technical Stack

The Stellar Atlas project utilizes a robust set of scientific and web development tools:

*   **MESA (Modules for Experiments in Stellar Astrophysics)**: The core simulation engine for generating 1D stellar evolution models.
*   **Python**: The primary programming language for data processing, analysis, and visualization.
    *   `Numpy` and `Pandas`: For efficient data manipulation and analysis.
    *   `Matplotlib`: For generating high-quality scientific plots and visualizations.
    *   `MESA_reader`: A custom Python library for parsing and interacting with MESA output files.
*   **Streamlit**: For building the interactive web application interface, enabling dynamic data exploration.
*   **FFMPEG**: Used for video generation from simulation data (e.g., time evolution of HR diagrams).
*   **Bash Scripting**: For automating simulation runs and data processing workflows.
*   **Zenodo**: Used for hosting the project database and simulation results, ensuring data accessibility and reproducibility.

## Installation and Local Setup

To run the Stellar Atlas Streamlit application locally, follow these steps:

### Prerequisites

*   **Python 3.x**: Ensure you have Python installed.
*   **Git**: For cloning the repository.
*   **MESA**: While not strictly required to run the Streamlit app (as pre-generated data is used), having MESA installed is necessary if you wish to run new simulations or modify existing ones. Refer to the [MESA website](http://mesa.sourceforge.net/) for installation instructions.

### Steps

1.  **Clone the Repository**

    ```bash
    git clone https://github.com/MadSc1ent1st96/Stellar-Atlas.git
    cd Stellar-Atlas
    ```

2.  **Create a Virtual Environment (Recommended)**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

    *Note: The `requirements.txt` file will be generated or provided within the repository. It will include `streamlit`, `numpy`, `pandas`, `matplotlib`, and `mesa_reader`.*

4.  **Run the Streamlit Application**

    ```bash
    streamlit run app.py
    ```

    This command will open the Streamlit application in your default web browser, typically at `http://localhost:8501`.

## Usage

Once the Streamlit application is running, you can:

*   **Navigate** through different sections using the sidebar menu (Atlas, About Project, Project Report).
*   In the **Atlas** section, select:
    *   **Stopping Condition**: Choose between Hydrogen-Exhaustion and Helium-Exhaustion (when available).
    *   **Section for Stopping Condition**: Explore Introduction, Discussion, Comparison, Conclusion, ZAMS Plot, or Star Simulations.
    *   **Metallicity Group (Z)**: Select different metallicity values.
    *   **Mass**: Choose specific stellar masses to view their evolution.
*   **Download** the full project report from the **Project Report** section.
*   Learn more about the project and the author in the **About Project** section.

## Project Structure

```
Stellar-Atlas/
├── data/                 # Contains pre-generated MESA simulation output data
├── src/                  # Source code for the Streamlit application and data processing scripts
│   ├── app.py            # Main Streamlit application file
│   ├── mesa_reader.py    # Custom utility for reading MESA data
│   └── ...               # Other scripts for plotting, analysis, etc.
├── docs/                 # Project documentation, including the final report
│   └── Stellar-Atlas-Final-Report.pdf
├── images/               # Screenshots and other relevant images
├── requirements.txt      # Python dependencies
├── README.md             # This file
└── LICENSE               # Project license information
```

## Contributing

Contributions to the Stellar Atlas project are welcome! If you have suggestions for improvements, bug reports, or would like to contribute code, please feel free to:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/YourFeature`).
3.  Make your changes.
4.  Commit your changes (`git commit -m 'Add some feature'`).
5.  Push to the branch (`git push origin feature/YourFeature`).
6.  Open a Pull Request.

## License

This project's content (e.g., documentation, data, and scientific findings) is licensed under the [Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

The code within this repository (e.g., Python scripts, Streamlit application code) is licensed under the [MIT License](LICENSE). See the `LICENSE` file for details.

## Contact

For any questions or inquiries, please contact Aniket Mishra at:

*   Email: `mas23ms096@iiserkol.ac.in`
*   Alternate Email: `aniket.mishra200510@gmail.com`
*   GitHub: [MadSc1ent1st96](https://github.com/MadSc1ent1st96)

---

