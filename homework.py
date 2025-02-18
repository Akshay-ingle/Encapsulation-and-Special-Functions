class StringReverser:
    def __init__(self, text):
        self.text = text
    
    def reverse_words(self):
        # Split the string into words, reverse the list, and join back
        return ' '.join(self.text.split()[::-1])
    
# Example usage:
if __name__ == "__main__":
    text = "Hello World! This is a test."
    reverser = StringReverser(text)
    print(reverser.reverse_words())
