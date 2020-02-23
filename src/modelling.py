# AUTOGENERATED! DO NOT EDIT! File to edit: notebooks/02_modelling.ipynb (unless otherwise specified).

__all__ = ['mish', 'Mish', 'predictions_vs_true_distribution_plots']

# Cell
import pandas as pd
from fastai2.tabular.all import *
from fastai2 import metrics
from sklearn import ensemble
from .utils import *

# Cell
def mish(x:torch.Tensor) -> torch.Tensor:
    return x * torch.tanh(F.softplus(x))

class Mish(torch.nn.Module):
    "Mish activation function: arXiv:1908.08681"
    def __init__(self):
        super().__init__()

    def forward(self, input):
        return mish(input)

# Cell
def predictions_vs_true_distribution_plots(y_pred:torch.Tensor, y_true:torch.Tensor, dep_var:str, bins:int=50):
    "Plots the predicted and true distributions side by side plus the residuals distribution"
    _y_p = y_pred.detach().numpy().ravel()
    _y_t = y_true.detach().numpy().ravel()

    fig, axs = plt.subplots(ncols=2, figsize=(14,4))
    ax = axs[0]
    ax.hist(_y_p, bins=bins, alpha=.5, label="pred")
    ax.hist(_y_t, bins=bins, alpha=.5, label="true")
    ax.set_xlabel(f"{dep_var}")
    ax.set_title(f"predicted vs true '{dep_var}'")
    ax.legend()

    ax = axs[1]
    ax.hist(_y_p-_y_t, bins=bins)
    ax.set_xlabel("Δ")
    ax.set_title(f"Δ-distribution: mean = {(_y_p-_y_t).mean():.2f}, std = {np.std(_y_p-_y_t):.2f}")
    plt.show()