# 4. PREDICT PENTAX 17 DIFFUSION (Steps 5, 6, 7)
# We use historical p and q, but adjust M for the modern niche market.
# Fermi Logic: Assume there are ~5 million potential global buyers for a premium film camera revival.
M_pentax = 5000  # in thousands
t_future = np.arange(1, 21) # Predict for the next 20 years

pentax_forecast = bass_model(t_future, p_hist, q_hist, M_pentax)
cum_pentax = np.cumsum(pentax_forecast)


# 5. VISUALIZATION
plt.figure(figsize=(12, 6))

# Subplot 1: Historical Fit
plt.subplot(1, 2, 1)
plt.scatter(years, sales, color='red', label='Actual Data (CIPA)')
plt.plot(years, bass_model(t, p_hist, q_hist, M_hist), label='Bass Model Fit')
plt.title('Historical Film Camera Diffusion')
plt.xlabel('Year')
plt.ylabel('Sales (1,000 units)')
plt.legend()

# Subplot 2: Pentax 17 Prediction
plt.subplot(1, 2, 2)
plt.bar(t_future, pentax_forecast, color='green', alpha=0.7, label='Predicted Annual Sales')
plt.plot(t_future, cum_pentax, color='blue', marker='o', label='Cumulative Adopters')
plt.title('Pentax 17 Predicted Diffusion Path')
plt.xlabel('Years from Launch')
plt.ylabel('Units (1,000s)')
plt.legend()

plt.tight_layout()
plt.show()

# Display Adopter Table for Step 7
forecast_table = pd.DataFrame({
    'Year': t_future,
    'Annual_Adopters': pentax_forecast.round(2),
    'Total_Adopters': cum_pentax.round(2)
})
print("\nPredicted Adopters by Period (Pentax 17):")
print(forecast_table)

# Saving the forecast table as a csv file
forecast_table.to_csv('pentax_predictions.csv', index=False)
