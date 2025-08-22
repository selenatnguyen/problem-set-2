'''
PART 5: SCATTER PLOTS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part5_plots`
'''

import seaborn as sns
import matplotlib.pyplot as plt

def scatter_felony_vs_nonfelony(pred_universe_with_felony):
    g1 = sns.lmplot(data=pred_universe_with_felony,
                    x='prediction_felony',
                    y='prediction_nonfelony',
                    hue='has_felony_charge',
                    fit_reg=False)
    g1.savefig('./data/part5_plots/scatter_felony_vs_nonfelony.png', bbox_inches='tight')
    plt.close(g1.fig)
    print("Dots on the right show individuals with high predicted felony risk, typically those with current felony charges.")

def scatter_felony_vs_rearrest(pred_universe_with_felony):
    g2 = sns.lmplot(data=pred_universe_with_felony,
                    x='prediction_felony',
                    y='rearrest_felony',
                    fit_reg=False)
    g2.savefig('./data/part5_plots/scatter_felony_vs_rearrest.png', bbox_inches='tight')
    plt.close(g2.fig)
    print("The plot shows calibration issues: predicted probabilities don’t align perfectly with actual rearrests.")
