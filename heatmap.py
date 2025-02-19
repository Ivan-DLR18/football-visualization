import plotly.graph_objects as go # type: ignore
import numpy as np # type: ignore

class Heatmap:
    def __init__(self):
        # Define pitch dimensions
        self.field_length = 100
        self.field_width = 70
        self.lines_color = 'white'

        # Draw pitch elements
        self.fig = go.Figure()

        self.field_x = [-self.field_length/2, self.field_length/2, self.field_length/2, -self.field_length/2, -self.field_length/2]
        self.field_y = [-self.field_width/2, -self.field_width/2, self.field_width/2, self.field_width/2, -self.field_width/2]

        # Area grande
        ag1_x = [-self.field_length/2, (-self.field_length/2)+16.5, (-self.field_length/2)+16.5, -self.field_length/2, -self.field_length/2]
        ag1_y = [(-self.field_width/2)+11.85, (-self.field_width/2)+11.85, (self.field_width/2)-11.85, (self.field_width/2)-11.85, -(self.field_width/2)+11.85]

        ag2_x = [self.field_length/2, (self.field_length/2)-16.5, (self.field_length/2)-16.5, self.field_length/2, self.field_length/2]
        ag2_y = [(-self.field_width/2)+11.85, (-self.field_width/2)+11.85, (self.field_width/2)-11.85, (self.field_width/2)-11.85, -(self.field_width/2)+11.85]

        # Area chica
        ac1_x = [-self.field_length/2, (-self.field_length/2)+5.5, (-self.field_length/2)+5.5, -self.field_length/2, -self.field_length/2]
        ac1_y = [(-self.field_width/2)+22.85, (-self.field_width/2)+22.85, (self.field_width/2)-22.85, (self.field_width/2)-22.85, -(self.field_width/2)+22.85]

        ac2_x = [self.field_length/2, (self.field_length/2)-5.5, (self.field_length/2)-5.5, self.field_length/2, self.field_length/2]
        ac2_y = [(-self.field_width/2)+22.85, (-self.field_width/2)+22.85, (self.field_width/2)-22.85, (self.field_width/2)-22.85, -(self.field_width/2)+22.85]

        # halfline
        line_x = [0, 0]
        line_y = [-self.field_width / 2, self.field_width / 2]

        self.fig.add_trace(go.Scatter(x=self.field_x, y=self.field_y, showlegend=False, hoverinfo='skip',  hovertemplate='', mode='lines', line=dict(color=self.lines_color, width=2)))
        self.fig.add_trace(go.Scatter(x=ag1_x, y=ag1_y, showlegend=False, hoverinfo='skip',  hovertemplate='', mode='lines', line=dict(color=self.lines_color, width=2)))
        self.fig.add_trace(go.Scatter(x=ag2_x, y=ag2_y, showlegend=False, hoverinfo='skip',  hovertemplate='', mode='lines', line=dict(color=self.lines_color, width=2)))
        self.fig.add_trace(go.Scatter(x=ac1_x, y=ac1_y, showlegend=False, hoverinfo='skip',  hovertemplate='', mode='lines', line=dict(color=self.lines_color, width=2)))
        self.fig.add_trace(go.Scatter(x=ac2_x, y=ac2_y, showlegend=False, hoverinfo='skip',  hovertemplate='', mode='lines', line=dict(color=self.lines_color, width=2)))
        self.fig.add_trace(go.Scatter(x=line_x, y=line_y, showlegend=False, hoverinfo='skip',  hovertemplate='', mode='lines', line=dict(color=self.lines_color, width=2)))

        # Define the circle's center and radius
        circle_center = (0, 0)  # center at (0, 0) in the x-y plane
        circle_radius = 9.15  # radius of the circle

        # Generate the points for the circle in the x-y plane
        theta = np.linspace(0, 2 * np.pi, 100)
        circle_center_x = circle_center[0] + circle_radius * np.cos(theta)
        circle_center_y = circle_center[1] + circle_radius * np.sin(theta)

        # Create a trace for the circle
        # Plot circle area
        theta = np.linspace(-0.295*np.pi, 0.295*np.pi, 100)  # Angle values from 0 to 2*pi
        circle_area1_x = -self.field_length/2+11 + circle_radius * np.cos(theta)
        circle_area1_y = 0 + circle_radius * np.sin(theta)

        # Plot circle area
        theta = np.linspace(0.705*np.pi, 1.295*np.pi, 100)  # Angle values from 0 to 2*pi
        circle_area2_x = self.field_length/2-11 + circle_radius * np.cos(theta)
        circle_area2_y = 0 + circle_radius * np.sin(theta)

        self.fig.add_trace(go.Scatter(x=circle_center_x, y=circle_center_y, showlegend=False, hoverinfo='skip',  hovertemplate='', mode='lines', line=dict(color=self.lines_color, width=2)))
        self.fig.add_trace(go.Scatter(x=circle_area1_x, y=circle_area1_y, showlegend=False, hoverinfo='skip',  hovertemplate='', mode='lines', line=dict(color=self.lines_color, width=2)))
        self.fig.add_trace(go.Scatter(x=circle_area2_x, y=circle_area2_y, showlegend=False, hoverinfo='skip',  hovertemplate='', mode='lines', line=dict(color=self.lines_color, width=2)))


    def build_graph(self, touches_df):
        self.fig.add_trace(go.Scatter(
            x=touches_df.x_scaled, 
            y=touches_df.y_scaled, 
            showlegend=False, 
            hoverinfo='skip', 
            hovertemplate='',
            mode="markers",
            marker=dict(size=5, color="blue", line=dict(width=1, color="grey"))
            )
            )

        # Plot KDE Heatmap
        self.fig.add_trace(go.Histogram2dContour(
            x=touches_df.x_scaled, 
            y=touches_df.y_scaled,
            contours=dict(
                coloring='heatmap', 
                start=0.5, 
                end=10, 
                size=1, 
                showlines=True
                ),
            line=dict(color='rgb(201, 201, 201)'),
            opacity=1,  # Equivalent to seaborn alpha=0.5
            showscale=False,
            hoverinfo='skip',
            hovertemplate='',
            histnorm='',
            colorscale=[
                [0.0, "rgba(0,0,0,0)"],  # Lowest values are fully transparent
                [0.1, "rgb(50, 18, 48)"],  
                [0.3, "rgb(142, 15, 81)"],  
                [0.5, "rgb(204, 37, 41)"],  
                [0.7, "rgb(252, 141, 89)"],  
                [0.9, "rgb(254, 224, 144)"],  
                [1.0, "rgb(255, 255, 178)"]
                ]
            )
        )
        
        # Set axis properties
        self.fig.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",  # Transparent background
            paper_bgcolor="rgba(0,0,0,0)",  # Transparent page background
            xaxis=dict(
                showgrid=False, 
                zeroline=False, 
                showticklabels=False,
                range=[-self.field_length/2-1, self.field_length/2+1]
                ),
            yaxis=dict(
                showgrid=False, 
                zeroline=False, 
                showticklabels=False, 
                range=[-self.field_width/2, self.field_width/2], 
                scaleanchor='x', 
                scaleratio=1
                ),
            # width=1000,
            autosize=True,
            height=170,
            margin=dict(l=0, r=0, t=0, b=0),
        )

