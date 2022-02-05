import matplotlib as mpl


def mpl_set_x_y_axis_same_limits(ax):
    """Set same limits on xlim and ylim"""
    min_shared = min(ax.get_xlim()[0], ax.get_ylim()[0])
    max_shared = max(ax.get_xlim()[1], ax.get_ylim()[1])
    ax.set_ylim((min_shared, max_shared))
    ax.set_xlim((min_shared, max_shared))


def mpl_add_commas_to_labels_on_axis(ax, xaxis=True): 
    """On a matplotlib axis set commas to larger numbers"""
    if xaxis:
        axis = ax.get_xaxis()
    else:
        axis = ax.get_yaxis()
    axis.set_major_formatter(mpl.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))


def mpl_set_label_rotation(ax, xaxis=True, rotation=45, ha='right'):
    """On a matplotlib axis set label rotation"""
    if xaxis:
        labels = ax.get_xticklabels()
        fn = ax.set_xticklabels    
    else:
        labels = ax.get_yticklabels()
        fn = ax.set_yticklabels
    fn(labels, rotation=rotation, ha=ha);