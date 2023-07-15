class Solution():

    def sub_sequence(self, string):

        A_count = 0
        count = 0
        for i in range(len(string)):

            if string[i] == "A":
                A_count += 1

            if string[i] == "G":
                count += A_count

        return count

object = Solution()
array = input()
print(object.sub_sequence(array))




