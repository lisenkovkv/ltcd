#https://leetcode.com/problems/flood-fill/

def floodFill(image, sr, sc, newColor):
    """
    :type image: List[List[int]]
    :type sr: int
    :type sc: int
    :type newColor: int
    :rtype: List[List[int]]
    """
    #Approach #1: Depth-First Search 
    R, C = len(image), len(image[0])
    color = image[sr][sc]
    if color == newColor:
        return image
    
    def dfs(r, c):
        if image[r][c] == color:
            image[r][c] = newColor
            if r >= 1: dfs(r-1, c)
            if r+1 < R: dfs(r+1, c)
            if c >= 1: dfs(r, c-1)
            if c+1 < C: dfs(r, c+1)  
 
    dfs(sr, sc)  
    
    return(image)

    #Runtime: 52 ms, faster than 96.82% of Python online submissions for Flood Fill.
    #Memory Usage: 13.8 MB, less than 8.49% of Python online submissions for Flood Fill.
    #Time Complexity: O(N), where NN is the number of pixels in the image. We might process every pixel.
    #Space Complexity: O(N), the size of the implicit call stack when calling dfs.