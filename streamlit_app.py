import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st


#st.set_page_config(layout="wide")
st.title('Nested Donut Chart')
st.set_option('deprecation.showPyplotGlobalUse', False)


outer_line_selected = st.sidebar.slider("Outer line, first chart:", 0.0, 1.0, step=0.01, value=0.75)
inner_line_selected = st.sidebar.slider("Inner line, first :", 0.0, 1.0, step=0.01, value=0.5)

outer_line_selected_2 = st.sidebar.slider("Outer line, first chart:", 0.0, 5.0, step=0.01, value=3.5)
inner_line_selected_2 = st.sidebar.slider("Inner line, first :", 0.0, 5.0, step=0.01, value=2.6)


width = st.sidebar.slider("Plot width", 1, 25, value=10)
height = st.sidebar.slider("Plot height", 1, 25, value=10)

number_size = st.sidebar.slider("Numbers size", 0, 100, value=50)

def pie_chart(outer_line, inner_line):

    fig, ax = plt.subplots(figsize=(width, height))

    # Background 
    background = "white"
    fig.patch.set_facecolor(background) # figure background color
    ax.set_facecolor(background)

    # Pie charts 

    size = 0.3
    outer_vals = [1-outer_line, outer_line]
    inner_vals = [1-inner_line, inner_line]

    outer_colors = ["#CFCFCF", "#42B0D5", ]
    inner_colors = ["#CFCFCF", "#00243E", ]

    ax.pie(outer_vals, radius=2, colors=outer_colors,
            wedgeprops=dict(width=size, edgecolor='w', linewidth= 0), startangle=270)

    ax.pie(inner_vals, radius=1.8-size, colors=inner_colors,
            wedgeprops=dict(width=size, edgecolor='w', linewidth= 0), startangle=270)


    ### Annotations
    Xstart, Xend = ax.get_xlim()
    Ystart, Yend = ax.get_ylim()

    # Outer figure number
    ax.text(0, Yend+0.9, outer_line, fontsize=number_size, fontweight='light', fontfamily='sansserif',color='black', horizontalalignment='center')

    # Inner figure number
    ax.text(0, Yend-1.3, inner_line, fontsize=number_size, fontweight='light', fontfamily='sansserif',color='black', horizontalalignment='center')

    ax.set()
    #fig.tight_layout()

fig = pie_chart(outer_line=outer_line_selected, inner_line=inner_line_selected)


st.pyplot(fig)

def pie_chart_2(outer_line, inner_line):
        
        fig, ax = plt.subplots(figsize=(width, height))

        # Background 
        background = "white"
        fig.patch.set_facecolor(background) # figure background color
        ax.set_facecolor(background)

        # Pie charts 

        size = 0.3
        outer_vals = [1-(outer_line*0.2), outer_line*0.2]
        inner_vals = [1-(inner_line*0.2), inner_line*0.2]

        outer_colors = ["#CFCFCF", "#42B0D5", ]
        inner_colors = ["#CFCFCF", "#00243E", ]

        ax.pie(outer_vals, radius=2, colors=outer_colors,
                wedgeprops=dict(width=size, edgecolor='w', linewidth= 0), startangle=270)

        ax.pie(inner_vals, radius=1.8-size, colors=inner_colors,
                wedgeprops=dict(width=size, edgecolor='w', linewidth= 0), startangle=270)


        ### Annotations
        Xstart, Xend = ax.get_xlim()
        Ystart, Yend = ax.get_ylim()

        # Outer figure number
        ax.text(0, Yend+0.9, outer_line, fontsize=number_size, fontweight='light', fontfamily='sansserif',color='black', horizontalalignment='center')

        # Inner figure number
        ax.text(0, Yend-1.3, inner_line, fontsize=number_size, fontweight='light', fontfamily='sansserif',color='black', horizontalalignment='center')

        ax.set()
        #fig.tight_layout()

fig_2 = pie_chart_2(outer_line=outer_line_selected_2, inner_line=inner_line_selected_2)

st.pyplot(fig_2)