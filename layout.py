layout = {

    "title": "title_name(name)",
    "width": 1000,
    "height": 550,

    "dragmode": "pan",
    "hoverlabel": {"bgcolor": "#FFFFFF"},


    "scene": {
        "xaxis": {
            "type": "category",
            "title": "",
            "tickfont": {"size": 10},
            "tickmode": "linear",
            "showspikes": True,
            "spikecolor": "#444",
            "spikesides": True,
            "spikethickness": 2
        },
        "yaxis": {
            "type": "date",
            "title": "Date",
            "showspikes": True,
            "spikecolor": "#444",
            "spikesides": True,
            "spikethickness": 2
        },
        "zaxis": {
            "title": "axis_name(name)",
            # "showgrid": False,
            "showspikes": True,
            "spikecolor": "#444",
            "zerolinecolor": "#FB0101",
            "spikesides": True,
            # "showticklabels": False,
            "spikethickness": 2
        },
        "camera": {
            "up": {
                "x": 0,
                "y": 0,
                "z": 1
            },
            "eye": {
                "x": 5.977482059557231,
                "y": 6.186390278730835,
                "z": 1.3243642163415283
            },
            "center": {
                "x": 1.4625424142545986,
                "y": 2.850591692648807,
                "z": -1.034529807802799
            }
        },
        "dragmode": "pan",
        "hovermode": "closest",
        "aspectmode": "manual",
        "aspectratio": {
            "x": 3,
            "y": 10,
            "z": 2
        }
    },
    "margin": {
        "b": 0,
        "l": 0,
        "r": 0,
        "t": 40
    }

}