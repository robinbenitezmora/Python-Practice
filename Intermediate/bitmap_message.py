import sys

# Try changing this multiline string to any image you like!
# There are 68 periods along the top and bottom of this string:
# '......................................................................'
# There are 8 periods along the left and right sides of this string:
# '........'
# The string is 8 characters wide and 6 characters tall.
bitmap = '''
 ....................................................................
    **************   *  *** **  *      ******************************
   ********************* ** ** *  * ****************************** *
  **      *****************       ******************************
           *************          **  * **** ** ************** *
            *********            *******   **************** * *
             ********           ***************************  *
    *        * **** ***         *************** ******  ** *
                ****  *         ***************   *** ***  *
                  ******         *************    **   **  *
                  ********        *************    *  ** ***
                    ********         ********          * *** ****
                    *********         ******  *        **** ** * **
                    *********         ****** * *           *** *   *
                      ******          ***** **             *****   *
                      *****            **** *            ********
                     *****             ****              *********
                     ****              **                 *******   *
                     ***                                       *    *
                     **     *                    *
....................................................................'''

print('Bitmap Message')
print('Enter the message to display with the bitmap (max 40 characters)')
message = input('> ')

if message == '':
    sys.exit()

# Loop over each line in the bitmap:
for line in bitmap.splitlines():
    # Loop over each character in the line:
    for i, bit in enumerate(line):
        if bit == ' ':
            # Print an empty space since there's a space in the bitmap:
            print(' ', end='')
        else:
            # Print a character from the message:
            print(message[(i % len(message))], end='')
    print()  # Print a newline at the end of the line.
# What is the output of the following code?
# A) The code will display the message "Bitmap Message" with the bitmap image.
# B) The code will display the message "Bitmap Message" without the bitmap image.
# C) The code will display the message "Bitmap Message" with the bitmap image repeated multiple times.
# D) The code will display the message "Bitmap Message" with the bitmap image rotated 90 degrees.
#
# Correct Answer: A) The code will display the message "Bitmap Message" with the bitmap image.

# Explanation: The code displays the message "Bitmap Message" with the bitmap image. The bitmap variable contains a multiline string representing an ASCII art image. The code prompts the user to enter a message to display with the bitmap. It then loops over each line in the bitmap and each character in the line. If the character is a space, it prints a space. Otherwise, it prints a character from the message. This results in the message being displayed with the bitmap image.
# The correct answer is A) The code will display the message "Bitmap Message" with the bitmap image.
# The code displays the message "Bitmap Message" with the bitmap image. The bitmap is an ASCII art image stored in the multiline string variable. The code prompts the user to enter a message, and then it loops over each line in the bitmap and each character in the line. If the character in the bitmap is a space, it prints a space; otherwise, it prints a character from the message. This creates the effect of displaying the message with the bitmap image.