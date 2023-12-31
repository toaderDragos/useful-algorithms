# 68. Text Justification
# Hard

# Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

# You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' 
when necessary so that each line has exactly maxWidth characters.

# Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, 
the empty slots on the left will be assigned more spaces than the slots on the right.

# For the last line of text, it should be left-justified, and no extra space is inserted between words.

# Note:

# A word is defined as a character sequence consisting of non-space characters only.
# Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
# The input array words contain at least one word.
 

# Example 1:

# Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
# Output:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]
# Example 2:

# Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
# Output:
# [
#   "What   must   be",
#   "acknowledgment  ",
#   "shall be        "
# ]
# Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
# Note that the second line is also left-justified because it contains only one word.
# Example 3:

# Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
# Output:
# [
#   "Science  is  what we",
#   "understand      well",
#   "enough to explain to",
#   "a  computer.  Art is",
#   "everything  else  we",
#   "do                  "
# ]
 

# Constraints:

# 1 <= words.length <= 300
# 1 <= words[i].length <= 20
# words[i] consists of only English letters and symbols.
# 1 <= maxWidth <= 100
# words[i].length <= maxWidth
# Accepted
# 356.3K
# Submissions
# 863.9K
# Acceptance Rate
# 41.2%


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        if len(words) == 1:
            pad_length = maxWidth - len(words[0])
            return [words[0] + pad_length * " "]

        lines = []
        i = 0
        # Step 1 put the words on their respective lines, align left, and ignore the last element for now
        while i <len(words)-1:
            if words[i] == maxWidth:
                lines.append([words[i]])
                i+=1
            else:
                temp = []
                ch_count = len(words[i])
                remaining_chr = maxWidth
             
                # Taking into consideration all elements except the last
                while ch_count <= maxWidth and i < len(words)-1:
                 
                    # Place the first word in the line
                    temp.append(words[i])
                    this_words_lenght = len(words[i])
                    remaining_chr = remaining_chr - this_words_lenght - 1

                    # Do we have space for another word or not? (use <= !! because we may have the exact number of chars as the line width) 
                    if len(words[i+1]) <= remaining_chr:
                     
                        # Add a space - now we would have 2 words 1 space
                        ch_count += len(words[i+1]) + 1
                     
                        # Last element check -> We put it on the same line here
                        if i+1 == len(words)-1:
                            temp.append(words[i+1])
                            lines.append(temp)
                    else:
                        ch_count += 1 + len(words[i+1]) # space + word
                        lines.append(temp)
                    # last element on a new line
                    if len(words[i+1]) > remaining_chr and i+1 == len(words)-1:
                        lines.append([words[-1]])
                    i+=1
        print(lines)
        
        # Step 2 Insert the spaces
        # rule for all except the last
        output = []
        for i in range(0, len(lines)-1):
            letter_count = 0
                    # special condition for a single word on the line
            if len(lines[i]) == 1:
                spaces = maxWidth - len(lines[i][0])
                string = lines[i][0] + spaces * " "
                output.append(string)
                continue

            for j in range(0, len(lines[i])):
                letter_count += len(lines[i][j])
                
            spaces = maxWidth - letter_count
            
            # The number of spaces should be divided by nr. words - 1
            one_space_temp = spaces// (len(lines[i]) - 1)
         
            # More spaces are until the x th usage
            x = spaces % (len(lines[i])-1)
            string = lines[i][0]
            for j in range(1, len(lines[i])):
                # If the indexes are lower than the delimiter of spaces
                if j <=x:
                    string = string + (one_space_temp + 1) * " " + lines[i][j]
                else:
                    string = string + one_space_temp * " " + lines[i][j]
            output.append(string)

        # The last line - first if we have a single word we fill everything else with spaces
        if len(lines[-1]) == 1:
            lstring = lines[-1][0] + (maxWidth - len(lines[-1][0])) * " "

        else:
            lstring = lines[-1][0]
            count = len(lines[-1][0])
            for j in range(1, len(lines[-1])):
                count += len(lines[-1][j]) + 1    # Because you add a space you add 1
                lstring += " " + lines[-1][j]

            dif = maxWidth - count
            if len(lines[-1]) > 1:
                lstring += dif * " " 

        output.append(lstring)   
        return output 
