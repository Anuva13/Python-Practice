import plotly.express as px
import pandas as pd

# Define the task data with estimated time spent for the roadmap
task_data = {
    'Task': [
        'Designing basic functionality (area, perimeter, etc.)',
        'Creating parameter parsers and validators',
        'Setting up tests with unittest',
        'Configuration files (setup.py, folder structures)',
        'Writing and reviewing documentation',
        'Researching best practices and resolving issues',
        'Debugging unexpected syntax and compatibility issues'
    ],
    'Start': [
        '2025-04-01', '2025-04-01', '2025-04-01', '2025-04-01', '2025-04-01', '2025-04-01', '2025-04-01'
    ],
    'Finish': [
        '2025-04-05', '2025-04-03', '2025-04-02', '2025-04-03', '2025-04-06', '2025-04-04', '2025-04-07'
    ],
    'Estimated Time Spent (hours)': [15, 10, 8, 6, 12, 15, 7],
    'Milestone': [
        'Start of project', 'Core functionality design', 'Unit tests setup', 'Config setup', 
        'Documentation review', 'Best practices research', 'Debugging'
    ]
}

# Create a DataFrame from the task data
df = pd.DataFrame(task_data)

# Convert 'Start' and 'Finish' columns to datetime format
df['Start'] = pd.to_datetime(df['Start'])
df['Finish'] = pd.to_datetime(df['Finish'])

# Plot the roadmap as a Gantt chart with milestones
fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task", color="Milestone", title="Project Roadmap")
fig.update_yaxes(autorange="reversed")  # Reverse the y-axis so tasks appear top to bottom

# Customize axis and layout
fig.update_layout(
    xaxis_title="Timeline",
    yaxis_title="Tasks",
    showlegend=True,
    bargap=0.3  # Adjust the gap between bars
)

# Show the chart
fig.show()
