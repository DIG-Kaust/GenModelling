import numpy as np
import matplotlib.pyplot as plt

def plot_random_samples(windows, num_plots=10):
    """
    Plots randomly selected samples from a 4D array.

    Parameters:
        windows (numpy.ndarray): A 4D array of shape (num_samples, channels, height, width).
        num_plots (int, optional): Number of random samples to plot. Defaults to 10.

    Returns:
        None
    """
    num_samples = windows.shape[0]

    # Generate random indices to select samples
    random_indices = np.random.choice(num_samples, size=num_plots, replace=False)

    # Create a subplot grid for the plots
    fig, axs = plt.subplots(2, 5, figsize=(12, 6))

    # Plot the randomly selected samples
    for i, idx in enumerate(random_indices):
        sample = windows[idx, 0]  # Assuming grayscale images (channels=1)
        row = i // 5
        col = i % 5
        axs[row, col].imshow(sample, cmap='gray')
        # axs[row, col].axis('off')
        axs[row, col].set_title(f"Sample {idx+1}")
        axs[row, col].set_xticks([])
        axs[row, col].set_yticks([])
        # axs[row, col].tick_params(axis='both', which='both', length=0)

    # Adjust the spacing between subplots
    plt.tight_layout()

    # Show the plot
    return fig
