#
#
#


class Queue(object):
	def __init__(self):
		self.list = []
	
	def enqueue(self, x):
		self.list.insert(0,x)
	
	def dequeue(self):
		return self.list.pop()

	def checkSize(self):
		return len(self.list)	


def testQueue():
	print("Testing Queue")
	queue=Queue()
	for i in range(1,11):
		queue.enqueue(i)
	while (queue.checkSize() != 0):
		print(queue.dequeue())
	

class Stack(object):
	def __init__(self):
		self.list = []

	def push(self, x):
		self.list.append(x)

	def pop(self):
		return self.list.pop()

	def checkSize(self):
		return len(self.list)

def testStack():
	print("Testing Stack")
	stack = Stack()
	for i in range(1,11):
		stack.push(i)
	while (stack.checkSize() != 0):
		print(stack.pop())


class Node(object):
	def __init__(self, intkey, left, right, parent):
		self.intkey = intkey
		self.left = left
		self.right = right
		self.parent = parent
		

class BinaryTree(object):
	def __init__(self, value):
		self.root = Node(value, None, None, None)
		self.nodes = []
		self.nodes.append(self.root)

	def findNode(self, nodeValue):
		for node in self.nodes:
			if node.intkey == nodeValue:
				return node

	def addNode(self, value, parentValue):
		node = None
		parentNode = self.findNode(parentValue)
		if parentNode == None:
			print("Parent not found")
		new_Node = Node(value, None, None, parentNode)
		if parentNode.left == None:
			parentNode.left = new_Node
			self.nodes.append(new_Node)
		elif parentNode.right == None:
			parentNode.right = new_Node
			self.nodes.append(new_Node)
		else:
			print("Parent has two children, node not added")
			return
		print "Node", value, "added with parent", parentValue


	def delete(self, value):
		node = self.findNode(value)
		if node == None:
			print "Node not found"
		elif node.left != None:
			print("Node not deleted, has children")
		elif node.right != None:
			print("Node not deleted, has children")
		else:
			self.nodes.remove(node)
			new_Parent = node.parent
			if new_Parent.left == node:
				new_Parent.left = None
			if new_Parent.right == node:
				new_Parent.right = None
			print "Node", value, "deleted"

	def printTree(self):
		self.print_help(self.root)

	def print_help(self, node):
		if node != None:
			node_Value = node.intkey
			node_Left = 0
			node_Right = 0
			if node.left != None:
				node_Left = node.left.intkey
			if node.right != None:
				node_Right = node.right.intkey
			print " ",node_Value
			print node_Left," ", node_Right
			self.print_help(node.left)
			self.print_help(node.right)


def testBinaryTree():
	print("Testing BinaryTree")
	myTree = BinaryTree(1)
	myTree.addNode(2, 1)
	myTree.addNode(3, 1)
	myTree.addNode(4, 2)
	myTree.addNode(5, 2)
	myTree.addNode(6, 3)
	myTree.addNode(7, 3)
	myTree.addNode(8, 4)
	myTree.addNode(9, 4)
	myTree.addNode(10, 5)
	myTree.addNode(11, 5)
	myTree.printTree()
	myTree.delete(8)
	myTree.delete(10)
	myTree.delete(11)
	myTree.printTree()



class Graph(object):
	def __init__(self, dict = {}):
		self.dict = dict

	def addVertex(self, value):
		if value in self.dict:
			print("Vertex already exists")
		else:
			self.dict[value] = []

	def addEdge(self, value1, value2):
		if value1 not in self.dict or value2 not in self.dict:
			print ("One or more vertices not found.")
		else:
			self.dict[value1].append(value2)
			self.dict[value2].append(value1)

	def findVertex(self, value):
		if value in self.dict:
			print(self.dict[value])

def testGraph():
	print("Testing Graph")
	graph = Graph()
	for i in range(1,22):
		graph.addVertex(i)
	for i in range(1,21):
		graph.addEdge(i,i+1)
	for i in range(2,7):
		graph.findVertex(i)


def main():
	#testQueue()
	#testStack()
	testBinaryTree()
	#testGraph()

if __name__ == '__main__':
	main()


		