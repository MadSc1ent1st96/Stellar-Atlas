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

sections = ["Introduction", "Discussion", "Comparison", "Conclusion", "Star Simulations"]
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
                with st.container():
                    col1, col2, col3 = st.columns([1, 2, 1])
                    with col2:
                        st.image(mass_path / filename, caption=caption, use_container_width=True)
                st.divider()

            def display_video(title, filename):
                st.markdown(f"## {title}")
                with open(mass_path / filename, "rb") as f:
                    video_bytes = f.read()
                col1, col2, col3 = st.columns([1, 2, 1])
                with col2:
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
            with st.container():
                col1, col2, col3 = st.columns([1, 2, 1])
                with col2:
                    st.image(base_path / filename, caption=caption, use_container_width=True)
            st.divider()

        def display_z_level_video(title, filename):
            st.markdown(f"## {title}")
            with open(base_path / filename, "rb") as f:
                video_bytes = f.read()
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
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
    st.markdown(f"Write your detailed content for **{selected_section}** of **{selected_stop}** here.")

    # Optional placeholders
    if selected_stop == "Hydrogen_Exhaustion" and selected_section == "Discussion":
        st.markdown("This is a placeholder for the hydrogen exhaustion discussion section.")
    if selected_stop == "Helium_Exhaustion" and selected_section == "Discussion":
        st.markdown("This is a placeholder for the helium exhaustion discussion section.")
