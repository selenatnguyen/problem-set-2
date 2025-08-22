'''
PART 4: CATEGORICAL PLOTS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part4_plots`
'''

import seaborn as sns
import matplotlib.pyplot as plt

def catplot_felony(pred_universe_with_felony):
    g1 = sns.catplot(data=pred_universe_with_felony,
                     x='has_felony_charge',
                     y='prediction_felony',
                     kind='bar')
    g1.savefig('./data/part4_plots/catplot_felony.png', bbox_inches='tight')
    plt.close(g1.fig)

def catplot_nonfelony(pred_universe_with_felony):
    g2 = sns.catplot(data=pred_universe_with_felony,
                     x='has_felony_charge',
                     y='prediction_nonfelony',
                     kind='bar')
    g2.savefig('./data/part4_plots/catplot_nonfelony.png', bbox_inches='tight')
    plt.close(g2.fig)
    print("Prediction for nonfelony differs from felony because the model may weigh charge type differently for risk scoring.")

def catplot_felony_with_outcome(pred_universe_with_felony):
    g3 = sns.catplot(data=pred_universe_with_felony,
                     x='has_felony_charge',
                     y='prediction_felony',
                     hue='rearrest_felony',
                     kind='bar')
    g3.savefig('./data/part4_plots/catplot_felony_with_outcome.png', bbox_inches='tight')
    plt.close(g3.fig)
    print("This shows prediction bias: people with current felony charges but no felony rearrest still have higher predicted risk than some with misdemeanors who actually recidivated.")
