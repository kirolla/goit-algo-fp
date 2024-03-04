k_1class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Додавання вузла в кінець списку
    def append(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)

    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        return "->".join(values)

    # Реверсування списку
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # Сортування списку вставкою
    def insertion_sort(self):
        sorted_list = SinglyLinkedList()
        current = self.head
        while current:
            next_node = current.next
            current.next = None
            self._insert_sorted(sorted_list, current)
            current = next_node
        self.head = sorted_list.head

    # Вставка відсортованого вузла
    def _insert_sorted(self, sorted_list, node):
        if sorted_list.head is None or node.value < sorted_list.head.value:
            node.next = sorted_list.head
            sorted_list.head = node
        else:
            current = sorted_list.head
            while current.next and current.next.value < node.value:
                current = current.next
            node.next = current.next
            current.next = node

    # Об'єднання двох відсортованих списків в один
    def merge_sorted_lists(list1, list2):
        dummy = Node()
        tail = dummy
        current1 = list1.head
        current2 = list2.head
        while current1 and current2:
            if current1.value < current2.value:
                tail.next, current1 = current1, current1.next
            else:
                tail.next, current2 = current2, current2.next
            tail = tail.next
        tail.next = current1 or current2
        merged_list = SinglyLinkedList()
        merged_list.head = dummy.next
        return merged_list


if __name__ == "__main__":
    list1 = SinglyLinkedList()
    for value in [3, 1, 4]:
        list1.append(value)
    list1.insertion_sort()

    list2 = SinglyLinkedList()
    for value in [2, 5, 6]:
        list2.append(value)
    list2.insertion_sort()

    print("Список 1:", list1)
    print("Список 2:", list2)

    merged_list = SinglyLinkedList.merge_sorted_lists(list1, list2)
    print("Об'єднаний список:", merged_list)