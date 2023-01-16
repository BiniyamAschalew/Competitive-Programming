class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        output = []
        last_element = ''
        for i in range(1, n+1):
            if i % 3 == 0:
                last_element += "Fizz"
            if i % 5 == 0:
                last_element += 'Buzz'
            if not last_element:
                last_element = str(i)
            output.append(last_element)
            last_element = ''
        return output
