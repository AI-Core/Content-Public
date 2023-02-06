# %%
import os
import torch
import plotly.express as px
from plotly.subplots import make_subplots
import numpy as np
import sys
sys.path.append('../../../../../..')
from utils.generate_gifs import find_gifs  # noqa


def generate_params():
    def reset_params():
        w = torch.tensor(0).float().unsqueeze(0)
        w = w.unsqueeze(0)
        b = torch.tensor(0).float().unsqueeze(0)
        return w, b

    thetas = torch.linspace(0, 2*np.pi, 100)
    w, b = reset_params()
    for theta in thetas:
        w = torch.ones_like(w) * torch.sin(theta)
        yield w, b

    w, b = reset_params()
    for theta in thetas:
        b = torch.ones_like(b) * torch.sin(theta)
        b *= 5
        yield w, b

    w, b = reset_params()
    for theta in thetas:
        w = torch.ones_like(w) * torch.sin(theta)
        b = torch.ones_like(b) * torch.cos(theta)
        b *= 5
        yield w, b


class LinearModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1, 1)

    def forward(self, x):
        return self.linear(x)


def generate_frames(output_name):
    model = LinearModel()
    inputs = np.linspace(-10, 10)
    inputs = torch.tensor(inputs).float().unsqueeze(1)

    if not os.path.exists("frames"):
        os.makedirs("frames", exist_ok=True)

    for idx, params in enumerate(generate_params()):
        w, b = params
        model.linear.weight = torch.nn.Parameter(w)
        model.linear.bias = torch.nn.Parameter(b)
        predictions = model(inputs)
        predictions = predictions.squeeze().detach().numpy()
        fig = make_subplots(rows=1, cols=2, specs=[
                            [{"type": "scatter"}, {"type": "scatter"}]])
        fig.add_trace(px.line(x=inputs.squeeze().numpy(),
                      y=predictions).data[0], row=1, col=1)

        b = b.squeeze().detach().numpy()
        w = w.squeeze().detach().numpy()
        fig.add_trace(px.scatter(x=[b], y=[w]).data[0], row=1, col=2)

        fig.update_xaxes(range=[-10, 10], row=1, col=1)
        fig.update_yaxes(range=[-10, 10], row=1, col=1)
        fig.update_xaxes(title_text="Input", row=1, col=1)
        fig.update_yaxes(title_text="Prediction", row=1, col=1)

        fig.update_xaxes(range=[-10, 10], row=1, col=2)
        fig.update_yaxes(range=[-1, 1], row=1, col=2)
        fig.update_xaxes(title_text="Bias", row=1, col=2)
        fig.update_yaxes(title_text="Weight", row=1, col=2)

        fig.update_layout(
            title_text=f"b: {np.round(b, 2)}, w: {float(w.round(2))}")

        fig.update_layout(width=1000, height=500)

        fig.write_image(f"frames/{output_name}-{idx}.png")


if __name__ == "__main__":
    generate_frames(output_name="How parameters affect predictions")
    find_gifs()

# %%
