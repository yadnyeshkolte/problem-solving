https://neetcode.io/problems/largest-rectangle-in-histogram/question

Largest Rectangle In Histogram
Solved 
Hard
Topics
Company Tags
Hints
You are given an array of integers heights where heights[i] represents the height of a bar. The width of each bar is 1.

Return the area of the largest rectangle that can be formed among the bars.

Note: This chart is known as a histogram.

Example 1:

Input: heights = [7,1,7,2,2,4]

Output: 8
Example 2:

Input: heights = [1,3,7]

Output: 7
Constraints:

1 <= heights.length <= 1000.
0 <= heights[i] <= 1000



class Solution {
    public int largestRectangleArea(int[] heights) {
        int n = heights.length;
        int area = 0;
        for(int i=0;i<n;i++){
            int minheight = heights[i];
            for(int j=i;j<n;j++){
                minheight = Math.min(heights[j], minheight);
                int dist = j-i+1;
                int areac = dist*minheight;
                area = Math.max(area, areac);
            }
        }
        return area;
        
    }
}
