class Link(object):
    # A sample method
    def __init__(self, parent_name, child_name):
        self.parent_name = parent_name
        self.child_name = child_name

    def find_parent(self, child_name):
        if (self.child_name == child_name):
            return self.parent_name
        else:
            return ""

    def __str__(self):
        return self.parent_name + " " + self.child_name

def find_venture(list_of_links, account_name):
    for l in list_of_links:
        p = l.find_parent(account_name)
        if p:
           for v in list_of_links:
               a = v.find_parent(p)
               if a == "Root":
                  print(p)

if __name__ == '__main__':
    top_left_link = Link("Root", "Colgate US")
    left_most_link = Link("Colgate US", "retailer1")
    L1 = [top_left_link, left_most_link]
    find_venture(L1, "retailer1")