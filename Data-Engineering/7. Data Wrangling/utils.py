import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Functions used for explaining probability distribution

#1: Getting frequency of each bin
def get_freq_data(x_lower, x_upper, data, bin_width):
    bins = np.arange(x_lower, x_upper+1, bin_width)
    frequencies = np.zeros(len(bins))
    sorted_data = np.sort(data, axis=None) # sorts into ascending order
    
    current_x = x_lower
    current_bin = 0
    bins[current_bin] = current_x
    data_idx = 0
    
    # While our current bin does not go beyond our upper limit
    while (current_bin < len(bins)-1) and (data_idx < len(sorted_data)-1):
        if sorted_data[data_idx] <= current_x + bin_width:
            frequencies[current_bin]+=1
            data_idx+=1
        else:
            current_bin+=1
            current_x += bin_width
            bins[current_bin] = current_x
    return bins, frequencies
    
#2: Getting probability of each bin
def get_prob_data(x_lower, x_upper, data, bin_width):
    bins, frequencies = get_freq_data(x_lower, x_upper, data, bin_width)
    probabilities = frequencies/np.sum(frequencies)
    return bins, probabilities

#3: Getting probability density of each bin
def get_density_data(x_lower, x_upper, data, bin_width):
    bins, probabilities = get_prob_data(x_lower, x_upper, data, bin_width)
    prob_densities = probabilities/bin_width
    return bins, prob_densities


#4: Returns a go.Figure() object with the histogram on it
def get_hist(bins, frequencies):
    fig = go.Figure()
    for current_bin, frequency in zip(bins, frequencies):
        fig.add_trace(go.Bar(x=[current_bin], y=[frequency], marker_color="orange"))
    fig.update_layout(showlegend=False, bargap=0)
    return fig
    

#5: Adds the appropriate histogram to the figure or to a subplot
def add_hist(fig, bins, frequencies, r=None, c=None):
    #Normal Plot
    if r==None:
        for current_bin, frequency in zip(bins, frequencies):
            fig.add_trace(go.Bar(x=[current_bin], y=[frequency], marker_color="orange"))
        fig.update_layout(showlegend=False, bargap=0)
    #Subplot
    else:
        for current_bin, frequency in zip(bins, frequencies):
            fig.add_trace(go.Bar(x=[current_bin], y=[frequency], marker_color="orange"), row=r, col=c)
        fig.update_layout(showlegend=False, bargap=0)
    return fig


#6: Adds a histogram estimate of a given interval of a desired pdf
def add_hist_approx(fig, x_lower, x_upper, pdf_func, bin_width, r=None, c=None):
    # Defining initial variables
    current_x = x_lower
    while current_x <= x_upper:
        if r==None:
            fig.add_trace(go.Bar(x=[current_x], y=[pdf_func(current_x)], marker_color="orange"))
        else:
            fig.add_trace(go.Bar(x=[current_x], y=[pdf_func(current_x)], marker_color="orange"), row=r, col=c)
        current_x = current_x + bin_width
    fig.update_layout(showlegend=False, bargap=0)
    return fig

#7: Crops the histogram given the densities and bins and only returns desired interval
def interval_hist(x_lower, x_upper, prob_densities, bins):
    prob_densities_new = np.array([])
    bins_new = np.array([])
    for current_bin, density in zip(bins, prob_densities):
        if density >= x_lower:
            if density < x_upper:
                prob_densities_new = np.append(prob_densities_new, density)
                bins_new = np.append(bins_new, current_bin)
    return bins_new, prob_densities_new
    
#8: Estimates the probability of an interval given a bin width and PDF
def prob_estimate(x_lower, x_upper, pdf_func, bin_width):
    area_count = 0
    current_x = x_lower
    while current_x < x_upper:
        area_count+= pdf_func(current_x)*bin_width # adding the area of the current interval
        current_x += bin_width
    return area_count
    

#9: Normal PDF
def normal(x, mean, std):
    exponent = ((x-mean)/std)**2
    exponent *= -0.5
    output = np.exp(exponent)/(std*np.sqrt(2*np.pi))
    return output

#10: Converts an RGB image to Grayscale
def rgb2gray(rgb_img):
    rows, columns,_ = np.shape(rgb_img)
    gray_img = np.zeros((rows, columns))
    # computing grayscale value at each pixel
    for i in range(rows):
        for j in range(columns):
            R, G, B = rgb_img[i, j, :]
            gray_img[i, j] = (0.3*R) + (0.59*G) + (0.11*B)
    return gray_img


# Visualization Code
#1:
def visualize_prob_hist(x):
	fig = make_subplots(rows=2, cols=2,
                    subplot_titles = ['bin width = 5cm', 'bin width = 3cm', 'bin width = 1cm', 'bin width = 0.1cm'])
	bin_widths = np.array([[5, 3], [1, 0.1]])

	for r in range(2):
		for c in range(2):
			bins, probabilities = get_prob_data(150, 200, x, bin_widths[r, c])
			fig = add_hist(fig, bins, probabilities, r+1, c+1)
			fig.update_yaxes(title_text="Probability", row=r+1, col=c+1)
			fig.update_xaxes(title_text="Height(cm)", row=r+1, col=c+1)
        
	fig.update_layout(showlegend=False)
	fig.show()

