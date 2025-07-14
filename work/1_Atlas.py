import streamlit as st
import os
import json

from utils import setup_page
setup_page()

# st.set_page_config(page_title="Stellar Atlas", layout="wide")
st.title("🌌 Stellar Evolution Atlas")

# First dropdown: Select Stopping Condition group
stop_groups = sorted([d for d in os.listdir("work") if os.path.isdir(f"work/{d}")])
selected_stop = st.selectbox("Select Stopping Condition", stop_groups)


# Second dropdown: Select section
sections = ["Introduction", "Discussion", "Comparison", "Conclusion", "Star Simulations"]
selected_section = st.selectbox(f"Select Section for {selected_stop}", sections)

if selected_section == "Star Simulations":
    
    # Third dropdown: Select Z group
    z_groups = sorted([d for d in os.listdir(f"work/{selected_stop}") if os.path.isdir(f"work/{selected_stop}/{d}")])
# selected_z = st.selectbox("Select Metallicity Group (Z)", z_groups)
    selected_z = st.selectbox(f"Select Section for {selected_stop}", z_groups)

    plot_path = f"work/{selected_stop}/{selected_z}"
    path = f"work/{selected_stop}/{selected_z}"

    if selected_z == "Individual-Example":

      mass_groups = sorted([d for d in os.listdir(f"work/{selected_stop}/Individual-Example") if os.path.isdir(f"work/{selected_stop}/Individual-Example/{d}")])
      selected_mass = st.selectbox(f"Select the mass", mass_groups)

      if selected_mass == "50M☉":
      # Load metadata
        with open(f"{path}/{selected_mass}/metadata.json") as f:
            meta = json.load(f)

        st.subheader(f"{meta['star_name']} — {meta['initial_mass']} M☉")
      # --- HR Diagram ---
        st.markdown("## Hertzsprung–Russell Diagram")
        with st.container():
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.image(f"{path}/{selected_mass}/hr_diagram.png", caption="HR Diagram", width=600)

    # Explanation...
        st.markdown("The above is the **HR diagram** produced from the *MESA* data and plotted using *matplotlib* and *mesa_reader*. The simulated star has a mass of 50M☉ and metallicity of 0.014. The metallicity of 0.014 has been discussed in asplund et al. (Citated in the final report) to be the metallicity of sun, which makes the study and interpretation of this metallicty important. From the HR diagram, we can observe how the star changes in the due couse of its life. It first starts at ZAMS followed by the pre-main sequence and the main sequence. As the stopping condition of this simulation was at hydrogen depletion, it has not yet evolved into a red giant, hence we do not see a shoot in the luminosity. The star is at the verge of evolving into a red giant.")

        st.divider()

    # --- Core Temp vs Density ---
        st.markdown("## Core Temperature vs Density Evolution")
        with st.container():
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.image(f"{path}/{selected_mass}/Tc_vs_rhoc.png", caption="Core Temp vs Density", width=600)

    # Explanation ...
        st.markdown("The above plot shows the variation of core temperature as the core density varies. We can observe that in the log scale that as the core temperature increases, the core density also increases. The plot is almost similar to the plot of y = x. ")

        st.divider()

    # --- Radius vs Age ---
        st.markdown("## Age vs Radius")
        with st.container():
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.image(f"{path}/{selected_mass}/age_vs_radius.png", caption="Radius Evolution", width=600)

      # Explanation...
        st.markdown("This graph shows the evolution of the star's radius with time. As it can be seen, the radius has a sharp drop in the beginning, mainly due to the starting convergence of the model or from the simulation of pre-main sequence model (also known as 'protostar'). The lowest point near the zero age should be the **ZAMS** point, the point at which the **protostar** evolves and becomes a **star** starting the fusion of **hydrogen**. The radius gradually increases from this point, and , a drop is seen at around $3.7 * 10^6$, which symbolizes the exhaustion of core hydrogen, and the star preparing to start the helium burning.")

        st.divider()

    # --- Luminosity vs Age ---
        st.markdown("## Age vs Luminosity")
        with st.container():
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.image(f"{path}/{selected_mass}/age_vs_luminosity.png", caption="Luminosity Evolution", width=600)

        st.divider()

    # --- HR Evolution Video ---
        st.markdown("## HR Diagram Animation")
        with open(f"{path}/{selected_mass}/hr_evolution.mp4", "rb") as f:
              video_bytes = f.read()
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
              st.video(video_bytes)

        st.divider()

    # --- T-Rho Video ---
        st.markdown("## Core Conditions Animation")
        with open(f"{path}/{selected_mass}/TRho_evolution.mp4", "rb") as f:
              video_bytes2 = f.read()
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
              st.video(video_bytes2)


      if selected_mass == "20M☉":
      # Load metadata
        with open(f"{path}/{selected_mass}/metadata.json") as f:
            meta = json.load(f)

        st.subheader(f"{meta['star_name']} — {meta['initial_mass']} M☉")
      # --- HR Diagram ---
        st.markdown("## Hertzsprung–Russell Diagram")
        with st.container():
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.image(f"{path}/{selected_mass}/hr_diagram.png", caption="HR Diagram", width=600)

    # Explanation...
        st.markdown("The above is the **HR diagram** produced from the *MESA* data and plotted using *matplotlib* and *mesa_reader*. The simulated star has a mass of 20M☉ and metallicity of 0.014. The metallicity of 0.014 has been discussed in asplund et al. (Citated in the final report) to be the metallicity of sun, which makes the study and interpretation of this metallicty important. From the HR diagram, we can observe how the star changes in the due couse of its life. It first starts at ZAMS followed by the pre-main sequence and the main sequence. As the stopping condition of this simulation was at hydrogen depletion, it has not yet evolved into a red giant, hence we do not see a shoot in the luminosity. The star is at the verge of evolving into a red giant.")

        st.divider()

    # --- Core Temp vs Density ---
        st.markdown("## Core Temperature vs Density Evolution")
        with st.container():
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.image(f"{path}/{selected_mass}/Tc_vs_rhoc.png", caption="Core Temp vs Density", width=600)

    # Explanation ...
        st.markdown("The above plot shows the variation of core temperature as the core density varies. We can observe that in the log scale that as the core temperature increases, the core density also increases. The plot is almost similar to the plot of y = x. ")

        st.divider()

    # --- Radius vs Age ---
        st.markdown("## Age vs Radius")
        with st.container():
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.image(f"{path}/{selected_mass}/age_vs_radius.png", caption="Radius Evolution", width=600)

      # Explanation...
        st.markdown("This graph shows the evolution of the star's radius with time. As it can be seen, the radius has a sharp drop in the beginning, mainly due to the starting convergence of the model or from the simulation of pre-main sequence model (also known as 'protostar'). The lowest point near the zero age should be the **ZAMS** point, the point at which the **protostar** evolves and becomes a **star** starting the fusion of **hydrogen**. The radius gradually increases from this point, and , a drop is seen at around $3.7 * 10^6$, which symbolizes the exhaustion of core hydrogen, and the star preparing to start the helium burning.")

        st.divider()

    # --- Luminosity vs Age ---
        st.markdown("## Age vs Luminosity")
        with st.container():
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.image(f"{path}/{selected_mass}/age_vs_luminosity.png", caption="Luminosity Evolution", width=600)

        st.divider()

    # --- HR Evolution Video ---
        st.markdown("## HR Diagram Animation")
        with open(f"{path}/{selected_mass}/hr_evolution.mp4", "rb") as f:
              video_bytes = f.read()
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
              st.video(video_bytes)

        st.divider()

    # --- T-Rho Video ---
        st.markdown("## Core Conditions Animation")
        with open(f"{path}/{selected_mass}/TRho_evolution.mp4", "rb") as f:
              video_bytes2 = f.read()
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
              st.video(video_bytes2)


      if selected_mass == "1M☉":
      # Load metadata
        with open(f"{path}/{selected_mass}/metadata.json") as f:
            meta = json.load(f)

        st.subheader(f"{meta['star_name']} — {meta['initial_mass']} M☉")
      # --- HR Diagram ---
        st.markdown("## Hertzsprung–Russell Diagram")
        with st.container():
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.image(f"{path}/{selected_mass}/hr_diagram.png", caption="HR Diagram", width=600)

    # Explanation...
        st.markdown("The above is the **HR diagram** produced from the *MESA* data and plotted using *matplotlib* and *mesa_reader*. The simulated star has a mass of 1M☉ and metallicity of 0.014. The metallicity of 0.014 has been discussed in asplund et al. (Citated in the final report) to be the metallicity of sun, which makes the study and interpretation of this metallicty important. From the HR diagram, we can observe how the star changes in the due couse of its life. It first starts at ZAMS followed by the pre-main sequence and the main sequence. As the stopping condition of this simulation was at hydrogen depletion, it has not yet evolved into a red giant, hence we do not see a shoot in the luminosity. The star is at the verge of evolving into a red giant.")

        st.divider()

    # --- Core Temp vs Density ---
        st.markdown("## Core Temperature vs Density Evolution")
        with st.container():
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.image(f"{path}/{selected_mass}/Tc_vs_rhoc.png", caption="Core Temp vs Density", width=600)

    # Explanation ...
        st.markdown("The above plot shows the variation of core temperature as the core density varies. We can observe that in the log scale that as the core temperature increases, the core density also increases. The plot is almost similar to the plot of y = x. ")

        st.divider()

    # --- Radius vs Age ---
        st.markdown("## Age vs Radius")
        with st.container():
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.image(f"{path}/{selected_mass}/age_vs_radius.png", caption="Radius Evolution", width=600)

      # Explanation...
        st.markdown("This graph shows the evolution of the star's radius with time. As it can be seen, the radius has a sharp drop in the beginning, mainly due to the starting convergence of the model or from the simulation of pre-main sequence model (also known as 'protostar'). The lowest point near the zero age should be the **ZAMS** point, the point at which the **protostar** evolves and becomes a **star** starting the fusion of **hydrogen**. The radius gradually increases from this point, and , a drop is seen at around $3.7 * 10^6$, which symbolizes the exhaustion of core hydrogen, and the star preparing to start the helium burning.")

        st.divider()

    # --- Luminosity vs Age ---
        st.markdown("## Age vs Luminosity")
        with st.container():
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.image(f"{path}/{selected_mass}/age_vs_luminosity.png", caption="Luminosity Evolution", width=600)

        st.divider()

    # --- HR Evolution Video ---
        st.markdown("## HR Diagram Animation")
        with open(f"{path}/{selected_mass}/hr_evolution.mp4", "rb") as f:
              video_bytes = f.read()
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
              st.video(video_bytes)

        st.divider()

    # --- T-Rho Video ---
        st.markdown("## Core Conditions Animation")
        with open(f"{path}/{selected_mass}/TRho_evolution.mp4", "rb") as f:
              video_bytes2 = f.read()
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
              st.video(video_bytes2)
  
    else:
      st.markdown("## HR Diagram")
      with st.container():
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(f"{plot_path}/HRD_highlighted.png", caption="All HR diagrams plotted in single diagram", width=600)
      st.divider()

      st.markdown("## HR Diagram Animation")
      with open(f"{path}/hr_mass_evolution.mp4", "rb") as f:
          video_bytes = f.read()
      col1, col2, col3 = st.columns([1, 2, 1])
      with col2:
          st.video(video_bytes)
      
      st.divider()

      st.markdown("## Core temperature vs core density plot")
      with st.container():
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(f"{plot_path}/Tc_Rhoc.png", caption="Temp vs. density", width=600)
      st.divider()

      st.markdown("## Core temperature vs core density Animation")
      with open(f"{path}/Tc_vs_rhoc_evolution.mp4", "rb") as f:
          video_bytes = f.read()
      col1, col2, col3 = st.columns([1, 2, 1])
      with col2:
          st.video(video_bytes)
      
      st.divider()

      st.markdown("## Luminosity change with Age")
      with st.container():
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(f"{plot_path}/Age_Luminosity.png", caption="Luminosity", width=600)
      st.divider()

      st.markdown("## Luminosity change with Age Animation")
      with open(f"{path}/age_vs_luminosity_evolution.mp4", "rb") as f:
          video_bytes = f.read()
      col1, col2, col3 = st.columns([1, 2, 1])
      with col2:
          st.video(video_bytes)
      
      st.divider()

      st.markdown("## Radius change with Age")
      with st.container():
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(f"{plot_path}/Age_Radius.png", caption="Radius of the star", width=600)
      st.divider()

      st.markdown("## Radius change with Age Animation")
      with open(f"{path}/age_vs_radius_evolution.mp4", "rb") as f:
          video_bytes = f.read()
      col1, col2, col3 = st.columns([1, 2, 1])
      with col2:
          st.video(video_bytes)
      
      st.divider()

      st.markdown("## Central **hydrogen** change with Age")
      with st.container():
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(f"{plot_path}/Central_H.png", caption="Central Density", width=600)
      st.divider()

      st.markdown("## Central **hydrogen** change with Age Animation")
      with open(f"{path}/central_H_vs_time_evolution.mp4", "rb") as f:
          video_bytes = f.read()
      col1, col2, col3 = st.columns([1, 2, 1])
      with col2:
          st.video(video_bytes)
      
      st.divider()



