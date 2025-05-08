from stats import word_count, char_count, get_list
import sys


def get_book_text(filepath):
	with open(filepath) as f:
		file_contents = f.read()
		return file_contents

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	count = word_count(get_book_text(sys.argv[1]))
	char_count_dict = char_count(get_book_text(sys.argv[1]))
	list = get_list(char_count_dict)
	print("""============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
--------- Character Count -------""")
	for i in range(len(list)):
		if(list[i][0].isalpha()):
			print(f"{list[i][0]}: {list[i][1]}")
	print("============= END ===============")
	# print(f"{count} words found in the document")
	# print(char_count_dict)


main()

