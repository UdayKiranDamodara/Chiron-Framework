# Test case for profiling: Complex pattern with loops and conditionals
:x = 50
:y = 30
:angle = 90
:count = 0

pendown

# Draw a pattern with multiple loops and conditionals
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
    :count = :count + 1
    
    # Conditional drawing
    if (:count > 1) [
        penup
        goto (:x * 2, :y * 2)
        pendown
        repeat 2 [
            forward :x
            left 90
        ]
    ]
]

penup 