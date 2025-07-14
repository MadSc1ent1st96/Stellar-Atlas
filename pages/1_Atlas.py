import streamlit as st
import os
import json
from pathlib import Path

from utils import setup_page
setup_page()

st.title("\U0001F30C Stellar Evolution Atlas")

# --- Constants ---
EXAMPLE_MASSES = ["1M☉", "20M☉", "50M☉"]

# --- UI Elements ---
stop_groups = sorted([d for d in os.listdir("work") if os.path.isdir(f"work/{d}")])
selected_stop = st.selectbox("Select Stopping Condition", stop_groups)

sections = ["Introduction", "Discussion", "Comparison", "Conclusion", "ZAMS Plot", "Star Simulations"]
selected_section = st.selectbox(f"Select Section for {selected_stop}", sections)

# --- Section Dispatcher ---
if selected_section == "Star Simulations":
    z_groups = sorted([d for d in os.listdir(f"work/{selected_stop}") if os.path.isdir(f"work/{selected_stop}/{d}")])
    selected_z = st.selectbox("Select Metallicity Group (Z)", z_groups)
    base_path = Path("work") / selected_stop / selected_z

    if selected_z == "Individual-Example":
        mass_groups = sorted([d for d in os.listdir(base_path) if os.path.isdir(base_path / d)])
        selected_mass = st.selectbox("Select the mass", mass_groups)
        mass_path = base_path / selected_mass

        if selected_mass in EXAMPLE_MASSES:
            # Metadata
            with open(mass_path / "metadata.json") as f:
                meta = json.load(f)
            st.subheader(f"{meta['star_name']} — {meta['initial_mass']} M☉")

            def display_image(title, filename, caption):
                st.markdown(f"## {title}")
                st.image(mass_path / filename, caption=caption, use_container_width=True)
                st.divider()

            def display_video(title, filename):
                st.markdown(f"## {title}")
                with open(mass_path / filename, "rb") as f:
                    video_bytes = f.read()
                st.video(video_bytes)
                st.divider()

            # Plots
            display_image("Hertzsprung–Russell Diagram", "hr_diagram.png", "HR Diagram")
            st.markdown(f"""
                The above is the **HR diagram** produced from *MESA* and plotted using *matplotlib* and *mesa_reader*.
                The star has mass {meta['initial_mass']}M☉ and solar metallicity (Z = 0.014, Asplund et al.).
                We observe the Pre-Main Sequence, ZAMS, and Main Sequence phases. No red giant phase is visible since the simulation stopped at hydrogen exhaustion.""")
            st.divider()

            display_image("Core Temperature vs Density Evolution", "Tc_vs_rhoc.png", "Core Temp vs Density")
            st.markdown("In log scale, both core temperature and density rise almost linearly, indicating a nearly $y = x$ trend.")
            st.divider()

            display_image("Age vs Radius", "age_vs_radius.png", "Radius Evolution")
            st.markdown("""
                The sharp initial drop corresponds to pre-main-sequence contraction.
                The lowest radius marks the ZAMS point. Gradual expansion follows, with the end around $3.7 \\times 10^6$(50M☉), $0.9 \\times 10^7$(20M☉) and $8.5 \\times 10^9$(1M☉) years indicating core hydrogen depletion.
            """)
            st.divider()  
 
            display_image("Age vs Luminosity", "age_vs_luminosity.png", "Luminosity Evolution")

            display_video("HR Diagram Animation", "hr_evolution.mp4")
            display_video("Core Conditions Animation", "TRho_evolution.mp4")

    else:
        def display_z_level_plot(title, filename, caption):
            st.markdown(f"## {title}")
            st.image(base_path / filename, caption=caption, use_container_width=True)
            st.divider()

        def display_z_level_video(title, filename):
            st.markdown(f"## {title}")
            with open(base_path / filename, "rb") as f:
                video_bytes = f.read()
            st.video(video_bytes)
            st.divider()

        display_z_level_plot("HR Diagram", "HRD_highlighted.png", "All HR diagrams combined")
        display_z_level_video("HR Diagram Animation", "hr_mass_evolution.mp4")

        display_z_level_plot("Core Temperature vs Core Density", "Tc_Rhoc.png", "Temp vs Density")
        display_z_level_video("Core Temperature vs Core Density Animation", "Tc_vs_rhoc_evolution.mp4")

        display_z_level_plot("Luminosity vs Age", "Age_Luminosity.png", "Luminosity Evolution")
        display_z_level_video("Luminosity vs Age Animation", "age_vs_luminosity_evolution.mp4")

        display_z_level_plot("Radius vs Age", "Age_Radius.png", "Radius Evolution")
        display_z_level_video("Radius vs Age Animation", "age_vs_radius_evolution.mp4")

        display_z_level_plot("Central Hydrogen vs Age", "Central_H.png", "Central H Content")
        display_z_level_video("Central Hydrogen vs Age Animation", "central_H_vs_time_evolution.mp4")

        display_z_level_plot("Comparison with GAIA D3 dataset", "HRD_Gaia_MESA_AutoOverlay.png", "GAIA and MESA Overlay")

