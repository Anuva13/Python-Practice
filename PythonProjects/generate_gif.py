import plotly.express as px
import pandas as pd
import plotly.io as pio
from PIL import Image
import tempfile

# Define the task data with estimated time spent
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
    'Estimated Time Spent (hours)': [15, 10, 8, 6, 12, 15, 7]
}

# Create a DataFrame from the task data
df = pd.DataFrame(task_data)

# Convert 'Start' and 'Finish' columns to datetime format
df['Start'] = pd.to_datetime(df['Start'])
df['Finish'] = pd.to_datetime(df['Finish'])

# Create a list to hold the frames for the GIF
frames = []
num_frames = 10
for i in range(1, num_frames + 1):
    progress_df = df.copy()
    progress_df["Finish"] = progress_df.apply(
        lambda row: row["Start"] + (row["Finish"] - row["Start"]) * min(i / num_frames, 1), axis=1
    )
    fig = px.timeline(progress_df, x_start="Start", x_end="Finish", y="Task", color="Task")
    fig.update_yaxes(autorange="reversed")

    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmpfile:
        pio.write_image(fig, tmpfile.name)
        frames.append(Image.open(tmpfile.name))

# Save the frames as a GIF
frames[0].save("mensurapy_progress.gif", save_all=True, append_images=frames[1:], duration=500, loop=0)
