# -*- coding: utf-8 -*-
"""Untitled346.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fQEuUOWl14GuG5Z0BXH_3FqoDvmNEmhm
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Streamlit App Title
st.title('Dynamic Visualization of Synaptic Plasticity')

# Add Sliders for user control
time_span = st.slider('Select Time Span for Input Intensity', 0.1, 1.0, 0.2, step=0.01)
matrix_size = st.slider('Select Matrix Size for Synaptic Weights', 50, 300, 200, step=50)

# Generate data for the top panel based on user input
input_intensity = np.linspace(0, time_span, 100)
mean_coupling = np.tanh(input_intensity * 10)  # Simulating coupling strength
response_stdp = np.tanh(input_intensity * 15)  # Simulating response (STDP)
response_fixed = np.exp(-input_intensity * 10)  # Simulating fixed response

# Create the figure and axis for the top panel
fig, ax1 = plt.subplots(2, 1, gridspec_kw={'height_ratios': [1, 2]}, figsize=(6, 8), dpi=300)

# First axis for mean coupling (left Y-axis)
ax1[0].plot(input_intensity, mean_coupling, 'o-', color='red', label='Mean Coupling K', markersize=5)
ax1[0].set_xlabel('Input Intensity (I)')
ax1[0].set_ylabel('Mean Coupling K', color='red')
ax1[0].tick_params(axis='y', labelcolor='red')

# Second axis for responses (right Y-axis)
ax2 = ax1[0].twinx()
ax2.plot(input_intensity, response_stdp, '^-', color='blue', label='R_STDP')
ax2.plot(input_intensity, response_fixed, '--', color='green', label='R_Fixed')
ax2.set_ylabel('Response <R>', color='blue')
ax2.tick_params(axis='y', labelcolor='blue')

# Add legends
ax1[0].legend(loc='upper left')
ax2.legend(loc='upper right')

# Bottom Panel: Heatmaps for Synaptic Connections
# Generate random data for synaptic connection matrix with dynamic size
synaptic_weights = np.random.rand(matrix_size, matrix_size)

# Plot the heatmap
sns.heatmap(synaptic_weights, ax=ax1[1], cmap='coolwarm', cbar_kws={'label': 'k_ij'})
ax1[1].set_title('Synaptic Weights Heatmap (k_ij)')
ax1[1].set_xlabel('Pre-synaptic Neuron #')
ax1[1].set_ylabel('Post-synaptic Neuron #')

# Show the plot in Streamlit
st.pyplot(fig)