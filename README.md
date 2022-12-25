# VADisabilityCalculator
Calculates Disability Rating and Payment

-----------------------------------------------------------------------------------------
# VADisabilityCalculator_v1.py
Graphical interface for calculating and displaying ratings and payments. Requires vaRating.py (included in this repository) for calculation of both ratings and payments. Users can assign ratings to arms and/or legs to determine bilateral factors for overall rating (10% if both sides affected). Any rating not assigned to an arm or leg is entered as "Other".
After getting the final disability rating, users will have the option to enter information to determine their monthly disability payment.
Includes dynamic input validation. GUI elements are visible/invisible based on user input.


-----------------------------------------------------------------------------------------
# VADisabilityCalculator_v2.py
Refactored for a cleaner interface using CustomTKinter. Retains all of the previous version's functionality, but all calculation is now dynamic and all options are available when the window opens.