#     # Third dropdown: Star selection
#     star_dirs = sorted([d for d in os.listdir(f"work/{selected_stop}/{selected_z}") if os.path.isdir(f"work/{selected_stop}/{selected_z}/{d}")])
#     selected_star = st.selectbox("Select a Star Model", star_dirs)

#     path = f"work/{selected_stop}/{selected_z}/{selected_star}"

#     # Load metadata
#     with open(f"{path}/metadata.json") as f:
#         meta = json.load(f)

#     st.subheader(f"{meta['star_name']} — {meta['initial_mass']} M☉")

#     # --- HR Diagram ---
#     st.markdown("## Hertzsprung–Russell Diagram")
#     with st.container():
#         col1, col2, col3 = st.columns([1, 2, 1])
#         with col2:
#             st.image(f"{path}/hr_diagram.png", caption="HR Diagram", width=600)

#     # Explanation...
#     st.markdown("Your explanation goes here...")

#     st.divider()

#     # --- Core Temp vs Density ---
#     st.markdown("## Core Temperature vs Density Evolution")
#     with st.container():
#         col1, col2, col3 = st.columns([1, 2, 1])
#         with col2:
#             st.image(f"{path}/Tc_vs_rhoc.png", caption="Core Temp vs Density", width=600)

#     st.divider()

