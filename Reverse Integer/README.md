# [Reverse Integer](https://leetcode.com/problems/reverse-integer/)
___

## Algorithm
Integer Reversal and Overflow CheckThis algorithm describes the process for reversing the digits of a 32-bit signed integer (x) while preserving its sign and ensuring the result remains within the $\text{Int32}$ range.

1. Handle the Sign and Initial Reversal
The first critical step is determining the number's sign to handle the reversal correctly:
    - **Check for Sign**: Determine if the input integer $x$ is negative (i.e., $x < 0$).
    - **Conversion**: Convert the absolute value of $x$ into a string representation.
    - **Conditional Reversal**:
        - If $x < 0$ (Negative): We insert the sign at position 0 of text variable and reverse the digit string from second position to the end.
        - If $x \ge 0$ (Positive/Zero): Simply reverse the entire digit string.
        
2.Final Conversion and Overflow Validation
After reversing the digits, the result must be converted back to an integer and validated against the $\text{Int32}$ boundaries.
- **Conversion**: Convert the reversed digit string back into a 32-bit integer.
- **Apply Sign**: If the original number was negative, prepend the minus sign to the resulting integer value.
- **Boundary Check (Overflow)**: Before returning the final value, check if the resulting integer falls within the maximum limits of $\text{Int32}$, which are:
    - Greater than or equal to $-2^{31}$ (the minimum value).
    - Less than or equal to $2^{31}-1$ (the maximum value).
- **Return Value**:
    - If the converted number is within the $\text{Int32}$ bounds, return the final converted number.
    - Otherwise (if an overflow or underflow occurred), return $0$.

