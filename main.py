def main():
    x = 'frankenstine'
    
    page_text = read_pages(x)
    word_count = count_words(page_text)
    c = count_char(page_text)
    print(f"-----Begin report of {x}------\n")
    print(f"There are {word_count} words in this book\n")
    for i in to_sorted_list(c):
        if i['char'].isalpha():
            print(f"The {i['char']} appeared {i['num']} times") 
    print("\n-----end of report-----")





def read_pages(book):
    with open(f"books/{book}.txt") as i:
        pages = i.read()
    return(pages)

def count_words(text):
    words = text.split()
    return(len(words))

def count_char(book):
    count = {}
    for i in book:
        x = i.lower()
        if x not in count:
            count[x] = 1
        else:
            count[x] += 1
    return count     

def sorty(item):
    return item['num']


def to_sorted_list(dict):
    sorted_list = []
    for d in dict:
        sorted_list.append({'char': d, 'num': dict[d]})
    sorted_list.sort(reverse=True, key=sorty) 
    return sorted_list



main()