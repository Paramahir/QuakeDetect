import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def generate_seismic_data(num_samples, num_features):
    seismic_data = []
    labels = []
    for _ in range(num_samples):
        waveform = np.random.randn(num_features)
        num_events = np.random.randint(1, 4)  # Random number of events (1 to 3)
        labels.append(1 if num_events >= 2 else 0)  # Example condition for labeling
        for _ in range(num_events):
            event_start = np.random.randint(0, num_features)
            event_end = min(num_features, event_start + np.random.randint(5, 20))
            event_amplitude = np.random.uniform(1, 3)
            waveform[event_start:event_end] += event_amplitude
        seismic_data.append(waveform)
    return np.array(seismic_data), np.array(labels)

num_samples = 1000
num_features = 1000
seismic_data, labels = generate_seismic_data(num_samples, num_features)

data = pd.DataFrame(seismic_data)
data['label'] = labels  # Add labels to the DataFrame

plt.figure(figsize=(10, 6))
subset = np.random.choice(range(num_samples), 5, replace=False)
for i, idx in enumerate(subset, 1):
    plt.subplot(5, 1, i)
    plt.plot(data.iloc[idx, :-1])
    plt.title(f'Sample {idx + 1} - Label: {data.iloc[idx, -1]}')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
plt.tight_layout()
plt.show()

data.to_csv('seismic_data_with_labels.csv', index=False)
print("Synthetic seismic data with labels saved to 'seismic_data_with_labels.csv'.")
