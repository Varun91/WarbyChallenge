"""
Author: John Lucas
Description: A solution to the Warby Parker programming challenge. A detailed
description of how it works can be found in main()'s docstring.
"""

import sys

class TreeNode(object):
    """
    A node for a tree structure which can have an arbitrary number of children.
    """
    def __init__(self, data=None, children=None, is_end=False):
        self.data = data
        self.is_end = False # Whether the node is the end of a pattern
        if children == None:
            self.children = []
        else:
            self.children = children

    def __str__(self):
        return 'Data = '+str(self.data)

    def inorder_traversal(self):
        """ 
        Prints an inorder traversal of the tree dominated by the given node.
        """
        sys.stdout.write(str(self.data) + ', ')
        for child in self.children:
            child.inorder_traversal()
    
    def add_child(self, new_child):
        """
        Adds new_child, a TreeNode, to the children of a given node.
        """
        self.children.append(new_child)

    def find_child_with_data(self, data):
        """
        Checks to see if a node has a child which contains the given data.
        Returns None if not, returns the child if it does.
        """
        for child in self.children:
            if child.data == data:
                return child
            
        return None

def main():
    """
    The main function for the program. First, builds up a tree based on the
    given patterns. Then, for a given path, traverses the tree to find
    all possible patterns. These patterns are then narrowed down to the
    optimal pattern by first, number of wild cards, and second, placement
    of wildcards, as defined in the challenge description. The pattern is
    then printed or, in the case of no match, NO MATCH is printed. This 
    is repeated for each pattern. Assumes a well formed input (no repeated
    patterns, no ill formed paths).
    """
    num_patterns = int(raw_input())
    
    pattern_tree_head = TreeNode(data='head')

    for _ in xrange(num_patterns):
        pattern = raw_input().split(',')
        add_to_tree(pattern_tree_head, pattern)

    num_paths = int(raw_input())
    for _ in xrange(num_paths):
        path = raw_input()
        path = preprocess_path(path) # split path into a list of pieces
        patterns_list = traverse_patterns(pattern_tree_head, path, '')
        if not patterns_list:
            print 'NO MATCH'
            continue
        
        least_wild_patterns = find_least_wilds(patterns_list)
        # If one pattern has less wildcards than all the others
        if len(least_wild_patterns) == 1:
            print least_wild_patterns[0]
            continue

        # Otherwise, find the optimal and print
        print find_optimal_pattern(least_wild_patterns)

def add_to_tree(head, pattern):
    """ 
    Adds a given pattern to a given tree. To do so it checks to 
    see if the first piece (character/string) of the pattern is already 
    contained in a child node. If it is, it traverses to that node and 
    moves to the next piece. If it is not, it makes a new node with the piece 
    as its data, then traverses to it and moves to the next piece of the path.
    """
    current_node = head

    for i in xrange(len(pattern)):
        piece = pattern[i]
       
        child = current_node.find_child_with_data(piece)
        if child != None:
            current_node = child
                
        else:
            new_node = TreeNode(data=piece)
            current_node.add_child(new_node)
            current_node = new_node

        if i == (len(pattern)-1):
            current_node.is_end = True

def preprocess_path(path):
    """
    Removes the leading and trailing slashes of a path. Returns as a list
    of the elements of the path, in order.
    """
    if path[0]=='/':
        path = path[1:]

    if path[-1]=='/':
        path = path[:-1]

    return path.split('/')

def traverse_patterns(head, path_list, current_pattern):
    """
    A function that traverses a pattern tree and returns a list of all
    possible patterns. To do this, for each piece of the pattern it checks 
    the current node's children for either the piece or a wild card. If 
    either, or both, are found, it recursively traverses to that/those nodes
    and moves to the next piece of the path. Once the end of the path has
    been reached, and it is confirmed that the current node is in fact the 
    end of a possible pattern, the current pattern is returned within a list.
    """
    
    # If end of path, remove trailing comma and return as successful pattern
    if (path_list == []):
        if head.is_end:
            return [current_pattern[:-1]]

        return []

    curr_element = path_list[0]
    path_list = path_list[1:] 

    matched_patterns = []

    exact_child = head.find_child_with_data(curr_element)
    exact_return = None
    if exact_child:
        exact_return = traverse_patterns(exact_child, path_list, 
                          current_pattern+curr_element+',')
        matched_patterns=exact_return

    wild_child = head.find_child_with_data('*')
    wild_return = None
    if wild_child:
        wild_return = traverse_patterns(wild_child, path_list,
                                        current_pattern+'*,')

        matched_patterns = matched_patterns + wild_return

    return matched_patterns


def find_least_wilds(pattern_list):
    """
    Given a list of patterns, finds the pattern, or patterns, with the 
    least number of wildcards. Returns as a list
    """
    least_wilds = None 
    least_wilds_list = []

    for pattern in pattern_list:
        wild_count = pattern.count('*')
        
        # Set least_wilds on first iteration
        if least_wilds == None:
            least_wilds = wild_count

        if wild_count < least_wilds:
            least_wilds = wild_count
            least_wilds_list = [pattern]

        elif wild_count == least_wilds:
            least_wilds_list.append(pattern)

    return least_wilds_list
            
def find_optimal_pattern(pattern_list):
    """
    Given a list of patterns that all have the same number of wild cards, 
    finds the pattern with the first wildcard furthest to the right. If two 
    patterns have the first wildcard in the same position, applies this rule 
    recursively.
    
    Assumes all patterns are the same length, there should be no reason they
    are not at this point.
    """
    
    # Convert the strings to lists
    for i in xrange(len(pattern_list)):
        pattern_list[i] = pattern_list[i].split(',')

    return ','.join(optimal_pattern_helper(pattern_list, 0)[0])

def optimal_pattern_helper(pattern_list, curr_index):
    """
    Helper function for find_optimal_pattern. On each call, checks to see 
    if there is a wild card at the given index in each pattern. If there
    are any patterns that do not have a wild card at the given index,
    the function is called recursively on those patterns and the index is 
    incremented. Otherwise, it is called on the original list (in this case
    every pattern has a wildcard at the given index)
    """

    # If pattern is found
    if len(pattern_list) == 1:
        return pattern_list

    no_wild_at_i=[]
    found_not_wild = False

    for pattern in pattern_list:
        if pattern[curr_index] != '*':
            found_not_wild = True
            no_wild_at_i.append(pattern)


    curr_index+=1
    if found_not_wild:
        return optimal_pattern_helper(no_wild_at_i, curr_index)

    return optimal_pattern_helper(pattern_list, curr_index)
    

main()