#     # --- Radius vs Age ---
#     st.markdown("## Age vs Radius")
#     with st.container():
#         col1, col2, col3 = st.columns([1, 2, 1])
#         with col2:
#             st.image(f"{path}/age_vs_radius.png", caption="Radius Evolution", width=600)

#     st.divider()

#     # --- Luminosity vs Age ---
#     st.markdown("## Age vs Luminosity")
#     with st.container():
#         col1, col2, col3 = st.columns([1, 2, 1])
#         with col2:
#             st.image(f"{path}/age_vs_luminosity.png", caption="Luminosity Evolution", width=600)

#     st.divider()

#     # --- HR Evolution Video ---
#     st.markdown("## HR Diagram Animation")
#     with open(f"{path}/hr_evolution.mp4", "rb") as f:
#         video_bytes = f.read()
#     col1, col2, col3 = st.columns([1, 2, 1])
#     with col2:
#         st.video(video_bytes)

#     st.divider()

#     # --- T-Rho Video ---
#     st.markdown("## Core Conditions Animation")
#     with open(f"{path}/TRho_evolution.mp4", "rb") as f:
#         video_bytes2 = f.read()
#     col1, col2, col3 = st.columns([1, 2, 1])
#     with col2:
#         st.video(video_bytes2)

# else:
#     st.markdown(f"## {selected_section}")
#     st.markdown(f"Write your detailed content for **{selected_section}** of **{selected_stop}** here.")

#     if selected_stop == "Helium_Exhaustion":
#         if selected_section == "Discussion":
#             st.markdown("This is a dummy discussion.")
#     if selected_stop == "Hydrogen_Exhaustion":
#         if selected_section == "Discussion":
#             st.markdown("This is a dummy discussion for Hydrogen Exhaustion")