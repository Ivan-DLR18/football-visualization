import numpy as np
import plotly.graph_objs as go

class Field3d:
    def __init__(self, data=None):
        self.field_length = 100
        self.field_width = 70
        self.grid = 25
        self.xT_rows = 17
        self.xT_cols = 21
        self.custom_colorscale = [
            [0.0, 'blue'],  # Color for the minimum value
            [0.49, 'blue'],
            [0.5, 'white'], # Thinner white transition (closer to blue)
            [0.51, 'red'],
            [1.0, 'red']    # Color for the maximum value
        ]
        self.fig = go.Figure(data=[])
    
    def build_graph(self, z):
        field_length = self.field_length
        field_width = self.field_width

        grid_size = (self.xT_rows, self.xT_cols)  # number of divisions in x and y directions

        # Generate x and y values covering the football field dimensions
        x = np.linspace(-field_length / 2, field_length / 2, grid_size[1])
        y = np.linspace(-field_width / 2, field_width / 2, grid_size[0])
        # Create x and y grid (original)
        xGrid, yGrid = np.meshgrid(x, y)
        # Create reversed x and y grid
        xRevGrid, yRevGrid = np.meshgrid(y, x)
        x, y = np.meshgrid(x, y)

        # Create a surface plot using Plotly with decreased opacity
        surface = go.Surface(x=x, y=y, z=z, showscale=False, cmin=-0.5, cmax=0.5, colorscale=self.custom_colorscale, opacity=0.6)

        # Define line marker for gridlines
        line_marker = dict(color='white', width=2)

        # Add the surface to the figure
        self.fig.add_trace(surface)

        # Add gridlines in one direction (using the original mesh grid)
        for i, j, k in zip(xGrid, yGrid, z):
            # Add gridline for each row (constant y)
            surface_grid_x = go.Scatter3d(
                x=i, y=j, z=k,
                mode='lines', 
                line=line_marker, 
                showlegend=False
            )
            self.fig.add_trace(surface_grid_x)

        # Add gridlines in perpendicular direction (using reversed mesh grid)
        for i, j, k in zip(xRevGrid, yRevGrid, z.T):
            # Add gridline for each column (constant x)
            surface_grid_y = go.Scatter3d(
                x=j, y=i, z=k,
                mode='lines', 
                line=line_marker, 
                showlegend=False
            )
            self.fig.add_trace(surface_grid_y)

        # Draw a rectangle in the xy plane (z = 0)
        # Define the corners of the rectangle
        field_x = [-field_length/2, field_length/2, field_length/2, -field_length/2, -field_length/2]
        field_y = [-field_width/2, -field_width/2, field_width/2, field_width/2, -field_width/2]
        field_z = [0, 0, 0, 0, 0]  # z = 0 for the xy plane

        # Area grande
        ag1_x = [-field_length/2, (-field_length/2)+16.5, (-field_length/2)+16.5, -field_length/2, -field_length/2]
        ag1_y = [(-field_width/2)+11.85, (-field_width/2)+11.85, (field_width/2)-11.85, (field_width/2)-11.85, -(field_width/2)+11.85]

        ag2_x = [field_length/2, (field_length/2)-16.5, (field_length/2)-16.5, field_length/2, field_length/2]
        ag2_y = [(-field_width/2)+11.85, (-field_width/2)+11.85, (field_width/2)-11.85, (field_width/2)-11.85, -(field_width/2)+11.85]

        # Area chica
        ac1_x = [-field_length/2, (-field_length/2)+5.5, (-field_length/2)+5.5, -field_length/2, -field_length/2]
        ac1_y = [(-field_width/2)+22.85, (-field_width/2)+22.85, (field_width/2)-22.85, (field_width/2)-22.85, -(field_width/2)+22.85]

        ac2_x = [field_length/2, (field_length/2)-5.5, (field_length/2)-5.5, field_length/2, field_length/2]
        ac2_y = [(-field_width/2)+22.85, (-field_width/2)+22.85, (field_width/2)-22.85, (field_width/2)-22.85, -(field_width/2)+22.85]

        # halfline
        line_x = [0, 0]
        line_y = [-field_width / 2, field_width / 2]
        line_z = [0, 0]


        # Define the circle's center and radius
        circle_center = (0, 0)  # center at (0, 0) in the x-y plane
        circle_radius = 9.15  # radius of the circle

        # Generate the points for the circle in the x-y plane
        theta = np.linspace(0, 2 * np.pi, 100)
        circle_center_x = circle_center[0] + circle_radius * np.cos(theta)
        circle_center_y = circle_center[1] + circle_radius * np.sin(theta)
        circle_center_z = np.zeros_like(circle_center_x)  # z=0 for the circle in the x-y plane

        # Create a trace for the circle
        # Plot circle area
        theta = np.linspace(-0.295*np.pi, 0.295*np.pi, 100)  # Angle values from 0 to 2*pi
        circle_area1_x = -field_length/2+11 + circle_radius * np.cos(theta)
        circle_area1_y = 0 + circle_radius * np.sin(theta)
        circle_area1_z = np.zeros_like(circle_area1_x)  # z = 0 for the xy plane

        # Plot circle area
        theta = np.linspace(0.705*np.pi, 1.295*np.pi, 100)  # Angle values from 0 to 2*pi
        circle_area2_x = field_length/2-11 + circle_radius * np.cos(theta)
        circle_area2_y = 0 + circle_radius * np.sin(theta)
        circle_area2_z = np.zeros_like(circle_area2_x)  # z = 0 for the xy plane


        # Define the coordinates of the triangle vertices in the xy plane
        triangle_home_x = [-field_length/2 + 15, -field_length/2 + 15, -field_length/2 + 20]  # x-coordinates of the vertices
        triangle_home_y = [-field_width/2 - 9, -field_width/2 - 3, -field_width/2 - 6]   # y-coordinates of the vertices
        triangle_home_z = [0, 0, 0]   # z-coordinates (all zeros to keep it in the xy plane)

        triangle_away_x = [field_length/2 - 15, field_length/2 - 15, field_length/2 - 20]  # x-coordinates of the vertices
        triangle_away_y = [-field_width/2 - 9, -field_width/2 - 3, -field_width/2 - 6]   # y-coordinates of the vertices
        triangle_away_z = [0, 0, 0]   # z-coordinates (all zeros to keep it in the xy plane)

        # Create a Mesh3d object to represent the triangle
        triangle_home = go.Mesh3d(
            x=triangle_home_x,
            y=triangle_home_y,
            z=triangle_home_z,
            color='red'      # Opacity of the triangle
        )

        triangle_away = go.Mesh3d(
            x=triangle_away_x,
            y=triangle_away_y,
            z=triangle_away_z,
            color='blue'      # Opacity of the triangle
        )
        triangle_home = go.Cone(
            x=[-field_length/2 + 15],
            y=[-field_width/2 - 6],
            z=[0],
            u=[8],
            v=[0],
            w=[0],
            colorscale=[[0, 'red'], [1, 'red']],
            anchor='tail',
            showscale=False  
        )
        triangle_away = go.Cone(
            x=[field_length/2 - 15],
            y=[-field_width/2 - 6],
            z=[0],
            u=[-8],
            v=[0],
            w=[0],
            colorscale=[[0, 'blue'], [1, 'blue']],
            anchor='tail',
            showscale=False  
        )

        arrow1_x = [-field_length/2 + 5, -field_length/2 + 15]
        arrow1_y = [-field_width/2 - 6, -field_width/2 - 6]
        arrow1_z = [0, 0]


        arrow2_x = [field_length/2 - 5, field_length/2 - 15]
        arrow2_y = [-field_width/2 - 6, -field_width/2 - 6]
        arrow2_z = [0, 0]



        ##########################
        # # Field and areas
        self.fig.add_trace(go.Scatter3d(x=field_x, y=field_y, z=field_z, showlegend=False, mode='lines', line=dict(color='black', width=4)))
        self.fig.add_trace(go.Scatter3d(x=ag1_x, y=ag1_y, z=field_z, showlegend=False, mode='lines', line=dict(color='black', width=4)))
        self.fig.add_trace(go.Scatter3d(x=ag2_x, y=ag2_y, z=field_z, showlegend=False, mode='lines', line=dict(color='black', width=4)))
        self.fig.add_trace(go.Scatter3d(x=ac1_x, y=ac1_y, z=field_z, showlegend=False, mode='lines', line=dict(color='black', width=4)))
        self.fig.add_trace(go.Scatter3d(x=ac2_x, y=ac2_y, z=field_z, showlegend=False, mode='lines', line=dict(color='black', width=4)))

        # Halfline
        self.fig.add_trace(go.Scatter3d(x=line_x, y=line_y, z=line_z, showlegend=False, mode='lines', line=dict(color='black', width=4)))

        # Circles (middle, and area)
        self.fig.add_trace(go.Scatter3d(x=circle_center_x, y=circle_center_y, z=circle_center_z, showlegend=False, mode='lines', line=dict(color='black', width=4)))
        self.fig.add_trace(go.Scatter3d(x=circle_area1_x, y=circle_area1_y, z=circle_area1_z, showlegend=False, mode='lines', line=dict(color='black', width=4)))
        self.fig.add_trace(go.Scatter3d(x=circle_area2_x, y=circle_area2_y, z=circle_area2_z, showlegend=False, mode='lines', line=dict(color='black', width=4)))

        # # Arrow head
        self.fig.add_trace(triangle_home)
        self.fig.add_trace(triangle_away)
        # Arrow
        self.fig.add_trace(go.Scatter3d(x=arrow1_x, y=arrow1_y, z=arrow1_z, showlegend=False, mode='lines', line=dict(color='red', width=8)))
        # Arrow
        self.fig.add_trace(go.Scatter3d(x=arrow2_x, y=arrow2_y, z=arrow2_z, showlegend=False, mode='lines', line=dict(color='blue', width=5)))
        ##########################



        # Create a layout for the plot with aspect ratio settings
        layout = go.Layout(
            title='3D Surface Plot of the Football Field with Shapes',
            scene=dict(
                # xaxis_title='X (meters)',
                # yaxis_title='Y (meters)',
                # zaxis_title='Z (height)',
                xaxis=dict(
                    title='',
                    range=[field_length/2, -field_length/2],
                    backgroundcolor='rgba(0, 0, 0, 0)',  # Transparent background
                    showticklabels=False,               # Hide axis ticks
                    showgrid=False,                     # Hide grid lines
                    zeroline=False                      # Hide zero lines
                    ),         # Range for the x-axis
                yaxis=dict(
                    title='',
                    range=[field_width/2, -field_width/2-10],
                    backgroundcolor='rgba(0, 0, 0, 0)',  # Transparent background
                    showticklabels=False,               # Hide axis ticks
                    showgrid=False,                     # Hide grid lines
                    zeroline=False                      # Hide zero lines
                    ),         # Range for the y-axis
                zaxis=dict(
                    title='',
                    range=[np.min(z), np.max(z)],
                    backgroundcolor='rgba(0, 0, 0, 0)',  # Transparent background
                    showticklabels=False,               # Hide axis ticks
                    showgrid=False,                     # Hide grid lines
                    zeroline=False                      # Hide zero lines
                    ),            # Range for the z-axis (keep it small)
                aspectmode='manual',
                aspectratio=dict(
                    x=field_length / field_length,  # 1 (normalized)
                    y=(field_width+10) / field_length,   # Preserve proportionality
                    z=0.5                           # Adjust for a flat appearance
                )
            ),
            margin=dict(l=65, r=50, b=70, t=90),
            scene_camera_eye=dict(x=0, y=0.8, z=0.5)
        )


        # Create the figure and add the surface plot, line, circle, and rectangle
        # fig = go.Figure(data=[surface, halfline, circle, circle_area1, circle_area2, field, ag1, ag2, ac1, ac2], layout=layout)
        # fig = go.Figure(data=[surface], layout=layout)
        # Update the layout of the figure
        self.fig.update_layout(layout)
    
    def show(self):
        self.fig.show()
