from matplotlib import animation
from gapminder import gapminder
import matplotlib.pyplot as plt

countries_plot = ['Spain', 'Italy', 'US', 'Ireland', 'China']
barchart_data = gapminder.loc[gapminder['country'].isin(countries_plot), :]
font = {'weight': 'normal',
        'size': 40,
        'color': 'lightgray'
}
years = barchart_data['year'].unique()
colors = ['#ff0000', '#169b62', '#008c45', '#aa151b', '#002868']
fig, ax = plt.subplots(figsize=(10, 5))
label = ax.text(0.95, 0.2, years[0],
                horizontalalignment='right', verticalalignment='top',
                transform=ax.transAxes, fontdict=font)


def update_barchart(i):
    year=years(i)
    data_temp = barchart_data.loc[barchart_data['year'] == year, :]
    ax.clear()
    ax.barh(data_temp.country, data_temp.gdpPercap, color=colors)
    label.set_text(year)
anim = animation.FuncAnimation(fig, update_barchart, frames = len(years))
plt.show()