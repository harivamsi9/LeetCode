class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        ## Brute Force:
        for i in range(len(image)):
            image[i] = image[i][::-1]
            for j in range(len(image[0])):
                if image[i][j] == 1:
                    image[i][j] = 0
                else:
                    image[i][j] = 1
        return image


        