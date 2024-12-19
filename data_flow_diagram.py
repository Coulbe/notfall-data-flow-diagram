import plotly.graph_objects as go

# Define nodes and their positions
nodes = [
    "User Types (Admin, Engineer, Customer)", "Login/Register Page", "Dashboard",
    "Onboarding Service", "Admin Onboarding", "Engineer Onboarding", "Customer Onboarding",
    "Task Creation (Trades, Tasks)", "Task Matching", "Engineer Acceptance/Rejection",
    "Engineer Dispatch", "Payment Processing", "Feedback Submission",
    "Blockchain Integration", "Digital Wallet", "Backend API", "Database"
]
positions = [
    (1, 12), (3, 12), (5, 12),            # Top row
    (7, 12), (9, 14), (9, 12), (9, 10),  # Onboarding row
    (5, 10), (7, 10), (9, 8),            # Task and matching
    (9, 6), (7, 6), (5, 6),              # Dispatch, payment, feedback
    (3, 6), (1, 6),                      # Blockchain and wallet
    (5, 4), (7, 4)                       # Backend and database
]

# Create node scatter plot
node_trace = go.Scatter(
    x=[pos[0] for pos in positions],
    y=[pos[1] for pos in positions],
    mode='markers+text',
    marker=dict(size=30, color='lightblue', line=dict(width=2, color='black')),
    text=nodes,
    textposition="bottom center"
)

# Define edges (arrows between nodes)
edges = [
    (0, 1), (1, 2), (2, 3),             # User interaction
    (3, 4), (3, 5), (3, 6),            # Onboarding paths
    (4, 15), (5, 15), (6, 15),         # Onboarding to backend
    (3, 7), (7, 8), (8, 9), (9, 10),   # Task flow
    (10, 11), (11, 12), (12, 13),      # Payment and feedback
    (7, 15), (8, 15), (9, 15),         # Backend connections
    (15, 16), (16, 15), (11, 14),      # Database and wallet
    (14, 13), (13, 12)                 # Blockchain integration
]
edge_traces = []
for start, end in edges:
    edge_traces.append(go.Scatter(
        x=[positions[start][0], positions[end][0]],
        y=[positions[start][1], positions[end][1]],
        mode='lines+markers',
        line=dict(width=3, color='gray', dash="solid"),
        hoverinfo='none'
    ))

# Combine all traces
fig = go.Figure([node_trace] + edge_traces)

# Customize layout
fig.update_layout(
    title="Expanded Interactive Data Flow Diagram with Onboarding",
    title_font=dict(size=24),
    xaxis=dict(showgrid=False, zeroline=False, visible=False),
    yaxis=dict(showgrid=False, zeroline=False, visible=False),
    showlegend=False,
    plot_bgcolor="white"
)

# Export to PNG and HTML
fig.write_image("expanded_data_flow_with_onboarding.png")
fig.write_html("expanded_data_flow_with_onboarding.html")

# Display the diagram
fig.show()
