import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st


#st.set_page_config(layout="wide")
st.title('Nested Pie Chart')
st.set_option('deprecation.showPyplotGlobalUse', False)


overall_engagement_selected = st.sidebar.slider("Outer line:", 1, 100, value=75)
maersk_engagement_selected = st.sidebar.slider("Inner line:", 1, 100, value=50)

width = st.sidebar.slider("plot width", 1, 25, value=10)
height = st.sidebar.slider("plot height", 1, 25, value=10)

number_size = st.sidebar.slider("Numbers size", 0, 100, value=50)

def pie_chart(overall_engagement, maersk_engagement):
    
    overall_engagement = overall_engagement/100
    maersk_engagement = maersk_engagement/100

    fig, ax = plt.subplots(figsize=(width, height))

    # Background 
    background = "white"
    fig.patch.set_facecolor(background) # figure background color
    ax.set_facecolor(background)

    # Pie charts 

    size = 0.3
    outer_vals = [1-overall_engagement, overall_engagement]
    inner_vals = [1-maersk_engagement, maersk_engagement]

    outer_colors = ["#CFCFCF", "#42B0D5", ]
    inner_colors = ["#CFCFCF", "#00243E", ]

    ax.pie(outer_vals, radius=2, colors=outer_colors,
            wedgeprops=dict(width=size, edgecolor='w', linewidth= 0), startangle=270)

    ax.pie(inner_vals, radius=1.8-size, colors=inner_colors,
            wedgeprops=dict(width=size, edgecolor='w', linewidth= 0), startangle=270)


    ### Annotations
    Xstart, Xend = ax.get_xlim()
    Ystart, Yend = ax.get_ylim()

    # Overall engagement Survey Rating
    ax.text(0, Yend+0.9, overall_engagement, fontsize=number_size, fontweight='light', fontfamily='sansserif',color='black', horizontalalignment='center')
    #ax.text(3, Yend+1, 'Overall Engagement', fontsize=10, fontweight='ultralight', fontfamily='sansserif',color='black')
    #ax.text(3, Yend+0.8, 'Survey Rating', fontsize=10, fontweight='ultralight', fontfamily='sansserif',color='black')
    #ax.hlines(y = Yend+ 0.95, xmin = Xstart+1.6, xmax = Xend+1.6, linewidth=0.5)

    # Maersk Overall Average
    ax.text(0, Yend-1.3, maersk_engagement, fontsize=number_size, fontweight='light', fontfamily='sansserif',color='black', horizontalalignment='center')
    #ax.text(3, Yend-1.3, 'Maersk Overall Average', fontsize=10, fontweight='ultralight', fontfamily='sansserif',color='black')
    #ax.hlines(y = Yend-1.25, xmin = Xstart+1.6, xmax = Xend+1.6, linewidth=0.5)

    # Target
    #ax.text(2.8, Yend-2, 'Company Target', fontsize=10, fontweight='ultralight', fontfamily='sansserif',color='black')
    #ax.text(2.3, Yend-2, 0.75, fontsize=10, fontweight='ultralight', fontfamily='sansserif',color='red')
    #ax.hlines(y = Yend-1.95, xmin = Xstart+1.9, xmax = Xend+1, linewidth=0.5, color='red')


    ax.set()
    #fig.tight_layout()

fig = pie_chart(overall_engagement=overall_engagement_selected, maersk_engagement=maersk_engagement_selected)

st.pyplot(fig)


    
