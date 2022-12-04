import pandas as pd
import matplotlib.pyplot as plt

plt.close("all")

loss_types = ["sty", "cyc", "ds", "norm", "asr", "f0", "adv", "adv_cls"]
loss_lambd = [1.,5.,1.,1.,10.,5.,2.,0.5]
loss_df = []

for j in range(8):
    temp = pd.read_csv('.\\docs\\loss\\VanillaModel\\run-.-tag-eval_' + loss_types[j] + '.csv', delimiter=',')
    temp = temp.drop(columns=['Wall time', 'Step'])
    temp.columns = [loss_types[j]]
    temp[loss_types[j]] = temp[loss_types[j]] * loss_lambd[j]
    temp.reset_index()
    loss_df.append(temp)

df = pd.concat(loss_df, axis=1, ignore_index=False)
df['ds'] = df['ds'] * -1
df['Full Objective'] = df[["sty", "cyc", "ds", "norm", "asr", "f0", "adv", "adv_cls"]].sum(axis=1)

df = df.rename(columns={"sty": "Style reconstruction loss", "cyc": "Cycle consistency loss","ds": "Style diversification loss","norm": "Norm consistency loss",
    "asr": "Speech consistency loss","f0": "F0 consistency loss","adv": "Adversarial loss","adv_cls" : "Adversarial source classifier loss",})
df.plot(subplots=True, layout=(3,3))



plt.show()