else:
    st.markdown(f"## {selected_section}")

    if selected_stop == "Hydrogen-Exhaustion":
        if selected_section == "Introduction":
            st.markdown("""
                In this stopping condition, simulations are terminated when the central hydrogen fraction drops below $10^{-5}$, marking the end of the main sequence. This phase is crucial because it represents the longest, most stable stage in a star’s life, during which hydrogen fusion occurs in the core.

                The goal here is to analyze how stars of varying mass and metallicity behave during the hydrogen-burning phase. Masses ranged from 0.5 M☉ to 100 M☉ (and even higher in some exploratory runs), and six different metallicity values were used.

                This part of the project captures key trends in core temperature, luminosity, surface temperature, and evolutionary time scales across masses and metallicities. The pre-main sequence, ZAMS point, and core hydrogen exhaustion are visible in most HR tracks.
            """)

        elif selected_section == "Discussion":
            st.markdown("""
                The results reaffirm that stellar evolution is primarily governed by initial mass and metallicity. Higher-mass stars evolve faster, reach higher temperatures and luminosities, and lie at the top-left of the HR diagram. In contrast, low-mass stars evolve slowly, appear in the bottom-right, and can show signs of degeneracy near hydrogen exhaustion.

                Metallicity introduces opacity effects. Low-Z stars are hotter and more compact, while high-Z stars are cooler with broader HR tracks. This is most evident for stars below 10 M☉. The trend begins to plateau after Z = 0.014, with Z = 0.02 and Z = 0.04 showing minor differences.

                The Tc–ρc plots support these conclusions. Low-mass stars curve toward degeneracy (especially < 0.7 M☉), while high-mass stars maintain thermally supported cores. Simulation tracks for stars >80 M☉ are unreliable due to timestep and convergence issues.
            """)

        elif selected_section == "Comparison":
            st.markdown("""
                To validate the simulations, HR diagrams were compared with real observational data from Gaia DR3. The solar-metallicity (Z = 0.02) models evolved until hydrogen exhaustion were used for this purpose.

                Key takeaways:
                - The main sequence in Gaia data matches the slope and structure of simulated tracks.
                - Observational data includes post-main-sequence and binary stars, resulting in a broader scatter.
                - Most stars in the Gaia sample lie between the 1–5 M☉ tracks, consistent with observed stellar population statistics.

                This comparison reinforces the accuracy of the simulated models and highlights the practical relevance of this project.
            """)

        elif selected_section == "Conclusion":
            st.markdown("""
                Simulations until hydrogen exhaustion successfully reproduced classical stellar evolution features. Key observations include:

                - Mass-luminosity and mass-temperature correlations.
                - Metallicity's impact on temperature, opacity, and lifetime.
                - Degeneracy onset in low-mass stars.

                Simulation robustness was good for most of the parameter space, though high-mass, high-Z stars showed instability. These results confirm MESA's reliability and provide a valuable visual reference for the hydrogen-burning stage of stellar evolution.
            """)

        elif selected_section == "ZAMS Plot":
            st.markdown("### Zero Age Main Sequence (ZAMS) (Same for both stopping condition)")
            st.divider()
            base_path = Path("work") 
            st.image("work/ZAMS_H_0.014.png", caption="ZAMS plot for Z = 0.014", use_container_width=True)
            st.divider()
            st.markdown("""
                This plot shows the **Zero Age Main Sequence (ZAMS)** locations for stars of various masses at solar metallicity (Z = 0.014).
                
                Each point represents the position a star first reaches when hydrogen fusion in the core begins, **the ZAMS phase**.
                We observe a clear increase in both luminosity and surface temperature with mass. 

                The trend is nonlinear: higher-mass stars rapidly rise in luminosity and shift leftward in temperature (toward bluer colors), while lower-mass stars remain in the cooler and fainter region of the diagram. 

                This matches the classical shape of the main sequence on the HR diagram. 
            """)
            st.divider()

            st.image("work/ZAMS_all_metallicities.png", caption="ZAMS plot across all metallicities", use_container_width=True)
            st.divider()
            st.markdown("""
                This extended plot includes ZAMS tracks for six different metallicities: Z = 0.0001, 0.001, 0.006, 0.014, 0.02, and 0.04.

                Metallicity has a strong effect on the ZAMS location:
                - **Low-Z stars** (Z = 0.0001) are more compact, hotter, and have higher surface temperatures.
                - **High-Z stars** (Z = 0.04) are cooler and puffier due to increased opacity.

                For low-mass stars (< 2 M☉), the ZAMS points shift vertically: higher-Z stars are more luminous.
                For higher masses, metallicity affects both temperature and luminosity more significantly.

                These results align with theory: higher metallicity increases opacity, leading to lower effective temperatures and changes in convective structure, especially in the envelope.

                This visualization demonstrates how metallicity influences the starting point of stellar evolution across the mass spectrum, anchoring the evolutionary trajectories observed in the rest of the Atlas.
            """)
            st.divider()

    elif selected_stop == "Helium-Exhaustion":
        if selected_section == "Introduction":
            st.markdown("""
                Simulations with this stopping condition continue beyond hydrogen burning until the central helium fraction falls below $10^{-5}$. This allows us to explore the post-main-sequence behavior of stars, including red giant phases and helium fusion.

                These simulations include mass loss, which becomes important at later stages, especially for massive stars. Results from this phase give insight into how internal structures evolve and prepare the star for advanced burning or collapse.
            """)

        elif selected_section == "Discussion":
            st.markdown("""
                The HR diagrams now include red giant branches and post-main-sequence loops, especially for stars in the 1–10 M☉ range. Higher-mass stars (>10 M☉) evolve rapidly and may not always reach helium depletion stably due to convergence issues.

                Metallicity again plays a significant role. Higher Z leads to cooler, more extended giants. Mass loss becomes a dominant effect in this regime and influences the final evolutionary track significantly.

                Degeneracy in low-mass stars persists beyond helium burning, while high-mass stars move toward more advanced fusion phases. However, many high-mass simulations terminated early due to timestep collapse or memory issues.
            """)

        elif selected_section == "Comparison":
            st.markdown("""
                Comparing helium-depletion tracks to Gaia DR3 data confirms the expected extension of stars beyond the main sequence. Features such as:

                - Red giant clump location,
                - Broad HR loops for massive stars,
                - Deviation from main sequence at lower temperatures,

                are visible in both the simulations and the Gaia diagram.

                These comparisons validate the extended simulation runs and provide insight into how real stars evolve after core hydrogen exhaustion.
            """)

        elif selected_section == "Conclusion":
            st.markdown("""
                Simulating evolution until helium exhaustion allows deeper insight into the late stages of stellar life. The results captured key features such as:

                - Red giant formation and HR diagram loops.
                - Mass loss effects on structure and evolution.
                - Core heating and transition to advanced burning.

                While the simulations faced stability challenges in the high-mass, high-Z regime, the overall trends are consistent with theoretical expectations and observational benchmarks.
            """)

        elif selected_section == "ZAMS Plot":
            st.markdown("### Zero Age Main Sequence (ZAMS) (Same for both stopping condition)")
            st.divider()
            base_path = Path("work") 
            st.image("work/ZAMS_H_0.014.png", caption="ZAMS plot for Z = 0.014", use_container_width=True)
            st.divider()
            st.markdown("""
                This plot shows the **Zero Age Main Sequence (ZAMS)** locations for stars of various masses at solar metallicity (Z = 0.014).
                
                Each point represents the position a star first reaches when hydrogen fusion in the core begins, **the ZAMS phase**.
                We observe a clear increase in both luminosity and surface temperature with mass. 

                The trend is nonlinear: higher-mass stars rapidly rise in luminosity and shift leftward in temperature (toward bluer colors), while lower-mass stars remain in the cooler and fainter region of the diagram. 

                This matches the classical shape of the main sequence on the HR diagram. 
            """)
            st.divider()

            st.image("work/ZAMS_all_metallicities.png", caption="ZAMS plot across all metallicities", use_container_width=True)
            st.divider()
            st.markdown("""
                This extended plot includes ZAMS tracks for six different metallicities: Z = 0.0001, 0.001, 0.006, 0.014, 0.02, and 0.04.

                Metallicity has a strong effect on the ZAMS location:
                - **Low-Z stars** (Z = 0.0001) are more compact, hotter, and have higher surface temperatures.
                - **High-Z stars** (Z = 0.04) are cooler and puffier due to increased opacity.

                For low-mass stars (< 2 M☉), the ZAMS points shift vertically: higher-Z stars are more luminous.
                For higher masses, metallicity affects both temperature and luminosity more significantly.

                These results align with theory: higher metallicity increases opacity, leading to lower effective temperatures and changes in convective structure, especially in the envelope.

                This visualization demonstrates how metallicity influences the starting point of stellar evolution across the mass spectrum, anchoring the evolutionary trajectories observed in the rest of the Atlas.
            """)
            st.divider()
