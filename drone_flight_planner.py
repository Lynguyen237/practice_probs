''' PRAMP - Drone Flight Planner
You’re an engineer at a disruptive drone delivery startup and your CTO asks you to come up with 
an efficient algorithm that calculates the minimum amount of energy required for the company’s drone 
to complete its flight. You know that the drone burns 1 kWh (kilowatt-hour is an energy unit) 
for every mile it ascends, and it gains 1 kWh for every mile it descends. 
Flying sideways neither burns nor adds any energy. Given an array route of 3D points, implement a 
function calcDroneMinEnergy that computes and returns the minimal amount of energy the drone 
would need to complete its route.Assume that the drone starts its flight at the first point in route. 
That is, no energy was expended to place the drone at the starting point.

For simplicity, every 3D point will be represented as an integer array whose length is 3. 
Also, the values at indexes 0, 1, and 2 represent the x, y and z coordinates in a 3D point, respectively.

Explain your solution and analyze its time and space complexities.

Example:

input:  route = [ [0,   2, 10],
                  [3,   5,  0],
                  [9,  20,  6],
                  [10, 12, 15],
                  [10, 10,  8] ]

output: 5 # less than 5 kWh and the drone would crash before the finish
          # line. More than `5` kWh and it’d end up with excess energy
Constraints:

[time limit] 5000ms

[input] array.array.integer route

1 ≤ route.length ≤ 100
[output] integer
'''

# We only worry about z in this case since only changes in height affects the energy level
#==== Solution1 (O(n) time complexity, O(1) space complexity) ====
def calc_drone_min_energy(route):

  min_energy = 0 #The minimum energy needed is 0
  current_energy = 0 #Suppose current_energy is 0 at the starting point
  
  if len(route) == 1:
    return 0
  
  for i in range(len(route)-1):
    #New current_energy is calculated by adding the height difference btw the current position and the next
    current_energy = current_energy + (route[i][2] - route[i+1][2])
    #If the current energy is less than the min_energy, update the min_energy
    if current_energy < min_energy:
      min_energy = current_energy

  return min_energy * (-1)

# Only 2 points matter: starting height and the max_height of all the points
#==== Solution2 (O(n) time complexity and O(1) space complexity ====
def calc_drone_min_energy(route):

  highest_point = 0
  
  for i in range(len(route)):
    if highest_point < route[i][2]:
      highest_point = route[i][2]
  
  return highest_point - route[0][2]

#==== One liner solution ====
def calc_drone_min_energy(route):
  return max([h for _,_,h in route]) - route[0][2]

# We are using only one auxiliary variable in the algorithm, 
# highest_point, and it uses a constant amount of space.

# Test cases
# [[0,1,19]] #single
# [[0,2,10],[10,10,8]] #2 elements going down
# [[0,2,6],[10,10,20]] #2 elements going up
# [[0,2,10],[3,5,0],[9,20,6],[10,12,15],[10,10,8]]
# [[0,2,2],[3,5,38],[9,20,6],[10,12,15],[10,10,8]]
# [[0,2,10],[3,5,9],[9,20,6],[10,12,2],[10,10,10],[10,10,2]]