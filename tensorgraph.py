import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

plt.close("all")

loss_types = ["sty", "cyc", "ds", "norm", "asr", "f0", "adv", "adv_cls"]
loss_lambd = [1.0, 5.0, 1.0, 1.0, 10.0, 5.0, 2.0, 0.5]

dfs = {}
for type in ["eval", "train"]:
    loss_df = []
    for j in range(len(loss_types)):
        temp = pd.read_csv(
            f".\\docs\\loss\\VanillaModel\\{type}\\run-.-tag-{type}_"
            + loss_types[j]
            + ".csv",
            delimiter=",",
        )
        temp = temp.drop(columns=["Wall time", "Step"])
        temp.columns = [loss_types[j]]
        temp[loss_types[j]] = temp[loss_types[j]] * loss_lambd[j]
        temp.reset_index()
        loss_df.append(temp)

    df = pd.concat(loss_df, axis=1, ignore_index=False)
    df["ds"] = df["ds"] * -1
    df["Full Objective"] = df[
        ["sty", "cyc", "ds", "norm", "asr", "f0", "adv", "adv_cls"]
    ].sum(axis=1)

    name_dict = {
        "sty": "Style reconstruction loss",  # 3
        "cyc": "Cycle consistency loss",  # 8
        "ds": "Style diversification loss",  # 4
        "norm": "Norm consistency loss",  # 7
        "asr": "Speech consistency loss",  # 6
        "f0": "F0 consistency loss",  # 5
        "adv": "Adversarial loss",  # 1
        "adv_cls": "Adversarial source classifier loss",  # 2
    }

    df = df.rename(columns=name_dict)
    dfs[type] = df
nrow = 3
ncol = 3
fig, axes = plt.subplots(nrow, ncol, figsize=(16, 12), sharex=True)
for type in ["train", "eval"]:
    for r in range(nrow):
        for c in range(ncol):
            key = list(dfs[type].columns)[r * 3 + c]
            dfs[type][key].plot(ax=axes[r, c])
            axes[r, c].set(title=key)
            axes[r, c].grid(True)
custom_lines = [
    Line2D([0], [0], color="C0", lw=4),
    Line2D([0], [0], color="C1", lw=4),
]
fig.legend(custom_lines, ["Train", "Validation"], loc="lower right")
plt.savefig("docs/figures/losses.png")
plt.show()
