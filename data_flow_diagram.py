import plotly.graph_objects as go

# Define nodes and their positions
nodes = [
    "User Types (Admin, Engineer, Customer)", "Login/Register Page", "Dashboard",
    "Onboarding Service", "Admin Onboarding", "Engineer Onboarding", "Customer Onboarding",
    "Task Creation (Trades, Tasks)", "Task Matching", "Engineer Acceptance/Rejection",
    "Engineer Dispatch", "Task Completion", "Payment Processing", "Feedback Submission",
    "AI Feedback Evaluation", "Blockchain Integration", "Digital Wallet", "Backend API", "Database"
]
positions = [
    (1, 12), (3, 12), (5, 12),            # Top row
    (7, 12), (9, 14), (9, 12), (9, 10),  # Onboarding row
    (5, 10), (7, 10), (9, 8),            # Task and matching
    (9, 6), (7, 6), (5, 6),              # Dispatch, completion, payment
    (3, 6), (1, 6),                      # Feedback, AI evaluation, blockchain
    (5, 4), (7, 4), (9, 4),              # Backend
    (11, 2)                              # Database (added)
]

# Validate node count matches positions
if len(nodes) != len(positions):
    raise ValueError(f"Number of nodes ({len(nodes)}) does not match number of positions ({len(positions)}).")

# Define edges
edges = [
    (0, 1), (1, 2), (2, 3),              # User interaction
    (3, 4), (3, 5), (3, 6),             # Onboarding paths
    (4, 17), (5, 17), (6, 17),          # Onboarding to backend
    (3, 7), (7, 8), (8, 9), (9, 10),    # Task flow
    (10, 11), (11, 12),                 # Task completion and payment
    (12, 13), (13, 14),                 # Feedback and AI evaluation
    (14, 15), (15, 16),                 # AI to blockchain and wallet
    (7, 17), (8, 17), (9, 17),          # Backend connections
    (17, 18), (18, 17)                  # Database interaction
]

# Validate edges
for start, end in edges:
    if max(start, end) >= len(positions):
        raise IndexError(f"Invalid edge: ({start}, {end}) references a non-existent position.")

# Build animation frames
frames = []
for idx, (start, end) in enumerate(edges):
    edge_trace = go.Scatter(
        x=[positions[start][0], positions[end][0]],
        y=[positions[start][1], positions[end][1]],
        mode='lines+markers',
        line=dict(width=4, color='gold'),
        hoverinfo='none'
    )
    node_trace = go.Scatter(
        x=[positions[start][0], positions[end][0]],
        y=[positions[start][1], positions[end][1]],
        mode='markers+text',
        marker=dict(size=[40, 30], color=['green', 'lightblue']),
        text=[nodes[start], nodes[end]],
        textposition="bottom center"
    )
    frames.append(go.Frame(data=[edge_trace, node_trace], name=f"frame{idx}"))

# Static base traces
static_edges = [
    go.Scatter(
        x=[positions[start][0], positions[end][0]],
        y=[positions[start][1], positions[end][1]],
        mode='lines',
        line=dict(width=2, color='gray'),
        hoverinfo='none'
    ) for start, end in edges
]

static_nodes = go.Scatter(
    x=[pos[0] for pos in positions],
    y=[pos[1] for pos in positions],
    mode='markers+text',
    marker=dict(size=30, color='lightblue', line=dict(width=2, color='black')),
    text=nodes,
    hovertext=[
        "User interaction", "Handles login", "Displays dashboard", "Manages onboarding process",
        "Admin onboarding", "Engineer onboarding", "Customer onboarding",
        "Task creation process", "AI-driven task matching", "Engineer task response",
        "Real-time dispatch system", "Task completion confirmation", "Payment gateway",
        "Feedback collection from users", "AI for feedback evaluation",
        "Blockchain for transparency", "Digital wallet for payments", "API service", "Database storage"
    ],
    hoverinfo="text",
    textposition="bottom center"
)

# Create figure with animation frames
fig = go.Figure(
    data=[*static_edges, static_nodes],
    layout=go.Layout(
        title="Enhanced Animated Notfall Engineers On-Demand Data Flow Diagram",
        title_font=dict(size=24),
        xaxis=dict(showgrid=False, zeroline=False, visible=False),
        yaxis=dict(showgrid=False, zeroline=False, visible=False),
        showlegend=False,
        plot_bgcolor="white",
        updatemenus=[{
            "buttons": [
                {
                    "args": [None, {"frame": {"duration": 2000, "redraw": True}, "fromcurrent": True}],  # Slower frame speed
                    "label": "Play",
                    "method": "animate"
                },
                {
                    "args": [[None], {"frame": {"duration": 0, "redraw": True}, "mode": "immediate", "transition": {"duration": 0}}],
                    "label": "Pause",
                    "method": "animate"
                }
            ],
            "direction": "left",
            "pad": {"r": 10, "t": 87},
            "showactive": False,
            "type": "buttons",
            "x": 0.1,
            "xanchor": "right",
            "y": 0,
            "yanchor": "top"
        }]
    ),
    frames=frames
)

# Add easing for smooth transitions
fig.update_layout(
    transition=dict(duration=1500, easing="cubic-in-out")  # Slower easing
)

# Export to HTML for interactive sharing
fig.write_html("enhanced_animated_data_flow_with_feedback_slow.html")

# Display animated figure
fig.show()

