# Initialize variables
:x = 50
:y = 30
:angle = 90

# Start drawing
pendown

# Draw a pattern
repeat 3 [
    # Draw a square
    repeat 4 [
        forward :x
        left :angle
    ]
    
    # Move to new position
    penup
    goto (:x + 20, :y + 20)
    pendown
    
    # Draw a triangle
    repeat 3 [
        forward :y
        left 120
    ]
    
    # Update variables
    :x = :x + 10
    :y = :y + 10
]

penup