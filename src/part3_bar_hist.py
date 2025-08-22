'''
PART 3: BAR PLOTS AND HISTOGRAMS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part3_plots`
'''

import seaborn as sns
import matplotlib.pyplot as plt

def bar_fta(pred_universe):
    sns.countplot(data=pred_universe, x='fta')
    plt.savefig('./data/part3_plots/fta_bar.png', bbox_inches='tight')
    plt.clf()

def bar_fta_by_sex(pred_universe):
    sns.countplot(data=pred_universe, x='fta', hue='sex')
    plt.savefig('./data/part3_plots/fta_bar_by_sex.png', bbox_inches='tight')
    plt.clf()

def hist_age(pred_universe):
    sns.histplot(data=pred_universe, x='age_at_arrest')
    plt.savefig('./data/part3_plots/age_hist.png', bbox_inches='tight')
    plt.clf()

def hist_age_grouped(pred_universe):
    bins = [18, 21, 30, 40, 100]
    sns.histplot(data=pred_universe, x='age_at_arrest', bins=bins)
    plt.savefig('./data/part3_plots/age_hist_grouped.png', bbox_inches='tight')
    plt.clf()
