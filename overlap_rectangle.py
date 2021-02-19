# An axis-aligned rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) is the coordinate of its bottom-left corner, and (x2, y2) is the coordinate of its top-right corner. Its top and bottom edges are parallel to the X-axis, and its left and right edges are parallel to the Y-axis.

# Two rectangles overlap if the area of their intersection is positive. To be clear, two rectangles that only touch at the corner or edges do not overlap.

# Given two axis-aligned rectangles rec1 and rec2, return true if they overlap, otherwise return false.
# https://leetcode.com/problems/rectangle-overlap/

def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
    # rec1 = [x1, y1, x2, y2]
    # rec2 = [xa, yb, xb, yb]
    
    
    # Same-position corners
    if (x1 == xa and ya == yb):
        return true
    elif (x2 == xb and y2 == yb):
        return true
    elif (x1 == xa and y2 == yb):
        return true
    elif (x2 == xb and y1 == ya):
        return true
    
    # Touching corners without overlapping
    if (x2 == xa and y2 == ya): #(x2,y2) (xa,ya)
        return false
    elif (x1 == xb and y1 == yb): #(x1,y1) (xb,yb)
        return false
    elif (x2 == xa and y1 == yb):
        return false # (x2,y1) (xa, yb)
    elif (x1 == xb and y2 == ya):
        return false
    
    # Other Overlapping cases
#         if ((x2-x1) + (xb-xa) < (xb - x1)) and ((y2-y1) + (yb-ya) < (yb-y1)):
#             return true
    
#         return false

    # above or bottom
    if ya > y2 or yb < y1 # 2nd one above:
        return false
    
    # elif yb < y1# 2nd one below