#2:
def visualize_density_hist(x):
	fig = make_subplots(rows=2, cols=2,
                    subplot_titles = ['bin width = 5cm', 'bin width = 3cm', 'bin width = 1cm', 'bin width = 0.1cm'])

	bin_widths = np.array([[5, 3], [1, 0.1]])

	for r in range(2):
		for c in range(2):
			bins, prob_densities = get_density_data(150, 200, x, bin_widths[r, c])
			fig = add_hist(fig, bins, prob_densities, r+1, c+1)
			fig.update_yaxes(title_text="Probability Density", row=r+1, col=c+1)
			fig.update_xaxes(title_text="Height(cm)", row=r+1, col=c+1)
        
	fig.update_layout(showlegend=False)
	fig.show()
	
#3:
def visualize_exp_approx(x_sample, x_true, f_true):
	fig = make_subplots(rows=2, cols=2,
                    subplot_titles = ['bin width = 5cm', 'bin width = 3cm', 'bin width = 1cm', 'bin width = 0.1cm'])

	bin_widths = np.array([[5, 3], [1, 0.1]])

	for r in range(2):
		for c in range(2):
			bins, prob_densities = get_density_data(0, 5, x_sample, bin_widths[r, c])
			fig = add_hist(fig, bins, prob_densities, r+1, c+1)
			fig.add_trace(go.Scatter(x=x_true, y=f_true, marker_color="black"), row=r+1, col=c+1)
			fig.update_yaxes(title_text="Probability Density", row=r+1, col=c+1)
			fig.update_xaxes(title_text="Height(cm)", row=r+1, col=c+1)
        
	fig.update_layout(showlegend=False)
	fig.show()
	
#4:
def visualize_exp_interval(x_true, f_true, pdf_func):
	interval_floor = 1
	interval_ceil = 3
	bin_widths = np.array([[3, 1], [0.1, 0.05]])
	probs = [prob_estimate(interval_floor, interval_ceil, pdf_func, bw) for bw in bin_widths.flatten()]
	widths = ['width = 3', 'width = 1', 'width = 0.1', 'width = 0.05']
	titles = [widths[i] + ', ' + 'prob = ' + str(round(probs[i], 4)) for i in range(len(widths))]

	fig = make_subplots(rows=2, cols=2,
                    subplot_titles = titles)


	for r in range(2):
		for c in range(2):
			fig = add_hist_approx(fig, interval_floor, interval_ceil, pdf_func, bin_widths[r, c], r+1, c+1)
			fig.add_trace(go.Scatter(x=x_true, y=f_true, marker_color="black"), row=r+1, col=c+1)
			fig.update_yaxes(title_text="Probability Density", row=r+1, col=c+1)
			fig.update_xaxes(title_text="x", row=r+1, col=c+1)
        
	fig.update_layout(showlegend=False)
	fig.show()

#5:
def visualize_exp_true(x_true, f_true):
	print("True Mean: 1, True Variance: 1")
	fig = go.Figure()
	fig.add_trace(go.Scatter(x=x_true, y=f_true, marker_color="black"))
	fig.update_layout(
    	title_text='Exponential Distribution', # title of plot
    	xaxis_title_text='x', # xaxis label
    	yaxis_title_text='Probability Density', # yaxis label
	)
	fig.show()
	
#6:
def visualize_mean_approx(n_vals, mean_sets):
	titles = ["Estimated distribution(n={size})".format(size=n) for n in n_vals]
	fig = make_subplots(rows=2, cols=2, subplot_titles=titles)

	idx = 0
	for r in range(2):
		for c in range(2):
			bins, prob_densities = get_density_data(0, 5, mean_sets[idx, :], 0.05)
			fig = add_hist(fig, bins, prob_densities, r+1, c+1)
			fig.update_yaxes(title_text="Probability Density", row=r+1, col=c+1)
			fig.update_xaxes(title_text="x", row=r+1, col=c+1)
			idx +=1
	fig.show()


#7:
def visualize_normal_interval(interval_floor, interval_ceil, normal_func, mean, std, bw=0.1):

	# Determined
	x_true = np.linspace(mean- 4*std, mean+ 4*std, 1000)
	f_true = normal_func(x_true)
	
	fig = go.Figure()
	fig = add_hist_approx(fig, interval_floor, interval_ceil, normal_func, bw)
	fig.add_trace(go.Scatter(x=x_true, y=f_true, marker_color="black"))
	fig.update_layout(
    	title_text='Height Normal Distribution', # title of plot
    	xaxis_title_text='x', # xaxis label
    	yaxis_title_text='Probability Density', # yaxis label
    	showlegend=False
	)
	fig.show()

#8:
def visualize_two_tail(critical_value, normal_func, bw=0.1):
	# Determined
	x_true = np.linspace(-4, 4, 1000)
	f_true = normal_func(x_true)
	bound_mag = 4
	

	fig = go.Figure()
	fig = add_hist_approx(fig, -bound_mag, -critical_value, normal_func, bw)
	fig = add_hist_approx(fig, critical_value, bound_mag, normal_func, bw)
	fig.add_trace(go.Scatter(x=x_true, y=f_true, marker_color="black"))
	fig.update_layout(
    	title_text='Height Normal Distribution', # title of plot
    	xaxis_title_text='x', # xaxis label
    	yaxis_title_text='Probability Density', # yaxis label
    	showlegend=False
	)
	fig.show()

