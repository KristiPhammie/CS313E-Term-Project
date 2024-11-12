import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data): 
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
            print()

#### return kozak sequences, 
# whichever protein has the best aligned kozak sequences,
# could return max heap or something, order proteins that would be most made

def process_sequence(sequence):
    linked_list = SinglyLinkedList()
    stop_codons = ['TAG', 'TAA', 'TGA']
    i = 0
    
    while i < len(sequence):
        # Look for ATG (start codon)
        if sequence[i:i+3] == 'ATG':
            start_pos = i
            j = i + 3
            found_stop = False
            
            # Search for stop codon
            while j <= len(sequence) - 3 and not found_stop:
                codon = sequence[j:j+3]
                if codon in stop_codons:
                    # Found a valid gene sequence
                    # Get 10 nucleotides before ATG (or from start if less than 10)
                    start_index = max(0, start_pos - 10)
                    gene_sequence = sequence[start_index:j+3]
                    linked_list.insert(gene_sequence)
                    found_stop = True
                    i = j + 3  # Move past the stop codon
                j += 3
            
            if not found_stop:
                i += 1
        else:
            i += 1
    
    return linked_list

def main():
    line = sys.stdin.readline()
    line = line.strip()
    
    # first line of input file is number of sequences
    num_protiens = int(line)

    # read the next num_protiens lines of input file
    for _ in range(num_protiens):
        line = sys.stdin.readline()
        line = line.strip()
        
        #call the function to process the sequence
        print(f'Sequence {_+1}:')
        process_sequence(line).print_list()

main()