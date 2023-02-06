# %%
import plotly.graph_objects as go

w = np.linspace(-10, 10, 100)
b = np.linspace(-10, 10, 100)
ww, bb = np.meshgrid(w, b)
zz = 0.3* ((ww-3)**2 + (bb-2)**2)

fig = go.Figure(data=[go.Surface(
    z=zz,
    contours = {
        "x": {
            "show": True, 
            # "start": 1.5, 
            # "end": 2, 
            "size": 10, 
            "color": "white"
        },
        "y": {
            "show": True, 
            # "start": 1.5, 
            # "end": 2, 
            "size": 10, 
            "color": "white"
        },
    },
)])

fig.update_layout(
    title='Loss Surface', 
    autosize=True,
    width=900, 
    height=800,
    margin=dict(l=65, r=50, b=30, t=60),
    scene = dict(
        # xaxis = dict(nticks=4, range=[-100,100],),
        # yaxis = dict(nticks=4, range=[-50,100],),
        zaxis = dict(nticks=4, range=[0,100],),
        xaxis_title='Param 1',
        yaxis_title='Param 2',
        zaxis_title='Loss'
    ),
    # width=700,
    # margin=dict(r=20, l=10, b=10, t=10)
    scene_camera=dict(
        up=dict(x=0, y=0, z=1), # set vertical direction
        center=dict(x=0, y=0, z=0), # set origin
        eye=dict(x=1.25, y=1.25, z=1.25) # control coordinates that origin is being looked toward from
    )
)

# # ADD PROJECTION CONTOURS
# fig.update_traces(contours_z=dict(show=True, usecolormap=True,
#                                   highlightcolor="limegreen", project_z=True))

fig.show()
# %%
