import networkx as nx  
import matplotlib.pyplot as plt  
b=nx.Graph()
b.add_node('helloworld')
b.add_node(1)
b.add_node(2)
'''Node can be called by any python-hashable obj like string,number etc'''
nx.draw(b)  #draws the networkx graph containing nodes which are declared till before
plt.show()  # displays the networkx graph on matplotlib canvas

print(b)