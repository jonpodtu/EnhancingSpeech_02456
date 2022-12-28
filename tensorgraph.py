import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

plt.close("all")

loss_types = ["sty", "cyc", "ds", "norm", "asr", "f0", "adv", "adv_cls", "real_adv_cls", "reg", "con_reg", "real", "fake", ]
loss_lambd = [1.0, 5.0, 1.0, 1.0, 10.0, 5.0, 2.0, 0.5, 0.1, 1.0, 10, 1.0, 1.0]

model_dfs = {}
for model in ["VanillaModel", "DWModel"]:
    dfs = {}
    for type in ["eval", "train"]:
        loss_df = []
        for j in range(len(loss_types)):
            temp = pd.read_csv(
                f".\\docs\\loss\\{model}\\{type}\\run-.-tag-{type}_"
                + loss_types[j]
                + ".csv",
                delimiter=",",
                )
            temp = temp.iloc[:140]
            temp = temp.drop(columns=["Wall time", "Step"])
            temp.columns = [loss_types[j]]
            temp[loss_types[j]] = temp[loss_types[j]] * loss_lambd[j]
            temp.reset_index()
            loss_df.append(temp)

        df = pd.concat(loss_df, axis=1, ignore_index=False)
        df["ds"] = df["ds"] * -1
        df["real"] = df["real"] * -1
        df["fake"] = df["fake"] * -1
        df["Full Generator Objective"] = df[
            ["sty", "cyc", "ds", "norm", "asr", "f0", "adv", "adv_cls"]
        ].sum(axis=1)
        df["Full Discriminator Objective"] = df[["real", "fake", "reg", "real_adv_cls", "con_reg"]].sum(axis=1)
                                        

        name_dict = {
            "sty": "Style reconstruction loss",  # 3
            "cyc": "Cycle consistency loss",  # 8
            "ds": "Style diversification loss",  # 4
            "norm": "Norm consistency loss",  # 7
            "asr": "Speech consistency loss",  # 6
            "f0": "F0 consistency loss",  # 5
            "adv": "Adversarial loss",  # 1
            "adv_cls": "Adversarial source classifier loss (Generator)",  # 2
            "real_adv_cls" : "Adversarial source classifier loss (Discriminator)",
            "reg" : "R1 regularizaition",
            "con_reg" : "Consistency regularization",
        }

        df = df.rename(columns=name_dict)
        dfs[type] = df
    model_dfs[model] = dfs
nrow = 2
ncol = 1
fig, axes = plt.subplots(nrow, ncol, figsize=(11, 11), sharex=True)


for type in ["train", "eval"]:
    for objective in ["Full Generator Objective","Full Discriminator Objective"]:
        for model in ["VanillaModel", "DWModel"]:
            if objective == "Full Generator Objective":
                if model == "VanillaModel":
                    if type == "train":
                        model_dfs[model][type][objective].plot(style='-', color='b', ax=axes[0])
                    else:
                        model_dfs[model][type][objective].plot(style='--', color='b', ax=axes[0])
                else: 
                    if type == "train":
                        model_dfs[model][type][objective].plot(style='-', color='r', ax=axes[0])
                    else:
                        model_dfs[model][type][objective].plot(style='--', color='r', ax=axes[0])
                axes[0].set_title(objective, fontdict={'fontsize': 23})
                axes[0].grid(True)
                axes[0].tick_params(axis='both', which='major', labelsize=18)
                axes[0].set_xlabel("Epochs", fontdict={'fontsize': 20})
                axes[0].axvline(29, c="black", linestyle=":")
                axes[0].axvline(49, c="black", linestyle="--")

            else:
                if model == "VanillaModel":
                    if type == "train":
                        model_dfs[model][type][objective].plot(style='-', color='b', ax=axes[1])
                    else:
                        model_dfs[model][type][objective].plot(style='--', color='b', ax=axes[1])
                else: 
                    if type == "train":
                        model_dfs[model][type][objective].plot(style='-', color='r', ax=axes[1])
                    else:
                        model_dfs[model][type][objective].plot(style='--', color='r', ax=axes[1])
                axes[1].set_title(objective, fontdict={'fontsize': 23})
                axes[1].grid(True)
                axes[1].tick_params(axis='both', which='major', labelsize=18)
                axes[1].set_xlabel("Epochs", fontdict={'fontsize': 20})
                axes[1].axvline(29, c="black", linestyle=":")
                axes[1].axvline(49, c="black", linestyle="--")

custom_lines = [
    Line2D([0], [0], linestyle='-', color='b', lw=4),
    Line2D([0], [0], linestyle='--', color='b', lw=4),
    Line2D([0], [0], linestyle='-', color='r', lw=4),
    Line2D([0], [0], linestyle='--', color='r', lw=4),
    Line2D([0], [0], linestyle=':', color='black', lw=4),
    Line2D([0], [0], linestyle='--', color='black', lw=4),
]
fig.legend(custom_lines, ["Train. original model", "Valid. original model","Train. reduced model", "Valid. reduced model", "Con. reg. intro.", "Adv. cls. intro."], prop={'size': 18}, ncol=3, bbox_to_anchor=(1, 0))
plt.tight_layout()
plt.savefig("docs/figures/losses.pdf", bbox_inches="tight", format='pdf')
plt.show()

